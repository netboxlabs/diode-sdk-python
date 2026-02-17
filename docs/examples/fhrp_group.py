"""
FHRPGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting FHRPGroup entities:
- fhrp_group_minimal: Required fields only
- fhrp_group_extended: Common optional fields
- fhrp_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    FHRPGroup,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "fhrp_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        fhrp_group = fhrp_group_minimal()
        # fhrp_group = fhrp_group_extended()
        # fhrp_group = fhrp_group_explicit()

        response = client.ingest(entities=[Entity(fhrp_group=fhrp_group)])
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
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        name="Example Name",
        auth_type="md5",
        auth_key="Example Auth Key",
        comments="Example comments",
    )


def fhrp_group_explicit() -> FHRPGroup:
    """Create a FHRPGroup with fully nested objects and all common fields."""
    return FHRPGroup(
        protocol="carp",
        group_id=1,
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        name="Example Name",
        auth_type="md5",
        auth_key="Example Auth Key",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
