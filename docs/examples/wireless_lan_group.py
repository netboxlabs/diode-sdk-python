"""
WirelessLANGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting WirelessLANGroup entities:
- wireless_lan_group_minimal: Required fields only
- wireless_lan_group_extended: Common optional fields
- wireless_lan_group_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    WirelessLANGroup,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "wireless_lan_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = wireless_lan_group_minimal()
        # entity = wireless_lan_group_extended()
        # entity = wireless_lan_group_explicit()

        response = client.ingest(entities=[Entity(wireless_lan_group=entity)])
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
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def wireless_lan_group_explicit() -> WirelessLANGroup:
    """Create a WirelessLANGroup with fully nested objects and all common fields."""
    return WirelessLANGroup(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
