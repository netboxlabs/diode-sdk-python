"""
Cable entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Cable entities:
- cable_minimal: Required fields only
- cable_extended: Common optional fields
- cable_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cable,
    Entity,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cable-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Cable entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cable = cable_minimal()
        # cable = cable_extended()
        # cable = cable_explicit()

        response = client.ingest(entities=[Entity(cable=cable)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Cable ingested successfully")


def cable_minimal() -> Cable:
    """Create a Cable with only required fields using flat strings."""
    return Cable(
        metadata={"source": "example"},
    )


def cable_extended() -> Cable:
    """Create a Cable with common optional fields."""
    return Cable(
        metadata={"source": "example"},
        status="connected",
        color="0000ff",
        description="Example description",
    )


def cable_explicit() -> Cable:
    """Create a Cable with fully nested objects and all common fields."""
    return Cable(
        metadata={"source": "example"},
        status="connected",
        color="0000ff",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
