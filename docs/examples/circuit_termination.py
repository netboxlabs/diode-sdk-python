"""
CircuitTermination entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CircuitTermination entities:
- circuit_termination_minimal: Required fields only
- circuit_termination_extended: Common optional fields
- circuit_termination_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Circuit,
    CircuitTermination,
    CircuitType,
    Provider,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "circuit_termination-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a CircuitTermination entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = circuit_termination_minimal()
        # entity = circuit_termination_extended()
        # entity = circuit_termination_explicit()

        response = client.ingest(entities=[Entity(circuit_termination=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CircuitTermination ingested successfully")


def circuit_termination_minimal() -> CircuitTermination:
    """Create a CircuitTermination with only required fields using flat strings."""
    return CircuitTermination(
        circuit="example-circuit",  # flat string -> Circuit
        term_side="A",
        metadata={"source": "example"},
    )


def circuit_termination_extended() -> CircuitTermination:
    """Create a CircuitTermination with common optional fields."""
    return CircuitTermination(
        circuit="example-circuit",
        term_side="A",
        description="Example description",
        metadata={"source": "example"},
    )


def circuit_termination_explicit() -> CircuitTermination:
    """Create a CircuitTermination with fully nested objects and all common fields."""
    return CircuitTermination(
        circuit=Circuit(
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
            metadata={"source": "example"},
        ),
        term_side="A",
        description="Example description",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
