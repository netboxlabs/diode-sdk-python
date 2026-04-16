"""
Contact entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Contact entities:
- contact_minimal: Required fields only
- contact_extended: Common optional fields
- contact_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Contact,
    ContactGroup,
    Entity,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "contact-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Contact entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        contact = contact_minimal()
        # contact = contact_extended()
        # contact = contact_explicit()

        response = client.ingest(entities=[Entity(contact=contact)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Contact ingested successfully")


def contact_minimal() -> Contact:
    """Create a Contact with only required fields using flat strings."""
    return Contact(
        name="Example Name",
        metadata={"source": "example"},
    )


def contact_extended() -> Contact:
    """Create a Contact with common optional fields."""
    return Contact(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        title="Example Title",
        phone="Example Phone",
        email="Example Email",
        address="192.0.2.1/32",
        link="Example Link",
        comments="Example comments",
    )


def contact_explicit() -> Contact:
    """Create a Contact with fully nested objects and all common fields."""
    return Contact(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        title="Example Title",
        phone="Example Phone",
        email="Example Email",
        address="192.0.2.1/32",
        link="Example Link",
        group=ContactGroup(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
