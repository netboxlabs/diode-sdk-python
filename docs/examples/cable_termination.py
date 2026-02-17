"""
CableTermination entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CableTermination entities:
- cable_termination_minimal: Required fields only
- cable_termination_extended: Common optional fields
- cable_termination_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cable,
    CableTermination,
    Entity,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cable_termination-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CableTermination entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cable_termination = cable_termination_minimal()
        # cable_termination = cable_termination_extended()
        # cable_termination = cable_termination_explicit()

        response = client.ingest(entities=[Entity(cable_termination=cable_termination)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CableTermination ingested successfully")


def cable_termination_minimal() -> CableTermination:
    """Create a CableTermination with only required fields using flat strings."""
    return CableTermination(
        cable="Example Cable",  # flat string -> Cable
        cable_end="A",
        metadata={"source": "example"},
    )


def cable_termination_extended() -> CableTermination:
    """Create a CableTermination with common optional fields."""
    return CableTermination(
        cable="Example Cable",
        cable_end="A",
        metadata={"source": "example", "custom_key": "custom_value"},
    )


def cable_termination_explicit() -> CableTermination:
    """Create a CableTermination with fully nested objects and all common fields."""
    return CableTermination(
        cable=Cable(status="active", color="0000ff", metadata={"source": "example"}),
        cable_end="A",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
    )


if __name__ == "__main__":
    main()
