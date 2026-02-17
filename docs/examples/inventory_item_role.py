"""
InventoryItemRole entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting InventoryItemRole entities:
- inventory_item_role_minimal: Required fields only
- inventory_item_role_extended: Common optional fields
- inventory_item_role_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    InventoryItemRole,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "inventory_item_role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a InventoryItemRole entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        inventory_item_role = inventory_item_role_minimal()
        # inventory_item_role = inventory_item_role_extended()
        # inventory_item_role = inventory_item_role_explicit()

        response = client.ingest(
            entities=[Entity(inventory_item_role=inventory_item_role)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("InventoryItemRole ingested successfully")


def inventory_item_role_minimal() -> InventoryItemRole:
    """Create a InventoryItemRole with only required fields using flat strings."""
    return InventoryItemRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def inventory_item_role_extended() -> InventoryItemRole:
    """Create a InventoryItemRole with common optional fields."""
    return InventoryItemRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        color="0000ff",
        comments="Example comments",
    )


def inventory_item_role_explicit() -> InventoryItemRole:
    """Create a InventoryItemRole with fully nested objects and all common fields."""
    return InventoryItemRole(
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
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
