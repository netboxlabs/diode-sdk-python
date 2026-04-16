"""
RackRole entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RackRole entities:
- rack_role_minimal: Required fields only
- rack_role_extended: Common optional fields
- rack_role_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    RackRole,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rack_role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a RackRole entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        rack_role = rack_role_minimal()
        # rack_role = rack_role_extended()
        # rack_role = rack_role_explicit()

        response = client.ingest(entities=[Entity(rack_role=rack_role)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RackRole ingested successfully")


def rack_role_minimal() -> RackRole:
    """Create a RackRole with only required fields using flat strings."""
    return RackRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def rack_role_extended() -> RackRole:
    """Create a RackRole with common optional fields."""
    return RackRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        color="0000ff",
        comments="Example comments",
    )


def rack_role_explicit() -> RackRole:
    """Create a RackRole with fully nested objects and all common fields."""
    return RackRole(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        color="0000ff",
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
