"""
CustomLink entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CustomLink entities:
- custom_link_minimal: Required fields only
- custom_link_extended: Common optional fields
- custom_link_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    CustomLink,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "custom_link-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a CustomLink entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = custom_link_minimal()
        # entity = custom_link_extended()
        # entity = custom_link_explicit()

        response = client.ingest(entities=[Entity(custom_link=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CustomLink ingested successfully")


def custom_link_minimal() -> CustomLink:
    """Create a CustomLink with only required fields using flat strings."""
    return CustomLink(
        name="Example Name",
        link_text="example-link-text",
        link_url="example-link-url",
        metadata={"source": "example"},
    )


def custom_link_extended() -> CustomLink:
    """Create a CustomLink with common optional fields."""
    return CustomLink(
        name="Example Name",
        link_text="example-link-text",
        link_url="example-link-url",
        metadata={"source": "example"},
    )


def custom_link_explicit() -> CustomLink:
    """Create a CustomLink with fully nested objects and all common fields."""
    return CustomLink(
        name="Example Name",
        link_text="example-link-text",
        link_url="example-link-url",
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
