"""
WirelessLAN entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting WirelessLAN entities:
- wireless_lan_minimal: Required fields only
- wireless_lan_extended: Common optional fields
- wireless_lan_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    Tenant,
    WirelessLAN,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "wireless_lan-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a WirelessLAN entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = wireless_lan_minimal()
        # entity = wireless_lan_extended()
        # entity = wireless_lan_explicit()

        response = client.ingest(entities=[Entity(wireless_lan=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("WirelessLAN ingested successfully")


def wireless_lan_minimal() -> WirelessLAN:
    """Create a WirelessLAN with only required fields using flat strings."""
    return WirelessLAN(
        ssid="Example-SSID",
        metadata={"source": "example"},
    )


def wireless_lan_extended() -> WirelessLAN:
    """Create a WirelessLAN with common optional fields."""
    return WirelessLAN(
        ssid="Example-SSID",
        description="Example description",
        status="active",
        comments="Example comments",
        metadata={"source": "example"},
    )


def wireless_lan_explicit() -> WirelessLAN:
    """Create a WirelessLAN with fully nested objects and all common fields."""
    return WirelessLAN(
        ssid="Example-SSID",
        description="Example description",
        status="active",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
