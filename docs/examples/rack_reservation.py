"""
RackReservation entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RackReservation entities:
- rack_reservation_minimal: Required fields only
- rack_reservation_extended: Common optional fields
- rack_reservation_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Rack,
    RackReservation,
    Site,
    Tag,
    Tenant,
    User,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rack_reservation-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        rack_reservation = rack_reservation_minimal()
        # rack_reservation = rack_reservation_extended()
        # rack_reservation = rack_reservation_explicit()

        response = client.ingest(entities=[Entity(rack_reservation=rack_reservation)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RackReservation ingested successfully")


def rack_reservation_minimal() -> RackReservation:
    """Create a RackReservation with only required fields using flat strings."""
    return RackReservation(
        rack="Example Rack",  # flat string -> Rack
        description="Example description",
        metadata={"source": "example"},
        user="Example User",  # flat string -> User
    )


def rack_reservation_extended() -> RackReservation:
    """Create a RackReservation with common optional fields."""
    return RackReservation(
        rack="Example Rack",
        description="Example description",
        metadata={"source": "example", "custom_key": "custom_value"},
        user="Example User",
        status="active",
        tenant="Example Tenant",
        comments="Example comments",
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
                metadata={"source": "example"},
            ),
            status="active",
            metadata={"source": "example"},
        ),
        description="Example description",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        user=User(username="Example Username", metadata={"source": "example"}),
        status="active",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
