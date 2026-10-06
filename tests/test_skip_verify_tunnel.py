#!/usr/bin/env python
# Copyright 2026 NetBox Labs Inc
"""
NetBox Labs - Tests for skip-TLS-verify behaviour.

These tests use real TLS servers. Mocking the TLS layer is what let the earlier
pin-and-rename implementation ship with every skip-verify test passing while the
real handshake still failed.
"""

import asyncio
import base64
import datetime as dt
import logging
import os
import socket
import ssl
import tempfile
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
from netboxlabs.diode.sdk import _skip_verify_tunnel as tunnel_module
from netboxlabs.diode.sdk._skip_verify_tunnel import SkipVerifyTunnel, split_authority
from netboxlabs.diode.sdk.client import DiodeOTLPClient
from netboxlabs.diode.sdk.diode.v1 import ingester_pb2, ingester_pb2_grpc
from netboxlabs.diode.sdk.exceptions import DiodeClientError
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


def test_tunnel_accepts_https_scheme_proxy_url_and_sends_plain_connect(tunnels, echo_server):
    """An https:// proxy URL is treated like grpc-go treats it: a plain CONNECT to the proxy."""
    proxy = ConnectProxy()
    try:
        tunnel = tunnels(f"localhost:{echo_server.port}", proxy_url=f"https://127.0.0.1:{proxy.port}")

        assert round_trip(tunnel.target) == b"ping"
        assert proxy.requests[0][0] == f"CONNECT localhost:{echo_server.port} HTTP/1.1"
    finally:
        proxy.close()


def test_tunnel_retries_in_tmp_when_the_temp_path_is_too_long(tunnels, echo_server, tmp_path, monkeypatch):
    """A long TMPDIR must not push the tunnel onto the unauthenticated loopback listener."""
    if not hasattr(socket, "AF_UNIX") or not os.path.isdir("/tmp"):
        pytest.skip("needs Unix sockets and /tmp")
    long_dir = tmp_path / ("d" * 90)
    long_dir.mkdir()
    monkeypatch.setattr(tempfile, "tempdir", str(long_dir))

    tunnel = tunnels(f"localhost:{echo_server.port}")

    assert tunnel.target.startswith("unix:/tmp/")
    assert round_trip(tunnel.target) == b"ping"


def test_tunnel_falls_back_to_loopback_and_warns_once(tunnels, echo_server, monkeypatch, caplog):
    """Without Unix sockets the loopback listener works and the reduced isolation is logged once."""
    monkeypatch.delattr(asyncio, "start_unix_server")
    monkeypatch.setattr(tunnel_module, "_loopback_warned", False)

    with caplog.at_level(logging.WARNING):
        first = tunnels(f"localhost:{echo_server.port}")
        second = tunnels(f"localhost:{echo_server.port}")

    assert first.target.startswith("127.0.0.1:")
    assert round_trip(second.target) == b"ping"
    assert caplog.text.count("listening on 127.0.0.1") == 1


class _IngesterServicer(ingester_pb2_grpc.IngesterServiceServicer):
    def Ingest(self, request, context):  # noqa: N802
        return ingester_pb2.IngestResponse()


class _LogsServicer(logs_service_pb2_grpc.LogsServiceServicer):
    def Export(self, request, context):  # noqa: N802
        return logs_service_pb2.ExportLogsServiceResponse()


@pytest.fixture
def grpc_tls_server(tmp_path):
    """Real gRPC server over TLS with an expired certificate whose SAN does not match 127.0.0.1."""
    cert, key = make_cert(tmp_path, expired=True)
    with open(key, "rb") as kf, open(cert, "rb") as cf:
        credentials = grpc.ssl_server_credentials([(kf.read(), cf.read())])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    ingester_pb2_grpc.add_IngesterServiceServicer_to_server(_IngesterServicer(), server)
    logs_service_pb2_grpc.add_LogsServiceServicer_to_server(_LogsServicer(), server)
    port = server.add_secure_port("127.0.0.1:0", credentials)
    server.start()
    yield port
    server.stop(0)


@pytest.fixture
def stub_auth():
    """Skip the OAuth token request; these tests are about the gRPC channel."""
    with mock.patch("netboxlabs.diode.sdk.client._DiodeAuthentication.authenticate", return_value="token"):
        yield


