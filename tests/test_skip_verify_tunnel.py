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
import gc
import logging
import os
import shutil
import socket
import ssl
import tempfile
import threading
import time
import types
from concurrent import futures
from unittest import mock
from urllib.parse import unquote

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
        self.open_connections = 0
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

    def reload(self, cert_path, key_path):
        """Present a different certificate to the next connection."""
        self._context.load_cert_chain(cert_path, key_path)

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
        self.open_connections += 1
        try:
            with self._context.wrap_socket(raw, server_side=True) as tls:
                self.alpn = tls.selected_alpn_protocol()
                self.tls_version = tls.version()
                while data := tls.recv(4096):
                    tls.sendall(data)
        except (OSError, ssl.SSLError):
            pass
        finally:
            self.open_connections -= 1

    def close(self):
        """Stop accepting connections."""
        self._listener.close()


class ConnectProxy:
    """Minimal HTTP CONNECT proxy that records requests and optionally demands Basic auth."""

    def __init__(self, *, require_auth=None, hang=False):
        """Start listening on a free loopback port. With ``hang`` the proxy never answers a CONNECT."""
        self.requests = []
        self._require_auth = require_auth
        self._hang = hang
        self._release = threading.Event()
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
        if self._hang:
            self._release.wait(30)
            client.close()
            return

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
        """Stop accepting connections and release any hanging CONNECT."""
        self._release.set()
        self._listener.close()


def connect_local(target):
    """Open a client socket to the tunnel's local listener."""
    if target.startswith("unix:"):
        sock = socket.socket(socket.AF_UNIX)
        try:
            sock.connect(unquote(target[len("unix:") :]))
        except OSError:
            sock.close()
            raise
        return sock
    host, port = split_authority(target)
    return socket.create_connection((host, port))


def round_trip(target, payload=b"ping"):
    """Send ``payload`` through a gRPC-style plaintext connection to ``target`` and return the echo."""
    with connect_local(target) as sock:
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
def percent_tmpdir(monkeypatch):
    """A short TMPDIR containing a literal percent escape, so the socket path stays under the length limit."""
    if not hasattr(socket, "AF_UNIX") or not os.path.isdir("/tmp"):
        pytest.skip("needs Unix sockets and /tmp")
    directory = tempfile.mkdtemp(prefix="p%41", dir="/tmp")
    monkeypatch.setattr(tempfile, "tempdir", directory)
    yield directory
    shutil.rmtree(directory, ignore_errors=True)


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
    """Nothing is pinned: the same tunnel accepts a different certificate on the next connection."""
    first_dir, second_dir = tmp_path / "a", tmp_path / "b"
    first_dir.mkdir()
    second_dir.mkdir()
    server = TLSEchoServer(*make_cert(first_dir))
    try:
        tunnel = tunnels(f"localhost:{server.port}")
        assert round_trip(tunnel.target) == b"ping"

        server.reload(*make_cert(second_dir, dns=("other.internal",)))

        assert round_trip(tunnel.target) == b"ping"
    finally:
        server.close()


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


@pytest.mark.parametrize("error", [NotImplementedError, AttributeError])
def test_tunnel_treats_an_unsupported_unix_server_like_a_missing_one(error, monkeypatch):
    """The Windows Proactor loop exposes start_unix_server but cannot serve it. That must reach the fallback."""

    async def unsupported(*_args, **_kwargs):
        raise error("create_unix_server")

    monkeypatch.setattr(asyncio, "start_unix_server", unsupported)
    monkeypatch.delenv(tunnel_module.ALLOW_LOOPBACK_ENVVAR_NAME, raising=False)

    with pytest.raises(DiodeConfigError, match="DIODE_SKIP_TLS_VERIFY_ALLOW_LOOPBACK"):
        SkipVerifyTunnel("localhost:443")

    monkeypatch.setenv(tunnel_module.ALLOW_LOOPBACK_ENVVAR_NAME, "true")
    monkeypatch.setattr(tunnel_module, "_loopback_warned", True)
    tunnel = SkipVerifyTunnel("localhost:443")
    try:
        assert tunnel.target.startswith("127.0.0.1:")
    finally:
        tunnel.close()


def test_tunnel_skips_unix_server_on_windows(monkeypatch):
    """On win32 the Unix socket path is not attempted at all."""
    called = []

    async def record(*_args, **_kwargs):
        called.append(True)
        raise AssertionError("must not be called on win32")

    monkeypatch.setattr(asyncio, "start_unix_server", record)
    monkeypatch.setattr(tunnel_module, "sys", types.SimpleNamespace(platform="win32"))
    monkeypatch.setenv(tunnel_module.ALLOW_LOOPBACK_ENVVAR_NAME, "true")
    monkeypatch.setattr(tunnel_module, "_loopback_warned", True)

    tunnel = SkipVerifyTunnel("localhost:443")
    try:
        assert tunnel.target.startswith("127.0.0.1:")
        assert not called
    finally:
        tunnel.close()


