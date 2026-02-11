"""
CustomField entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CustomField entities:
- custom_field_minimal: Required fields only
- custom_field_extended: Common optional fields
- custom_field_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    CustomField,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "custom_field-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a CustomField entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = custom_field_minimal()
        # entity = custom_field_extended()
        # entity = custom_field_explicit()

        response = client.ingest(entities=[Entity(custom_field=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CustomField ingested successfully")


def custom_field_minimal() -> CustomField:
    """Create a CustomField with only required fields using flat strings."""
    return CustomField(
        type="boolean",
        name="Example Name",
        metadata={"source": "example"},
    )


def custom_field_extended() -> CustomField:
    """Create a CustomField with common optional fields."""
    return CustomField(
        type="boolean",
        name="Example Name",
        label="Example label",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def custom_field_explicit() -> CustomField:
    """Create a CustomField with fully nested objects and all common fields."""
    return CustomField(
        type="boolean",
        name="Example Name",
        label="Example label",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
