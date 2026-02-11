"""
ContactAssignment entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ContactAssignment entities:
- contact_assignment_minimal: Required fields only
- contact_assignment_extended: Common optional fields
- contact_assignment_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Contact,
    ContactAssignment,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "contact_assignment-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a ContactAssignment entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = contact_assignment_minimal()
        # entity = contact_assignment_extended()
        # entity = contact_assignment_explicit()

        response = client.ingest(entities=[Entity(contact_assignment=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ContactAssignment ingested successfully")


def contact_assignment_minimal() -> ContactAssignment:
    """Create a ContactAssignment with only required fields using flat strings."""
    return ContactAssignment(
        contact="example-contact",  # flat string -> Contact
        metadata={"source": "example"},
    )


def contact_assignment_extended() -> ContactAssignment:
    """Create a ContactAssignment with common optional fields."""
    return ContactAssignment(
        contact="example-contact",
        metadata={"source": "example"},
    )


def contact_assignment_explicit() -> ContactAssignment:
    """Create a ContactAssignment with fully nested objects and all common fields."""
    return ContactAssignment(
        contact=Contact(
            name="Example Name",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
