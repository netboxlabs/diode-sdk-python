"""
TunnelGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting TunnelGroup entities:
- tunnel_group_minimal: Required fields only
- tunnel_group_extended: Common optional fields
- tunnel_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Tag,
    TunnelGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "tunnel_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a TunnelGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        tunnel_group = tunnel_group_minimal()
        # tunnel_group = tunnel_group_extended()
        # tunnel_group = tunnel_group_explicit()

        response = client.ingest(entities=[Entity(tunnel_group=tunnel_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("TunnelGroup ingested successfully")


def tunnel_group_minimal() -> TunnelGroup:
    """Create a TunnelGroup with only required fields using flat strings."""
    return TunnelGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def tunnel_group_extended() -> TunnelGroup:
    """Create a TunnelGroup with common optional fields."""
    return TunnelGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def tunnel_group_explicit() -> TunnelGroup:
    """Create a TunnelGroup with fully nested objects and all common fields."""
    return TunnelGroup(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
