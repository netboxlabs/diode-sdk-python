#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs - Tests."""
import os
from unittest import mock

import grpc
import pytest

from netboxlabs.diode.sdk.client import (
    _DIODE_API_KEY_ENVVAR_NAME,
    _DIODE_SENTRY_DSN_ENVVAR_NAME,
    DiodeClient,
    DiodeMethodClientInterceptor,
    _ClientCallDetails,
    _get_api_key,
    _get_sentry_dsn,
    _load_certs,
    parse_target,
)
from netboxlabs.diode.sdk.exceptions import DiodeClientError, DiodeConfigError


def test_init():
    """Check we can initiate a client configuration."""
    config = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    assert config.target == "localhost:8081"
    assert config.name == "diode-sdk-python"
    assert config.version == "0.0.1"
    assert config.app_name == "my-producer"
    assert config.app_version == "0.0.1"
    assert config.tls_verify is False
    assert config.path == ""


def test_config_error():
    """Check we can raise a config error."""
    with pytest.raises(DiodeConfigError) as err:
        DiodeClient(
            target="grpc://localhost:8081", app_name="my-producer", app_version="0.0.1"
        )
    assert (
        str(err.value) == "api_key param or DIODE_API_KEY environment variable required"
    )


def test_client_error():
    """Check we can raise a client error."""
    with pytest.raises(DiodeClientError) as err:
        client = DiodeClient(
            target="grpc://invalid:8081",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
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


def test_get_api_key_returns_env_var_when_no_input():
    """Check that _get_api_key returns the env var when no input is provided."""
    os.environ[_DIODE_API_KEY_ENVVAR_NAME] = "env_var_key"
    assert _get_api_key() == "env_var_key"


def test_get_api_key_returns_input_when_provided():
    """Check that _get_api_key returns the input when provided."""
    os.environ[_DIODE_API_KEY_ENVVAR_NAME] = "env_var_key"
    assert _get_api_key("input_key") == "input_key"


def test_get_api_key_raises_error_when_no_input_or_env_var():
    """Check that _get_api_key raises an error when no input or env var is provided."""
    if _DIODE_API_KEY_ENVVAR_NAME in os.environ:
        del os.environ[_DIODE_API_KEY_ENVVAR_NAME]
    with pytest.raises(DiodeConfigError):
        _get_api_key()


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


def test_setup_sentry_initializes_with_correct_parameters():
    """Check that DiodeClient._setup_sentry() initializes with the correct parameters."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with mock.patch("sentry_sdk.init") as mock_init:
        client._setup_sentry("https://user@password.mock.dsn/123456", 0.5, 0.5)
        mock_init.assert_called_once_with(
            dsn="https://user@password.mock.dsn/123456",
            release=client.version,
            traces_sample_rate=0.5,
            profiles_sample_rate=0.5,
        )


def test_client_sets_up_secure_channel_when_grpcs_scheme_is_found_in_target():
    """Check that DiodeClient.__init__() sets up the gRPC secure channel when grpcs:// scheme is found in the target."""
    client = DiodeClient(
        target="grpcs://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with (
        mock.patch("grpc.secure_channel") as mock_secure_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpcs://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
        )

        mock_debug.assert_called_once_with("Setting up gRPC secure channel")
        mock_secure_channel.assert_called_once()


def test_client_sets_up_insecure_channel_when_grpc_scheme_is_found_in_target():
    """Check that DiodeClient.__init__() sets up the gRPC insecure channel when grpc:// scheme is found in the target."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with (
        mock.patch("grpc.insecure_channel") as mock_insecure_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
        )

        mock_debug.assert_called_with(
            "Setting up gRPC insecure channel",
        )
        mock_insecure_channel.assert_called_once()


def test_client_interceptor_setup_with_path():
    """Check that DiodeClient.__init__() sets up the gRPC interceptor when a path is provided."""
    client = DiodeClient(
        target="grpc://localhost:8081/my-path",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with (
        mock.patch("grpc.intercept_channel") as mock_intercept_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpc://localhost:8081/my-path",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
        )

        mock_debug.assert_called_with(
            "Setting up gRPC interceptor for path: /my-path",
        )
        mock_intercept_channel.assert_called_once()


def test_client_interceptor_not_setup_without_path():
    """Check that DiodeClient.__init__() does not set up the gRPC interceptor when no path is provided."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with (
        mock.patch("grpc.intercept_channel") as mock_intercept_channel,
        mock.patch("logging.Logger.debug") as mock_debug,
    ):
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
        )

        mock_debug.assert_called_with(
            "Setting up gRPC insecure channel",
        )
        mock_intercept_channel.assert_not_called()


def test_client_setup_sentry_called_when_sentry_dsn_exists():
    """Check that DiodeClient._setup_sentry() is called when sentry_dsn exists."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
        sentry_dsn="https://user@password.mock.dsn/123456",
    )
    with mock.patch.object(client, "_setup_sentry") as mock_setup_sentry:
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
            sentry_dsn="https://user@password.mock.dsn/123456",
        )
        mock_setup_sentry.assert_called_once_with(
            "https://user@password.mock.dsn/123456", 1.0, 1.0
        )


def test_client_setup_sentry_not_called_when_sentry_dsn_not_exists():
    """Check that DiodeClient._setup_sentry() is not called when sentry_dsn does not exist."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with mock.patch.object(client, "_setup_sentry") as mock_setup_sentry:
        client.__init__(
            target="grpc://localhost:8081",
            app_name="my-producer",
            app_version="0.0.1",
            api_key="abcde",
        )
        mock_setup_sentry.assert_not_called()


def test_client_properties_return_expected_values():
    """Check that DiodeClient properties return the expected values."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    assert client.name == "diode-sdk-python"
    assert client.version == "0.0.1"
    assert client.target == "localhost:8081"
    assert client.path == ""
    assert client.tls_verify is False
    assert client.app_name == "my-producer"
    assert client.app_version == "0.0.1"
    assert isinstance(client.channel, grpc.Channel)


def test_client_enter_returns_self():
    """Check that DiodeClient.__enter__() returns self."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    assert client.__enter__() is client


def test_client_exit_closes_channel():
    """Check that DiodeClient.__exit__() closes the channel."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with mock.patch.object(client._channel, "close") as mock_close:
        client.__exit__(None, None, None)
        mock_close.assert_called_once()


def test_client_close_closes_channel():
    """Check that DiodeClient.close() closes the channel."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
    )
    with mock.patch.object(client._channel, "close") as mock_close:
        client.close()
        mock_close.assert_called_once()


def test_setup_sentry_sets_correct_tags():
    """Check that DiodeClient._setup_sentry() sets the correct tags."""
    client = DiodeClient(
        target="grpc://localhost:8081",
        app_name="my-producer",
        app_version="0.0.1",
        api_key="abcde",
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
