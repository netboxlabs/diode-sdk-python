"""
L2VPN entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting L2VPN entities:
- l2vpn_minimal: Required fields only
- l2vpn_extended: Common optional fields
- l2vpn_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    L2VPN,
    Owner,
    OwnerGroup,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "l2vpn-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        l2vpn = l2vpn_minimal()
        # l2vpn = l2vpn_extended()
        # l2vpn = l2vpn_explicit()

        response = client.ingest(entities=[Entity(l2vpn=l2vpn)])
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
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        identifier=1,
        type="ep-lan",
        comments="Example comments",
        tenant="Example Tenant",
    )


def l2vpn_explicit() -> L2VPN:
    """Create a L2VPN with fully nested objects and all common fields."""
    return L2VPN(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        identifier=1,
        type="ep-lan",
        tenant=Tenant(
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