def _client(port, **kwargs):
    return DiodeClient(
        target=f"grpcs://127.0.0.1:{port}",
        app_name="tls-test",
        app_version="0.0.1",
        client_id="id",
        client_secret="secret",
        **kwargs,
    )


def _ingest(client):
    return client.ingest(entities=[Entity(site=Site(name="tls-test"))])


def test_client_fails_by_default_against_untrusted_certificate(grpc_tls_server, stub_auth):
    """Control: without skip-verify the same server is rejected."""
    with _client(grpc_tls_server) as client, pytest.raises(DiodeClientError):
        _ingest(client)


def test_client_skip_tls_verify_argument_ingests_through_expired_mismatched_certificate(grpc_tls_server, stub_auth):
    """skip_tls_verify=True behaves like Go: expiry and a name mismatch are ignored."""
    with _client(grpc_tls_server, skip_tls_verify=True) as client:
        assert not _ingest(client).errors


def test_client_env_var_ingests_through_expired_mismatched_certificate(grpc_tls_server, stub_auth, monkeypatch):
    """DIODE_SKIP_TLS_VERIFY has the same effect as the constructor argument."""
    monkeypatch.setenv("DIODE_SKIP_TLS_VERIFY", "true")
    with _client(grpc_tls_server) as client:
        assert not _ingest(client).errors


def test_client_close_stops_the_tunnel(grpc_tls_server, stub_auth):
    """Closing the client tears the tunnel down."""
    client = _client(grpc_tls_server, skip_tls_verify=True)
    tunnel = client._tunnel
    assert tunnel is not None

    client.close()

    with pytest.raises(OSError):
        round_trip(tunnel.target)


def test_otlp_client_skip_tls_verify(grpc_tls_server):
    """The OTLP client shares the same skip-verify channel."""
    with DiodeOTLPClient(
        target=f"grpcs://127.0.0.1:{grpc_tls_server}",
        app_name="tls-test",
        app_version="0.0.1",
        skip_tls_verify=True,
    ) as client:
        assert not client.ingest(entities=[Entity(site=Site(name="tls-test"))]).errors


def test_plaintext_target_ignores_skip_tls_verify(stub_auth):
    """skip_tls_verify must not change a plaintext target, and needs no tunnel."""
    client = DiodeClient(
        target="grpc://127.0.0.1:1",
        app_name="tls-test",
        app_version="0.0.1",
        client_id="id",
        client_secret="secret",
        skip_tls_verify=True,
    )
    try:
        assert client._tunnel is None
    finally:
        client.close()


def test_secure_target_with_skip_uses_tunnel_channel_not_proxy_option(stub_auth, monkeypatch):
    """The tunnel owns the proxy hop. gRPC gets an insecure local channel with the real authority."""
    monkeypatch.setenv("HTTPS_PROXY", "http://proxy.example.com:8080")
    tunnel = mock.Mock(target="unix:/tmp/t.sock")
    with (
        mock.patch("netboxlabs.diode.sdk.client.SkipVerifyTunnel", return_value=tunnel) as tunnel_cls,
        mock.patch("grpc.insecure_channel") as insecure_channel,
        mock.patch("grpc.secure_channel") as secure_channel,
    ):
        DiodeClient(
            target="grpcs://example.com:8443",
            app_name="tls-test",
            app_version="0.0.1",
            client_id="id",
            client_secret="secret",
            skip_tls_verify=True,
        )

    tunnel_cls.assert_called_once_with("example.com:8443", proxy_url="http://proxy.example.com:8080")
    secure_channel.assert_not_called()
    args, kwargs = insecure_channel.call_args
    assert args[0] == "unix:/tmp/t.sock"
    options = dict(kwargs["options"])
    assert options["grpc.default_authority"] == "example.com:8443"
    assert options["grpc.enable_http_proxy"] == 0
    assert "grpc.http_proxy" not in options
    assert "grpc.ssl_target_name_override" not in options


def test_secure_target_with_verification_still_uses_secure_channel(stub_auth):
    """Default behaviour is untouched: verification on means a normal secure channel and no tunnel."""
    with mock.patch("grpc.secure_channel") as secure_channel:
        client = DiodeClient(
            target="grpcs://example.com:8443",
            app_name="tls-test",
            app_version="0.0.1",
            client_id="id",
            client_secret="secret",
        )

    secure_channel.assert_called_once()
    assert client._tunnel is None
