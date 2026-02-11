"""
Role entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Role entities:
- role_minimal: Required fields only
- role_extended: Common optional fields
- role_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Role,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = role_minimal()
        # entity = role_extended()
        # entity = role_explicit()

        response = client.ingest(entities=[Entity(role=entity)])
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
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def role_explicit() -> Role:
    """Create a Role with fully nested objects and all common fields."""
    return Role(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
