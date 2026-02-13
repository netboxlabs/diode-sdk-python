"""
ContactGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ContactGroup entities:
- contact_group_minimal: Required fields only
- contact_group_extended: Common optional fields
- contact_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ContactGroup,
    Entity,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "contact_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ContactGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        contact_group = contact_group_minimal()
        # contact_group = contact_group_extended()
        # contact_group = contact_group_explicit()

        response = client.ingest(entities=[Entity(contact_group=contact_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ContactGroup ingested successfully")


def contact_group_minimal() -> ContactGroup:
    """Create a ContactGroup with only required fields using flat strings."""
    return ContactGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def contact_group_extended() -> ContactGroup:
    """Create a ContactGroup with common optional fields."""
    return ContactGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def contact_group_explicit() -> ContactGroup:
    """Create a ContactGroup with fully nested objects and all common fields."""
    return ContactGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
