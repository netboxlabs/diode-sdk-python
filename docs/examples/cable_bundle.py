"""
CableBundle entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CableBundle entities:
- cable_bundle_minimal: Required fields only
- cable_bundle_extended: Common optional fields
- cable_bundle_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CableBundle,
    Entity,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cable_bundle-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CableBundle entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cable_bundle = cable_bundle_minimal()
        # cable_bundle = cable_bundle_extended()
        # cable_bundle = cable_bundle_explicit()

        response = client.ingest(entities=[Entity(cable_bundle=cable_bundle)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CableBundle ingested successfully")


def cable_bundle_minimal() -> CableBundle:
    """Create a CableBundle with only required fields using flat strings."""
    return CableBundle(
        name="Example Name",
        metadata={"source": "example"},
    )


def cable_bundle_extended() -> CableBundle:
    """Create a CableBundle with common optional fields."""
    return CableBundle(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def cable_bundle_explicit() -> CableBundle:
    """Create a CableBundle with fully nested objects and all common fields."""
    return CableBundle(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
