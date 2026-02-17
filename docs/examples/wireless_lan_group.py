"""
WirelessLANGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting WirelessLANGroup entities:
- wireless_lan_group_minimal: Required fields only
- wireless_lan_group_extended: Common optional fields
- wireless_lan_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Tag,
    WirelessLANGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "wireless_lan_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a WirelessLANGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        wireless_lan_group = wireless_lan_group_minimal()
        # wireless_lan_group = wireless_lan_group_extended()
        # wireless_lan_group = wireless_lan_group_explicit()

        response = client.ingest(
            entities=[Entity(wireless_lan_group=wireless_lan_group)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("WirelessLANGroup ingested successfully")


def wireless_lan_group_minimal() -> WirelessLANGroup:
    """Create a WirelessLANGroup with only required fields using flat strings."""
    return WirelessLANGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def wireless_lan_group_extended() -> WirelessLANGroup:
    """Create a WirelessLANGroup with common optional fields."""
    return WirelessLANGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def wireless_lan_group_explicit() -> WirelessLANGroup:
    """Create a WirelessLANGroup with fully nested objects and all common fields."""
    return WirelessLANGroup(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        parent=WirelessLANGroup(
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
