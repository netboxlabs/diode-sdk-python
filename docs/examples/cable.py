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
    CableBundle,
    Entity,
    Owner,
    OwnerGroup,
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
        metadata={"source": "example", "custom_key": "custom_value"},
        status="connected",
        description="Example description",
        color="0000ff",
        type="aoc",
        tenant="Example Tenant",
        label="Example Label",
        length=1.0,
        length_unit="cm",
        comments="Example comments",
        profile="breakout-1c2p-2c1p",
    )


def cable_explicit() -> Cable:
    """Create a Cable with fully nested objects and all common fields."""
    return Cable(
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="connected",
        description="Example description",
        color="0000ff",
        comments="Example comments",
        type="aoc",
        label="Example Label",
        length=1.0,
        length_unit="cm",
        profile="breakout-1c2p-2c1p",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        bundle=CableBundle(name="Example Name", metadata={"source": "example"}),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
