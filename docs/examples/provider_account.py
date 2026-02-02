"""
ProviderAccount entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ProviderAccount entities:
- provider_account_minimal: Required fields only
- provider_account_extended: Common optional fields
- provider_account_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Provider,
    ProviderAccount,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "provider_account-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ProviderAccount entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        provider_account = provider_account_minimal()
        # provider_account = provider_account_extended()
        # provider_account = provider_account_explicit()

        response = client.ingest(entities=[Entity(provider_account=provider_account)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ProviderAccount ingested successfully")


def provider_account_minimal() -> ProviderAccount:
    """Create a ProviderAccount with only required fields using flat strings."""
    return ProviderAccount(
        provider="Example Provider",  # flat string -> Provider
        account="Example Account",
        metadata={"source": "example"},
    )


def provider_account_extended() -> ProviderAccount:
    """Create a ProviderAccount with common optional fields."""
    return ProviderAccount(
        provider="Example Provider",
        account="Example Account",
        metadata={"source": "example"},
        description="Example description",
    )


def provider_account_explicit() -> ProviderAccount:
    """Create a ProviderAccount with fully nested objects and all common fields."""
    return ProviderAccount(
        provider=Provider(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        account="Example Account",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
