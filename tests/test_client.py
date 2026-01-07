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
    DiodeOTLPClient,
    _ClientCallDetails,
    _DiodeAuthentication,
    _get_sentry_dsn,
    _load_certs,
    load_dryrun_entities,
    parse_target,
)
from netboxlabs.diode.sdk.diode.v1 import ingester_pb2
from netboxlabs.diode.sdk.exceptions import (
    DiodeClientError,
    DiodeConfigError,
    OTLPClientError,
)
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


def test_parse_target_handles_ftp_prefix():
    """Check that parse_target raises an error when the target contains ftp://."""
    with pytest.raises(ValueError):
        parse_target("ftp://localhost:8081")


def test_parse_target_parses_authority_correctly():
    """Check that parse_target parses the authority correctly."""
    authority, path, tls_verify = parse_target("grpc://localhost:8081")
    assert authority == "localhost:8081"
    assert path == ""
    assert tls_verify is False


def test_parse_target_adds_default_port_if_missing():
    """Check that parse_target adds the default port if missing."""
    authority, _, _ = parse_target("grpc://localhost")
    assert authority == "localhost:80"
    authority, _, _ = parse_target("http://localhost")
    assert authority == "localhost:80"
    authority, _, _ = parse_target("grpcs://localhost")
    assert authority == "localhost:443"
    authority, _, _ = parse_target("https://localhost")
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
    _, _, tls_verify = parse_target("grpc://localhost:8081")
    assert tls_verify is False
    _, _, tls_verify = parse_target("http://localhost:8081")
    assert tls_verify is False
    _, _, tls_verify = parse_target("grpcs://localhost:8081")
    assert tls_verify is True
    _, _, tls_verify = parse_target("https://localhost:8081")
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

        # Check that debug was called with the secure channel message
        debug_calls = [call[0][0] for call in mock_debug.call_args_list]
        assert any("Setting up gRPC secure channel with" in call for call in debug_calls)
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
        sdk_name="diode-sdk-python",
        sdk_version="0.1.0",
        app_name="test-app",
        app_version="1.0.0",
    )
    with mock.patch("requests.Session") as mock_session_class:
        mock_session = mock_session_class.return_value
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"access_token": "mocked_token"}
        mock_session.post.return_value = mock_response

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
        sdk_name="diode-sdk-python",
        sdk_version="0.1.0",
        app_name="test-app",
        app_version="1.0.0",
    )
    with mock.patch("requests.Session") as mock_session_class:
        mock_session = mock_session_class.return_value
        mock_response = mock.Mock()
        mock_response.status_code = 401
        mock_response.reason = "Unauthorized"
        mock_session.post.return_value = mock_response

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
        sdk_name="diode-sdk-python",
        sdk_version="0.1.0",
        app_name="test-app",
        app_version="1.0.0",
    )
    with mock.patch("requests.Session") as mock_session_class:
        mock_session = mock_session_class.return_value
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"access_token": "mocked_token"}
        mock_session.post.return_value = mock_response

        auth.authenticate()

        # Verify the URL in the post call
        mock_session.post.assert_called_once()
        call_args = mock_session.post.call_args
        url = call_args[0][0]
        expected_url = f"http://localhost:8081{(path or '').rstrip('/')}/auth/token"
        assert url == expected_url


def test_diode_authentication_request_exception(mock_diode_authentication):
    """Test that an exception during the request raises a DiodeConfigError."""
    auth = _DiodeAuthentication(
        target="localhost:8081",
        path="/diode",
        tls_verify=False,
        client_id="test_client_id",
        client_secret="test_client_secret",
        scope="diode:ingest",
        sdk_name="diode-sdk-python",
        sdk_version="0.1.0",
        app_name="test-app",
        app_version="1.0.0",
    )
    with mock.patch("requests.Session") as mock_session_class:
        mock_session = mock_session_class.return_value
        # Import requests.RequestException for the side effect
        import requests
        mock_session.post.side_effect = requests.RequestException("Connection error")

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


def test_otlp_client_exports_entities():
    """Ensure DiodeOTLPClient serializes entities and exports them as logs."""
    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.insecure_channel"
        ) as mock_insecure_channel,
        patch(
            "netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"
        ) as mock_stub_cls,
    ):
        mock_insecure_channel.return_value = mock.Mock()
        stub_instance = mock_stub_cls.return_value

        client = DiodeOTLPClient(
            target="grpc://collector:4317",
            app_name="orb-producer",
            app_version="1.2.3",
        )

        response = client.ingest(
            entities=[Entity(site="Site1"), Entity(device="Device1")]
        )

        stub_instance.Export.assert_called_once()
        export_args, export_kwargs = stub_instance.Export.call_args
        request = export_args[0]
        resource_logs = request.resource_logs[0]
        scope_logs = resource_logs.scope_logs[0]
        log_records = scope_logs.log_records
        assert len(log_records) == 2
        body = json.loads(log_records[0].body.string_value)
        assert body["site"]["name"] == "Site1"
        attributes = {kv.key: kv.value.string_value for kv in log_records[0].attributes}
        assert attributes["diode.entity"] == "site"
        assert export_kwargs["timeout"] == client.timeout
        assert isinstance(response, ingester_pb2.IngestResponse)


