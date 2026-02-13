"""
IPRange entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPRange entities:
- ip_range_minimal: Required fields only
- ip_range_extended: Common optional fields
- ip_range_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IPRange,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "ip_range-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a IPRange entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        ip_range = ip_range_minimal()
        # ip_range = ip_range_extended()
        # ip_range = ip_range_explicit()

        response = client.ingest(entities=[Entity(ip_range=ip_range)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPRange ingested successfully")


def ip_range_minimal() -> IPRange:
    """Create a IPRange with only required fields using flat strings."""
    return IPRange(
        start_address="Example Start Address",
        end_address="Example End Address",
        metadata={"source": "example"},
    )


def ip_range_extended() -> IPRange:
    """Create a IPRange with common optional fields."""
    return IPRange(
        start_address="Example Start Address",
        end_address="Example End Address",
        metadata={"source": "example"},
        status="active",
        description="Example description",
    )


def ip_range_explicit() -> IPRange:
    """Create a IPRange with fully nested objects and all common fields."""
    return IPRange(
        start_address="Example Start Address",
        end_address="Example End Address",
        metadata={"source": "example"},
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
