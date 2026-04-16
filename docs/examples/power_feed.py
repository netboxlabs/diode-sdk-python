"""
PowerFeed entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting PowerFeed entities:
- power_feed_minimal: Required fields only
- power_feed_extended: Common optional fields
- power_feed_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    PowerFeed,
    PowerPanel,
    Rack,
    Site,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "power_feed-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a PowerFeed entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        power_feed = power_feed_minimal()
        # power_feed = power_feed_extended()
        # power_feed = power_feed_explicit()

        response = client.ingest(entities=[Entity(power_feed=power_feed)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("PowerFeed ingested successfully")


def power_feed_minimal() -> PowerFeed:
    """Create a PowerFeed with only required fields using flat strings."""
    return PowerFeed(
        power_panel="Example Power Panel",  # flat string -> PowerPanel
        name="Example Name",
        metadata={"source": "example"},
    )


def power_feed_extended() -> PowerFeed:
    """Create a PowerFeed with common optional fields."""
    return PowerFeed(
        power_panel="Example Power Panel",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        rack="Example Rack",
        type="primary",
        supply="ac",
        phase="single-phase",
        voltage=1,
        amperage=1,
        max_utilization=1,
        mark_connected=True,
        tenant="Example Tenant",
        comments="Example comments",
    )


def power_feed_explicit() -> PowerFeed:
    """Create a PowerFeed with fully nested objects and all common fields."""
    return PowerFeed(
        power_panel=PowerPanel(
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                metadata={"source": "example"},
            ),
            name="Example Name",
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
        type="primary",
        supply="ac",
        phase="single-phase",
        voltage=1,
        amperage=1,
        max_utilization=1,
        mark_connected=True,
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
