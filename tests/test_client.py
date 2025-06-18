#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs - Tests."""

import json
import os
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock, patch

import grpc
import pytest

from netboxlabs.diode.sdk.client import (
    _DIODE_SENTRY_DSN_ENVVAR_NAME,
    DiodeClient,
    DiodeDryRunClient,
    DiodeMethodClientInterceptor,
    _ClientCallDetails,
    _DiodeAuthentication,
    _get_sentry_dsn,
    _load_certs,
    load_dryrun_entities,
    parse_target,
)
from netboxlabs.diode.sdk.diode.v1 import ingester_pb2
from netboxlabs.diode.sdk.exceptions import DiodeClientError, DiodeConfigError
from netboxlabs.diode.sdk.ingester import Entity
from netboxlabs.diode.sdk.version import version_semver


def test_init(mock_diode_authentication):
    """Check we can initiate a client configuration."""
    config = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    assert config.target == "localhost:8081"
    assert config.name == "diode-sdk-python"
    assert config.version == version_semver()
    assert config.app_name == "my-producer"
    assert config.app_version == "0.0.1"
    assert config.tls_verify is False
    assert config.path == ""


@pytest.mark.parametrize(
    "client_id,client_secret,env_var_name",
    [
        (None, "123", "DIODE_CLIENT_ID"),
        ("123", None, "DIODE_CLIENT_SECRET"),
        (None, None, "DIODE_CLIENT_ID"),
    ],
)
def test_config_errors(client_id, client_secret, env_var_name):
    """Check we can raise a config error."""
    with pytest.raises(DiodeConfigError) as err:
        DiodeClient(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id=client_id,
            client_secret=client_secret,
        )
    assert (
        str(err.value) == f"parameter or {env_var_name} environment variable required"
    )


