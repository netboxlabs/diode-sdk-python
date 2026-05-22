"""
DeviceBay entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting DeviceBay entities:
- device_bay_minimal: Required fields only
- device_bay_extended: Common optional fields
- device_bay_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceBay,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "device_bay-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a DeviceBay entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        device_bay = device_bay_minimal()
        # device_bay = device_bay_extended()
        # device_bay = device_bay_explicit()

        response = client.ingest(entities=[Entity(device_bay=device_bay)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("DeviceBay ingested successfully")


def device_bay_minimal() -> DeviceBay:
    """Create a DeviceBay with only required fields using flat strings."""
    return DeviceBay(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def device_bay_extended() -> DeviceBay:
    """Create a DeviceBay with common optional fields."""
    return DeviceBay(
        device="Example Device",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        label="Example Label",
        enabled=True,
    )


def device_bay_explicit() -> DeviceBay:
    """Create a DeviceBay with fully nested objects and all common fields."""
    return DeviceBay(
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
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        label="Example Label",
        enabled=True,
        installed_device=Device(
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
