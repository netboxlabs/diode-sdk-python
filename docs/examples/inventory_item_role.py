"""
InventoryItemRole entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting InventoryItemRole entities:
- inventory_item_role_minimal: Required fields only
- inventory_item_role_extended: Common optional fields
- inventory_item_role_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    InventoryItemRole,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "inventory_item_role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an InventoryItemRole entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = inventory_item_role_minimal()
        # entity = inventory_item_role_extended()
        # entity = inventory_item_role_explicit()

        response = client.ingest(entities=[Entity(inventory_item_role=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("InventoryItemRole ingested successfully")


def inventory_item_role_minimal() -> InventoryItemRole:
    """Create an InventoryItemRole with only required fields using flat strings."""
    return InventoryItemRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def inventory_item_role_extended() -> InventoryItemRole:
    """Create an InventoryItemRole with common optional fields."""
    return InventoryItemRole(
        name="Example Name",
        slug="example-slug",
        color="0000ff",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def inventory_item_role_explicit() -> InventoryItemRole:
    """Create an InventoryItemRole with fully nested objects and all common fields."""
    return InventoryItemRole(
        name="Example Name",
        slug="example-slug",
        color="0000ff",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
