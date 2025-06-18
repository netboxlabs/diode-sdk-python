from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol, runtime_checkable

from netboxlabs.diode.sdk.diode.v1 import ingester_pb2
from netboxlabs.diode.sdk.ingester import Entity

_DEFAULT_STREAM: str

@runtime_checkable
class DiodeClientInterface(Protocol):
    """Interface implemented by diode clients."""

    @property
    def name(self) -> str: ...
    @property
    def version(self) -> str: ...
    def ingest(
        self,
        entities: Iterable[Entity | ingester_pb2.Entity | None],
        stream: str | None = _DEFAULT_STREAM,
    ) -> ingester_pb2.IngestResponse: ...
    def __enter__(self) -> DiodeClientInterface: ...
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None: ...
