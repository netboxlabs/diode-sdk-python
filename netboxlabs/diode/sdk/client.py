#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs, Diode - SDK - Client."""
import collections
import logging
import os
import platform
import uuid
from collections.abc import Iterable
from urllib.parse import urlparse

import certifi
import grpc
import sentry_sdk

from netboxlabs.diode.sdk.diode.v1 import ingester_pb2, ingester_pb2_grpc
from netboxlabs.diode.sdk.exceptions import DiodeClientError, DiodeConfigError
from netboxlabs.diode.sdk.ingester import Entity

_DIODE_API_KEY_ENVVAR_NAME = "DIODE_API_KEY"
_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME = "DIODE_SDK_LOG_LEVEL"
_DIODE_SENTRY_DSN_ENVVAR_NAME = "DIODE_SENTRY_DSN"
_DEFAULT_STREAM = "latest"
_LOGGER = logging.getLogger(__name__)


def _load_certs() -> bytes:
    """Loads cacert.pem."""
    with open(certifi.where(), "rb") as f:
        return f.read()


def _get_api_key(api_key: str | None = None) -> str:
    """Get API Key either from provided value or environment variable."""
    if api_key is None:
        api_key = os.getenv(_DIODE_API_KEY_ENVVAR_NAME)
    if api_key is None:
        raise DiodeConfigError(
            f"api_key param or {_DIODE_API_KEY_ENVVAR_NAME} environment variable required"
        )
    return api_key


def parse_target(target: str) -> tuple[str, str, bool]:
    """Parse the target into authority, path and tls_verify."""
    parsed_target = urlparse(target)

    if parsed_target.scheme not in ["grpc", "grpcs"]:
        raise ValueError("target should start with grpc:// or grpcs://")

    tls_verify = parsed_target.scheme == "grpcs"

    authority = parsed_target.netloc

    if ":" not in authority:
        authority += ":443"

    return authority, parsed_target.path, tls_verify


def _get_sentry_dsn(sentry_dsn: str | None = None) -> str | None:
    """Get Sentry DSN either from provided value or environment variable."""
    if sentry_dsn is None:
        sentry_dsn = os.getenv(_DIODE_SENTRY_DSN_ENVVAR_NAME)
    return sentry_dsn


