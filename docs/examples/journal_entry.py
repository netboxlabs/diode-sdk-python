"""
JournalEntry entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting JournalEntry entities:
- journal_entry_minimal: Required fields only
- journal_entry_extended: Common optional fields
- journal_entry_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    JournalEntry,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "journal_entry-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = journal_entry_minimal()
        # entity = journal_entry_extended()
        # entity = journal_entry_explicit()

        response = client.ingest(entities=[Entity(journal_entry=entity)])
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
        metadata={"source": "example"},
    )


def journal_entry_explicit() -> JournalEntry:
    """Create a JournalEntry with fully nested objects and all common fields."""
    return JournalEntry(
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
