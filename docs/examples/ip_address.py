"""
IPAddress entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPAddress entities:
- ip_address_minimal: Required fields only
- ip_address_extended: Common optional fields
- ip_address_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IPAddress,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "ip_address-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an IPAddress entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = ip_address_minimal()
        # entity = ip_address_extended()
        # entity = ip_address_explicit()

        response = client.ingest(entities=[Entity(ip_address=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPAddress ingested successfully")


def ip_address_minimal() -> IPAddress:
    """Create an IPAddress with only required fields using flat strings."""
    return IPAddress(
        address="192.0.2.1/32",
        metadata={"source": "example"},
    )


def ip_address_extended() -> IPAddress:
    """Create an IPAddress with common optional fields."""
    return IPAddress(
        address="192.0.2.1/32",
        status="active",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def ip_address_explicit() -> IPAddress:
    """Create an IPAddress with fully nested objects and all common fields."""
    return IPAddress(
        address="192.0.2.1/32",
        status="active",
        description="Example description",
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
