"""
FHRPGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting FHRPGroup entities:
- fhrp_group_minimal: Required fields only
- fhrp_group_extended: Common optional fields
- fhrp_group_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    FHRPGroup,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "fhrp_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a FHRPGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = fhrp_group_minimal()
        # entity = fhrp_group_extended()
        # entity = fhrp_group_explicit()

        response = client.ingest(entities=[Entity(fhrp_group=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("FHRPGroup ingested successfully")


def fhrp_group_minimal() -> FHRPGroup:
    """Create a FHRPGroup with only required fields using flat strings."""
    return FHRPGroup(
        protocol="carp",
        group_id=1,
        metadata={"source": "example"},
    )


def fhrp_group_extended() -> FHRPGroup:
    """Create a FHRPGroup with common optional fields."""
    return FHRPGroup(
        protocol="carp",
        group_id=1,
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def fhrp_group_explicit() -> FHRPGroup:
    """Create a FHRPGroup with fully nested objects and all common fields."""
    return FHRPGroup(
        protocol="carp",
        group_id=1,
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
