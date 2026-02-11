"""
VirtualDeviceContext entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualDeviceContext entities:
- virtual_device_context_minimal: Required fields only
- virtual_device_context_extended: Common optional fields
- virtual_device_context_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    Manufacturer,
    Site,
    Tag,
    Tenant,
    VirtualDeviceContext,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "virtual_device_context-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = virtual_device_context_minimal()
        # entity = virtual_device_context_extended()
        # entity = virtual_device_context_explicit()

        response = client.ingest(entities=[Entity(virtual_device_context=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualDeviceContext ingested successfully")


def virtual_device_context_minimal() -> VirtualDeviceContext:
    """Create a VirtualDeviceContext with only required fields using flat strings."""
    return VirtualDeviceContext(
        name="Example Name",
        device="example-device",  # flat string -> Device
        status="active",
        metadata={"source": "example"},
    )


def virtual_device_context_extended() -> VirtualDeviceContext:
    """Create a VirtualDeviceContext with common optional fields."""
    return VirtualDeviceContext(
        name="Example Name",
        device="example-device",
        status="active",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
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
                    description="Example description",
                    comments="Example comments",
                    metadata={"source": "example"},
                ),
                model="Model X",
                slug="example-slug",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            role=DeviceRole(
                name="Example Name",
                slug="example-slug",
                color="0000ff",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            serial="SN-001234",
            asset_tag="ASSET-001",
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            status="active",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
