"""
RackGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RackGroup entities:
- rack_group_minimal: Required fields only
- rack_group_extended: Common optional fields
- rack_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    RackGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rack_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a RackGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        rack_group = rack_group_minimal()
        # rack_group = rack_group_extended()
        # rack_group = rack_group_explicit()

        response = client.ingest(entities=[Entity(rack_group=rack_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RackGroup ingested successfully")


def rack_group_minimal() -> RackGroup:
    """Create a RackGroup with only required fields using flat strings."""
    return RackGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def rack_group_extended() -> RackGroup:
    """Create a RackGroup with common optional fields."""
    return RackGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def rack_group_explicit() -> RackGroup:
    """Create a RackGroup with fully nested objects and all common fields."""
    return RackGroup(
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
