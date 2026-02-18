"""
InventoryItem entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting InventoryItem entities:
- inventory_item_minimal: Required fields only
- inventory_item_extended: Common optional fields
- inventory_item_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    InventoryItem,
    InventoryItemRole,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "inventory_item-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a InventoryItem entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        inventory_item = inventory_item_minimal()
        # inventory_item = inventory_item_extended()
        # inventory_item = inventory_item_explicit()

        response = client.ingest(entities=[Entity(inventory_item=inventory_item)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("InventoryItem ingested successfully")


def inventory_item_minimal() -> InventoryItem:
    """Create a InventoryItem with only required fields using flat strings."""
    return InventoryItem(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def inventory_item_extended() -> InventoryItem:
    """Create a InventoryItem with common optional fields."""
    return InventoryItem(
        device="Example Device",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        serial="SN-001234",
        description="Example description",
        label="Example Label",
        role="Example Role",
        manufacturer="Example Manufacturer",
        part_id="Example Part Id",
        asset_tag="ASSET-001",
        discovered=True,
    )


def inventory_item_explicit() -> InventoryItem:
    """Create a InventoryItem with fully nested objects and all common fields."""
    return InventoryItem(
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
        status="active",
        serial="SN-001234",
        description="Example description",
        asset_tag="ASSET-001",
        label="Example Label",
        part_id="Example Part Id",
        discovered=True,
        parent=InventoryItem(
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
            status="active",
            metadata={"source": "example"},
        ),
        role=InventoryItemRole(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
            metadata={"source": "example"},
        ),
        manufacturer=Manufacturer(
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
