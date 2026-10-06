#!/usr/bin/env python
# Copyright 2026 NetBox Labs Inc
"""
NetBox Labs - Tests for skip-TLS-verify behaviour.

These tests use real TLS servers. Mocking the TLS layer is what let the earlier
pin-and-rename implementation ship with every skip-verify test passing while the
real handshake still failed.
"""

import base64
import datetime as dt
import logging
import os
import socket
import ssl
import threading
from concurrent import futures
from unittest import mock

import grpc
import pytest
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from opentelemetry.proto.collector.logs.v1 import (
    logs_service_pb2,
    logs_service_pb2_grpc,
)

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk._skip_verify_tunnel import SkipVerifyTunnel, split_authority
from netboxlabs.diode.sdk.client import DiodeOTLPClient
from netboxlabs.diode.sdk.diode.v1 import ingester_pb2, ingester_pb2_grpc
from netboxlabs.diode.sdk.exceptions import DiodeClientError, DiodeConfigError
from netboxlabs.diode.sdk.ingester import Entity, Site

NOW = dt.datetime.now(dt.timezone.utc)


def make_cert(
    directory,
    *,
    dns=("diode.internal",),
    expired=False,
    key_bits=2048,
    signature_hash=hashes.SHA256(),
):
    """Write a self-signed certificate and key to ``directory`` and return both paths."""
    key = rsa.generate_private_key(public_exponent=65537, key_size=key_bits)
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "tls-test")])
    not_before, not_after = (
        (NOW - dt.timedelta(days=30), NOW - dt.timedelta(days=1)) if expired else (NOW - dt.timedelta(hours=1), NOW + dt.timedelta(days=30))
    )
    builder = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(not_before)
        .not_valid_after(not_after)
    )
    if dns:
        builder = builder.add_extension(x509.SubjectAlternativeName([x509.DNSName(d) for d in dns]), critical=False)
    cert = builder.sign(key, signature_hash)

    cert_path = os.path.join(directory, "server.crt")
    key_path = os.path.join(directory, "server.key")
    with open(cert_path, "wb") as fh:
        fh.write(cert.public_bytes(serialization.Encoding.PEM))
    with open(key_path, "wb") as fh:
        fh.write(
            key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption(),
            )
        )
    return cert_path, key_path


class TLSEchoServer:
    """Threaded TLS server that echoes bytes and records what the client negotiated."""

    def __init__(self, cert_path, key_path, *, low_security=False):
        """Start listening on a free loopback port."""
        self.sni = None
        self.alpn = None
        self.tls_version = None
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        if low_security:
            context.set_ciphers("DEFAULT:@SECLEVEL=0")
        context.load_cert_chain(cert_path, key_path)
        context.set_alpn_protocols(["h2", "http/1.1"])
        context.sni_callback = self._record_sni
        self._context = context
        self._listener = socket.socket()
        self._listener.bind(("127.0.0.1", 0))
        self._listener.listen()
        self.port = self._listener.getsockname()[1]
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()

    def _record_sni(self, _sock, server_name, _context):
        self.sni = server_name

    def _serve(self):
        while True:
            try:
                raw, _ = self._listener.accept()
            except OSError:
                return
            threading.Thread(target=self._echo, args=(raw,), daemon=True).start()

    def _echo(self, raw):
        try:
            with self._context.wrap_socket(raw, server_side=True) as tls:
                self.alpn = tls.selected_alpn_protocol()
                self.tls_version = tls.version()
                while data := tls.recv(4096):
                    tls.sendall(data)
        except (OSError, ssl.SSLError):
            pass

    def close(self):
        """Stop accepting connections."""
        self._listener.close()


