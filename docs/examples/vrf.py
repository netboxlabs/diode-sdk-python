"""
VRF entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VRF entities:
- vrf_minimal: Required fields only
- vrf_extended: Common optional fields
- vrf_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    Tenant,
    VRF,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vrf-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VRF entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        vrf = vrf_minimal()
        # vrf = vrf_extended()
        # vrf = vrf_explicit()

        response = client.ingest(entities=[Entity(vrf=vrf)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VRF ingested successfully")


def vrf_minimal() -> VRF:
    """Create a VRF with only required fields using flat strings."""
    return VRF(
        name="Example Name",
        metadata={"source": "example"},
    )


def vrf_extended() -> VRF:
    """Create a VRF with common optional fields."""
    return VRF(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def vrf_explicit() -> VRF:
    """Create a VRF with fully nested objects and all common fields."""
    return VRF(
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
