"""
VLAN entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VLAN entities:
- vlan_minimal: Required fields only
- vlan_extended: Common optional fields
- vlan_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    Tenant,
    VLAN,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vlan-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VLAN entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        vlan = vlan_minimal()
        # vlan = vlan_extended()
        # vlan = vlan_explicit()

        response = client.ingest(entities=[Entity(vlan=vlan)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VLAN ingested successfully")


def vlan_minimal() -> VLAN:
    """Create a VLAN with only required fields using flat strings."""
    return VLAN(
        vid=1,
        name="Example Name",
        metadata={"source": "example"},
    )


def vlan_extended() -> VLAN:
    """Create a VLAN with common optional fields."""
    return VLAN(
        vid=1,
        name="Example Name",
        metadata={"source": "example"},
        status="active",
        description="Example description",
    )


def vlan_explicit() -> VLAN:
    """Create a VLAN with fully nested objects and all common fields."""
    return VLAN(
        vid=1,
        name="Example Name",
        metadata={"source": "example"},
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
