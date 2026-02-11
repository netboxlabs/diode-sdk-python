"""
IPRange entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPRange entities:
- ip_range_minimal: Required fields only
- ip_range_extended: Common optional fields
- ip_range_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IPRange,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "ip_range-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an IPRange entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = ip_range_minimal()
        # entity = ip_range_extended()
        # entity = ip_range_explicit()

        response = client.ingest(entities=[Entity(ip_range=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPRange ingested successfully")


def ip_range_minimal() -> IPRange:
    """Create an IPRange with only required fields using flat strings."""
    return IPRange(
        start_address="example-start-address",
        end_address="example-end-address",
        metadata={"source": "example"},
    )


def ip_range_extended() -> IPRange:
    """Create an IPRange with common optional fields."""
    return IPRange(
        start_address="example-start-address",
        end_address="example-end-address",
        status="active",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def ip_range_explicit() -> IPRange:
    """Create an IPRange with fully nested objects and all common fields."""
    return IPRange(
        start_address="example-start-address",
        end_address="example-end-address",
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
