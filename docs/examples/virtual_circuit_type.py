"""
VirtualCircuitType entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualCircuitType entities:
- virtual_circuit_type_minimal: Required fields only
- virtual_circuit_type_extended: Common optional fields
- virtual_circuit_type_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    VirtualCircuitType,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_circuit_type-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VirtualCircuitType entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        virtual_circuit_type = virtual_circuit_type_minimal()
        # virtual_circuit_type = virtual_circuit_type_extended()
        # virtual_circuit_type = virtual_circuit_type_explicit()

        response = client.ingest(
            entities=[Entity(virtual_circuit_type=virtual_circuit_type)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualCircuitType ingested successfully")


def virtual_circuit_type_minimal() -> VirtualCircuitType:
    """Create a VirtualCircuitType with only required fields using flat strings."""
    return VirtualCircuitType(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def virtual_circuit_type_extended() -> VirtualCircuitType:
    """Create a VirtualCircuitType with common optional fields."""
    return VirtualCircuitType(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
    )


def virtual_circuit_type_explicit() -> VirtualCircuitType:
    """Create a VirtualCircuitType with fully nested objects and all common fields."""
    return VirtualCircuitType(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
