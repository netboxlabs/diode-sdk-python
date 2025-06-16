#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs, Diode - SDK - Client."""

import collections
import http.client
import json
import logging
import os
import platform
import ssl
import sys
import time
import uuid
from collections.abc import Iterable
from pathlib import Path
from urllib.parse import urlencode, urlparse

import certifi
import grpc
import sentry_sdk
from google.protobuf.json_format import MessageToJson, ParseDict

from netboxlabs.diode.sdk.diode.v1 import ingester_pb2, ingester_pb2_grpc
from netboxlabs.diode.sdk.exceptions import DiodeClientError, DiodeConfigError
from netboxlabs.diode.sdk.ingester import Entity
from netboxlabs.diode.sdk.version import version_semver

_MAX_RETRIES_ENVVAR_NAME = "DIODE_MAX_AUTH_RETRIES"
_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME = "DIODE_SDK_LOG_LEVEL"
_DIODE_SENTRY_DSN_ENVVAR_NAME = "DIODE_SENTRY_DSN"
_CLIENT_ID_ENVVAR_NAME = "DIODE_CLIENT_ID"
_CLIENT_SECRET_ENVVAR_NAME = "DIODE_CLIENT_SECRET"
_DRY_RUN_OUTPUT_DIR_ENVVAR_NAME = "DIODE_DRY_RUN_OUTPUT_DIR"
_INGEST_SCOPE = "diode:ingest"
_DEFAULT_STREAM = "latest"
_LOGGER = logging.getLogger(__name__)


def load_dryrun_entities(file_path: str | Path) -> Iterable[Entity]:
    """Yield entities from a file with concatenated JSON messages."""
    path = Path(file_path)
    with path.open("r") as fh:
        request = json.load(fh)
        req_pb = ingester_pb2.IngestRequest()
        ParseDict(request, req_pb)
        yield from req_pb.entities


class DiodeClientInterface:
    """Runtime placeholder for the Diode client interface."""

    pass


def _load_certs() -> bytes:
    """Loads cacert.pem."""
    with open(certifi.where(), "rb") as f:
        return f.read()


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


def _get_required_config_value(env_var_name: str, value: str | None = None) -> str:
    """Get required config value either from provided value or environment variable."""
    if value is None:
        value = os.getenv(env_var_name)
    if value is None:
        raise DiodeConfigError(
            f"parameter or {env_var_name} environment variable required"
        )
    return value


def _get_optional_config_value(
    env_var_name: str, value: str | None = None
) -> str | None:
    """Get optional config value either from provided value or environment variable."""
    if value is None:
        value = os.getenv(env_var_name)
    return value