def test_tunnel_close_from_its_own_thread_does_not_hang_or_leak(echo_server):
    """A finalizer can run on the loop thread, which cannot wait for itself."""
    tunnel = SkipVerifyTunnel(f"localhost:{echo_server.port}")
    directory = os.path.dirname(unquote(tunnel.target[len("unix:") :])) if tunnel.target.startswith("unix:") else None

    started = time.monotonic()
    tunnel._loop.call_soon_threadsafe(tunnel.close)
    tunnel._thread.join(timeout=5)

    assert time.monotonic() - started < 2
    assert not tunnel._thread.is_alive()
    assert tunnel._loop.is_closed()
    if directory:
        assert not os.path.exists(directory)


@pytest.mark.skipif(not hasattr(os, "fork"), reason="needs fork")
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_close_in_a_forked_child_leaves_the_parents_tunnel_alone(tunnels, echo_server):
    """A forked worker exiting through atexit must not delete the socket the parent still uses."""
    tunnel = tunnels(f"localhost:{echo_server.port}")
    assert round_trip(tunnel.target) == b"ping"

    pid = os.fork()
    if pid == 0:
        started = time.monotonic()
        tunnel.close()
        os._exit(0 if time.monotonic() - started < 1 else 1)
    _, status = os.waitpid(pid, 0)

    assert os.WEXITSTATUS(status) == 0
    assert round_trip(tunnel.target) == b"ping"


@pytest.mark.parametrize("proxy_url", ["http://h:99999", "http://u:p@:1", "http://", "http://h:0"])
def test_tunnel_rejects_unusable_proxy_url_up_front(proxy_url):
    """A bad proxy URL fails the constructor, instead of every connection later."""
    with pytest.raises(DiodeConfigError, match="host or port"):
        SkipVerifyTunnel("localhost:443", proxy_url=proxy_url)


def test_tunnel_records_why_a_dial_failed(tunnels):
    """The reason is kept so the client can add it to the otherwise bare UNAVAILABLE error."""
    refused = socket.socket()
    refused.bind(("127.0.0.1", 0))
    port = refused.getsockname()[1]
    refused.close()
    tunnel = tunnels(f"127.0.0.1:{port}")

    assert round_trip(tunnel.target) == b""

    assert tunnel.last_error and f"127.0.0.1:{port}" in tunnel.last_error


def test_tunnel_records_a_proxy_rejection(tunnels, echo_server):
    """A 407 from the proxy is the recorded reason."""
    proxy = ConnectProxy(require_auth="lab:lab")
    try:
        tunnel = tunnels(f"localhost:{echo_server.port}", proxy_url=f"http://127.0.0.1:{proxy.port}")
        round_trip(tunnel.target)
        assert "407" in tunnel.last_error
    finally:
        proxy.close()


def test_proxy_credentials_are_decoded_as_bytes(tunnels, echo_server):
    """A non-UTF-8 percent escape reaches the proxy as the raw byte, as Go sends it."""
    proxy = ConnectProxy()
    try:
        tunnel = tunnels(f"localhost:{echo_server.port}", proxy_url=f"http://us%E9er:pw@127.0.0.1:{proxy.port}")
        assert round_trip(tunnel.target) == b"ping"
        assert proxy.requests[0][1] == "Basic " + base64.b64encode(b"us\xe9er:pw").decode()
    finally:
        proxy.close()


def test_tunnel_socket_path_with_percent_in_tmpdir_is_escaped(tunnels, echo_server, percent_tmpdir):
    """A literal % in TMPDIR has to be escaped in the unix: target, which gRPC percent-decodes."""
    tunnel = tunnels(f"localhost:{echo_server.port}")

    assert "%2541" in tunnel.target
    assert round_trip(tunnel.target) == b"ping"


def test_tunnel_close_cancels_a_connect_that_is_still_in_flight(echo_server):
    """close() must not leave the event loop running while a proxy CONNECT is unanswered."""
    proxy = ConnectProxy(hang=True)
    tunnel = SkipVerifyTunnel(f"localhost:{echo_server.port}", proxy_url=f"http://127.0.0.1:{proxy.port}")
    try:
        with connect_local(tunnel.target) as sock:
            sock.sendall(b"ping")
            deadline = time.monotonic() + 5
            while not proxy.requests and time.monotonic() < deadline:
                time.sleep(0.02)
            assert proxy.requests, "the tunnel never reached the proxy"

            started = time.monotonic()
            tunnel.close()
            elapsed = time.monotonic() - started

        assert elapsed < 2
        assert not tunnel._thread.is_alive()
        assert tunnel._loop.is_closed()
        assert not tunnel._tasks
    finally:
        tunnel.close()
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


