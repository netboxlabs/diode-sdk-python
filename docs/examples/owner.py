"""
Owner entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Owner entities:
- owner_minimal: Required fields only
- owner_extended: Common optional fields
- owner_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "owner-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Owner entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        owner = owner_minimal()
        # owner = owner_extended()
        # owner = owner_explicit()

        response = client.ingest(entities=[Entity(owner=owner)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Owner ingested successfully")


def owner_minimal() -> Owner:
    """Create a Owner with only required fields using flat strings."""
    return Owner(
        name="Example Name",
        group="Example Group",  # flat string -> OwnerGroup
        metadata={"source": "example"},
    )


def owner_extended() -> Owner:
    """Create a Owner with common optional fields."""
    return Owner(
        name="Example Name",
        group="Example Group",
        metadata={"source": "example"},
        description="Example description",
    )


def owner_explicit() -> Owner:
    """Create a Owner with fully nested objects and all common fields."""
    return Owner(
        name="Example Name",
        group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
        metadata={"source": "example"},
        description="Example description",
    )


if __name__ == "__main__":
    main()
