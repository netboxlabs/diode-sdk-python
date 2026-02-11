"""
L2VPNTermination entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting L2VPNTermination entities:
- l2vpn_termination_minimal: Required fields only
- l2vpn_termination_extended: Common optional fields
- l2vpn_termination_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    L2VPN,
    L2VPNTermination,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "l2vpn_termination-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a L2VPNTermination entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = l2vpn_termination_minimal()
        # entity = l2vpn_termination_extended()
        # entity = l2vpn_termination_explicit()

        response = client.ingest(entities=[Entity(l2vpn_termination=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("L2VPNTermination ingested successfully")


def l2vpn_termination_minimal() -> L2VPNTermination:
    """Create a L2VPNTermination with only required fields using flat strings."""
    return L2VPNTermination(
        l2vpn="example-l2vpn",  # flat string -> L2VPN
        metadata={"source": "example"},
    )


def l2vpn_termination_extended() -> L2VPNTermination:
    """Create a L2VPNTermination with common optional fields."""
    return L2VPNTermination(
        l2vpn="example-l2vpn",
        metadata={"source": "example"},
    )


def l2vpn_termination_explicit() -> L2VPNTermination:
    """Create a L2VPNTermination with fully nested objects and all common fields."""
    return L2VPNTermination(
        l2vpn=L2VPN(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            status="active",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
