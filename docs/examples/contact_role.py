"""
ContactRole entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ContactRole entities:
- contact_role_minimal: Required fields only
- contact_role_extended: Common optional fields
- contact_role_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ContactRole,
    Entity,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "contact_role-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ContactRole entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        contact_role = contact_role_minimal()
        # contact_role = contact_role_extended()
        # contact_role = contact_role_explicit()

        response = client.ingest(entities=[Entity(contact_role=contact_role)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ContactRole ingested successfully")


def contact_role_minimal() -> ContactRole:
    """Create a ContactRole with only required fields using flat strings."""
    return ContactRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def contact_role_extended() -> ContactRole:
    """Create a ContactRole with common optional fields."""
    return ContactRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def contact_role_explicit() -> ContactRole:
    """Create a ContactRole with fully nested objects and all common fields."""
    return ContactRole(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
