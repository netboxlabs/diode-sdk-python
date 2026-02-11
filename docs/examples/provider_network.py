"""
ProviderNetwork entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ProviderNetwork entities:
- provider_network_minimal: Required fields only
- provider_network_extended: Common optional fields
- provider_network_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Provider,
    ProviderNetwork,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "provider_network-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a ProviderNetwork entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = provider_network_minimal()
        # entity = provider_network_extended()
        # entity = provider_network_explicit()

        response = client.ingest(entities=[Entity(provider_network=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ProviderNetwork ingested successfully")


def provider_network_minimal() -> ProviderNetwork:
    """Create a ProviderNetwork with only required fields using flat strings."""
    return ProviderNetwork(
        provider="example-provider",  # flat string -> Provider
        name="Example Name",
        metadata={"source": "example"},
    )


def provider_network_extended() -> ProviderNetwork:
    """Create a ProviderNetwork with common optional fields."""
    return ProviderNetwork(
        provider="example-provider",
        name="Example Name",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def provider_network_explicit() -> ProviderNetwork:
    """Create a ProviderNetwork with fully nested objects and all common fields."""
    return ProviderNetwork(
        provider=Provider(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        name="Example Name",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
