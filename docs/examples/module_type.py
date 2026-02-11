"""
ModuleType entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ModuleType entities:
- module_type_minimal: Required fields only
- module_type_extended: Common optional fields
- module_type_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Manufacturer,
    ModuleType,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "module_type-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a ModuleType entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = module_type_minimal()
        # entity = module_type_extended()
        # entity = module_type_explicit()

        response = client.ingest(entities=[Entity(module_type=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ModuleType ingested successfully")


def module_type_minimal() -> ModuleType:
    """Create a ModuleType with only required fields using flat strings."""
    return ModuleType(
        manufacturer="example-manufacturer",  # flat string -> Manufacturer
        model="Model X",
        metadata={"source": "example"},
    )


def module_type_extended() -> ModuleType:
    """Create a ModuleType with common optional fields."""
    return ModuleType(
        manufacturer="example-manufacturer",
        model="Model X",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def module_type_explicit() -> ModuleType:
    """Create a ModuleType with fully nested objects and all common fields."""
    return ModuleType(
        manufacturer=Manufacturer(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        model="Model X",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
