"""
RackReservation entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RackReservation entities:
- rack_reservation_minimal: Required fields only
- rack_reservation_extended: Common optional fields
- rack_reservation_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Rack,
    RackReservation,
    Site,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "rack_reservation-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a RackReservation entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = rack_reservation_minimal()
        # entity = rack_reservation_extended()
        # entity = rack_reservation_explicit()

        response = client.ingest(entities=[Entity(rack_reservation=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RackReservation ingested successfully")


def rack_reservation_minimal() -> RackReservation:
    """Create a RackReservation with only required fields using flat strings."""
    return RackReservation(
        rack="example-rack",  # flat string -> Rack
        description="Example description",
        metadata={"source": "example"},
    )


def rack_reservation_extended() -> RackReservation:
    """Create a RackReservation with common optional fields."""
    return RackReservation(
        rack="example-rack",
        description="Example description",
        comments="Example comments",
        status="active",
        metadata={"source": "example"},
    )


def rack_reservation_explicit() -> RackReservation:
    """Create a RackReservation with fully nested objects and all common fields."""
    return RackReservation(
        rack=Rack(
            name="Example Name",
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            status="active",
            serial="SN-001234",
            asset_tag="ASSET-001",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        description="Example description",
        comments="Example comments",
        status="active",
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
