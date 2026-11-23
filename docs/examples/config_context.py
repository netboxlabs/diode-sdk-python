"""
ConfigContext entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ConfigContext entities:
- config_context_minimal: Required fields only
- config_context_extended: Common optional fields
- config_context_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ConfigContext,
    Entity,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "config_context-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ConfigContext entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        config_context = config_context_minimal()
        # config_context = config_context_extended()
        # config_context = config_context_explicit()

        response = client.ingest(entities=[Entity(config_context=config_context)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ConfigContext ingested successfully")


def config_context_minimal() -> ConfigContext:
    """Create a ConfigContext with only required fields using flat strings."""
    return ConfigContext(
        name="Example Name",
        data="Example Data",
        metadata={"source": "example"},
    )


def config_context_extended() -> ConfigContext:
    """Create a ConfigContext with common optional fields."""
    return ConfigContext(
        name="Example Name",
        data="Example Data",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        weight=1,
        is_active=True,
    )


def config_context_explicit() -> ConfigContext:
    """Create a ConfigContext with fully nested objects and all common fields."""
    return ConfigContext(
        name="Example Name",
        data="Example Data",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        weight=1,
        is_active=True,
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
