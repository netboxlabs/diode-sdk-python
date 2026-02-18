"""
CustomFieldChoiceSet entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CustomFieldChoiceSet entities:
- custom_field_choice_set_minimal: Required fields only
- custom_field_choice_set_extended: Common optional fields
- custom_field_choice_set_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CustomFieldChoiceSet,
    Entity,
    Owner,
    OwnerGroup,
)

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
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        base_choices="IATA",
        order_alphabetically=True,
    )


def custom_field_choice_set_explicit() -> CustomFieldChoiceSet:
    """Create a CustomFieldChoiceSet with fully nested objects and all common fields."""
    return CustomFieldChoiceSet(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        base_choices="IATA",
        order_alphabetically=True,
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
    )


if __name__ == "__main__":
    main()
