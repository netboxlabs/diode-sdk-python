"""
CablePath entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CablePath entities:
- cable_path_minimal: Required fields only
- cable_path_extended: Common optional fields
- cable_path_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    CablePath,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "cable_path-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a CablePath entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = cable_path_minimal()
        # entity = cable_path_extended()
        # entity = cable_path_explicit()

        response = client.ingest(entities=[Entity(cable_path=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CablePath ingested successfully")


def cable_path_minimal() -> CablePath:
    """Create a CablePath with only required fields using flat strings."""
    return CablePath(
        metadata={"source": "example"},
    )


def cable_path_extended() -> CablePath:
    """Create a CablePath with common optional fields."""
    return CablePath(
        metadata={"source": "example"},
    )


def cable_path_explicit() -> CablePath:
    """Create a CablePath with fully nested objects and all common fields."""
    return CablePath(
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
