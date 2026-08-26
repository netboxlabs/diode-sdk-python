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
    Owner,
    OwnerGroup,
    Platform,
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
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        part_number="Example Part Number",
        u_height=1.0,
        exclude_from_utilization=True,
        is_full_depth=True,
        subdevice_role="child",
        airflow="bottom-to-top",
        weight=1.0,
        weight_unit="g",
        comments="Example comments",
        cooling_method="air",
    )


def device_type_explicit() -> DeviceType:
    """Create a DeviceType with fully nested objects and all common fields."""
    return DeviceType(
        manufacturer=Manufacturer(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        model="Model X",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        part_number="Example Part Number",
        u_height=1.0,
        exclude_from_utilization=True,
        is_full_depth=True,
        subdevice_role="child",
        airflow="bottom-to-top",
        weight=1.0,
        weight_unit="g",
        cooling_method="air",
        default_platform=Platform(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
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
