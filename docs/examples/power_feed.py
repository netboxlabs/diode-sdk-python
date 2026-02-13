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
    PowerFeed,
    PowerPanel,
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
        metadata={"source": "example"},
        status="active",
        description="Example description",
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
