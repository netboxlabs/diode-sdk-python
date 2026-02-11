"""
ProviderAccount entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ProviderAccount entities:
- provider_account_minimal: Required fields only
- provider_account_extended: Common optional fields
- provider_account_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Provider,
    ProviderAccount,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "provider_account-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = provider_account_minimal()
        # entity = provider_account_extended()
        # entity = provider_account_explicit()

        response = client.ingest(entities=[Entity(provider_account=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ProviderAccount ingested successfully")


def provider_account_minimal() -> ProviderAccount:
    """Create a ProviderAccount with only required fields using flat strings."""
    return ProviderAccount(
        provider="example-provider",  # flat string -> Provider
        account="example-account",
        metadata={"source": "example"},
    )


def provider_account_extended() -> ProviderAccount:
    """Create a ProviderAccount with common optional fields."""
    return ProviderAccount(
        provider="example-provider",
        account="example-account",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def provider_account_explicit() -> ProviderAccount:
    """Create a ProviderAccount with fully nested objects and all common fields."""
    return ProviderAccount(
        provider=Provider(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        account="example-account",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
