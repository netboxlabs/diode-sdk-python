"""
CustomFieldChoiceSet entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CustomFieldChoiceSet entities:
- custom_field_choice_set_minimal: Required fields only
- custom_field_choice_set_extended: Common optional fields
- custom_field_choice_set_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "custom_field_choice_set-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CustomFieldChoiceSet entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        custom_field_choice_set = custom_field_choice_set_minimal()
        # custom_field_choice_set = custom_field_choice_set_extended()
        # custom_field_choice_set = custom_field_choice_set_explicit()

        response = client.ingest(
            entities=[Entity(custom_field_choice_set=custom_field_choice_set)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CustomFieldChoiceSet ingested successfully")


def custom_field_choice_set_minimal() -> CustomFieldChoiceSet:
    """Create a CustomFieldChoiceSet with only required fields using flat strings."""
    return CustomFieldChoiceSet(
        name="Example Name",
        metadata={"source": "example"},
    )


def custom_field_choice_set_extended() -> CustomFieldChoiceSet:
    """Create a CustomFieldChoiceSet with common optional fields."""
    return CustomFieldChoiceSet(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def custom_field_choice_set_explicit() -> CustomFieldChoiceSet:
    """Create a CustomFieldChoiceSet with fully nested objects and all common fields."""
    return CustomFieldChoiceSet(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


if __name__ == "__main__":
    main()
