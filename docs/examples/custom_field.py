"""
CustomField entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CustomField entities:
- custom_field_minimal: Required fields only
- custom_field_extended: Common optional fields
- custom_field_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "custom_field-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        custom_field = custom_field_minimal()
        # custom_field = custom_field_extended()
        # custom_field = custom_field_explicit()

        response = client.ingest(entities=[Entity(custom_field=custom_field)])
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
        metadata={"source": "example"},
        description="Example description",
    )


def custom_field_explicit() -> CustomField:
    """Create a CustomField with fully nested objects and all common fields."""
    return CustomField(
        type="boolean",
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
    )


if __name__ == "__main__":
    main()
