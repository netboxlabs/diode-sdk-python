#!/usr/bin/env python
# Copyright 2026 NetBox Labs Inc
"""
Local TLS tunnel that gives grpcio the semantics of Go's ``InsecureSkipVerify``.

grpcio offers no way to turn certificate verification off for a secure channel.
The only knobs are the trusted roots and ``grpc.ssl_target_name_override``, which
can only emulate skipping by pinning the server leaf and renaming the peer. That
breaks as soon as the certificate expires, the name is not a single-label wildcard
match, the server picks a certificate by SNI, the leaf rotates, or Host-based
routing looks at ``:authority``.

This module avoids all of that. gRPC speaks plaintext HTTP/2 to a private local
listener (a Unix socket in a 0700 directory where available, loopback otherwise)
and the tunnel carries each connection to the real server over TLS with
verification disabled. The server sees what it would see from Go: the real host as
SNI and ``:authority``, no pinning, any certificate.
"""

import asyncio
import base64
import contextlib
import logging
import os
import shutil
import socket
import ssl
import sys
import tempfile
import threading
from urllib.parse import quote, unquote_to_bytes, urlparse

from netboxlabs.diode.sdk.exceptions import DiodeConfigError

_LOGGER = logging.getLogger(__name__)

ALLOW_LOOPBACK_ENVVAR_NAME = "DIODE_SKIP_TLS_VERIFY_ALLOW_LOOPBACK"

_CONNECT_TIMEOUT_S = 10.0
_HANDSHAKE_TIMEOUT_S = 10.0
_STARTUP_TIMEOUT_S = 10.0
_SHUTDOWN_TIMEOUT_S = 5.0
# Time to flush a TLS close_notify. Peers such as grpc-core never answer it, and Go does not wait for the reply either.
_CLOSE_TIMEOUT_S = 0.1
_CHUNK_SIZE = 64 * 1024
_PROXY_RESPONSE_LIMIT = 16 * 1024
# sun_path is 104 bytes on macOS and 108 on Linux.
_UNIX_PATH_LIMIT = 100


def split_authority(authority: str, default_port: int = 443) -> tuple[str, int]:
    """Split ``host:port`` or ``[v6]:port`` into a bare host and a port."""
    if authority.startswith("["):
        host, _, rest = authority[1:].partition("]")
        port = rest.lstrip(":")
        return host, int(port) if port else default_port
    host, separator, port = authority.rpartition(":")
    if not separator:
        return authority, default_port
    return host, int(port)


def _bracket(host: str) -> str:
    return f"[{host}]" if ":" in host else host


def _client_context() -> ssl.SSLContext:
    """TLS client context that accepts any certificate, as Go's InsecureSkipVerify does."""
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.set_alpn_protocols(["h2"])
    return context


async def _http_connect(sock: socket.socket, host: str, port: int, proxy) -> None:
    """Open a tunnel through an HTTP proxy with CONNECT. Every await here can be cancelled."""
    loop = asyncio.get_running_loop()
    authority = f"{_bracket(host)}:{port}"
    lines = [f"CONNECT {authority} HTTP/1.1", f"Host: {authority}"]
    if proxy.username is not None:
        credentials = unquote_to_bytes(proxy.username) + b":" + unquote_to_bytes(proxy.password or "")
        token = base64.b64encode(credentials).decode()
        lines.append(f"Proxy-Authorization: Basic {token}")
    await loop.sock_sendall(sock, ("\r\n".join(lines) + "\r\n\r\n").encode())

    response = b""
    while b"\r\n\r\n" not in response:
        chunk = await asyncio.wait_for(loop.sock_recv(sock, 4096), _CONNECT_TIMEOUT_S)
        if not chunk:
            raise DiodeConfigError(f"Proxy closed the connection during CONNECT to {authority}")
        response += chunk
        if len(response) > _PROXY_RESPONSE_LIMIT:
            raise DiodeConfigError(f"Proxy CONNECT response for {authority} is too large")

    status_line = response.split(b"\r\n", 1)[0].decode("latin1")
    parts = status_line.split(" ", 2)
    if len(parts) < 2 or parts[1] != "200":
        raise DiodeConfigError(f"Proxy CONNECT to {authority} failed: {status_line}")


