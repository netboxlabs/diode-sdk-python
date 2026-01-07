#!/usr/bin/env python
# Copyright 2026 NetBox Labs Inc
"""NetBox Labs, Diode - SDK - Client."""

import collections
import json
import logging
import os
import platform
import sys
import tempfile
import time
import uuid
from collections.abc import Iterable
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import certifi
import grpc
import requests
import sentry_sdk
from google.protobuf.json_format import MessageToJson, ParseDict
from opentelemetry.proto.collector.logs.v1 import (
    logs_service_pb2,
    logs_service_pb2_grpc,
)
from opentelemetry.proto.common.v1 import common_pb2
from opentelemetry.proto.logs.v1 import logs_pb2

from netboxlabs.diode.sdk.diode.v1 import ingester_pb2, ingester_pb2_grpc
from netboxlabs.diode.sdk.exceptions import (
    DiodeClientError,
    DiodeConfigError,
    OTLPClientError,
)
from netboxlabs.diode.sdk.ingester import Entity, convert_dict_to_struct
from netboxlabs.diode.sdk.version import version_semver

Metadata = dict[str, Any]

_CLIENT_ID_ENVVAR_NAME = "DIODE_CLIENT_ID"
_CLIENT_SECRET_ENVVAR_NAME = "DIODE_CLIENT_SECRET"
_DEFAULT_STREAM = "latest"
_DIODE_CERT_FILE_ENVVAR_NAME = "DIODE_CERT_FILE"
_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME = "DIODE_SDK_LOG_LEVEL"
_DIODE_SENTRY_DSN_ENVVAR_NAME = "DIODE_SENTRY_DSN"
_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME = "DIODE_SKIP_TLS_VERIFY"
_DRY_RUN_OUTPUT_DIR_ENVVAR_NAME = "DIODE_DRY_RUN_OUTPUT_DIR"
_INGEST_SCOPE = "diode:ingest"
_LOGGER = logging.getLogger(__name__)
_MAX_RETRIES_ENVVAR_NAME = "DIODE_MAX_AUTH_RETRIES"


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


def _load_certs(cert_file: str | None = None) -> bytes:
    """Loads cacert.pem or custom certificate file."""
    cert_path = cert_file or certifi.where()
    with open(cert_path, "rb") as f:
        return f.read()


def _should_verify_tls(scheme: str) -> bool:
    """Determine if TLS verification should be enabled based on scheme and environment variable."""
    # Check if scheme is insecure
    insecure_scheme = scheme in ["grpc", "http"]

    # Check environment variable
    skip_tls_env = os.getenv(_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME, "").lower()
    skip_tls_from_env = skip_tls_env in ["true", "1", "yes", "on"]

    # TLS verification is enabled by default, disabled only for insecure schemes or env var
    return not (insecure_scheme or skip_tls_from_env)


def parse_target(target: str) -> tuple[str, str, bool]:
    """Parse the target into authority, path and tls_verify."""
    parsed_target = urlparse(target)

    if parsed_target.scheme not in ["grpc", "grpcs", "http", "https"]:
        raise ValueError(
            "target should start with grpc://, grpcs://, http:// or https://"
        )

    # Determine if TLS verification should be enabled
    tls_verify = _should_verify_tls(parsed_target.scheme)

    authority = parsed_target.netloc

    if ":" not in authority:
        if parsed_target.scheme in ["grpc", "http"]:
            authority += ":80"
        elif parsed_target.scheme in ["grpcs", "https"]:
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


def _get_proxy_env_var(var_name: str) -> str | None:
    """Get proxy environment variable (case-insensitive)."""
    value = os.getenv(var_name.upper())
    if value:
        return value
    return os.getenv(var_name.lower())


def _validate_proxy_url(url: str) -> bool:
    """
    Validate proxy URL format.

    Args:
        url: Proxy URL to validate

    Returns:
        True if URL is valid, False otherwise

    """
    if not url:
        return False
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False


