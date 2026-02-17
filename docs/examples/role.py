"""
Role entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Role entities:
- role_minimal: Required fields only
- role_extended: Common optional fields
- role_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Role,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Role entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        role = role_minimal()
        # role = role_extended()
        # role = role_explicit()

        response = client.ingest(entities=[Entity(role=role)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Role ingested successfully")


def role_minimal() -> Role:
    """Create a Role with only required fields using flat strings."""
    return Role(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def role_extended() -> Role:
    """Create a Role with common optional fields."""
    return Role(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        weight=1,
        comments="Example comments",
    )


def role_explicit() -> Role:
    """Create a Role with fully nested objects and all common fields."""
    return Role(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        weight=1,
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
