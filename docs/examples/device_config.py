"""
DeviceConfig entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting DeviceConfig entities:
- device_config_minimal: Required fields only
- device_config_extended: Common optional fields
- device_config_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    DeviceConfig,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "device_config-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = device_config_minimal()
        # entity = device_config_extended()
        # entity = device_config_explicit()

        response = client.ingest(entities=[Entity(device_config=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("DeviceConfig ingested successfully")


def device_config_minimal() -> DeviceConfig:
    """Create a DeviceConfig with only required fields using flat strings."""
    return DeviceConfig(
        startup=b"example startup",
        running=b"example running",
        candidate=b"example candidate",
        metadata={"source": "example"},
    )


def device_config_extended() -> DeviceConfig:
    """Create a DeviceConfig with common optional fields."""
    return DeviceConfig(
        startup=b"example startup",
        running=b"example running",
        candidate=b"example candidate",
        metadata={"source": "example"},
    )


def device_config_explicit() -> DeviceConfig:
    """Create a DeviceConfig with fully nested objects and all common fields."""
    return DeviceConfig(
        startup=b"example startup",
        running=b"example running",
        candidate=b"example candidate",
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