def _matches_no_proxy_entry(host: str, entry: str) -> bool:
    """Check if host matches a single NO_PROXY entry."""
    if entry == "*":
        _LOGGER.debug("NO_PROXY='*' - bypassing proxy for all hosts")
        return True

    if entry == host:
        _LOGGER.debug(f"NO_PROXY exact match: {host}")
        return True

    if not entry.startswith(".") and not entry.startswith("*"):
        if host.endswith(f".{entry}"):
            _LOGGER.debug(f"NO_PROXY subdomain match: {host} ends with .{entry}")
            return True

    if entry.startswith("."):
        if host.endswith(entry):
            _LOGGER.debug(f"NO_PROXY suffix match: {host} ends with {entry}")
            return True

    if entry.startswith("*."):
        suffix = entry[1:]
        if host.endswith(suffix):
            _LOGGER.debug(f"NO_PROXY wildcard match: {host} ends with {suffix}")
            return True

    return False


def _should_bypass_proxy(target_host: str) -> bool:
    """
    Check if target should bypass proxy based on NO_PROXY.

    Implements Go net/http compatible NO_PROXY matching:
    - "*" disables proxy for all hosts
    - "example.com" matches example.com AND all subdomains
    - ".example.com" matches only subdomains, NOT example.com itself
    - Port numbers are stripped before matching
    - Matching is case-insensitive
    - localhost and 127.0.0.1 always bypass proxy
    - NO_PROXY entries longer than 256 characters are ignored (security limit)
    """
    host = target_host.split(":")[0].lower()

    if host in ("localhost", "127.0.0.1", "::1"):
        return True

    no_proxy = _get_proxy_env_var("NO_PROXY")
    if not no_proxy:
        return False

    # Maximum reasonable length for hostname/domain (RFC 1035: 253 chars, we allow 256)
    MAX_NO_PROXY_ENTRY_LENGTH = 256

    no_proxy_list = [
        entry.strip().lower()
        for entry in no_proxy.split(",")
        if len(entry.strip()) <= MAX_NO_PROXY_ENTRY_LENGTH
    ]

    filtered_count = len([e for e in no_proxy.split(",") if len(e.strip()) > MAX_NO_PROXY_ENTRY_LENGTH])
    if filtered_count > 0:
        _LOGGER.warning(
            f"Ignored {filtered_count} NO_PROXY entries exceeding {MAX_NO_PROXY_ENTRY_LENGTH} characters"
        )

    for entry in no_proxy_list:
        if entry and _matches_no_proxy_entry(host, entry):
            return True

    return False


