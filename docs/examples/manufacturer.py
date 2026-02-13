"""
Manufacturer entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Manufacturer entities:
- manufacturer_minimal: Required fields only
- manufacturer_extended: Common optional fields
- manufacturer_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Manufacturer,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "manufacturer-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Manufacturer entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        manufacturer = manufacturer_minimal()
        # manufacturer = manufacturer_extended()
        # manufacturer = manufacturer_explicit()

        response = client.ingest(entities=[Entity(manufacturer=manufacturer)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Manufacturer ingested successfully")


def manufacturer_minimal() -> Manufacturer:
    """Create a Manufacturer with only required fields using flat strings."""
    return Manufacturer(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def manufacturer_extended() -> Manufacturer:
    """Create a Manufacturer with common optional fields."""
    return Manufacturer(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def manufacturer_explicit() -> Manufacturer:
    """Create a Manufacturer with fully nested objects and all common fields."""
    return Manufacturer(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
