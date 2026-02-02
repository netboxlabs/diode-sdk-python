"""
VMInterface entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VMInterface entities:
- vm_interface_minimal: Required fields only
- vm_interface_extended: Common optional fields
- vm_interface_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    VMInterface,
    VirtualMachine,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vm_interface-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        vm_interface = vm_interface_minimal()
        # vm_interface = vm_interface_extended()
        # vm_interface = vm_interface_explicit()

        response = client.ingest(entities=[Entity(vm_interface=vm_interface)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VMInterface ingested successfully")


def vm_interface_minimal() -> VMInterface:
    """Create a VMInterface with only required fields using flat strings."""
    return VMInterface(
        virtual_machine="Example Virtual Machine",  # flat string -> VirtualMachine
        name="Example Name",
        metadata={"source": "example"},
    )


def vm_interface_extended() -> VMInterface:
    """Create a VMInterface with common optional fields."""
    return VMInterface(
        virtual_machine="Example Virtual Machine",
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def vm_interface_explicit() -> VMInterface:
    """Create a VMInterface with fully nested objects and all common fields."""
    return VMInterface(
        virtual_machine=VirtualMachine(
            name="Example Name", status="active", metadata={"source": "example"}
        ),
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