def test_otlp_client_raises_on_rpc_error():
    """Ensure DiodeOTLPClient wraps gRPC errors in OTLPClientError."""

    class DummyRpcError(grpc.RpcError):
        def __init__(self, code, details):
            self._code = code
            self._details = details

        def code(self):
            return self._code

        def details(self):
            return self._details

    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.insecure_channel"
        ) as mock_insecure_channel,
        patch(
            "netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"
        ) as mock_stub_cls,
    ):
        mock_insecure_channel.return_value = mock.Mock()
        stub_instance = mock_stub_cls.return_value
        stub_instance.Export.side_effect = DummyRpcError(
            grpc.StatusCode.UNAVAILABLE, "endpoint offline"
        )

        client = DiodeOTLPClient(
            target="grpc://collector:4317",
            app_name="orb-producer",
            app_version="1.2.3",
        )

        with pytest.raises(OTLPClientError) as excinfo:
            client.ingest(entities=[Entity(site="Site1")])

        assert excinfo.value.status_code == grpc.StatusCode.UNAVAILABLE
        assert "details=endpoint offline" in str(excinfo.value)


def test_otlp_client_grpcs_uses_secure_channel():
    """Ensure DiodeOTLPClient configures SSL credentials for secure targets."""
    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.ssl_channel_credentials"
        ) as mock_ssl_credentials,
        patch("netboxlabs.diode.sdk.client.grpc.secure_channel") as mock_secure_channel,
        patch(
            "netboxlabs.diode.sdk.client.grpc.intercept_channel"
        ) as mock_intercept_channel,
        patch("netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"),
    ):
        base_channel = mock.Mock()
        mock_secure_channel.return_value = base_channel
        intercept_channel = mock.Mock()
        mock_intercept_channel.return_value = intercept_channel
        mock_ssl_credentials.return_value = mock.Mock()

        client = DiodeOTLPClient(
            target="grpcs://collector.example:4317/custom",
            app_name="orb-producer",
            app_version="1.2.3",
        )

        mock_ssl_credentials.assert_called_once()
        mock_secure_channel.assert_called_once()
        mock_intercept_channel.assert_called_once()

        client.close()
        base_channel.close.assert_called_once()


def test_diode_authentication_with_custom_certificates():
    """Test _DiodeAuthentication with custom certificates - covers SSL context creation."""
    # Create test certificate content
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )

    auth = _DiodeAuthentication(
        target="example.com:443",
        path="/api/v1",
        tls_verify=True,
        client_id="test_client",
        client_secret="test_secret",
        scope="test_scope",
        sdk_name="diode-sdk-python",
        sdk_version="0.1.0",
        app_name="test-app",
        app_version="1.0.0",
        certificates=cert_content,
    )

    with (
        mock.patch("requests.Session") as mock_session_class,
        mock.patch("tempfile.NamedTemporaryFile") as mock_tempfile,
        mock.patch("os.path.exists") as mock_exists,
        mock.patch("os.unlink") as mock_unlink,
    ):
        # Setup temp file mock
        mock_temp_file = mock.Mock()
        mock_temp_file.name = "/tmp/test_cert.pem"
        mock_temp_file.__enter__ = mock.Mock(return_value=mock_temp_file)
        mock_temp_file.__exit__ = mock.Mock(return_value=False)
        mock_tempfile.return_value = mock_temp_file

        # Mock os.path.exists to return True so cleanup happens
        mock_exists.return_value = True

        # Setup session mock
        mock_session = mock_session_class.return_value
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"access_token": "test_token"}
        mock_session.post.return_value = mock_response

        # Call authenticate
        token = auth.authenticate()

        # Verify tempfile was created for the certificate
        mock_tempfile.assert_called_once()
        call_kwargs = mock_tempfile.call_args[1]
        assert call_kwargs["mode"] == "wb"
        assert call_kwargs["delete"] is False
        assert call_kwargs["suffix"] == ".pem"

        # Verify certificate was written
        mock_temp_file.write.assert_called_once_with(cert_content)

        # Verify session.verify was set to the temp file path
        assert mock_session.verify == "/tmp/test_cert.pem"

        # Verify the post request was made
        mock_session.post.assert_called_once()

        # Verify os.path.exists was checked
        mock_exists.assert_called_once_with("/tmp/test_cert.pem")

        # Verify temp file was cleaned up
        mock_unlink.assert_called_once_with("/tmp/test_cert.pem")

        # Verify token was returned
        assert token == "test_token"


def test_load_certs_with_custom_cert_file(tmp_path):
    """Test _load_certs loads custom certificate file."""
    # Create a dummy certificate file
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    result = _load_certs(str(cert_file))
    assert result == cert_content


def test_load_certs_with_none_uses_default():
    """Test _load_certs uses default certifi when cert_file is None."""
    result = _load_certs(None)
    assert isinstance(result, bytes)
    assert len(result) > 0


def test_client_with_cert_file_parameter(mock_diode_authentication, tmp_path):
    """Test DiodeClient with cert_file parameter loads custom cert but respects TLS scheme."""
    # Create a dummy certificate file
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
        client = DiodeClient(
            target="grpc://localhost:8081",  # Note: grpc:// insecure scheme
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
            cert_file=str(cert_file),
        )

        # Should respect scheme (insecure) even with cert file
        assert client.tls_verify is False

        # Should use insecure channel
        mock_insecure_channel.assert_called_once()

        # Verify certificate was still loaded for potential use
        assert client._certificates == cert_content


def test_client_with_cert_file_env_var(mock_diode_authentication, tmp_path):
    """Test DiodeClient with DIODE_CERT_FILE environment variable respects scheme."""
    from netboxlabs.diode.sdk.client import _DIODE_CERT_FILE_ENVVAR_NAME

    # Create a dummy certificate file
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    # Set environment variable
    original_env = os.environ.get(_DIODE_CERT_FILE_ENVVAR_NAME)
    os.environ[_DIODE_CERT_FILE_ENVVAR_NAME] = str(cert_file)

    try:
        with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
            client = DiodeClient(
                target="grpc://localhost:8081",  # Note: grpc:// insecure scheme
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
            )

            # Should respect scheme (insecure) even with cert file
            assert client.tls_verify is False

            # Should use insecure channel
            mock_insecure_channel.assert_called_once()

            # Verify certificate was still loaded
            assert client._certificates == cert_content

    finally:
        # Clean up environment variable
        if original_env is not None:
            os.environ[_DIODE_CERT_FILE_ENVVAR_NAME] = original_env
        else:
            if _DIODE_CERT_FILE_ENVVAR_NAME in os.environ:
                del os.environ[_DIODE_CERT_FILE_ENVVAR_NAME]


