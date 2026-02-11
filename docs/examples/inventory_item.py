"""
InventoryItem entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting InventoryItem entities:
- inventory_item_minimal: Required fields only
- inventory_item_extended: Common optional fields
- inventory_item_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    InventoryItem,
    Manufacturer,
    Site,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "inventory_item-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an InventoryItem entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = inventory_item_minimal()
        # entity = inventory_item_extended()
        # entity = inventory_item_explicit()

        response = client.ingest(entities=[Entity(inventory_item=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("InventoryItem ingested successfully")


def inventory_item_minimal() -> InventoryItem:
    """Create an InventoryItem with only required fields using flat strings."""
    return InventoryItem(
        device="example-device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def inventory_item_extended() -> InventoryItem:
    """Create an InventoryItem with common optional fields."""
    return InventoryItem(
        device="example-device",
        name="Example Name",
        label="Example label",
        status="active",
        serial="SN-001234",
        asset_tag="ASSET-001",
        description="Example description",
        metadata={"source": "example"},
    )


def inventory_item_explicit() -> InventoryItem:
    """Create an InventoryItem with fully nested objects and all common fields."""
    return InventoryItem(
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
        status="active",
        serial="SN-001234",
        asset_tag="ASSET-001",
        description="Example description",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
