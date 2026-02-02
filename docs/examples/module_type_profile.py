"""
ModuleTypeProfile entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ModuleTypeProfile entities:
- module_type_profile_minimal: Required fields only
- module_type_profile_extended: Common optional fields
- module_type_profile_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ModuleTypeProfile,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "module_type_profile-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ModuleTypeProfile entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        module_type_profile = module_type_profile_minimal()
        # module_type_profile = module_type_profile_extended()
        # module_type_profile = module_type_profile_explicit()

        response = client.ingest(
            entities=[Entity(module_type_profile=module_type_profile)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ModuleTypeProfile ingested successfully")


def module_type_profile_minimal() -> ModuleTypeProfile:
    """Create a ModuleTypeProfile with only required fields using flat strings."""
    return ModuleTypeProfile(
        name="Example Name",
        metadata={"source": "example"},
    )


def module_type_profile_extended() -> ModuleTypeProfile:
    """Create a ModuleTypeProfile with common optional fields."""
    return ModuleTypeProfile(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def module_type_profile_explicit() -> ModuleTypeProfile:
    """Create a ModuleTypeProfile with fully nested objects and all common fields."""
    return ModuleTypeProfile(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
