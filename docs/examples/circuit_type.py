"""
CircuitType entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CircuitType entities:
- circuit_type_minimal: Required fields only
- circuit_type_extended: Common optional fields
- circuit_type_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CircuitType,
    Entity,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "circuit_type-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CircuitType entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        circuit_type = circuit_type_minimal()
        # circuit_type = circuit_type_extended()
        # circuit_type = circuit_type_explicit()

        response = client.ingest(entities=[Entity(circuit_type=circuit_type)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CircuitType ingested successfully")


def circuit_type_minimal() -> CircuitType:
    """Create a CircuitType with only required fields using flat strings."""
    return CircuitType(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def circuit_type_extended() -> CircuitType:
    """Create a CircuitType with common optional fields."""
    return CircuitType(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
    )


def circuit_type_explicit() -> CircuitType:
    """Create a CircuitType with fully nested objects and all common fields."""
    return CircuitType(
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