class DiodeClient:
    """Diode Client."""

    _name = "diode-sdk-python"
    _version = "0.0.1"
    _app_name = None
    _app_version = None
    _channel = None
    _stub = None

    def __init__(
        self,
        target: str,
        app_name: str,
        app_version: str,
        api_key: str | None = None,
        sentry_dsn: str = None,
        sentry_traces_sample_rate: float = 1.0,
        sentry_profiles_sample_rate: float = 1.0,
    ):
        """Initiate a new client."""
        log_level = os.getenv(_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME, "INFO").upper()
        logging.basicConfig(level=log_level)

        self._target, self._path, self._tls_verify = parse_target(target)
        self._app_name = app_name
        self._app_version = app_version
        self._platform = platform.platform()
        self._python_version = platform.python_version()

        api_key = _get_api_key(api_key)
        self._metadata = (
            ("diode-api-key", api_key),
            ("platform", self._platform),
            ("python-version", self._python_version),
        )

        if self._tls_verify:
            _LOGGER.debug("Setting up gRPC secure channel")
            self._channel = grpc.secure_channel(
                self._target,
                grpc.ssl_channel_credentials(
                    root_certificates=_load_certs(),
                ),
            )
        else:
            _LOGGER.debug("Setting up gRPC insecure channel")
            self._channel = grpc.insecure_channel(
                target=self._target,
            )

        channel = self._channel

        if self._path:
            _LOGGER.debug(f"Setting up gRPC interceptor for path: {self._path}")
            rpc_method_interceptor = DiodeMethodClientInterceptor(subpath=self._path)

            intercept_channel = grpc.intercept_channel(
                self._channel, rpc_method_interceptor
            )
            channel = intercept_channel

        self._stub = ingester_pb2_grpc.IngesterServiceStub(channel)

        self._sentry_dsn = _get_sentry_dsn(sentry_dsn)

        if self._sentry_dsn is not None:
            _LOGGER.debug("Setting up Sentry")
            self._setup_sentry(
                self._sentry_dsn, sentry_traces_sample_rate, sentry_profiles_sample_rate
            )

    @property
    def name(self) -> str:
        """Retrieve the name."""
        return self._name

    @property
    def version(self) -> str:
        """Retrieve the version."""
        return self._version

    @property
    def target(self) -> str:
        """Retrieve the target."""
        return self._target

    @property
    def path(self) -> str:
        """Retrieve the path."""
        return self._path

    @property
    def tls_verify(self) -> bool:
        """Retrieve the tls_verify."""
        return self._tls_verify

    @property
    def app_name(self) -> str:
        """Retrieve the app name."""
        return self._app_name

    @property
    def app_version(self) -> str:
        """Retrieve the app version."""
        return self._app_version

    @property
    def channel(self) -> grpc.Channel:
        """Retrieve the channel."""
        return self._channel

    def __enter__(self):
        """Enters the runtime context related to the channel object."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exits the runtime context related to the channel object."""
        self.close()

    def close(self):
        """Close the channel."""
        self._channel.close()

    def ingest(
        self,
        entities: Iterable[Entity | ingester_pb2.Entity | None],
        stream: str | None = _DEFAULT_STREAM,
    ) -> ingester_pb2.IngestResponse:
        """Ingest entities."""
        try:
            request = ingester_pb2.IngestRequest(
                stream=stream,
                id=str(uuid.uuid4()),
                entities=entities,
                sdk_name=self.name,
                sdk_version=self.version,
                producer_app_name=self.app_name,
                producer_app_version=self.app_version,
            )

            return self._stub.Ingest(request, metadata=self._metadata)
        except grpc.RpcError as err:
            raise DiodeClientError(err) from err

    def _setup_sentry(
        self, dsn: str, traces_sample_rate: float, profiles_sample_rate: float
    ):
        sentry_sdk.init(
            dsn=dsn,
            release=self.version,
            traces_sample_rate=traces_sample_rate,
            profiles_sample_rate=profiles_sample_rate,
        )
        sentry_sdk.set_tag("target", self.target)
        sentry_sdk.set_tag("path", self.path if self.path else "/")
        sentry_sdk.set_tag("app_name", self.app_name)
        sentry_sdk.set_tag("app_version", self.app_version)
        sentry_sdk.set_tag("sdk_version", self.version)
        sentry_sdk.set_tag("platform", self._platform)
        sentry_sdk.set_tag("python_version", self._python_version)


class _ClientCallDetails(
    collections.namedtuple(
        "_ClientCallDetails",
        (
            "method",
            "timeout",
            "metadata",
            "credentials",
            "wait_for_ready",
            "compression",
        ),
    ),
    grpc.ClientCallDetails,
):
    """
    _ClientCallDetails class.

    This class describes an RPC to be invoked and is required for custom gRPC interceptors.

    """

    pass


class DiodeMethodClientInterceptor(
    grpc.UnaryUnaryClientInterceptor, grpc.StreamUnaryClientInterceptor
):
    """
    Diode Method Client Interceptor class.

    This class is used to intercept the client calls and modify the method details. It inherits from
    grpc.UnaryUnaryClientInterceptor and grpc.StreamUnaryClientInterceptor.

    Diode's default method generated from Protocol Buffers definition is /diode.v1.IngesterService/Ingest and in order
    to use Diode targets with path (i.e. localhost:8081/this/is/custom/path), this interceptor is used to modify the
    method details, by prepending the generated method name with the path extracted from initial target.

    """

    def __init__(self, subpath):
        """Initiate a new interceptor."""
        self._subpath = subpath

    def _intercept_call(self, continuation, client_call_details, request_or_iterator):
        """Intercept call."""
        method = client_call_details.method
        if client_call_details.method is not None:
            method = f"{self._subpath}{client_call_details.method}"

        client_call_details = _ClientCallDetails(
            method,
            client_call_details.timeout,
            client_call_details.metadata,
            client_call_details.credentials,
            client_call_details.wait_for_ready,
            client_call_details.compression,
        )

        response = continuation(client_call_details, request_or_iterator)
        return response

    def intercept_unary_unary(self, continuation, client_call_details, request):
        """Intercept unary unary."""
        return self._intercept_call(continuation, client_call_details, request)

    def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        """Intercept stream unary."""
        return self._intercept_call(continuation, client_call_details, request_iterator)
