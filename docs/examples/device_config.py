"""
DeviceConfig entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting DeviceConfig entities:
- device_config_minimal: Required fields only
- device_config_extended: Common optional fields
- device_config_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    DeviceConfig,
    Entity,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "device_config-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a DeviceConfig entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        device_config = device_config_minimal()
        # device_config = device_config_extended()
        # device_config = device_config_explicit()

        response = client.ingest(entities=[Entity(device_config=device_config)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("DeviceConfig ingested successfully")


def device_config_minimal() -> DeviceConfig:
    """Create a DeviceConfig with only required fields using flat strings."""
    return DeviceConfig(
        startup=b"example data",
        metadata={"source": "example"},
    )


def device_config_extended() -> DeviceConfig:
    """Create a DeviceConfig with common optional fields."""
    return DeviceConfig(
        startup=b"example data",
        running=b"example data",
        metadata={"source": "example", "custom_key": "custom_value"},
    )


def device_config_explicit() -> DeviceConfig:
    """Create a DeviceConfig with fully nested objects and all common fields."""
    return DeviceConfig(
        startup=b"example data",
        running=b"example data",
        candidate=b"example data",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
    )


if __name__ == "__main__":
    main()
