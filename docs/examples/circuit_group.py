"""
CircuitGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CircuitGroup entities:
- circuit_group_minimal: Required fields only
- circuit_group_extended: Common optional fields
- circuit_group_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    CircuitGroup,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "circuit_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a CircuitGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = circuit_group_minimal()
        # entity = circuit_group_extended()
        # entity = circuit_group_explicit()

        response = client.ingest(entities=[Entity(circuit_group=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CircuitGroup ingested successfully")


def circuit_group_minimal() -> CircuitGroup:
    """Create a CircuitGroup with only required fields using flat strings."""
    return CircuitGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def circuit_group_extended() -> CircuitGroup:
    """Create a CircuitGroup with common optional fields."""
    return CircuitGroup(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def circuit_group_explicit() -> CircuitGroup:
    """Create a CircuitGroup with fully nested objects and all common fields."""
    return CircuitGroup(
        name="Example Name",
        slug="example-slug",
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