class ConnectProxy:
    """Minimal HTTP CONNECT proxy that records requests and optionally demands Basic auth."""

    def __init__(self, *, require_auth=None):
        """Start listening on a free loopback port."""
        self.requests = []
        self._require_auth = require_auth
        self._listener = socket.socket()
        self._listener.bind(("127.0.0.1", 0))
        self._listener.listen()
        self.port = self._listener.getsockname()[1]
        threading.Thread(target=self._serve, daemon=True).start()

    def _serve(self):
        while True:
            try:
                client, _ = self._listener.accept()
            except OSError:
                return
            threading.Thread(target=self._handle, args=(client,), daemon=True).start()

    def _handle(self, client):
        head = b""
        while b"\r\n\r\n" not in head:
            chunk = client.recv(4096)
            if not chunk:
                client.close()
                return
            head += chunk
        lines = head.decode().split("\r\n")
        headers = {k.lower(): v for k, _, v in (line.partition(": ") for line in lines[1:] if line)}
        self.requests.append((lines[0], headers.get("proxy-authorization")))

        expected = None
        if self._require_auth:
            expected = "Basic " + base64.b64encode(self._require_auth.encode()).decode()
        if expected and headers.get("proxy-authorization") != expected:
            client.sendall(b"HTTP/1.1 407 Proxy Authentication Required\r\nContent-Length: 0\r\n\r\n")
            client.close()
            return

        host, _, port = lines[0].split(" ")[1].rpartition(":")
        upstream = socket.create_connection((host, int(port)))
        client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        for source, sink in ((client, upstream), (upstream, client)):
            threading.Thread(target=self._copy, args=(source, sink), daemon=True).start()

    @staticmethod
    def _copy(source, sink):
        try:
            while data := source.recv(4096):
                sink.sendall(data)
        except OSError:
            pass
        finally:
            sink.close()

    def close(self):
        """Stop accepting connections."""
        self._listener.close()


def round_trip(target, payload=b"ping"):
    """Send ``payload`` through a gRPC-style plaintext connection to ``target`` and return the echo."""
    if target.startswith("unix:"):
        sock = socket.socket(socket.AF_UNIX)
        sock.connect(target[len("unix:") :])
    else:
        host, port = split_authority(target)
        sock = socket.create_connection((host, port))
    with sock:
        sock.settimeout(5)
        sock.sendall(payload)
        return sock.recv(len(payload))


@pytest.fixture
def tunnels():
    """Collect tunnels so a failing test cannot leak a listener thread."""
    created = []

    def make(authority, **kwargs):
        tunnel = SkipVerifyTunnel(authority, **kwargs)
        created.append(tunnel)
        return tunnel

    yield make
    for tunnel in created:
        tunnel.close()


@pytest.fixture
def echo_server(tmp_path):
    """Echo server presenting an expired certificate whose name does not match the host."""
    cert, key = make_cert(tmp_path, expired=True)
    server = TLSEchoServer(cert, key)
    yield server
    server.close()


@pytest.mark.parametrize(
    "authority, expected",
    [
        ("example.com:8443", ("example.com", 8443)),
        ("example.com", ("example.com", 443)),
        ("127.0.0.1:80", ("127.0.0.1", 80)),
        ("[::1]:9000", ("::1", 9000)),
        ("[::1]", ("::1", 443)),
    ],
)
def test_split_authority(authority, expected):
    """Hosts, IPv4 and bracketed IPv6 literals split into host and port."""
    assert split_authority(authority) == expected


def test_tunnel_forwards_bytes_to_server_with_expired_mismatched_certificate(tunnels, echo_server):
    """Verification is skipped entirely: expiry and a wrong name do not stop the connection."""
    tunnel = tunnels(f"localhost:{echo_server.port}")

    assert round_trip(tunnel.target, b"hello over tls") == b"hello over tls"


def test_tunnel_sends_real_host_as_sni_and_offers_h2(tunnels, echo_server):
    """The server sees the dialled host as SNI, never a name taken from the certificate."""
    tunnel = tunnels(f"localhost:{echo_server.port}")

    round_trip(tunnel.target)

    assert echo_server.sni == "localhost"
    assert echo_server.alpn == "h2"
    assert echo_server.tls_version in ("TLSv1.2", "TLSv1.3")