def _get_grpc_proxy_url(target_host: str, use_tls: bool) -> str | None:
    """
    Get proxy URL for gRPC target, respecting environment variables.

    Args:
        target_host: gRPC target (may include port)
        use_tls: Whether connection uses TLS

    Returns:
        Proxy URL if proxy should be used, None otherwise

    """
    if _should_bypass_proxy(target_host):
        return None

    # For HTTPS: check HTTPS_PROXY first, fall back to HTTP_PROXY
    if use_tls:
        proxy_url = _get_proxy_env_var("HTTPS_PROXY")
        if not proxy_url:
            proxy_url = _get_proxy_env_var("HTTP_PROXY")
    else:
        # For HTTP: only check HTTP_PROXY
        proxy_url = _get_proxy_env_var("HTTP_PROXY")

    if proxy_url:
        if not _validate_proxy_url(proxy_url):
            _LOGGER.warning(
                f"Invalid proxy URL format: {proxy_url}. "
                f"Proxy URL must be http:// or https:// with valid host. Ignoring proxy."
            )
            return None
        _LOGGER.debug(f"Using proxy {proxy_url} for gRPC target {target_host}")

    return proxy_url


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
        cert_file: str | None = None,
    ):
        """Initiate a new client."""
        log_level = os.getenv(_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME, "INFO").upper()
        logging.basicConfig(level=log_level)

        self._max_auth_retries = int(
            _get_optional_config_value(_MAX_RETRIES_ENVVAR_NAME, str(max_auth_retries))
            or max_auth_retries
        )
        self._cert_file = _get_optional_config_value(
            _DIODE_CERT_FILE_ENVVAR_NAME, cert_file
        )
        self._target, self._path, self._tls_verify = parse_target(target)

        # Load certificates once if needed
        self._certificates = (
            _load_certs(self._cert_file)
            if (self._tls_verify or self._cert_file)
            else None
        )
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

        channel_opts = [
            (
                "grpc.primary_user_agent",
                f"{self._name}/{self._version} {self._app_name}/{self._app_version}",
            ),
        ]

        proxy_url = _get_grpc_proxy_url(self._target, self._tls_verify)
        if proxy_url:
            channel_opts.append(("grpc.http_proxy", proxy_url))
            _LOGGER.debug(f"Configured gRPC proxy: {proxy_url}")

        channel_opts = tuple(channel_opts)

        # Channel creation logic
        if self._tls_verify:
            credentials = (
                grpc.ssl_channel_credentials(root_certificates=self._certificates)
                if self._certificates
                else grpc.ssl_channel_credentials()
            )

            _LOGGER.debug(
                f"Setting up gRPC secure channel with "
                f"{'custom certificates' if self._certificates else 'system certificates'}"
                f"{' via proxy' if proxy_url else ''}"
            )
            self._channel = grpc.secure_channel(
                self._target,
                credentials,
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
        *,
        metadata: Metadata | None = None,
    ) -> ingester_pb2.IngestResponse:
        """Ingest entities with optional request-level metadata."""
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
                if metadata is not None:
                    request_metadata = convert_dict_to_struct(metadata)
                    request.metadata.CopyFrom(request_metadata)
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
            self._name,
            self._version,
            self._app_name,
            self._app_version,
            self._certificates,
            self._cert_file,
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
        *,
        metadata: Metadata | None = None,
    ) -> ingester_pb2.IngestResponse:
        """Ingest entities in dry run mode with optional request-level metadata."""
        request = ingester_pb2.IngestRequest(
            stream=stream,
            id=str(uuid.uuid4()),
            producer_app_name=self._app_name,
            entities=entities,
            sdk_name=self.name,
            sdk_version=self.version,
        )
        if metadata is not None:
            request_metadata = convert_dict_to_struct(metadata)
            request.metadata.CopyFrom(request_metadata)

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


