"""
VirtualChassis entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualChassis entities:
- virtual_chassis_minimal: Required fields only
- virtual_chassis_extended: Common optional fields
- virtual_chassis_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    VirtualChassis,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "virtual_chassis-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a VirtualChassis entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = virtual_chassis_minimal()
        # entity = virtual_chassis_extended()
        # entity = virtual_chassis_explicit()

        response = client.ingest(entities=[Entity(virtual_chassis=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualChassis ingested successfully")


def virtual_chassis_minimal() -> VirtualChassis:
    """Create a VirtualChassis with only required fields using flat strings."""
    return VirtualChassis(
        name="Example Name",
        metadata={"source": "example"},
    )


def virtual_chassis_extended() -> VirtualChassis:
    """Create a VirtualChassis with common optional fields."""
    return VirtualChassis(
        name="Example Name",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def virtual_chassis_explicit() -> VirtualChassis:
    """Create a VirtualChassis with fully nested objects and all common fields."""
    return VirtualChassis(
        name="Example Name",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
