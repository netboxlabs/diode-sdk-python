"""
VLANTranslationPolicy entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VLANTranslationPolicy entities:
- vlan_translation_policy_minimal: Required fields only
- vlan_translation_policy_extended: Common optional fields
- vlan_translation_policy_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vlan_translation_policy-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VLANTranslationPolicy entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        vlan_translation_policy = vlan_translation_policy_minimal()
        # vlan_translation_policy = vlan_translation_policy_extended()
        # vlan_translation_policy = vlan_translation_policy_explicit()

        response = client.ingest(
            entities=[Entity(vlan_translation_policy=vlan_translation_policy)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VLANTranslationPolicy ingested successfully")


def vlan_translation_policy_minimal() -> VLANTranslationPolicy:
    """Create a VLANTranslationPolicy with only required fields using flat strings."""
    return VLANTranslationPolicy(
        name="Example Name",
        metadata={"source": "example"},
    )


def vlan_translation_policy_extended() -> VLANTranslationPolicy:
    """Create a VLANTranslationPolicy with common optional fields."""
    return VLANTranslationPolicy(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def vlan_translation_policy_explicit() -> VLANTranslationPolicy:
    """Create a VLANTranslationPolicy with fully nested objects and all common fields."""
    return VLANTranslationPolicy(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
    )


if __name__ == "__main__":
    main()
