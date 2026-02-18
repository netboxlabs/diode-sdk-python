"""
VirtualDisk entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualDisk entities:
- virtual_disk_minimal: Required fields only
- virtual_disk_extended: Common optional fields
- virtual_disk_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Tag,
    VirtualDisk,
    VirtualMachine,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_disk-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VirtualDisk entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        virtual_disk = virtual_disk_minimal()
        # virtual_disk = virtual_disk_extended()
        # virtual_disk = virtual_disk_explicit()

        response = client.ingest(entities=[Entity(virtual_disk=virtual_disk)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualDisk ingested successfully")


def virtual_disk_minimal() -> VirtualDisk:
    """Create a VirtualDisk with only required fields using flat strings."""
    return VirtualDisk(
        virtual_machine="Example Virtual Machine",  # flat string -> VirtualMachine
        name="Example Name",
        size=1,
        metadata={"source": "example"},
    )


def virtual_disk_extended() -> VirtualDisk:
    """Create a VirtualDisk with common optional fields."""
    return VirtualDisk(
        virtual_machine="Example Virtual Machine",
        name="Example Name",
        size=1,
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
    )


def virtual_disk_explicit() -> VirtualDisk:
    """Create a VirtualDisk with fully nested objects and all common fields."""
    return VirtualDisk(
        virtual_machine=VirtualMachine(
            name="Example Name", status="active", metadata={"source": "example"}
        ),
        name="Example Name",
        size=1,
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
