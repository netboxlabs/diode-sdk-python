"""
Interface entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Interface entities:
- interface_minimal: Required fields only
- interface_extended: Common optional fields
- interface_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    Interface,
    Manufacturer,
    Site,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "interface-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an Interface entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = interface_minimal()
        # entity = interface_extended()
        # entity = interface_explicit()

        response = client.ingest(entities=[Entity(interface=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Interface ingested successfully")


def interface_minimal() -> Interface:
    """Create an Interface with only required fields using flat strings."""
    return Interface(
        device="example-device",  # flat string -> Device
        name="Example Name",
        type="1000base-bx10-d",
        metadata={"source": "example"},
    )


def interface_extended() -> Interface:
    """Create an Interface with common optional fields."""
    return Interface(
        device="example-device",
        name="Example Name",
        type="1000base-bx10-d",
        label="Example label",
        description="Example description",
        metadata={"source": "example"},
    )


def interface_explicit() -> Interface:
    """Create an Interface with fully nested objects and all common fields."""
    return Interface(
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
        name="Example Name",
        type="1000base-bx10-d",
        label="Example label",
        description="Example description",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
