"""
Device entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Device entities:
- device_minimal: Required fields only
- device_extended: Common optional fields
- device_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    Manufacturer,
    Platform,
    Site,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "device-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a Device entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = device_minimal()
        # entity = device_extended()
        # entity = device_explicit()

        response = client.ingest(entities=[Entity(device=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Device ingested successfully")


def device_minimal() -> Device:
    """Create a Device with only required fields using flat strings."""
    return Device(
        device_type="example-device-type",  # flat string -> DeviceType
        role="example-role",  # flat string -> DeviceRole
        site="example-site",  # flat string -> Site
        metadata={"source": "example"},
    )


def device_extended() -> Device:
    """Create a Device with common optional fields."""
    return Device(
        device_type="example-device-type",
        role="example-role",
        site="example-site",
        serial="SN-001234",
        asset_tag="ASSET-001",
        status="active",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def device_explicit() -> Device:
    """Create a Device with fully nested objects and all common fields."""
    return Device(
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
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        serial="SN-001234",
        asset_tag="ASSET-001",
        status="active",
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
