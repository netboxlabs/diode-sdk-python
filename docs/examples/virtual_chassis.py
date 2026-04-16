"""
VirtualChassis entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualChassis entities:
- virtual_chassis_minimal: Required fields only
- virtual_chassis_extended: Common optional fields
- virtual_chassis_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
    VirtualChassis,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_chassis-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        virtual_chassis = virtual_chassis_minimal()
        # virtual_chassis = virtual_chassis_extended()
        # virtual_chassis = virtual_chassis_explicit()

        response = client.ingest(entities=[Entity(virtual_chassis=virtual_chassis)])
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
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        domain="Example Domain",
        comments="Example comments",
    )


def virtual_chassis_explicit() -> VirtualChassis:
    """Create a VirtualChassis with fully nested objects and all common fields."""
    return VirtualChassis(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        domain="Example Domain",
        master=Device(
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
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
