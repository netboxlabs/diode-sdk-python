"""
RackType entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RackType entities:
- rack_type_minimal: Required fields only
- rack_type_extended: Common optional fields
- rack_type_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Manufacturer,
    RackType,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rack_type-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a RackType entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        rack_type = rack_type_minimal()
        # rack_type = rack_type_extended()
        # rack_type = rack_type_explicit()

        response = client.ingest(entities=[Entity(rack_type=rack_type)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RackType ingested successfully")


def rack_type_minimal() -> RackType:
    """Create a RackType with only required fields using flat strings."""
    return RackType(
        manufacturer="Example Manufacturer",  # flat string -> Manufacturer
        model="Model X",
        slug="example-slug",
        metadata={"source": "example"},
    )


def rack_type_extended() -> RackType:
    """Create a RackType with common optional fields."""
    return RackType(
        manufacturer="Example Manufacturer",
        model="Model X",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def rack_type_explicit() -> RackType:
    """Create a RackType with fully nested objects and all common fields."""
    return RackType(
        manufacturer=Manufacturer(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        model="Model X",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