def test_client_cert_file_parameter_overrides_env_var(
    mock_diode_authentication, tmp_path
):
    """Test cert_file parameter takes precedence over environment variable."""
    from netboxlabs.diode.sdk.client import _DIODE_CERT_FILE_ENVVAR_NAME

    # Create two dummy certificate files
    env_cert_content = (
        b"-----BEGIN CERTIFICATE-----\nENV CERT\n-----END CERTIFICATE-----\n"
    )
    param_cert_content = (
        b"-----BEGIN CERTIFICATE-----\nPARAM CERT\n-----END CERTIFICATE-----\n"
    )

    env_cert_file = tmp_path / "env.pem"
    param_cert_file = tmp_path / "param.pem"

    env_cert_file.write_bytes(env_cert_content)
    param_cert_file.write_bytes(param_cert_content)

    # Set environment variable
    original_env = os.environ.get(_DIODE_CERT_FILE_ENVVAR_NAME)
    os.environ[_DIODE_CERT_FILE_ENVVAR_NAME] = str(env_cert_file)

    try:
        with mock.patch("netboxlabs.diode.sdk.client._load_certs") as mock_load_certs:
            mock_load_certs.return_value = param_cert_content

            client = DiodeClient(
                target="grpc://localhost:8081",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
                cert_file=str(param_cert_file),
            )

            # Should use the parameter file, not the environment variable
            mock_load_certs.assert_called_with(str(param_cert_file))
            # grpc:// scheme should keep tls_verify=False even with cert file
            assert client.tls_verify is False

    finally:
        # Clean up environment variable
        if original_env is not None:
            os.environ[_DIODE_CERT_FILE_ENVVAR_NAME] = original_env
        else:
            if _DIODE_CERT_FILE_ENVVAR_NAME in os.environ:
                del os.environ[_DIODE_CERT_FILE_ENVVAR_NAME]


def test_client_secure_channel_uses_custom_cert(mock_diode_authentication, tmp_path):
    """Test secure channel creation uses custom certificate when provided."""
    # Create a dummy certificate file
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    with (
        mock.patch("grpc.secure_channel") as mock_secure_channel,
        mock.patch("grpc.ssl_channel_credentials") as mock_ssl_creds,
        mock.patch("netboxlabs.diode.sdk.client._load_certs") as mock_load_certs,
    ):
        mock_load_certs.return_value = cert_content

        _ = DiodeClient(
            target="grpcs://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
            cert_file=str(cert_file),
        )

        # Verify _load_certs was called with the custom cert file
        mock_load_certs.assert_called_with(str(cert_file))

        # Verify ssl_channel_credentials was called with the custom cert content
        mock_ssl_creds.assert_called_once_with(root_certificates=cert_content)

        # Verify secure_channel was called
        mock_secure_channel.assert_called_once()


def test_client_without_cert_file_uses_default_certs(mock_diode_authentication):
    """Test secure channel uses default certificates when no cert_file provided."""
    with (
        mock.patch("grpc.secure_channel") as mock_secure_channel,
        mock.patch("grpc.ssl_channel_credentials") as mock_ssl_creds,
        mock.patch("netboxlabs.diode.sdk.client._load_certs") as mock_load_certs,
    ):
        mock_load_certs.return_value = b"default cert content"

        _ = DiodeClient(
            target="grpcs://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
        )

        # Verify _load_certs was called with None (default)
        mock_load_certs.assert_called_with(None)

        # Verify ssl_channel_credentials was called with default cert content
        mock_ssl_creds.assert_called_once_with(
            root_certificates=b"default cert content"
        )

        # Verify secure_channel was called
        mock_secure_channel.assert_called_once()


def test_should_verify_tls_with_different_schemes():
    """Test _should_verify_tls with different URL schemes."""
    from netboxlabs.diode.sdk.client import (
        _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME,
        _should_verify_tls,
    )

    # Clear environment variable to avoid interference
    if _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME in os.environ:
        del os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME]

    assert _should_verify_tls("grpc") is False  # insecure scheme
    assert _should_verify_tls("http") is False  # insecure scheme
    assert _should_verify_tls("grpcs") is True  # secure scheme
    assert _should_verify_tls("https") is True  # secure scheme


def test_should_verify_tls_with_skip_env_var():
    """Test _should_verify_tls with DIODE_SKIP_TLS_VERIFY environment variable."""
    from netboxlabs.diode.sdk.client import (
        _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME,
        _should_verify_tls,
    )

    original_env = os.environ.get(_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME)

    try:
        # Test truthy values that should skip TLS verification
        for skip_value in ["true", "True", "TRUE", "1", "yes", "on"]:
            os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = skip_value
            assert (
                _should_verify_tls("grpcs") is False
            )  # Should skip even for secure schemes

        # Test falsy values that should NOT skip TLS verification
        for verify_value in ["false", "0", "no", "off", "", "random"]:
            os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = verify_value
            assert (
                _should_verify_tls("grpcs") is True
            )  # Should verify for secure schemes

    finally:
        # Clean up environment variable
        if original_env is not None:
            os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = original_env
        else:
            if _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME in os.environ:
                del os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME]