def test_tunnel_follows_certificate_rotation(tunnels, tmp_path):
    """Nothing is pinned: a new certificate on the next connection is accepted."""
    first_dir, second_dir = tmp_path / "a", tmp_path / "b"
    first_dir.mkdir()
    second_dir.mkdir()
    first = TLSEchoServer(*make_cert(first_dir))
    tunnel = tunnels(f"localhost:{first.port}")
    assert round_trip(tunnel.target) == b"ping"
    first.close()

    second = TLSEchoServer(*make_cert(second_dir, dns=("other.internal",)))
    try:
        tunnel_two = tunnels(f"localhost:{second.port}")
        assert round_trip(tunnel_two.target) == b"ping"
    finally:
        second.close()


def test_tunnel_accepts_weak_certificate_like_go(tunnels, tmp_path):
    """A 1024-bit RSA key is accepted, as Go's InsecureSkipVerify does. OpenSSL's default floor refuses it."""
    try:
        cert, key = make_cert(tmp_path, key_bits=1024)
        server = TLSEchoServer(cert, key, low_security=True)
    except (ssl.SSLError, ValueError) as exc:
        pytest.skip(f"this OpenSSL cannot serve a weak certificate: {exc}")
    try:
        tunnel = tunnels(f"localhost:{server.port}")
        assert round_trip(tunnel.target) == b"ping"
    finally:
        server.close()


def test_tunnel_listens_on_private_unix_socket(tunnels, echo_server):
    """Where Unix sockets exist the listener is reachable only through a 0700 directory."""
    if not hasattr(socket, "AF_UNIX"):
        pytest.skip("no Unix sockets on this platform")
    tunnel = tunnels(f"localhost:{echo_server.port}")

    assert tunnel.target.startswith("unix:")
    directory = os.path.dirname(tunnel.target[len("unix:") :])
    assert os.stat(directory).st_mode & 0o777 == 0o700


def test_tunnel_close_is_idempotent_and_removes_socket(echo_server):
    """Closing twice is safe and leaves no socket directory behind."""
    tunnel = SkipVerifyTunnel(f"localhost:{echo_server.port}")
    target = tunnel.target

    tunnel.close()
    tunnel.close()

    if target.startswith("unix:"):
        assert not os.path.exists(os.path.dirname(target[len("unix:") :]))
    with pytest.raises(OSError):
        round_trip(target)


def test_tunnel_connects_through_http_proxy_with_basic_auth(tunnels, echo_server):
    """Credentials in the proxy URL are percent-decoded and sent as Proxy-Authorization."""
    proxy = ConnectProxy(require_auth="us@er:p/w")
    try:
        tunnel = tunnels(
            f"localhost:{echo_server.port}",
            proxy_url=f"http://us%40er:p%2Fw@127.0.0.1:{proxy.port}",
        )

        assert round_trip(tunnel.target) == b"ping"

        line, auth = proxy.requests[0]
        assert line == f"CONNECT localhost:{echo_server.port} HTTP/1.1"
        assert auth == "Basic " + base64.b64encode(b"us@er:p/w").decode()
    finally:
        proxy.close()


def test_tunnel_reports_proxy_rejection_without_forwarding(tunnels, echo_server, caplog):
    """A 407 from the proxy drops the connection and is logged with the status line."""
    proxy = ConnectProxy(require_auth="lab:lab")
    try:
        tunnel = tunnels(f"localhost:{echo_server.port}", proxy_url=f"http://127.0.0.1:{proxy.port}")
        with caplog.at_level(logging.WARNING):
            assert round_trip(tunnel.target) == b""
        assert "407" in caplog.text
        assert echo_server.sni is None
    finally:
        proxy.close()


def test_tunnel_rejects_https_proxy_url():
    """A gRPC channel cannot use an https:// proxy, so fail loudly instead of connecting direct."""
    with pytest.raises(DiodeConfigError, match="http:// proxy"):
        SkipVerifyTunnel("localhost:443", proxy_url="https://proxy.example.com:3128")