class DiodeOTLPClient(DiodeClientInterface):
    """Diode OTLP client that exports ingestion entities as OTLP logs."""

    _name = "diode-sdk-python-otlp"
    _version = version_semver()

    def __init__(
        self,
        target: str,
        app_name: str,
        app_version: str,
        *,
        timeout: float = 10.0,
        metadata: dict[str, str] | Iterable[tuple[str, str]] | None = None,
        cert_file: str | None = None,
    ):
        """Initiate a new Diode OTLP client."""
        log_level = os.getenv(_DIODE_SDK_LOG_LEVEL_ENVVAR_NAME, "INFO").upper()
        logging.basicConfig(level=log_level)

        self._app_name = app_name
        self._app_version = app_version
        self._platform = platform.platform()
        self._python_version = platform.python_version()
        self._timeout = timeout

        self._target, self._path, self._tls_verify = parse_target(target)
        self._cert_file = _get_optional_config_value(
            _DIODE_CERT_FILE_ENVVAR_NAME, cert_file
        )
        self._certificates = (
            _load_certs(self._cert_file)
            if (self._tls_verify or self._cert_file)
            else None
        )

        channel_opts = [
            (
                "grpc.primary_user_agent",
                f"{self._name}/{self._version} {self._app_name}/{self._app_version}",
            ),
        ]

        proxy_url = _get_grpc_proxy_url(self._target, self._tls_verify)
        if proxy_url:
            channel_opts.append(("grpc.http_proxy", proxy_url))
            # Extract hostname for SSL target name override
            target_host = self._target.split(":")[0]
            channel_opts.append(("grpc.ssl_target_name_override", target_host))
            _LOGGER.debug(f"Configured gRPC proxy: {proxy_url}")
            _LOGGER.debug(f"SSL target name override: {target_host}")

        channel_opts = tuple(channel_opts)

        # Channel creation logic
        if self._tls_verify:
            credentials = (
                grpc.ssl_channel_credentials(root_certificates=self._certificates)
                if self._certificates
                else grpc.ssl_channel_credentials()
            )

            _LOGGER.debug(
                f"Setting up gRPC secure channel with "
                f"{'custom certificates' if self._certificates else 'system certificates'}"
                f"{' via proxy' if proxy_url else ''}"
            )
            base_channel = grpc.secure_channel(
                self._target,
                credentials,
                options=channel_opts,
            )
        else:
            _LOGGER.debug(f"Setting up gRPC insecure channel")
            base_channel = grpc.insecure_channel(
                target=self._target,
                options=channel_opts,
            )

        self._base_channel = base_channel
        channel = base_channel
        if self._path:
            interceptor = DiodeMethodClientInterceptor(subpath=self._path)
            channel = grpc.intercept_channel(base_channel, interceptor)

        self._channel = channel
        self._stub = logs_service_pb2_grpc.LogsServiceStub(channel)
        self._metadata = self._prepare_metadata(metadata)

    @staticmethod
    def _prepare_metadata(
        metadata: dict[str, str] | Iterable[tuple[str, str]] | None,
    ) -> tuple[tuple[str, str], ...] | None:
        if metadata is None:
            return None
        if isinstance(metadata, dict):
            return tuple(metadata.items())
        return tuple(metadata)

    @property
    def name(self) -> str:
        """Retrieve the client name."""
        return self._name

    @property
    def version(self) -> str:
        """Retrieve the client version."""
        return self._version

    @property
    def app_name(self) -> str:
        """Retrieve the producer application name."""
        return self._app_name

    @property
    def app_version(self) -> str:
        """Retrieve the producer application version."""
        return self._app_version

    @property
    def timeout(self) -> float:
        """Retrieve the export timeout."""
        return self._timeout

    @property
    def target(self) -> str:
        """Retrieve the export target."""
        return self._target

    def __enter__(self):
        """Enter the runtime context."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exit the runtime context."""
        self.close()

    def close(self):
        """Close the underlying channel."""
        if getattr(self, "_base_channel", None):
            self._base_channel.close()

    def ingest(
        self,
        entities: Iterable[Entity | ingester_pb2.Entity | None],
        stream: str | None = _DEFAULT_STREAM,
        *,
        metadata: Metadata | None = None,
    ) -> ingester_pb2.IngestResponse:
        """Export entities as OTLP logs with optional request-level metadata."""
        stream = stream or _DEFAULT_STREAM
        log_records = [
            self._entity_to_log_record(entity)
            for entity in self._normalize_entities(entities)
        ]

        if not log_records:
            return ingester_pb2.IngestResponse()

        request = self._build_export_request(log_records, stream, metadata)

        try:
            self._stub.Export(
                request,
                timeout=self._timeout,
                metadata=self._metadata,
            )
        except grpc.RpcError as err:
            raise OTLPClientError(err) from err

        return ingester_pb2.IngestResponse()

    def _normalize_entities(
        self, entities: Iterable[Entity | ingester_pb2.Entity | None]
    ) -> list[ingester_pb2.Entity]:
        normalized: list[ingester_pb2.Entity] = []
        for entity in entities:
            if entity is None:
                continue
            if not isinstance(entity, ingester_pb2.Entity):
                raise TypeError("DiodeOTLPClient expects ingester_pb2.Entity instances")
            normalized.append(entity)
        return normalized

    def _build_export_request(
        self,
        log_records: list[logs_pb2.LogRecord],
        stream: str | None,
        metadata: Metadata | None = None,
    ) -> logs_service_pb2.ExportLogsServiceRequest:
        resource_logs = logs_pb2.ResourceLogs()
        resource_logs.resource.attributes.extend(self._resource_attributes())
        resource_logs.resource.attributes.append(
            self._string_kv("diode.stream", stream)
        )

        # Add request-level metadata as resource attributes with diode.metadata.* prefix
        if metadata:
            for key, value in metadata.items():
                resource_attr = self._metadata_value_to_kv(f"diode.metadata.{key}", value)
                if resource_attr:
                    resource_logs.resource.attributes.append(resource_attr)

        scope_logs = resource_logs.scope_logs.add()
        scope_logs.scope.CopyFrom(
            common_pb2.InstrumentationScope(
                name=self._name,
                version=self._version,
            )
        )
        scope_logs.log_records.extend(log_records)

        request = logs_service_pb2.ExportLogsServiceRequest()
        request.resource_logs.append(resource_logs)
        return request

    def _resource_attributes(self) -> list[common_pb2.KeyValue]:
        return [
            self._string_kv("service.name", self._app_name),
            self._string_kv("service.version", self._app_version),
            self._string_kv("os.description", self._platform),
            self._string_kv("process.runtime.version", self._python_version),
        ]

    def _entity_to_log_record(
        self,
        entity: ingester_pb2.Entity,
    ) -> logs_pb2.LogRecord:
        body_json = MessageToJson(entity, preserving_proto_field_name=True)
        entity_type = entity.WhichOneof("entity") or "unknown"

        log_record = logs_pb2.LogRecord(
            time_unix_nano=time.time_ns(),
            severity_number=logs_pb2.SeverityNumber.SEVERITY_NUMBER_INFO,
            severity_text="INFO",
        )
        log_record.body.CopyFrom(common_pb2.AnyValue(string_value=body_json))
        log_record.attributes.extend(
            [
                self._string_kv("diode.entity", entity_type),
            ]
        )
        return log_record

    @staticmethod
    def _string_kv(key: str, value: str) -> common_pb2.KeyValue:
        return common_pb2.KeyValue(
            key=key, value=common_pb2.AnyValue(string_value=value)
        )

    @staticmethod
    def _value_to_any_value(value: Any) -> common_pb2.AnyValue | None:  # noqa: C901
        """Convert a Python value to OTLP AnyValue recursively."""
        if value is None:
            return None
        if isinstance(value, bool):
            # Check bool before int since bool is a subclass of int in Python
            return common_pb2.AnyValue(bool_value=value)
        if isinstance(value, str):
            return common_pb2.AnyValue(string_value=value)
        if isinstance(value, int):
            return common_pb2.AnyValue(int_value=value)
        if isinstance(value, float):
            return common_pb2.AnyValue(double_value=value)
        if isinstance(value, list):
            # Recursively convert list items
            array_values = []
            for item in value:
                any_value = DiodeOTLPClient._value_to_any_value(item)
                if any_value:
                    array_values.append(any_value)
            return common_pb2.AnyValue(
                array_value=common_pb2.ArrayValue(values=array_values)
            )
        if isinstance(value, dict):
            # Recursively convert dict to KeyValueList
            kvlist = common_pb2.KeyValueList()
            for k, v in value.items():
                any_value = DiodeOTLPClient._value_to_any_value(v)
                if any_value:
                    kvlist.values.append(
                        common_pb2.KeyValue(key=k, value=any_value)
                    )
            return common_pb2.AnyValue(kvlist_value=kvlist)
        # Skip unsupported types
        return None

    @staticmethod
    def _metadata_value_to_kv(key: str, value: Any) -> common_pb2.KeyValue | None:
        """Convert metadata key-value pair to OTLP KeyValue with appropriate type."""
        any_value = DiodeOTLPClient._value_to_any_value(value)
        if any_value:
            return common_pb2.KeyValue(key=key, value=any_value)
        return None