def test_client_with_skip_tls_verify_env_var(mock_diode_authentication):
    """Test DiodeClient with DIODE_SKIP_TLS_VERIFY environment variable."""
    from netboxlabs.diode.sdk.client import _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME

    original_env = os.environ.get(_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME)

    try:
        # Set environment variable to skip TLS verification
        os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = "true"

        with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
            client = DiodeClient(
                target="grpcs://localhost:8081",  # Note: grpcs:// but TLS should be skipped
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
            )

            # Should skip TLS verification due to environment variable
            assert client.tls_verify is False

            # Should use insecure channel even with grpcs://
            mock_insecure_channel.assert_called_once()

    finally:
        # Clean up environment variable
        if original_env is not None:
            os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = original_env
        else:
            if _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME in os.environ:
                del os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME]


def test_client_cert_file_with_skip_tls_verify_env_var(
    mock_diode_authentication, tmp_path
):
    """Test cert_file parameter with DIODE_SKIP_TLS_VERIFY environment variable."""
    from netboxlabs.diode.sdk.client import _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME

    # Create a dummy certificate file
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    original_skip_env = os.environ.get(_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME)

    try:
        # Set environment variable to skip TLS verification
        os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = "true"

        with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
            client = DiodeClient(
                target="grpcs://localhost:8081",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
                cert_file=str(cert_file),
            )

            # Should respect DIODE_SKIP_TLS_VERIFY=true even with cert_file
            assert client.tls_verify is False

            # Should use insecure channel due to environment variable
            mock_insecure_channel.assert_called_once()

            # Certificate should still be loaded for potential use
            assert client._certificates == cert_content

    finally:
        # Clean up environment variable
        if original_skip_env is not None:
            os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME] = original_skip_env
        else:
            if _DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME in os.environ:
                del os.environ[_DIODE_SKIP_TLS_VERIFY_ENVVAR_NAME]


def test_certificate_loading_efficiency(tmp_path):
    """Test that certificates are loaded only once during client initialization."""
    # Create a dummy certificate file
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    with (
        mock.patch("netboxlabs.diode.sdk.client._load_certs") as mock_load_certs,
        mock.patch(
            "netboxlabs.diode.sdk.client._DiodeAuthentication"
        ) as mock_auth_class,
    ):
        mock_load_certs.return_value = cert_content
        mock_auth_instance = mock_auth_class.return_value
        mock_auth_instance.authenticate.return_value = "test_token"

        # Create client with custom certificate
        client = DiodeClient(
            target="grpcs://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            client_id="abcde",
            client_secret="123456",
            cert_file=str(cert_file),
        )

        # Verify _load_certs was called exactly once during initialization
        mock_load_certs.assert_called_once_with(str(cert_file))

        # Verify certificates are stored and reused
        assert client._certificates == cert_content

        # Verify that the authentication class was created with the certificate bytes and cert_file
        mock_auth_class.assert_called_once()
        auth_call_args = mock_auth_class.call_args

        # The second-to-last argument should be the certificate bytes
        assert auth_call_args[0][-2] == cert_content  # certificates parameter
        # The last argument should be the cert_file path
        assert auth_call_args[0][-1] == str(cert_file)  # cert_file parameter

        # Reset the mock to verify no additional calls during authentication
        mock_load_certs.reset_mock()

        # Authentication should have already been called during initialization
        # and should have used the preloaded certificates
        mock_auth_instance.authenticate.assert_called_once()

        # Verify _load_certs was NOT called again (certificates reused)
        mock_load_certs.assert_not_called()


# ==================== Request-Level Metadata Tests ====================


def test_grpc_client_ingest_with_request_metadata(mock_diode_authentication):
    """Test DiodeClient includes request-level metadata in IngestRequest."""
    with patch("netboxlabs.diode.sdk.client.grpc.insecure_channel") as mock_channel:
        mock_stub = MagicMock()
        mock_channel.return_value = MagicMock()

        client = DiodeClient(
            target="grpc://localhost:8081",
            app_name="test-app",
            app_version="1.0.0",
            client_id="test-id",
            client_secret="test-secret",
        )
        client._stub = mock_stub
        mock_stub.Ingest.return_value = ingester_pb2.IngestResponse()

        # Ingest with request-level metadata
        metadata = {
            "batch_id": "batch-123",
            "record_count": 150,
            "validated": True,
        }

        response = client.ingest(
            entities=[Entity(site="TestSite")],
            metadata=metadata,
        )

        # Verify Ingest was called
        assert mock_stub.Ingest.called
        call_args = mock_stub.Ingest.call_args[0]
        request = call_args[0]

        # Verify metadata is in the request
        assert request.HasField("metadata")
        assert "batch_id" in request.metadata.fields
        assert request.metadata.fields["batch_id"].string_value == "batch-123"
        assert "record_count" in request.metadata.fields
        assert request.metadata.fields["record_count"].number_value == 150
        assert "validated" in request.metadata.fields
        assert request.metadata.fields["validated"].bool_value is True

        assert isinstance(response, ingester_pb2.IngestResponse)


def test_grpc_client_ingest_without_metadata(mock_diode_authentication):
    """Test DiodeClient works without metadata (backward compatibility)."""
    with patch("netboxlabs.diode.sdk.client.grpc.insecure_channel") as mock_channel:
        mock_stub = MagicMock()
        mock_channel.return_value = MagicMock()

        client = DiodeClient(
            target="grpc://localhost:8081",
            app_name="test-app",
            app_version="1.0.0",
            client_id="test-id",
            client_secret="test-secret",
        )
        client._stub = mock_stub
        mock_stub.Ingest.return_value = ingester_pb2.IngestResponse()

        # Ingest without metadata
        response = client.ingest(entities=[Entity(site="TestSite")])

        # Verify Ingest was called
        assert mock_stub.Ingest.called
        call_args = mock_stub.Ingest.call_args[0]
        request = call_args[0]

        # Verify metadata field exists but is empty
        assert not request.HasField("metadata") or len(request.metadata.fields) == 0
        assert isinstance(response, ingester_pb2.IngestResponse)