def test_tunnel_refuses_loopback_fallback_by_default(monkeypatch):
    """Without Unix sockets the unauthenticated loopback listener is off unless the user opts in."""
    monkeypatch.delattr(asyncio, "start_unix_server")
    monkeypatch.delenv(tunnel_module.ALLOW_LOOPBACK_ENVVAR_NAME, raising=False)

    with pytest.raises(DiodeConfigError, match="DIODE_SKIP_TLS_VERIFY_ALLOW_LOOPBACK"):
        SkipVerifyTunnel("localhost:443")

    assert not [t for t in threading.enumerate() if t.name == "diode-skip-verify-tunnel"]


def test_tunnel_loopback_fallback_works_when_opted_in_and_warns_once(tunnels, echo_server, monkeypatch, caplog):
    """Opting in gives the loopback listener, and the reduced isolation is logged once."""
    monkeypatch.delattr(asyncio, "start_unix_server")
    monkeypatch.setenv(tunnel_module.ALLOW_LOOPBACK_ENVVAR_NAME, "true")
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
    with mock.patch("grpc.secure_channel") as secure_channel, mock.patch("grpc.insecure_channel") as insecure_channel:
        client = DiodeClient(
            target="grpcs://example.com:8443",
            app_name="tls-test",
            app_version="0.0.1",
            client_id="id",
            client_secret="secret",
        )

    insecure_channel.assert_not_called()
    args, kwargs = secure_channel.call_args
    assert args[0] == "example.com:8443"
    options = dict(kwargs["options"])
    assert "grpc.default_authority" not in options
    assert "grpc.enable_http_proxy" not in options
    assert client._tunnel is None


def test_client_error_names_the_tunnel_failure(stub_auth):
    """An unreachable server surfaces its real cause, not just a bare UNAVAILABLE."""
    refused = socket.socket()
    refused.bind(("127.0.0.1", 0))
    port = refused.getsockname()[1]
    refused.close()

    with _client(port, skip_tls_verify=True) as client, pytest.raises(DiodeClientError) as excinfo:
        _ingest(client)

    assert "skip-verify tunnel" in excinfo.value.details
    assert f"127.0.0.1:{port}" in excinfo.value.details


def test_client_channel_keeps_working_after_the_client_is_collected(grpc_tls_server, stub_auth):
    """client.channel is public: the tunnel must live as long as the channel, not as long as the client."""
    channel = _client(grpc_tls_server, skip_tls_verify=True).channel
    gc.collect()

    stub = ingester_pb2_grpc.IngesterServiceStub(channel)
    assert not stub.Ingest(ingester_pb2.IngestRequest(), timeout=5).errors
    channel.close()


def test_percent_in_tmpdir_works_end_to_end(grpc_tls_server, stub_auth, percent_tmpdir):
    """A literal % in TMPDIR must not break the channel gRPC builds from the unix: target."""
    with _client(grpc_tls_server, skip_tls_verify=True) as client:
        assert not _ingest(client).errors


def test_proxy_credentials_are_redacted_from_logs(stub_auth, monkeypatch, caplog):
    """Proxy credentials must not appear in the debug or warning log lines."""
    monkeypatch.setenv("HTTPS_PROXY", "http://user:secret@proxy.example.com:8080")
    tunnel = mock.Mock(target="unix:/tmp/t.sock", last_error=None)
    with (
        caplog.at_level(logging.DEBUG, logger="netboxlabs.diode.sdk.client"),
        mock.patch("netboxlabs.diode.sdk.client.SkipVerifyTunnel", return_value=tunnel),
        mock.patch("grpc.insecure_channel"),
    ):
        DiodeClient(
            target="grpcs://example.com:8443",
            app_name="tls-test",
            app_version="0.0.1",
            client_id="id",
            client_secret="secret",
            skip_tls_verify=True,
        )

    assert "secret" not in caplog.text
    assert "***@proxy.example.com:8080" in caplog.text


@pytest.mark.skipif(not os.path.isdir("/dev/fd"), reason="counts open descriptors through /dev/fd")
def test_closing_clients_leaves_no_descriptors_behind(grpc_tls_server, stub_auth):
    """Each close() must close its upstream TLS socket itself rather than leave it to the garbage collector."""

    def cycle():
        with _client(grpc_tls_server, skip_tls_verify=True) as client:
            _ingest(client)

    cycle()  # one-off setup is not a leak
    gc.collect()
    gc.disable()
    try:
        time.sleep(0.3)
        before = len(os.listdir("/dev/fd"))
        for _ in range(6):
            cycle()
        time.sleep(0.5)
        after = len(os.listdir("/dev/fd"))
    finally:
        gc.enable()

    assert after <= before
