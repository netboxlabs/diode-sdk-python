"""
Region entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Region entities:
- region_minimal: Required fields only
- region_extended: Common optional fields
- region_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Region,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "region-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = region_minimal()
        # entity = region_extended()
        # entity = region_explicit()

        response = client.ingest(entities=[Entity(region=entity)])
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
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def region_explicit() -> Region:
    """Create a Region with fully nested objects and all common fields."""
    return Region(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