def test_dryrun_client_includes_metadata_in_output(tmp_path):
    """Test DiodeDryRunClient includes request-level metadata in JSON output."""
    output_dir = tmp_path / "dryrun_output"
    output_dir.mkdir()

    client = DiodeDryRunClient(
        app_name="test-producer",
        output_dir=str(output_dir),
    )

    metadata = {
        "import_id": "imp-456",
        "source": "csv-import",
        "priority": 5,
    }

    client.ingest(
        entities=[Entity(site="Site1"), Entity(device="Device1")],
        metadata=metadata,
    )

    # Find the generated JSON file
    json_files = list(output_dir.glob("*.json"))
    assert len(json_files) == 1

    with open(json_files[0]) as f:
        data = json.load(f)

    # Verify metadata is in the output
    assert "metadata" in data
    assert data["metadata"]["import_id"] == "imp-456"
    assert data["metadata"]["source"] == "csv-import"
    assert data["metadata"]["priority"] == 5

    # Verify entities are present
    assert "entities" in data
    assert len(data["entities"]) == 2


def test_otlp_client_maps_metadata_to_resource_attributes():
    """Test DiodeOTLPClient maps request metadata to OTLP resource attributes."""
    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.insecure_channel"
        ) as mock_insecure_channel,
        patch(
            "netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"
        ) as mock_stub_cls,
    ):
        mock_insecure_channel.return_value = mock.Mock()
        stub_instance = mock_stub_cls.return_value

        client = DiodeOTLPClient(
            target="grpc://collector:4317",
            app_name="test-app",
            app_version="1.0.0",
        )

        metadata = {
            "environment": "production",
            "region": "us-west",
            "instance_count": 10,
        }

        client.ingest(
            entities=[Entity(site="TestSite")],
            metadata=metadata,
        )

        # Get the Export call arguments
        stub_instance.Export.assert_called_once()
        export_args, _ = stub_instance.Export.call_args
        request = export_args[0]
        resource_logs = request.resource_logs[0]

        # Extract resource attributes
        attributes = {kv.key: kv.value for kv in resource_logs.resource.attributes}

        # Verify metadata is mapped with diode.metadata.* prefix
        assert "diode.metadata.environment" in attributes
        assert attributes["diode.metadata.environment"].string_value == "production"
        assert "diode.metadata.region" in attributes
        assert attributes["diode.metadata.region"].string_value == "us-west"
        assert "diode.metadata.instance_count" in attributes
        assert attributes["diode.metadata.instance_count"].int_value == 10


def test_otlp_client_handles_nested_metadata():
    """Test DiodeOTLPClient handles nested metadata structures."""
    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.insecure_channel"
        ) as mock_insecure_channel,
        patch(
            "netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"
        ) as mock_stub_cls,
    ):
        mock_insecure_channel.return_value = mock.Mock()
        stub_instance = mock_stub_cls.return_value

        client = DiodeOTLPClient(
            target="grpc://collector:4317",
            app_name="test-app",
            app_version="1.0.0",
        )

        metadata = {
            "tags": ["prod", "critical"],
            "config": {
                "retry_count": 3,
                "timeout": 30.5,
                "features": {
                    "validation": True,
                    "auto_sync": False,
                },
            },
        }

        client.ingest(
            entities=[Entity(site="TestSite")],
            metadata=metadata,
        )

        # Get the Export call arguments
        stub_instance.Export.assert_called_once()
        export_args, _ = stub_instance.Export.call_args
        request = export_args[0]
        resource_logs = request.resource_logs[0]

        # Extract resource attributes
        attributes = {kv.key: kv.value for kv in resource_logs.resource.attributes}

        # Verify nested metadata is present
        assert "diode.metadata.tags" in attributes
        assert attributes["diode.metadata.tags"].HasField("array_value")
        tags_array = attributes["diode.metadata.tags"].array_value.values
        assert len(tags_array) == 2
        assert tags_array[0].string_value == "prod"
        assert tags_array[1].string_value == "critical"

        assert "diode.metadata.config" in attributes
        assert attributes["diode.metadata.config"].HasField("kvlist_value")
        config_kvlist = attributes["diode.metadata.config"].kvlist_value.values
        config_dict = {kv.key: kv.value for kv in config_kvlist}

        assert "retry_count" in config_dict
        assert config_dict["retry_count"].int_value == 3
        assert "timeout" in config_dict
        assert config_dict["timeout"].double_value == 30.5
        assert "features" in config_dict
        assert config_dict["features"].HasField("kvlist_value")


def test_otlp_client_metadata_type_conversion():
    """Test DiodeOTLPClient correctly converts different Python types."""
    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.insecure_channel"
        ) as mock_insecure_channel,
        patch(
            "netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"
        ) as mock_stub_cls,
    ):
        mock_insecure_channel.return_value = mock.Mock()
        stub_instance = mock_stub_cls.return_value

        client = DiodeOTLPClient(
            target="grpc://collector:4317",
            app_name="test-app",
            app_version="1.0.0",
        )

        metadata = {
            "string_val": "test",
            "int_val": 42,
            "float_val": 3.14,
            "bool_true": True,
            "bool_false": False,
        }

        client.ingest(
            entities=[Entity(site="TestSite")],
            metadata=metadata,
        )

        # Get the Export call arguments
        stub_instance.Export.assert_called_once()
        export_args, _ = stub_instance.Export.call_args
        request = export_args[0]
        resource_logs = request.resource_logs[0]

        # Extract resource attributes
        attributes = {kv.key: kv.value for kv in resource_logs.resource.attributes}

        # Verify type conversions
        assert attributes["diode.metadata.string_val"].string_value == "test"
        assert attributes["diode.metadata.int_val"].int_value == 42
        assert attributes["diode.metadata.float_val"].double_value == 3.14
        assert attributes["diode.metadata.bool_true"].bool_value is True
        assert attributes["diode.metadata.bool_false"].bool_value is False