async def _open_socket(host: str, port: int) -> socket.socket:
    """Connect a TCP socket without blocking a thread, so close() can cancel it."""
    loop = asyncio.get_running_loop()
    last_error: BaseException = OSError(f"No address found for {_bracket(host)}:{port}")
    addresses = await asyncio.wait_for(loop.getaddrinfo(host, port, type=socket.SOCK_STREAM), _CONNECT_TIMEOUT_S)
    for family, kind, proto, _, address in addresses:
        sock = socket.socket(family, kind, proto)
        sock.setblocking(False)
        try:
            await asyncio.wait_for(loop.sock_connect(sock, address), _CONNECT_TIMEOUT_S)
        except (OSError, asyncio.TimeoutError) as exc:
            sock.close()
            last_error = exc
        except BaseException:
            sock.close()
            raise
        else:
            return sock
    raise last_error


_loopback_warned = False


def _allow_loopback() -> bool:
    return os.getenv(ALLOW_LOOPBACK_ENVVAR_NAME, "").lower() in ("true", "1", "yes", "on")


def _warn_loopback_once() -> None:
    global _loopback_warned
    if not _loopback_warned:
        _loopback_warned = True
        _LOGGER.warning(
            f"Skip-verify tunnel is listening on 127.0.0.1 because {ALLOW_LOOPBACK_ENVVAR_NAME} is set and Unix sockets "
            "are unavailable. Any local user can connect to it and reach the server through this client's proxy settings."
        )


async def _close_stream(stream: asyncio.StreamWriter) -> None:
    """Close a stream, then abort its transport if the peer has not finished closing it almost at once."""
    stream.close()
    try:
        await asyncio.wait_for(stream.wait_closed(), _CLOSE_TIMEOUT_S)
    except asyncio.CancelledError:
        stream.transport.abort()
        raise
    except (OSError, ssl.SSLError, asyncio.TimeoutError):
        stream.transport.abort()