class DiodeClient(DiodeClientInterface):
    """Diode Client."""

    _name = "diode-sdk-python"
    _version = version_semver()
    _app_name = None
    _app_version = None
    _channel = None
    _stub = None

    def __init__(
        self,
        target: str,
        app_name: str,
        app_version: str,
        client_id: str | None = None,
        client_secret: str | None = None,
        sentry_dsn: str = None,
        sentry_traces_sample_rate: float = 1.0,
        sentry_profiles_sample_rate: float = 1.0,
        max_auth_retries: int = 3,
    ):
        """Initiate a new client."""
        log_level = os.getenv(_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME, "INFO").upper()
        logging.basicConfig(level=log_level)

        self._max_auth_retries = _get_optional_config_value(
            _MAX_RETRIES_ENVVAR_NAME, max_auth_retries
        )
        self._target, self._path, self._tls_verify = parse_target(target)
        self._app_name = app_name
        self._app_version = app_version
        self._platform = platform.platform()
        self._python_version = platform.python_version()

        # Read client credentials from environment variables
        self._client_id = _get_required_config_value(_CLIENT_ID_ENVVAR_NAME, client_id)
        self._client_secret = _get_required_config_value(
            _CLIENT_SECRET_ENVVAR_NAME, client_secret
        )

        self._metadata = (
            ("platform", self._platform),
            ("python-version", self._python_version),
        )

        self._authenticate(_INGEST_SCOPE)

        channel_opts = (
            (
                "grpc.primary_user_agent",
                f"{self._name}/{self._version} {self._app_name}/{self._app_version}",
            ),
        )

        if self._tls_verify:
            _LOGGER.debug("Setting up gRPC secure channel")
            self._channel = grpc.secure_channel(
                self._target,
                grpc.ssl_channel_credentials(
                    root_certificates=_load_certs(),
                ),
                options=channel_opts,
            )
        else:
            _LOGGER.debug("Setting up gRPC insecure channel")
            self._channel = grpc.insecure_channel(
                target=self._target,
                options=channel_opts,
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
        for attempt in range(self._max_auth_retries):
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
                if err.code() == grpc.StatusCode.UNAUTHENTICATED:
                    if attempt < self._max_auth_retries - 1:
                        _LOGGER.info(
                            f"Retrying ingestion due to UNAUTHENTICATED error, attempt {attempt + 1}"
                        )
                        self._authenticate(_INGEST_SCOPE)
                        continue
                raise DiodeClientError(err) from err
        raise RuntimeError("Max retries exceeded")

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

    def _authenticate(self, scope: str):
        authentication_client = _DiodeAuthentication(
            self._target,
            self._path,
            self._tls_verify,
            self._client_id,
            self._client_secret,
            scope,
        )
        access_token = authentication_client.authenticate()
        self._metadata = list(
            filter(lambda x: x[0] != "authorization", self._metadata)
        ) + [("authorization", f"Bearer {access_token}")]


class DiodeDryRunClient(DiodeClientInterface):
    """Client that outputs ingestion requests instead of sending them."""

    _name = "diode-sdk-python-dry-run"
    _version = version_semver()
    _app_name = None
    _app_version = None

    def __init__(self, app_name: str = "dryrun", output_dir: str | None = None):
        """Initiate a new dry run client."""
        self._output_dir = os.getenv(_DRY_RUN_OUTPUT_DIR_ENVVAR_NAME, output_dir)
        self._app_name = app_name

    @property
    def name(self) -> str:
        """Retrieve the name."""
        return self._name

    @property
    def version(self) -> str:
        """Retrieve the version."""
        return self._version

    @property
    def app_name(self) -> str:
        """Retrieve the app name."""
        return self._app_name

    @property
    def output_dir(self) -> str | None:
        """Retrieve the dry run output dir."""
        return self._output_dir

    def __enter__(self):
        """Enters the runtime context related to the channel object."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exits the runtime context related to the channel object."""

    def ingest(
        self,
        entities: Iterable[Entity | ingester_pb2.Entity | None],
        stream: str | None = _DEFAULT_STREAM,
    ) -> ingester_pb2.IngestResponse:
        """Ingest entities in dry run mode."""
        request = ingester_pb2.IngestRequest(
            stream=stream,
            id=str(uuid.uuid4()),
            producer_app_name=self._app_name,
            entities=entities,
            sdk_name=self.name,
            sdk_version=self.version,
        )

        output = MessageToJson(request, preserving_proto_field_name=True)
        if self._output_dir:
            timestamp = time.perf_counter_ns()
            path = Path(self._output_dir)
            path.mkdir(parents=True, exist_ok=True)
            filename = "".join(
                c if c.isalnum() or c in ("_", "-") else "_" for c in self._app_name
            )
            file_path = path / f"{filename}_{timestamp}.json"
            with file_path.open("w") as fh:
                fh.write(output)
        else:
            print(output, file=sys.stdout)
        return ingester_pb2.IngestResponse()


class _DiodeAuthentication:
    def __init__(
        self,
        target: str,
        path: str,
        tls_verify: bool,
        client_id: str,
        client_secret: str,
        scope: str,
    ):
        self._target = target
        self._tls_verify = tls_verify
        self._client_id = client_id
        self._client_secret = client_secret
        self._path = path
        self._scope = scope

    def authenticate(self) -> str:
        """Request an OAuth2 token using client credentials and return it."""
        if self._tls_verify:
            conn = http.client.HTTPSConnection(
                self._target,
                context=None if self._tls_verify else ssl._create_unverified_context(),
            )
        else:
            conn = http.client.HTTPConnection(
                self._target,
            )
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        data = urlencode(
            {
                "grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "scope": self._scope,
            }
        )
        url = self._get_auth_url()
        try:
            conn.request("POST", url, data, headers)
            response = conn.getresponse()
        except Exception as e:
            raise DiodeConfigError(f"Failed to obtain access token: {e}")
        if response.status != 200:
            raise DiodeConfigError(f"Failed to obtain access token: {response.reason}")
        token_info = json.loads(response.read().decode())
        access_token = token_info.get("access_token")
        if not access_token:
            raise DiodeConfigError(
                f"Failed to obtain access token for client {self._client_id}"
            )

        _LOGGER.debug(f"Access token obtained for client {self._client_id}")
        return access_token

    def _get_auth_url(self) -> str:
        """Construct the authentication URL, handling trailing slashes in the path."""
        # Ensure the path does not have trailing slashes
        path = self._path.rstrip("/") if self._path else ""
        return f"{path}/auth/token"


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