def test_otlp_client_without_metadata():
    """Test DiodeOTLPClient works without metadata (backward compatibility)."""
    with (
        patch(
            "netboxlabs.diode.sdk.client.grpc.insecure_channel"
        ) as mock_insecure_channel,
        patch(
            "netboxlabs.diode.sdk.client.logs_service_pb2_grpc.LogsServiceStub"
        ) as mock_stub_cls,
    ):
        mock_insecure_channel.return_value = mock.Mock()
        stub_instance = mock_stub_cls.return_value

        client = DiodeOTLPClient(
            target="grpc://collector:4317",
            app_name="test-app",
            app_version="1.0.0",
        )

        # Ingest without metadata
        client.ingest(entities=[Entity(site="TestSite")])

        # Get the Export call arguments
        stub_instance.Export.assert_called_once()
        export_args, _ = stub_instance.Export.call_args
        request = export_args[0]
        resource_logs = request.resource_logs[0]

        # Extract resource attributes
        attributes = {kv.key for kv in resource_logs.resource.attributes}

        # Verify no diode.metadata.* attributes are present
        metadata_attrs = [k for k in attributes if k.startswith("diode.metadata.")]
        assert len(metadata_attrs) == 0


def test_get_proxy_env_var_uppercase():
    """Test _get_proxy_env_var returns uppercase environment variable."""
    from netboxlabs.diode.sdk.client import _get_proxy_env_var

    os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
    try:
        assert _get_proxy_env_var("HTTP_PROXY") == "http://proxy.example.com:8080"
    finally:
        del os.environ["HTTP_PROXY"]


def test_get_proxy_env_var_lowercase():
    """Test _get_proxy_env_var returns lowercase environment variable."""
    from netboxlabs.diode.sdk.client import _get_proxy_env_var

    os.environ["http_proxy"] = "http://proxy.example.com:8080"
    try:
        assert _get_proxy_env_var("http_proxy") == "http://proxy.example.com:8080"
    finally:
        del os.environ["http_proxy"]


def test_get_proxy_env_var_prefers_uppercase():
    """Test _get_proxy_env_var prefers uppercase over lowercase."""
    from netboxlabs.diode.sdk.client import _get_proxy_env_var

    os.environ["HTTP_PROXY"] = "http://upper.example.com:8080"
    os.environ["http_proxy"] = "http://lower.example.com:8080"
    try:
        assert _get_proxy_env_var("http_proxy") == "http://upper.example.com:8080"
    finally:
        del os.environ["HTTP_PROXY"]
        del os.environ["http_proxy"]


def test_should_bypass_proxy_localhost():
    """Test _should_bypass_proxy returns True for localhost."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    assert _should_bypass_proxy("localhost") is True
    assert _should_bypass_proxy("localhost:8080") is True


def test_should_bypass_proxy_127_0_0_1():
    """Test _should_bypass_proxy returns True for 127.0.0.1."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    assert _should_bypass_proxy("127.0.0.1") is True
    assert _should_bypass_proxy("127.0.0.1:8080") is True


def test_should_bypass_proxy_with_no_proxy_asterisk():
    """Test _should_bypass_proxy returns True when NO_PROXY is '*'."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    os.environ["NO_PROXY"] = "*"
    try:
        assert _should_bypass_proxy("example.com") is True
        assert _should_bypass_proxy("any.host.com") is True
    finally:
        del os.environ["NO_PROXY"]


def test_should_bypass_proxy_exact_match():
    """Test _should_bypass_proxy matches exact hostname."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    os.environ["NO_PROXY"] = "example.com"
    try:
        assert _should_bypass_proxy("example.com") is True
        assert _should_bypass_proxy("example.com:443") is True
    finally:
        del os.environ["NO_PROXY"]


