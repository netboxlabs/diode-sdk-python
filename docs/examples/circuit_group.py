"""
CircuitGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CircuitGroup entities:
- circuit_group_minimal: Required fields only
- circuit_group_extended: Common optional fields
- circuit_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CircuitGroup,
    Entity,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "circuit_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        circuit_group = circuit_group_minimal()
        # circuit_group = circuit_group_extended()
        # circuit_group = circuit_group_explicit()

        response = client.ingest(entities=[Entity(circuit_group=circuit_group)])
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
        metadata={"source": "example"},
        description="Example description",
    )


def circuit_group_explicit() -> CircuitGroup:
    """Create a CircuitGroup with fully nested objects and all common fields."""
    return CircuitGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