async def _pipe(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    """Copy bytes until the source ends or either side fails."""
    try:
        while data := await reader.read(_CHUNK_SIZE):
            writer.write(data)
            await writer.drain()
    except (OSError, ssl.SSLError):
        pass


class SkipVerifyTunnel:
    """Plaintext local listener that forwards every connection over unverified TLS."""

    def __init__(self, authority: str, *, proxy_url: str | None = None):
        """Start the tunnel for ``authority`` (``host:port``), optionally through an HTTP proxy."""
        self._host, self._port = split_authority(authority)
        self._proxy = None
        if proxy_url:
            # The URL scheme is advisory. Like grpc-go, the tunnel always sends a plain
            # CONNECT, so an https:// URL works with the usual plain-HTTP proxy.
            self._proxy = urlparse(proxy_url)
            try:
                valid = bool(self._proxy.hostname) and (self._proxy.port is None or self._proxy.port > 0)
            except ValueError:
                valid = False
            if not valid:
                raise DiodeConfigError("Proxy URL has no usable host or port")

        self._pid = os.getpid()
        self.last_error: str | None = None
        self._context = _client_context()
        self._loop = asyncio.new_event_loop()
        self._tasks: set[asyncio.Task] = set()
        self._server: asyncio.AbstractServer | None = None
        self._tmpdir: str | None = None
        self._closed = False
        self._close_lock = threading.Lock()

        self._thread = threading.Thread(target=self._run_loop, name="diode-skip-verify-tunnel", daemon=True)
        self._thread.start()
        try:
            self.target: str = asyncio.run_coroutine_threadsafe(self._listen(), self._loop).result(timeout=_STARTUP_TIMEOUT_S)
        except BaseException:
            self.close()
            raise
        _LOGGER.debug(f"Skip-verify tunnel {self.target} -> {_bracket(self._host)}:{self._port}")

    def _run_loop(self) -> None:
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_forever()
        finally:
            self._loop.close()
            self._remove_tmpdir()

    def _unix_socket_path(self) -> str | None:
        """Create the private socket directory and return the socket path inside it."""
        for base in (None, "/tmp"):
            if base is not None and not os.path.isdir(base):
                continue
            directory = tempfile.mkdtemp(prefix="diode-", dir=base)
            path = os.path.join(directory, "t.sock")
            if len(path) < _UNIX_PATH_LIMIT:
                self._tmpdir = directory
                return path
            shutil.rmtree(directory, ignore_errors=True)
        return None

    async def _listen(self) -> str:
        if sys.platform != "win32" and hasattr(asyncio, "start_unix_server"):
            try:
                path = self._unix_socket_path()
                if path:
                    self._server = await asyncio.start_unix_server(self._handle, path=path)
                    return f"unix:{quote(path, safe='/')}"
            except (OSError, NotImplementedError, AttributeError) as exc:
                _LOGGER.debug(f"Unix socket unavailable for skip-verify tunnel: {exc!r}")
            self._remove_tmpdir()

        if not _allow_loopback():
            raise DiodeConfigError(
                "DIODE_SKIP_TLS_VERIFY needs a Unix socket, which is unavailable here. The fallback is a loopback port that "
                "any local user can connect to, so it is off by default. "
                f"Set {ALLOW_LOOPBACK_ENVVAR_NAME}=true to accept that, or use DIODE_CERT_FILE instead."
            )
        _warn_loopback_once()
        self._server = await asyncio.start_server(self._handle, "127.0.0.1", 0)
        return f"127.0.0.1:{self._server.sockets[0].getsockname()[1]}"

    async def _connect(self) -> socket.socket:
        if self._proxy is None:
            sock = await _open_socket(self._host, self._port)
        else:
            proxy_port = self._proxy.port or (443 if self._proxy.scheme == "https" else 80)
            sock = await _open_socket(self._proxy.hostname, proxy_port)
            try:
                await _http_connect(sock, self._host, self._port, self._proxy)
            except BaseException:
                sock.close()
                raise
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        return sock

    async def _dial(self) -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        sock = await self._connect()
        try:
            return await asyncio.open_connection(
                sock=sock,
                ssl=self._context,
                server_hostname=self._host,
                ssl_handshake_timeout=_HANDSHAKE_TIMEOUT_S,
            )
        except BaseException:
            sock.close()
            raise

    async def _handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        task = asyncio.current_task()
        self._tasks.add(task)
        upstream_writer = None
        try:
            upstream_reader, upstream_writer = await self._dial()
            pipes = [
                asyncio.ensure_future(_pipe(reader, upstream_writer)),
                asyncio.ensure_future(_pipe(upstream_reader, writer)),
            ]
            try:
                await asyncio.wait(pipes, return_when=asyncio.FIRST_COMPLETED)
            finally:
                for pipe in pipes:
                    pipe.cancel()
                await asyncio.gather(*pipes, return_exceptions=True)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            self.last_error = f"{_bracket(self._host)}:{self._port}: {exc}"
            _LOGGER.warning(f"Skip-verify tunnel to {self.last_error}")
        finally:
            try:
                for stream in (upstream_writer, writer):
                    if stream is not None:
                        await _close_stream(stream)
            finally:
                self._tasks.discard(task)

    async def _shutdown(self) -> None:
        if self._server is not None:
            self._server.close()
        tasks = list(self._tasks)
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        with contextlib.suppress(asyncio.TimeoutError):
            await asyncio.wait_for(self._loop.shutdown_default_executor(), _SHUTDOWN_TIMEOUT_S / 2)

    def _remove_tmpdir(self) -> None:
        if self._tmpdir:
            shutil.rmtree(self._tmpdir, ignore_errors=True)
            self._tmpdir = None

    async def _shutdown_and_stop(self) -> None:
        await self._shutdown()
        self._loop.stop()

    def close(self) -> None:
        """Stop the listener, drop live connections and remove the socket. Safe to call twice."""
        with self._close_lock:
            if self._closed:
                return
            self._closed = True

        if os.getpid() != self._pid:
            # A forked child shares the parent's socket path but not its loop thread. Leave both alone.
            return

        if threading.current_thread() is self._thread:
            # Reached from a garbage-collection pass on the loop thread: it cannot wait for itself.
            self._loop.create_task(self._shutdown_and_stop())
            return

        if self._loop.is_running():
            with contextlib.suppress(Exception):
                asyncio.run_coroutine_threadsafe(self._shutdown(), self._loop).result(timeout=_SHUTDOWN_TIMEOUT_S)
            self._loop.call_soon_threadsafe(self._loop.stop)
        self._thread.join(timeout=_SHUTDOWN_TIMEOUT_S)
        self._remove_tmpdir()
