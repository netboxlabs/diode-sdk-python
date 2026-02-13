"""
Tunnel entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Tunnel entities:
- tunnel_minimal: Required fields only
- tunnel_extended: Common optional fields
- tunnel_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    Tenant,
    Tunnel,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "tunnel-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Tunnel entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        tunnel = tunnel_minimal()
        # tunnel = tunnel_extended()
        # tunnel = tunnel_explicit()

        response = client.ingest(entities=[Entity(tunnel=tunnel)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Tunnel ingested successfully")


def tunnel_minimal() -> Tunnel:
    """Create a Tunnel with only required fields using flat strings."""
    return Tunnel(
        name="Example Name",
        status="active",
        encapsulation="gre",
        metadata={"source": "example"},
    )


def tunnel_extended() -> Tunnel:
    """Create a Tunnel with common optional fields."""
    return Tunnel(
        name="Example Name",
        status="active",
        encapsulation="gre",
        metadata={"source": "example"},
        description="Example description",
    )


def tunnel_explicit() -> Tunnel:
    """Create a Tunnel with fully nested objects and all common fields."""
    return Tunnel(
        name="Example Name",
        status="active",
        encapsulation="gre",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
