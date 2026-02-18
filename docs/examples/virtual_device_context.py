"""
VirtualDeviceContext entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualDeviceContext entities:
- virtual_device_context_minimal: Required fields only
- virtual_device_context_extended: Common optional fields
- virtual_device_context_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    IPAddress,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
    Tenant,
    VirtualDeviceContext,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_device_context-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VirtualDeviceContext entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        virtual_device_context = virtual_device_context_minimal()
        # virtual_device_context = virtual_device_context_extended()
        # virtual_device_context = virtual_device_context_explicit()

        response = client.ingest(
            entities=[Entity(virtual_device_context=virtual_device_context)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualDeviceContext ingested successfully")


def virtual_device_context_minimal() -> VirtualDeviceContext:
    """Create a VirtualDeviceContext with only required fields using flat strings."""
    return VirtualDeviceContext(
        name="Example Name",
        device="Example Device",  # flat string -> Device
        status="active",
        metadata={"source": "example"},
    )


def virtual_device_context_extended() -> VirtualDeviceContext:
    """Create a VirtualDeviceContext with common optional fields."""
    return VirtualDeviceContext(
        name="Example Name",
        device="Example Device",
        status="active",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        identifier=1,
        tenant="Example Tenant",
        comments="Example comments",
    )


def virtual_device_context_explicit() -> VirtualDeviceContext:
    """Create a VirtualDeviceContext with fully nested objects and all common fields."""
    return VirtualDeviceContext(
        name="Example Name",
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
        status="active",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        identifier=1,
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        primary_ip4=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        primary_ip6=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
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
