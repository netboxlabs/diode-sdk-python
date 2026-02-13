"""
DeviceType entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting DeviceType entities:
- device_type_minimal: Required fields only
- device_type_extended: Common optional fields
- device_type_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    DeviceType,
    Entity,
    Manufacturer,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "device_type-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a DeviceType entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        device_type = device_type_minimal()
        # device_type = device_type_extended()
        # device_type = device_type_explicit()

        response = client.ingest(entities=[Entity(device_type=device_type)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("DeviceType ingested successfully")


def device_type_minimal() -> DeviceType:
    """Create a DeviceType with only required fields using flat strings."""
    return DeviceType(
        manufacturer="Example Manufacturer",  # flat string -> Manufacturer
        model="Model X",
        slug="example-slug",
        metadata={"source": "example"},
    )


def device_type_extended() -> DeviceType:
    """Create a DeviceType with common optional fields."""
    return DeviceType(
        manufacturer="Example Manufacturer",
        model="Model X",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def device_type_explicit() -> DeviceType:
    """Create a DeviceType with fully nested objects and all common fields."""
    return DeviceType(
        manufacturer=Manufacturer(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        model="Model X",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
