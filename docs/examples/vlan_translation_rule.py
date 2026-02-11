"""
VLANTranslationRule entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VLANTranslationRule entities:
- vlan_translation_rule_minimal: Required fields only
- vlan_translation_rule_extended: Common optional fields
- vlan_translation_rule_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    VLANTranslationPolicy,
    VLANTranslationRule,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "vlan_translation_rule-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = vlan_translation_rule_minimal()
        # entity = vlan_translation_rule_extended()
        # entity = vlan_translation_rule_explicit()

        response = client.ingest(entities=[Entity(vlan_translation_rule=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VLANTranslationRule ingested successfully")


def vlan_translation_rule_minimal() -> VLANTranslationRule:
    """Create a VLANTranslationRule with only required fields using flat strings."""
    return VLANTranslationRule(
        policy="example-policy",  # flat string -> VLANTranslationPolicy
        local_vid=1,
        remote_vid=1,
        metadata={"source": "example"},
    )


def vlan_translation_rule_extended() -> VLANTranslationRule:
    """Create a VLANTranslationRule with common optional fields."""
    return VLANTranslationRule(
        policy="example-policy",
        local_vid=1,
        remote_vid=1,
        description="Example description",
        metadata={"source": "example"},
    )


def vlan_translation_rule_explicit() -> VLANTranslationRule:
    """Create a VLANTranslationRule with fully nested objects and all common fields."""
    return VLANTranslationRule(
        policy=VLANTranslationPolicy(
            name="Example Name",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        local_vid=1,
        remote_vid=1,
        description="Example description",
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
