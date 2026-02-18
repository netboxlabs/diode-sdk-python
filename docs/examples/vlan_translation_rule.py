"""
VLANTranslationRule entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VLANTranslationRule entities:
- vlan_translation_rule_minimal: Required fields only
- vlan_translation_rule_extended: Common optional fields
- vlan_translation_rule_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    VLANTranslationPolicy,
    VLANTranslationRule,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vlan_translation_rule-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VLANTranslationRule entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        vlan_translation_rule = vlan_translation_rule_minimal()
        # vlan_translation_rule = vlan_translation_rule_extended()
        # vlan_translation_rule = vlan_translation_rule_explicit()

        response = client.ingest(
            entities=[Entity(vlan_translation_rule=vlan_translation_rule)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VLANTranslationRule ingested successfully")


def vlan_translation_rule_minimal() -> VLANTranslationRule:
    """Create a VLANTranslationRule with only required fields using flat strings."""
    return VLANTranslationRule(
        policy="Example Policy",  # flat string -> VLANTranslationPolicy
        local_vid=1,
        remote_vid=1,
        metadata={"source": "example"},
    )


def vlan_translation_rule_extended() -> VLANTranslationRule:
    """Create a VLANTranslationRule with common optional fields."""
    return VLANTranslationRule(
        policy="Example Policy",
        local_vid=1,
        remote_vid=1,
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
    )


def vlan_translation_rule_explicit() -> VLANTranslationRule:
    """Create a VLANTranslationRule with fully nested objects and all common fields."""
    return VLANTranslationRule(
        policy=VLANTranslationPolicy(
            name="Example Name", metadata={"source": "example"}
        ),
        local_vid=1,
        remote_vid=1,
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
    )


if __name__ == "__main__":
    main()
