"""
DeviceRole entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting DeviceRole entities:
- device_role_minimal: Required fields only
- device_role_extended: Common optional fields
- device_role_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    DeviceRole,
    Entity,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "device_role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a DeviceRole entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        device_role = device_role_minimal()
        # device_role = device_role_extended()
        # device_role = device_role_explicit()

        response = client.ingest(entities=[Entity(device_role=device_role)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("DeviceRole ingested successfully")


def device_role_minimal() -> DeviceRole:
    """Create a DeviceRole with only required fields using flat strings."""
    return DeviceRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def device_role_extended() -> DeviceRole:
    """Create a DeviceRole with common optional fields."""
    return DeviceRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        color="0000ff",
        vm_role=True,
        comments="Example comments",
    )


def device_role_explicit() -> DeviceRole:
    """Create a DeviceRole with fully nested objects and all common fields."""
    return DeviceRole(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        color="0000ff",
        comments="Example comments",
        vm_role=True,
        parent=DeviceRole(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
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
