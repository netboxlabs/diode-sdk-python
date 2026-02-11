"""
Platform entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Platform entities:
- platform_minimal: Required fields only
- platform_extended: Common optional fields
- platform_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Platform,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "platform-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a Platform entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = platform_minimal()
        # entity = platform_extended()
        # entity = platform_explicit()

        response = client.ingest(entities=[Entity(platform=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Platform ingested successfully")


def platform_minimal() -> Platform:
    """Create a Platform with only required fields using flat strings."""
    return Platform(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def platform_extended() -> Platform:
    """Create a Platform with common optional fields."""
    return Platform(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def platform_explicit() -> Platform:
    """Create a Platform with fully nested objects and all common fields."""
    return Platform(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
