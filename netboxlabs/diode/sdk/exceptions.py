#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs, Diode - SDK - Exceptions."""

import grpc
from google.protobuf.json_format import MessageToDict
from grpc import RpcError
from grpc_status import rpc_status


class BaseError(Exception):
    """Base error class for Diode SDK."""

    pass


class DiodeConfigError(BaseError):
    """Diode Config Error."""

    pass


class DiodeClientError(RpcError):
    """Diode Client Error."""

    _status_code = None
    _details = None
    _grpc_status = None

    def __init__(self, err: RpcError):
        """Initialize DiodeClientError."""
        self._status_code = err.code()
        self._details = err.details()

    @property
    def status_code(self):
        """Return status code."""
        return self._status_code

    @property
    def details(self):
        """Return error details."""
        return self._details

    def __repr__(self):
        """Return string representation."""
        return f"<DiodeClientError status code: {self._status_code}, details: {self._details}>"


class QueueClientError(BaseError):
    """Raised when the queue client fails to enqueue a payload."""

    def __init__(
        self,
        status_code: int,
        message: str,
        response_body: str | None = None,
    ):
        """Initialize QueueClientError."""
        self.status_code = status_code
        self.message = message
        self.response_body = response_body
        detail = message
        if response_body:
            detail = f"{message}: {response_body}"
        super().__init__(f"{status_code} {detail}")

    def __repr__(self):
        """Return string representation."""
        body = f", response_body={self.response_body!r}" if self.response_body else ""
        return (
            f"<QueueClientError status_code={self.status_code}, "
            f"message={self.message!r}{body}>"
        )
