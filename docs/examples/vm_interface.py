"""
VMInterface entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VMInterface entities:
- vm_interface_minimal: Required fields only
- vm_interface_extended: Common optional fields
- vm_interface_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    VMInterface,
    VirtualMachine,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "vm_interface-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a VMInterface entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = vm_interface_minimal()
        # entity = vm_interface_extended()
        # entity = vm_interface_explicit()

        response = client.ingest(entities=[Entity(vm_interface=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VMInterface ingested successfully")


def vm_interface_minimal() -> VMInterface:
    """Create a VMInterface with only required fields using flat strings."""
    return VMInterface(
        virtual_machine="example-virtual-machine",  # flat string -> VirtualMachine
        name="Example Name",
        metadata={"source": "example"},
    )


def vm_interface_extended() -> VMInterface:
    """Create a VMInterface with common optional fields."""
    return VMInterface(
        virtual_machine="example-virtual-machine",
        name="Example Name",
        description="Example description",
        metadata={"source": "example"},
    )


def vm_interface_explicit() -> VMInterface:
    """Create a VMInterface with fully nested objects and all common fields."""
    return VMInterface(
        virtual_machine=VirtualMachine(
            name="Example Name",
            status="active",
            serial="SN-001234",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        name="Example Name",
        description="Example description",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