def test_should_bypass_proxy_subdomain_match():
    """Test _should_bypass_proxy matches subdomains."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    os.environ["NO_PROXY"] = "example.com"
    try:
        assert _should_bypass_proxy("api.example.com") is True
        assert _should_bypass_proxy("www.example.com") is True
    finally:
        del os.environ["NO_PROXY"]


def test_get_grpc_proxy_url_https_proxy_for_tls():
    """Test _get_grpc_proxy_url uses HTTPS_PROXY for TLS connections."""
    from netboxlabs.diode.sdk.client import _get_grpc_proxy_url

    os.environ["HTTPS_PROXY"] = "http://https-proxy.example.com:8080"
    try:
        proxy_url = _get_grpc_proxy_url("example.com:443", use_tls=True)
        assert proxy_url == "http://https-proxy.example.com:8080"
    finally:
        del os.environ["HTTPS_PROXY"]


def test_get_grpc_proxy_url_http_proxy_fallback_for_tls():
    """Test _get_grpc_proxy_url falls back to HTTP_PROXY for TLS connections."""
    from netboxlabs.diode.sdk.client import _get_grpc_proxy_url

    os.environ["HTTP_PROXY"] = "http://http-proxy.example.com:8080"
    try:
        proxy_url = _get_grpc_proxy_url("example.com:443", use_tls=True)
        assert proxy_url == "http://http-proxy.example.com:8080"
    finally:
        del os.environ["HTTP_PROXY"]


def test_get_grpc_proxy_url_respects_no_proxy():
    """Test _get_grpc_proxy_url respects NO_PROXY."""
    from netboxlabs.diode.sdk.client import _get_grpc_proxy_url

    os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
    os.environ["NO_PROXY"] = "example.com"
    try:
        proxy_url = _get_grpc_proxy_url("example.com:443", use_tls=True)
        assert proxy_url is None
    finally:
        del os.environ["HTTP_PROXY"]
        del os.environ["NO_PROXY"]


def test_diode_client_configures_proxy_option(mock_diode_authentication):
    """Test DiodeClient adds grpc.http_proxy option when proxy is detected."""
    os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
    try:
        with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
            DiodeClient(
                target="grpc://example.com:8081",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
            )

            # Should use insecure channel for grpc:// target, even with proxy
            mock_insecure_channel.assert_called_once()
            _, kwargs = mock_insecure_channel.call_args
            options = kwargs["options"]

            # Check that grpc.http_proxy option is present
            proxy_option = next(
                (opt for opt in options if opt[0] == "grpc.http_proxy"), None
            )
            assert proxy_option is not None
            assert proxy_option[1] == "http://proxy.example.com:8080"
    finally:
        del os.environ["HTTP_PROXY"]


def test_diode_client_uses_insecure_channel_with_proxy_when_skip_tls(
    mock_diode_authentication,
):
    """Test DiodeClient uses insecure channel with proxy when SKIP_TLS_VERIFY is set."""
    os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
    os.environ["DIODE_SKIP_TLS_VERIFY"] = "true"
    try:
        with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
            DiodeClient(
                target="grpcs://example.com:443",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
            )

            # Should use insecure channel when SKIP_TLS_VERIFY is set, even with proxy
            mock_insecure_channel.assert_called_once()
            _, kwargs = mock_insecure_channel.call_args
            options = kwargs["options"]

            # Verify proxy option is set
            proxy_option = next(
                (opt for opt in options if opt[0] == "grpc.http_proxy"), None
            )
            assert proxy_option is not None
            assert proxy_option[1] == "http://proxy.example.com:8080"
    finally:
        del os.environ["HTTP_PROXY"]
        del os.environ["DIODE_SKIP_TLS_VERIFY"]


def test_diode_client_respects_no_proxy_for_target(mock_diode_authentication):
    """Test DiodeClient respects NO_PROXY environment variable."""
    os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
    os.environ["NO_PROXY"] = "example.com"
    try:
        with mock.patch("grpc.insecure_channel") as mock_insecure_channel:
            DiodeClient(
                target="grpc://example.com:8081",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
            )

            mock_insecure_channel.assert_called_once()
            _, kwargs = mock_insecure_channel.call_args
            options = kwargs["options"]

            # Check that grpc.http_proxy option is NOT present
            proxy_option = next(
                (opt for opt in options if opt[0] == "grpc.http_proxy"), None
            )
            assert proxy_option is None
    finally:
        del os.environ["HTTP_PROXY"]
        del os.environ["NO_PROXY"]


def test_diode_client_with_proxy_and_custom_cert(mock_diode_authentication, tmp_path):
    """Test DiodeClient with proxy and custom certificate (for MITM proxies)."""
    cert_content = (
        b"-----BEGIN CERTIFICATE-----\nTEST CERT\n-----END CERTIFICATE-----\n"
    )
    cert_file = tmp_path / "custom.pem"
    cert_file.write_bytes(cert_content)

    os.environ["HTTPS_PROXY"] = "http://proxy.example.com:8080"
    try:
        with (
            mock.patch("grpc.secure_channel") as mock_secure_channel,
            mock.patch("grpc.ssl_channel_credentials") as mock_ssl_creds,
        ):
            mock_ssl_creds.return_value = mock.Mock()

            DiodeClient(
                target="grpcs://example.com:443",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
                cert_file=str(cert_file),
            )

            # Should use secure channel
            mock_secure_channel.assert_called_once()

            # Should use custom certificate
            mock_ssl_creds.assert_called_once()
            ssl_call_args = mock_ssl_creds.call_args
            assert ssl_call_args[1]["root_certificates"] == cert_content

            # Verify proxy option is set
            _, kwargs = mock_secure_channel.call_args
            options = kwargs["options"]
            proxy_option = next(
                (opt for opt in options if opt[0] == "grpc.http_proxy"), None
            )
            assert proxy_option is not None
            assert proxy_option[1] == "http://proxy.example.com:8080"
    finally:
        del os.environ["HTTPS_PROXY"]


def test_validate_proxy_url_valid_http():
    """Test _validate_proxy_url with valid HTTP URL."""
    from netboxlabs.diode.sdk.client import _validate_proxy_url

    assert _validate_proxy_url("http://proxy.example.com:8080") is True


def test_validate_proxy_url_valid_https():
    """Test _validate_proxy_url with valid HTTPS URL."""
    from netboxlabs.diode.sdk.client import _validate_proxy_url

    assert _validate_proxy_url("https://proxy.example.com:8443") is True


def test_validate_proxy_url_invalid_scheme():
    """Test _validate_proxy_url with invalid scheme."""
    from netboxlabs.diode.sdk.client import _validate_proxy_url

    assert _validate_proxy_url("ftp://proxy.example.com:8080") is False
    assert _validate_proxy_url("socks5://proxy.example.com:1080") is False


def test_validate_proxy_url_missing_netloc():
    """Test _validate_proxy_url with missing netloc."""
    from netboxlabs.diode.sdk.client import _validate_proxy_url

    assert _validate_proxy_url("http://") is False
    assert _validate_proxy_url("https://") is False


def test_validate_proxy_url_empty_string():
    """Test _validate_proxy_url with empty string."""
    from netboxlabs.diode.sdk.client import _validate_proxy_url

    assert _validate_proxy_url("") is False


def test_validate_proxy_url_malformed():
    """Test _validate_proxy_url with malformed URLs."""
    from netboxlabs.diode.sdk.client import _validate_proxy_url

    assert _validate_proxy_url("not_a_url") is False
    assert _validate_proxy_url("://missing-scheme") is False


def test_get_grpc_proxy_url_invalid_proxy_url():
    """Test _get_grpc_proxy_url with invalid proxy URL format."""
    from netboxlabs.diode.sdk.client import _get_grpc_proxy_url

    os.environ["HTTP_PROXY"] = "not_a_valid_url"
    try:
        with mock.patch("logging.Logger.warning") as mock_warning:
            result = _get_grpc_proxy_url("example.com:443", use_tls=False)

            # Should return None for invalid proxy URL
            assert result is None

            # Should log warning
            mock_warning.assert_called_once()
            warning_message = mock_warning.call_args[0][0]
            assert "Invalid proxy URL format" in warning_message
            assert "not_a_valid_url" in warning_message
    finally:
        del os.environ["HTTP_PROXY"]


def test_get_grpc_proxy_url_ftp_scheme_rejected():
    """Test _get_grpc_proxy_url rejects non-HTTP/HTTPS schemes."""
    from netboxlabs.diode.sdk.client import _get_grpc_proxy_url

    os.environ["HTTP_PROXY"] = "ftp://proxy.example.com:21"
    try:
        with mock.patch("logging.Logger.warning") as mock_warning:
            result = _get_grpc_proxy_url("example.com:443", use_tls=False)

            # Should return None
            assert result is None

            # Should log warning
            mock_warning.assert_called_once()
    finally:
        del os.environ["HTTP_PROXY"]


def test_should_bypass_proxy_with_long_no_proxy_entries():
    """Test _should_bypass_proxy filters out entries exceeding max length."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    # Create a NO_PROXY with one valid and one excessively long entry
    valid_entry = "example.com"
    long_entry = "a" * 300  # 300 characters, exceeds 256 limit

    os.environ["NO_PROXY"] = f"{valid_entry},{long_entry}"
    try:
        with mock.patch("logging.Logger.warning") as mock_warning:
            # Should match valid entry
            result = _should_bypass_proxy("example.com:443")
            assert result is True

            # Should warn about filtered entries
            mock_warning.assert_called_once()
            warning_message = mock_warning.call_args[0][0]
            assert "Ignored 1 NO_PROXY entries exceeding 256 characters" in warning_message
    finally:
        del os.environ["NO_PROXY"]


