"""
Circuit entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Circuit entities:
- circuit_minimal: Required fields only
- circuit_extended: Common optional fields
- circuit_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Circuit,
    CircuitType,
    Provider,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "circuit-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a Circuit entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = circuit_minimal()
        # entity = circuit_extended()
        # entity = circuit_explicit()

        response = client.ingest(entities=[Entity(circuit=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Circuit ingested successfully")


def circuit_minimal() -> Circuit:
    """Create a Circuit with only required fields using flat strings."""
    return Circuit(
        cid="CID-001",
        provider="example-provider",  # flat string -> Provider
        type="example-type",  # flat string -> CircuitType
        metadata={"source": "example"},
    )


def circuit_extended() -> Circuit:
    """Create a Circuit with common optional fields."""
    return Circuit(
        cid="CID-001",
        provider="example-provider",
        type="example-type",
        status="active",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def circuit_explicit() -> Circuit:
    """Create a Circuit with fully nested objects and all common fields."""
    return Circuit(
        cid="CID-001",
        provider=Provider(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        type=CircuitType(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
