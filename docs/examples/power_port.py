"""
PowerPort entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting PowerPort entities:
- power_port_minimal: Required fields only
- power_port_extended: Common optional fields
- power_port_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    Manufacturer,
    PowerPort,
    Site,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "power_port-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a PowerPort entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = power_port_minimal()
        # entity = power_port_extended()
        # entity = power_port_explicit()

        response = client.ingest(entities=[Entity(power_port=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("PowerPort ingested successfully")


def power_port_minimal() -> PowerPort:
    """Create a PowerPort with only required fields using flat strings."""
    return PowerPort(
        device="example-device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def power_port_extended() -> PowerPort:
    """Create a PowerPort with common optional fields."""
    return PowerPort(
        device="example-device",
        name="Example Name",
        label="Example label",
        description="Example description",
        metadata={"source": "example"},
    )


def power_port_explicit() -> PowerPort:
    """Create a PowerPort with fully nested objects and all common fields."""
    return PowerPort(
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
        label="Example label",
        description="Example description",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
