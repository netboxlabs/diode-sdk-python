"""
ContactAssignment entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ContactAssignment entities:
- contact_assignment_minimal: Required fields only
- contact_assignment_extended: Common optional fields
- contact_assignment_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Contact,
    ContactAssignment,
    Entity,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "contact_assignment-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        contact_assignment = contact_assignment_minimal()
        # contact_assignment = contact_assignment_extended()
        # contact_assignment = contact_assignment_explicit()

        response = client.ingest(
            entities=[Entity(contact_assignment=contact_assignment)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ContactAssignment ingested successfully")


def contact_assignment_minimal() -> ContactAssignment:
    """Create a ContactAssignment with only required fields using flat strings."""
    return ContactAssignment(
        contact="Example Contact",  # flat string -> Contact
        metadata={"source": "example"},
    )


def contact_assignment_extended() -> ContactAssignment:
    """Create a ContactAssignment with common optional fields."""
    return ContactAssignment(
        contact="Example Contact",
        metadata={"source": "example"},
    )


def contact_assignment_explicit() -> ContactAssignment:
    """Create a ContactAssignment with fully nested objects and all common fields."""
    return ContactAssignment(
        contact=Contact(name="Example Name", metadata={"source": "example"}),
        metadata={"source": "example"},
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
