"""
JournalEntry entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting JournalEntry entities:
- journal_entry_minimal: Required fields only
- journal_entry_extended: Common optional fields
- journal_entry_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    JournalEntry,
    Tag,
    User,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "journal_entry-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a JournalEntry entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        journal_entry = journal_entry_minimal()
        # journal_entry = journal_entry_extended()
        # journal_entry = journal_entry_explicit()

        response = client.ingest(entities=[Entity(journal_entry=journal_entry)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("JournalEntry ingested successfully")


def journal_entry_minimal() -> JournalEntry:
    """Create a JournalEntry with only required fields using flat strings."""
    return JournalEntry(
        comments="Example comments",
        metadata={"source": "example"},
    )


def journal_entry_extended() -> JournalEntry:
    """Create a JournalEntry with common optional fields."""
    return JournalEntry(
        comments="Example comments",
        metadata={"source": "example", "custom_key": "custom_value"},
        kind="danger",
    )


def journal_entry_explicit() -> JournalEntry:
    """Create a JournalEntry with fully nested objects and all common fields."""
    return JournalEntry(
        comments="Example comments",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        kind="danger",
        created_by=User(username="Example Username", metadata={"source": "example"}),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
