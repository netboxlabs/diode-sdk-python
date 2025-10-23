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


class OTLPClientError(BaseError):
    """Raised when the OTLP client fails to export log data."""

    def __init__(self, error: Exception, message: str | None = None):
        """Initialize OTLPClientError."""
        self._message = message or "OTLP export failed"
        self.status_code = None
        self.details = None

        if isinstance(error, grpc.RpcError):
            try:
                self.status_code = error.code()
            except Exception:  # pragma: no cover - defensive
                self.status_code = None
            try:
                self.details = error.details()
            except Exception:  # pragma: no cover - defensive
                self.details = None
        else:
            self.details = str(error)

        parts: list[str] = [self._message]
        if self.status_code is not None:
            status_name = getattr(self.status_code, "name", str(self.status_code))
            parts.append(f"status={status_name}")
        if self.details:
            parts.append(f"details={self.details}")

        super().__init__(", ".join(parts))

    def __repr__(self):
        """Return string representation."""
        status = getattr(self.status_code, "name", self.status_code)
        return (
            f"<OTLPClientError message={self._message!r}, "
            f"status_code={status!r}, details={self.details!r}>"
        )
