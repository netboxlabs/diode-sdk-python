"""
MACAddress entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting MACAddress entities:
- mac_address_minimal: Required fields only
- mac_address_extended: Common optional fields
- mac_address_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    MACAddress,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "mac_address-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a MACAddress entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = mac_address_minimal()
        # entity = mac_address_extended()
        # entity = mac_address_explicit()

        response = client.ingest(entities=[Entity(mac_address=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("MACAddress ingested successfully")


def mac_address_minimal() -> MACAddress:
    """Create a MACAddress with only required fields using flat strings."""
    return MACAddress(
        mac_address="00:1A:2B:3C:4D:5E",
        metadata={"source": "example"},
    )


def mac_address_extended() -> MACAddress:
    """Create a MACAddress with common optional fields."""
    return MACAddress(
        mac_address="00:1A:2B:3C:4D:5E",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def mac_address_explicit() -> MACAddress:
    """Create a MACAddress with fully nested objects and all common fields."""
    return MACAddress(
        mac_address="00:1A:2B:3C:4D:5E",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
