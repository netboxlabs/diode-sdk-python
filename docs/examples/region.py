"""
Region entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Region entities:
- region_minimal: Required fields only
- region_extended: Common optional fields
- region_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Region,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "region-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Region entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        region = region_minimal()
        # region = region_extended()
        # region = region_explicit()

        response = client.ingest(entities=[Entity(region=region)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Region ingested successfully")


def region_minimal() -> Region:
    """Create a Region with only required fields using flat strings."""
    return Region(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def region_extended() -> Region:
    """Create a Region with common optional fields."""
    return Region(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def region_explicit() -> Region:
    """Create a Region with fully nested objects and all common fields."""
    return Region(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        parent=Region(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
