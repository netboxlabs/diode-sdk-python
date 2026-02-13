"""
Location entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Location entities:
- location_minimal: Required fields only
- location_extended: Common optional fields
- location_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Location,
    Site,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "location-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Location entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        location = location_minimal()
        # location = location_extended()
        # location = location_explicit()

        response = client.ingest(entities=[Entity(location=location)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Location ingested successfully")


def location_minimal() -> Location:
    """Create a Location with only required fields using flat strings."""
    return Location(
        name="Example Name",
        slug="example-slug",
        site="Example Site",  # flat string -> Site
        metadata={"source": "example"},
    )


def location_extended() -> Location:
    """Create a Location with common optional fields."""
    return Location(
        name="Example Name",
        slug="example-slug",
        site="Example Site",
        metadata={"source": "example"},
        status="active",
        description="Example description",
    )


def location_explicit() -> Location:
    """Create a Location with fully nested objects and all common fields."""
    return Location(
        name="Example Name",
        slug="example-slug",
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        metadata={"source": "example"},
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
