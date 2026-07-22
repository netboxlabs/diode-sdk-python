"""
MACAddress entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting MACAddress entities:
- mac_address_minimal: Required fields only
- mac_address_extended: Common optional fields
- mac_address_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Interface,
    MACAddress,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
    VMInterface,
    VirtualMachine,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "mac_address-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a MACAddress entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        mac_address = mac_address_minimal()
        # mac_address = mac_address_extended()
        # mac_address = mac_address_explicit()

        response = client.ingest(entities=[Entity(mac_address=mac_address)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("MACAddress ingested successfully")


def mac_address_minimal() -> MACAddress:
    """Create a MACAddress with only required fields using flat strings."""
    return MACAddress(
        mac_address="00:11:22:33:44:55",
        metadata={"source": "example"},
    )


def mac_address_extended() -> MACAddress:
    """Create a MACAddress with common optional fields."""
    return MACAddress(
        mac_address="00:11:22:33:44:55",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def mac_address_explicit() -> MACAddress:
    """Create a MACAddress with fully nested objects and all common fields."""
    return MACAddress(
        mac_address="00:11:22:33:44:55",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        # Polymorphic 'assigned_object' — choose ONE of these mutually exclusive variants:
        assigned_object_interface=Interface(
            device=Device(
                device_type=DeviceType(
                    manufacturer=Manufacturer(
                        name="Example Name",
                        slug="example-slug",
                        metadata={"source": "example"},
                    ),
                    model="Model X",
                    slug="example-slug",
                    metadata={"source": "example"},
                ),
                role=DeviceRole(
                    name="Example Name",
                    slug="example-slug",
                    color="0000ff",
                    metadata={"source": "example"},
                ),
                site=Site(
                    name="Example Name",
                    slug="example-slug",
                    status="active",
                    metadata={"source": "example"},
                ),
                status="active",
                metadata={"source": "example"},
            ),
            name="Example Name",
            type="1000base-t",
            metadata={"source": "example"},
        ),
        # assigned_object_vm_interface=VMInterface(virtual_machine=VirtualMachine(name="Example Name", status="active", metadata={"source": "example"}), name="Example Name", metadata={"source": "example"}),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
