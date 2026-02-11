"""
L2VPN entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting L2VPN entities:
- l2vpn_minimal: Required fields only
- l2vpn_extended: Common optional fields
- l2vpn_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    L2VPN,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "l2vpn-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a L2VPN entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = l2vpn_minimal()
        # entity = l2vpn_extended()
        # entity = l2vpn_explicit()

        response = client.ingest(entities=[Entity(l2vpn=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("L2VPN ingested successfully")


def l2vpn_minimal() -> L2VPN:
    """Create a L2VPN with only required fields using flat strings."""
    return L2VPN(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def l2vpn_extended() -> L2VPN:
    """Create a L2VPN with common optional fields."""
    return L2VPN(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        status="active",
        metadata={"source": "example"},
    )


def l2vpn_explicit() -> L2VPN:
    """Create a L2VPN with fully nested objects and all common fields."""
    return L2VPN(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        status="active",
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