def test_should_bypass_proxy_with_multiple_long_entries():
    """Test _should_bypass_proxy warns about multiple long entries."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    # Create multiple excessively long entries
    long_entry1 = "a" * 300
    long_entry2 = "b" * 400
    long_entry3 = "c" * 500
    valid_entry = "valid.example.com"

    os.environ["NO_PROXY"] = f"{long_entry1},{valid_entry},{long_entry2},{long_entry3}"
    try:
        with mock.patch("logging.Logger.warning") as mock_warning:
            # Should match valid entry
            result = _should_bypass_proxy("valid.example.com:443")
            assert result is True

            # Should warn about 3 filtered entries
            mock_warning.assert_called_once()
            warning_message = mock_warning.call_args[0][0]
            assert "Ignored 3 NO_PROXY entries exceeding 256 characters" in warning_message
    finally:
        del os.environ["NO_PROXY"]


def test_should_bypass_proxy_max_length_entry_accepted():
    """Test _should_bypass_proxy accepts entries at max length (256 chars)."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    # Create an entry exactly 256 characters long
    max_length_entry = "a" * 256

    os.environ["NO_PROXY"] = max_length_entry
    try:
        with mock.patch("logging.Logger.warning") as mock_warning:
            # Should not match (hostname doesn't match)
            result = _should_bypass_proxy("example.com:443")
            assert result is False

            # Should NOT warn (entry is within limit)
            mock_warning.assert_not_called()
    finally:
        del os.environ["NO_PROXY"]


def test_should_bypass_proxy_over_max_length_filtered():
    """Test _should_bypass_proxy filters entries over max length (257+ chars)."""
    from netboxlabs.diode.sdk.client import _should_bypass_proxy

    # Create an entry just over max length
    over_max_entry = "a" * 257

    os.environ["NO_PROXY"] = over_max_entry
    try:
        with mock.patch("logging.Logger.warning") as mock_warning:
            result = _should_bypass_proxy("example.com:443")
            assert result is False

            # Should warn about filtered entry
            mock_warning.assert_called_once()
    finally:
        del os.environ["NO_PROXY"]


def test_diode_client_with_invalid_proxy_url_falls_back_to_no_proxy(
    mock_diode_authentication,
):
    """Test DiodeClient falls back to no proxy when proxy URL is invalid."""
    os.environ["HTTP_PROXY"] = "invalid_url_format"
    try:
        with (
            mock.patch("grpc.insecure_channel") as mock_insecure_channel,
            mock.patch("logging.Logger.warning") as mock_warning,
        ):
            DiodeClient(
                target="grpc://example.com:8081",
                app_name="my-producer",
                app_version="0.0.1",
                client_id="abcde",
                client_secret="123456",
            )

            # Should use insecure channel without proxy
            mock_insecure_channel.assert_called_once()

            # Verify no proxy option is set (invalid proxy was rejected)
            _, kwargs = mock_insecure_channel.call_args
            options = kwargs["options"]
            proxy_option = next(
                (opt for opt in options if opt[0] == "grpc.http_proxy"), None
            )
            assert proxy_option is None

            # Should log warning about invalid proxy
            assert any("Invalid proxy URL format" in str(call) for call in mock_warning.call_args_list)
    finally:
        del os.environ["HTTP_PROXY"]