def test_client_error(mock_diode_authentication):
    """Check we can raise a client error."""
    with pytest.raises(DiodeClientError) as err:
        client = DiodeClient(
            target="grpc://invalid:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )
        client.ingest(entities=[])
    assert err.value.status_code == grpc.StatusCode.UNAVAILABLE
    assert "DNS resolution failed for invalid:8081" in err.value.details


def test_diode_client_error_repr_returns_correct_string():
    """Check we can return the correct string representation of the error."""
    grpc_error = grpc.RpcError()
    grpc_error.code = lambda: grpc.StatusCode.UNAVAILABLE
    grpc_error.details = lambda: "Some details about the error"
    error = DiodeClientError(grpc_error)
    error._status_code = grpc.StatusCode.UNAVAILABLE
    error._details = "Some details about the error"
    assert (
        repr(error)
        == "<DiodeClientError status code: StatusCode.UNAVAILABLE, details: Some details about the error>"
    )


def test_load_certs_returns_bytes():
    """Check that _load_certs returns bytes."""
    assert isinstance(_load_certs(), bytes)


def test_parse_target_handles_http_prefix():
    """Check that parse_target raises an error when the target contains http://."""
    with pytest.raises(ValueError):
        parse_target("http://localhost:8081")


def test_parse_target_handles_https_prefix():
    """Check that parse_target raises an error when the target contains https://."""
    with pytest.raises(ValueError):
        parse_target("https://localhost:8081")


def test_parse_target_parses_authority_correctly():
    """Check that parse_target parses the authority correctly."""
    authority, path, tls_verify = parse_target("grpc://localhost:8081")
    assert authority == "localhost:8081"
    assert path == ""
    assert tls_verify is False


def test_parse_target_adds_default_port_if_missing():
    """Check that parse_target adds the default port if missing."""
    authority, _, _ = parse_target("grpc://localhost")
    assert authority == "localhost:443"


def test_parse_target_parses_path_correctly():
    """Check that parse_target parses the path correctly."""
    _, path, _ = parse_target("grpc://localhost:8081/my/path")
    assert path == "/my/path"


def test_parse_target_handles_no_path():
    """Check that parse_target handles no path."""
    _, path, _ = parse_target("grpc://localhost:8081")
    assert path == ""


def test_parse_target_parses_tls_verify_correctly():
    """Check that parse_target parses tls_verify correctly."""
    _, _, tls_verify = parse_target("grpcs://localhost:8081")
    assert tls_verify is True


def test_get_sentry_dsn_returns_env_var_when_no_input():
    """Check that _get_sentry_dsn returns the env var when no input is provided."""
    os.environ[_DIODE_SENTRY_DSN_ENVVAR_NAME] = "env_var_dsn"
    assert _get_sentry_dsn() == "env_var_dsn"


def test_get_sentry_dsn_returns_input_when_provided():
    """Check that _get_sentry_dsn returns the input when provided."""
    os.environ[_DIODE_SENTRY_DSN_ENVVAR_NAME] = "env_var_dsn"
    assert _get_sentry_dsn("input_dsn") == "input_dsn"


def test_get_sentry_dsn_returns_none_when_no_input_or_env_var():
    """Check that _get_sentry_dsn returns None when no input or env var is provided."""
    if _DIODE_SENTRY_DSN_ENVVAR_NAME in os.environ:
        del os.environ[_DIODE_SENTRY_DSN_ENVVAR_NAME]
    assert _get_sentry_dsn() is None


def test_setup_sentry_initializes_with_correct_parameters(mock_diode_authentication):
    """Check that DiodeClient._setup_sentry() initializes with the correct parameters."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with mock.patch("sentry_sdk.init") as mock_init:
        client._setup_sentry("https://user@password.mock.dsn/123456", 0.5, 0.5)
        mock_init.assert_called_once_with(
            dsn="https://user@password.mock.dsn/123456",
            release=client.version,
            traces_sample_rate=0.5,
            profiles_sample_rate=0.5,
        )


def test_client_sets_up_secure_channel_when_grpcs_scheme_is_found_in_target(
    mock_diode_authentication,
):
    """Check that DiodeClient.__init__() sets up the gRPC secure channel when grpcs:// scheme is found in the target."""
    client = DiodeClient(
        target="grpcs://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with (
        mock.patch("grpc.secure_channel") as mock_secure_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpcs://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        mock_debug.assert_called_once_with("Setting up gRPC secure channel")
        mock_secure_channel.assert_called_once()


def test_client_sets_up_insecure_channel_when_grpc_scheme_is_found_in_target(
    mock_diode_authentication,
):
    """Check that DiodeClient.__init__() sets up the gRPC insecure channel when grpc:// scheme is found in the target."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with (
        mock.patch("grpc.insecure_channel") as mock_insecure_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        mock_debug.assert_called_with(
            "Setting up gRPC insecure channel",
        )
        mock_insecure_channel.assert_called_once()


def test_insecure_channel_options_with_primary_user_agent(mock_diode_authentication):
    """Check that DiodeClient.__init__() sets the gRPC primary_user_agent option for insecure channel."""
    with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
        client = DiodeClient(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        mock_insecure_channel.assert_called_once()
        _, kwargs = mock_insecure_channel.call_args
        assert kwargs["options"] == (
            (
                "grpc.primary_user_agent",
                f"{client.name}/{client.version} {client.app_name}/{client.app_version}",
            ),
        )


def test_secure_channel_options_with_primary_user_agent(mock_diode_authentication):
    """Check that DiodeClient.__init__() sets the gRPC primary_user_agent option for secure channel."""
    with mock.patch("grpc.secure_channel") as mock_secure_channel:
        client = DiodeClient(
            target="grpcs://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        mock_secure_channel.assert_called_once()
        _, kwargs = mock_secure_channel.call_args
        assert kwargs["options"] == (
            (
                "grpc.primary_user_agent",
                f"{client.name}/{client.version} {client.app_name}/{client.app_version}",
            ),
        )


def test_client_interceptor_setup_with_path(mock_diode_authentication):
    """Check that DiodeClient.__init__() sets up the gRPC interceptor when a path is provided."""
    client = DiodeClient(
        target="grpc://localhost:8081/my-path",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with (
        mock.patch("grpc.intercept_channel") as mock_intercept_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpc://localhost:8081/my-path",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        mock_debug.assert_called_with(
            "Setting up gRPC interceptor for path: /my-path",
        )
        mock_intercept_channel.assert_called_once()


def test_client_interceptor_not_setup_without_path(mock_diode_authentication):
    """Check that DiodeClient.__init__() does not set up the gRPC interceptor when no path is provided."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with (
        mock.patch("grpc.intercept_channel") as mock_intercept_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        mock_debug.assert_called_with(
            "Setting up gRPC insecure channel",
        )
        mock_intercept_channel.assert_not_called()


def test_client_setup_sentry_called_when_sentry_dsn_exists(mock_diode_authentication):
    """Check that DiodeClient._setup_sentry() is called when sentry_dsn exists."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
        sentry_dsn="https://user@password.mock.dsn/123456",
    )
    with mock.patch.object(client, "_setup_sentry") as mock_setup_sentry:
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
            sentry_dsn="https://user@password.mock.dsn/123456",
        )
        mock_setup_sentry.assert_called_once_with(
            "https://user@password.mock.dsn/123456", 1.0, 1.0
        )


def test_client_setup_sentry_not_called_when_sentry_dsn_not_exists(
    mock_diode_authentication,
):
    """Check that DiodeClient._setup_sentry() is not called when sentry_dsn does not exist."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with mock.patch.object(client, "_setup_sentry") as mock_setup_sentry:
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )
        mock_setup_sentry.assert_not_called()


def test_client_properties_return_expected_values(mock_diode_authentication):
    """Check that DiodeClient properties return the expected values."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    assert client.name == "diode-sdk-python"
    assert client.version == version_semver()
    assert client.target == "localhost:8081"
    assert client.path == ""
    assert client.tls_verify is False
    assert client.app_name == "my-producer"
    assert client.app_version == "0.0.1"
    assert isinstance(client.channel, grpc.Channel)


def test_client_enter_returns_self(mock_diode_authentication):
    """Check that DiodeClient.__enter__() returns self."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    assert client.__enter__() is client


def test_client_exit_closes_channel(mock_diode_authentication):
    """Check that DiodeClient.__exit__() closes the channel."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with mock.patch.object(client._channel, "close") as mock_close:
        client.__exit__(None, None, None)
        mock_close.assert_called_once()


def test_client_close_closes_channel(mock_diode_authentication):
    """Check that DiodeClient.close() closes the channel."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with mock.patch.object(client._channel, "close") as mock_close:
        client.close()
        mock_close.assert_called_once()


def test_setup_sentry_sets_correct_tags(mock_diode_authentication):
    """Check that DiodeClient._setup_sentry() sets the correct tags."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )
    with mock.patch("sentry_sdk.set_tag") as mock_set_tag:
        client._setup_sentry("https://user@password.mock.dsn/123456", 0.5, 0.5)
        mock_set_tag.assert_any_call("target", client.target)
        mock_set_tag.assert_any_call("path", client.path if client.path else "/")
        mock_set_tag.assert_any_call("app_name", client.app_name)
        mock_set_tag.assert_any_call("app_version", client.app_version)
        mock_set_tag.assert_any_call("sdk_version", client.version)
        mock_set_tag.assert_any_call("platform", client._platform)
        mock_set_tag.assert_any_call("python_version", client._python_version)


def test_interceptor_init_sets_subpath():
    """Check that DiodeMethodClientInterceptor.__init__() sets the subpath."""
    interceptor = DiodeMethodClientInterceptor("/my/path")
    assert interceptor._subpath == "/my/path"


def test_interceptor_intercepts_unary_unary_calls():
    """Check that the interceptor intercepts unary unary calls."""
    interceptor = DiodeMethodClientInterceptor("/my/path")

    def continuation(x, _):
        return x.method

    client_call_details = _ClientCallDetails(
        "/diode.v1.IngesterService/Ingest",
        None,
        None,
        None,
        None,
        None,
    )
    request = None
    assert (
        interceptor.intercept_unary_unary(continuation, client_call_details, request)
        == "/my/path/diode.v1.IngesterService/Ingest"
    )


def test_interceptor_intercepts_stream_unary_calls():
    """Check that DiodeMethodClientInterceptor.intercept_stream_unary() intercepts stream unary calls."""
    interceptor = DiodeMethodClientInterceptor("/my/path")

    def continuation(x, _):
        return x.method

    client_call_details = _ClientCallDetails(
        "/diode.v1.IngesterService/Ingest",
        None,
        None,
        None,
        None,
        None,
    )
    request_iterator = None
    assert (
        interceptor.intercept_stream_unary(
            continuation, client_call_details, request_iterator
        )
        == "/my/path/diode.v1.IngesterService/Ingest"
    )


@pytest.fixture
def message_path() -> Path:
    """Path to the bundled dry-run message."""
    return Path(__file__).resolve().parent / "fixtures" / "message.json"


@pytest.fixture
def mock_diode_authentication():
    """
    Fixture to mock the Diode authentication process.

    This mock replaces the _DiodeAuthentication class with a mock object
    that returns a mocked token for authentication.
    """
    with patch("netboxlabs.diode.sdk.client._DiodeAuthentication") as MockAuth:
        mock_instance = MockAuth.return_value
        mock_instance.authenticate.return_value = "mocked_token"
        yield MockAuth


def test_diode_client_with_mocked_authentication(mock_diode_authentication):
    """
    Test the DiodeClient initialization with mocked authentication.

    This test verifies that the client is initialized correctly with the mocked
    authentication token and that the metadata includes the expected platform
    and authorization headers.
    """
    client = DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
        client_id="test_client_id",
        client_secret="test_client_secret",
    )
    assert client._metadata[0] == ("platform", client._platform)
    assert client._metadata[-1] == ("authorization", "Bearer mocked_token")


def test_ingest_retries_on_unauthenticated_error(mock_diode_authentication):
    """Test that the ingest method retries on UNAUTHENTICATED error."""
    # Create a mock stub that raises UNAUTHENTICATED error
    mock_stub = MagicMock()
    mock_stub.Ingest.side_effect = grpc.RpcError()
    mock_stub.Ingest.side_effect.code = lambda: grpc.StatusCode.UNAUTHENTICATED
    mock_stub.Ingest.side_effect.details = lambda: "Something went wrong"

    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        client_id="abcde",
        client_secret="123456",
    )

    # Patch the DiodeClient to use the mock stub
    client._stub = mock_stub

    # Attempt to ingest entities and expect a DiodeClientError after retries
    with pytest.raises(DiodeClientError):
        client.ingest(entities=[])

    # Verify that the Ingest method was called the expected number of times
    assert mock_stub.Ingest.call_count == client._max_auth_retries


def test_diode_authentication_success(mock_diode_authentication):
    """Test successful authentication in _DiodeAuthentication."""
    auth = _DiodeAuthentication(
        target="localhost:8081",
        path="/diode",
        tls_verify=False,
        client_id="test_client_id",
        client_secret="test_client_secret",
        scope="diode:ingest",
    )
    with mock.patch("http.client.HTTPConnection") as mock_http_conn:
        mock_conn_instance = mock_http_conn.return_value
        mock_conn_instance.getresponse.return_value.status = 200
        mock_conn_instance.getresponse.return_value.read.return_value = json.dumps(
            {"access_token": "mocked_token"}
        ).encode()

        token = auth.authenticate()
        assert token == "mocked_token"


def test_diode_authentication_failure(mock_diode_authentication):
    """Test authentication failure in _DiodeAuthentication."""
    auth = _DiodeAuthentication(
        target="localhost:8081",
        path="/diode",
        tls_verify=False,
        client_id="test_client_id",
        client_secret="test_client_secret",
        scope="diode:ingest",
    )
    with mock.patch("http.client.HTTPConnection") as mock_http_conn:
        mock_conn_instance = mock_http_conn.return_value
        mock_conn_instance.getresponse.return_value.status = 401
        mock_conn_instance.getresponse.return_value.reason = "Unauthorized"

        with pytest.raises(DiodeConfigError) as excinfo:
            auth.authenticate()
        assert "Failed to obtain access token" in str(excinfo.value)


@pytest.mark.parametrize(
    "path",
    [
        "/diode",
        "",
        None,
        "/diode/",
        "diode",
        "diode/",
    ],
)
def test_diode_authentication_url_with_path(mock_diode_authentication, path):
    """Test that the authentication URL is correctly formatted with a path."""
    auth = _DiodeAuthentication(
        target="localhost:8081",
        path=path,
        tls_verify=False,
        client_id="test_client_id",
        client_secret="test_client_secret",
        scope="diode:ingest",
    )
    with mock.patch("http.client.HTTPConnection") as mock_http_conn:
        mock_conn_instance = mock_http_conn.return_value
        mock_conn_instance.getresponse.return_value.status = 200
        mock_conn_instance.getresponse.return_value.read.return_value = json.dumps(
            {"access_token": "mocked_token"}
        ).encode()
        auth.authenticate()
        mock_conn_instance.request.assert_called_once_with(
            "POST", f"{(path or '').rstrip('/')}/auth/token", mock.ANY, mock.ANY
        )


def test_diode_authentication_request_exception(mock_diode_authentication):
    """Test that an exception during the request raises a DiodeConfigError."""
    auth = _DiodeAuthentication(
        target="localhost:8081",
        path="/diode",
        tls_verify=False,
        client_id="test_client_id",
        client_secret="test_client_secret",
        scope="diode:ingest",
    )
    with mock.patch("http.client.HTTPConnection") as mock_http_conn:
        mock_conn_instance = mock_http_conn.return_value
        mock_conn_instance.request.side_effect = Exception("Connection error")

        with pytest.raises(DiodeConfigError) as excinfo:
            auth.authenticate()
        assert "Failed to obtain access token: Connection error" in str(excinfo.value)


def test_ingest_dry_run_stdout(capsys):
    """Verify ingest prints JSON when dry run is enabled."""
    client = DiodeDryRunClient()

    client._stub = MagicMock()
    client.ingest(entities=[])

    captured = capsys.readouterr()
    assert client._stub.Ingest.call_count == 0
    assert captured.out.startswith("{")


def test_ingest_dry_run_file(tmp_path):
    """Verify ingest writes JSON to file when dry run output file is set."""
    client = DiodeDryRunClient(
        app_name="agent/my-producer",
        output_dir=str(tmp_path),
    )

    client._stub = MagicMock()
    client.ingest(entities=[Entity(site="Site1"), Entity(device="Device1")])
    client.ingest(entities=[Entity(site="Site2"), Entity(device="Device2")])

    files = list(tmp_path.glob("agent_my-producer*.json"))
    assert len(files) == 2
    assert client._stub.Ingest.call_count == 0
    for f in files:
        assert f.read_text().startswith("{")


def test_load_dryrun_entities(tmp_path):
    """Verify ``load_dryrun_entities`` yields protobuf entities."""
    client = DiodeDryRunClient(output_dir=str(tmp_path))

    client.ingest(entities=[Entity(site="Site1"), Entity(device="Device1")])

    files = list(tmp_path.glob("dryrun*.json"))
    assert len(files) == 1
    entities = list(load_dryrun_entities(files[0]))

    assert len(entities) == 2
    assert isinstance(entities[0], ingester_pb2.Entity)
    assert entities[0].site.name == "Site1"
    assert isinstance(entities[1], ingester_pb2.Entity)
    assert entities[1].device.name == "Device1"


def test_load_dryrun_entities_from_fixture(message_path, tmp_path):
    """Ensure entities load correctly from the bundled fixture."""
    entities = list(load_dryrun_entities(message_path))

    assert len(entities) == 94
    assert isinstance(entities[0], ingester_pb2.Entity)
    assert entities[0].asn.asn == 555
    assert entities[33].ip_address.address == "192.168.100.1/24"
    assert (
        entities[33].ip_address.assigned_object_interface.name == "GigabitEthernet1/0/1"
    )
    assert entities[-1].wireless_link.ssid == "P2P-Link-1"

    client = DiodeDryRunClient(output_dir=str(tmp_path))

    client._stub = MagicMock()
    client.ingest(entities=entities)

    assert client._stub.Ingest.call_count == 0
    files = list(tmp_path.glob("dryrun*.json"))
    assert len(files) == 1
    entities = list(load_dryrun_entities(files[0]))
    assert files[0].read_text().startswith("{")

    entities = list(load_dryrun_entities(files[0]))

    assert len(entities) == 94
    assert isinstance(entities[0], ingester_pb2.Entity)
    assert entities[0].asn.asn == 555
    assert entities[33].ip_address.address == "192.168.100.1/24"
    assert (
        entities[33].ip_address.assigned_object_interface.name == "GigabitEthernet1/0/1"
    )
    assert entities[-1].wireless_link.ssid == "P2P-Link-1"
