"""
VirtualMachine entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualMachine entities:
- virtual_machine_minimal: Required fields only
- virtual_machine_extended: Common optional fields
- virtual_machine_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Platform,
    Tag,
    Tenant,
    VirtualMachine,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "virtual_machine-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a VirtualMachine entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = virtual_machine_minimal()
        # entity = virtual_machine_extended()
        # entity = virtual_machine_explicit()

        response = client.ingest(entities=[Entity(virtual_machine=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualMachine ingested successfully")


def virtual_machine_minimal() -> VirtualMachine:
    """Create a VirtualMachine with only required fields using flat strings."""
    return VirtualMachine(
        name="Example Name",
        metadata={"source": "example"},
    )


def virtual_machine_extended() -> VirtualMachine:
    """Create a VirtualMachine with common optional fields."""
    return VirtualMachine(
        name="Example Name",
        status="active",
        serial="SN-001234",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def virtual_machine_explicit() -> VirtualMachine:
    """Create a VirtualMachine with fully nested objects and all common fields."""
    return VirtualMachine(
        name="Example Name",
        status="active",
        serial="SN-001234",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        platform=Platform(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
