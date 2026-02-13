"""
Provider entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Provider entities:
- provider_minimal: Required fields only
- provider_extended: Common optional fields
- provider_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Provider,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "provider-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Provider entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        provider = provider_minimal()
        # provider = provider_extended()
        # provider = provider_explicit()

        response = client.ingest(entities=[Entity(provider=provider)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Provider ingested successfully")


def provider_minimal() -> Provider:
    """Create a Provider with only required fields using flat strings."""
    return Provider(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def provider_extended() -> Provider:
    """Create a Provider with common optional fields."""
    return Provider(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def provider_explicit() -> Provider:
    """Create a Provider with fully nested objects and all common fields."""
    return Provider(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