class _DiodeAuthentication:
    def __init__(
        self,
        target: str,
        path: str,
        tls_verify: bool,
        client_id: str,
        client_secret: str,
        scope: str,
        sdk_name: str,
        sdk_version: str,
        app_name: str,
        app_version: str,
        certificates: bytes | None = None,
        cert_file: str | None = None,
    ):
        self._target = target
        self._tls_verify = tls_verify
        self._client_id = client_id
        self._client_secret = client_secret
        self._path = path
        self._scope = scope
        self._sdk_name = sdk_name
        self._sdk_version = sdk_version
        self._app_name = app_name
        self._app_version = app_version
        self._certificates = certificates
        self._cert_file = cert_file

    def authenticate(self) -> str:
        """Request an OAuth2 token using client credentials and return it."""
        session = requests.Session()
        temp_cert_file = None

        try:
            # Configure SSL verification
            if self._tls_verify and self._certificates:
                # Use cert_file path directly if available, otherwise write to temp file
                if self._cert_file:
                    session.verify = self._cert_file
                else:
                    # Write certificates to temp file for requests
                    with tempfile.NamedTemporaryFile(
                        mode="wb", delete=False, suffix=".pem"
                    ) as f:
                        f.write(self._certificates)
                        temp_cert_file = f.name
                    session.verify = temp_cert_file
            elif not self._tls_verify:
                session.verify = False

            # Prepare auth request
            url = self._get_full_auth_url()
            data = {
                "grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "scope": self._scope,
            }
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": f"{self._sdk_name}/{self._sdk_version} {self._app_name}/{self._app_version}",
            }

            response = session.post(url, data=data, headers=headers)

            if response.status_code != 200:
                raise DiodeConfigError(
                    f"Failed to obtain access token: {response.reason}"
                )

            token_info = response.json()
            access_token = token_info.get("access_token")

            if not access_token:
                raise DiodeConfigError(
                    f"Failed to obtain access token for client {self._client_id}"
                )

            _LOGGER.debug(f"Access token obtained for client {self._client_id}")
            return access_token

        except requests.RequestException as e:
            raise DiodeConfigError(f"Failed to obtain access token: {e}")
        finally:
            # Clean up temp certificate file
            if temp_cert_file and os.path.exists(temp_cert_file):
                try:
                    os.unlink(temp_cert_file)
                    _LOGGER.debug(f"Cleaned up temp certificate file: {temp_cert_file}")
                except OSError as e:
                    _LOGGER.warning(
                        f"Failed to clean up temp certificate file {temp_cert_file}: {e}"
                    )

    def _get_auth_url(self) -> str:
        """Construct the authentication URL, handling trailing slashes in the path."""
        # Ensure the path does not have trailing slashes
        path = self._path.rstrip("/") if self._path else ""
        return f"{path}/auth/token"

    def _get_full_auth_url(self) -> str:
        """Construct full authentication URL with scheme and authority."""
        # Determine the correct scheme
        # If tls_verify is False, check if SKIP_TLS_VERIFY was set
        # If it was set, the original scheme was likely HTTPS but verification is disabled
        skip_tls_env = os.getenv(_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME, "").lower()
        skip_tls_from_env = skip_tls_env in ["true", "1", "yes", "on"]

        # Use HTTPS if:
        # 1. tls_verify is True, OR
        # 2. tls_verify is False but SKIP_TLS_VERIFY is set (original was HTTPS)
        use_https = self._tls_verify or (not self._tls_verify and skip_tls_from_env)
        scheme = "https" if use_https else "http"

        path = self._path.rstrip("/") if self._path else ""
        return f"{scheme}://{self._target}{path}/auth/token"


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
