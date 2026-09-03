"""
CoolingFeed entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CoolingFeed entities:
- cooling_feed_minimal: Required fields only
- cooling_feed_extended: Common optional fields
- cooling_feed_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CoolingFeed,
    CoolingSource,
    Entity,
    Owner,
    OwnerGroup,
    Rack,
    Site,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cooling_feed-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CoolingFeed entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cooling_feed = cooling_feed_minimal()
        # cooling_feed = cooling_feed_extended()
        # cooling_feed = cooling_feed_explicit()

        response = client.ingest(entities=[Entity(cooling_feed=cooling_feed)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CoolingFeed ingested successfully")


def cooling_feed_minimal() -> CoolingFeed:
    """Create a CoolingFeed with only required fields using flat strings."""
    return CoolingFeed(
        cooling_source="Example Cooling Source",  # flat string -> CoolingSource
        name="Example Name",
        metadata={"source": "example"},
    )


def cooling_feed_extended() -> CoolingFeed:
    """Create a CoolingFeed with common optional fields."""
    return CoolingFeed(
        cooling_source="Example Cooling Source",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        rack="Example Rack",
        cooling_capacity=1.0,
        max_flow=1.0,
        max_flow_unit="gpm",
        tenant="Example Tenant",
        comments="Example comments",
    )


def cooling_feed_explicit() -> CoolingFeed:
    """Create a CoolingFeed with fully nested objects and all common fields."""
    return CoolingFeed(
        cooling_source=CoolingSource(
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                metadata={"source": "example"},
            ),
            name="Example Name",
            type="chiller",
            status="active",
            metadata={"source": "example"},
        ),
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        cooling_capacity=1.0,
        max_flow=1.0,
        max_flow_unit="gpm",
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
