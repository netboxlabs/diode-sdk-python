"""
CustomField entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CustomField entities:
- custom_field_minimal: Required fields only
- custom_field_extended: Common optional fields
- custom_field_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CustomField,
    CustomFieldChoiceSet,
    Entity,
    Owner,
    OwnerGroup,
)

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
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        related_object_type="circuits.circuit",
        label="Example Label",
        group_name="Example Group Name",
        required=True,
        unique=True,
        search_weight=1,
        filter_logic="disabled",
        ui_visible="always",
        ui_editable="hidden",
        is_cloneable=True,
        default="Example Default",
        related_object_filter="Example Related Object Filter",
        weight=1,
        validation_minimum=1.0,
        validation_maximum=1.0,
        validation_regex="Example Validation Regex",
        comments="Example comments",
    )


def custom_field_explicit() -> CustomField:
    """Create a CustomField with fully nested objects and all common fields."""
    return CustomField(
        type="boolean",
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        related_object_type="circuits.circuit",
        label="Example Label",
        group_name="Example Group Name",
        required=True,
        unique=True,
        search_weight=1,
        filter_logic="disabled",
        ui_visible="always",
        ui_editable="hidden",
        is_cloneable=True,
        default="Example Default",
        related_object_filter="Example Related Object Filter",
        weight=1,
        validation_minimum=1.0,
        validation_maximum=1.0,
        validation_regex="Example Validation Regex",
        choice_set=CustomFieldChoiceSet(
            name="Example Name", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
    )


if __name__ == "__main__":
    main()
