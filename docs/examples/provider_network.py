"""
ProviderNetwork entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ProviderNetwork entities:
- provider_network_minimal: Required fields only
- provider_network_extended: Common optional fields
- provider_network_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Provider,
    ProviderNetwork,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "provider_network-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        provider_network = provider_network_minimal()
        # provider_network = provider_network_extended()
        # provider_network = provider_network_explicit()

        response = client.ingest(entities=[Entity(provider_network=provider_network)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ProviderNetwork ingested successfully")


def provider_network_minimal() -> ProviderNetwork:
    """Create a ProviderNetwork with only required fields using flat strings."""
    return ProviderNetwork(
        provider="Example Provider",  # flat string -> Provider
        name="Example Name",
        metadata={"source": "example"},
    )


def provider_network_extended() -> ProviderNetwork:
    """Create a ProviderNetwork with common optional fields."""
    return ProviderNetwork(
        provider="Example Provider",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        service_id="Example Service Id",
        comments="Example comments",
    )


def provider_network_explicit() -> ProviderNetwork:
    """Create a ProviderNetwork with fully nested objects and all common fields."""
    return ProviderNetwork(
        provider=Provider(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        service_id="Example Service Id",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
