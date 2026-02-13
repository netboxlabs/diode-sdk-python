"""
PowerPanel entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting PowerPanel entities:
- power_panel_minimal: Required fields only
- power_panel_extended: Common optional fields
- power_panel_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    PowerPanel,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "power_panel-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a PowerPanel entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        power_panel = power_panel_minimal()
        # power_panel = power_panel_extended()
        # power_panel = power_panel_explicit()

        response = client.ingest(entities=[Entity(power_panel=power_panel)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("PowerPanel ingested successfully")


def power_panel_minimal() -> PowerPanel:
    """Create a PowerPanel with only required fields using flat strings."""
    return PowerPanel(
        site="Example Site",  # flat string -> Site
        name="Example Name",
        metadata={"source": "example"},
    )


def power_panel_extended() -> PowerPanel:
    """Create a PowerPanel with common optional fields."""
    return PowerPanel(
        site="Example Site",
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def power_panel_explicit() -> PowerPanel:
    """Create a PowerPanel with fully nested objects and all common fields."""
    return PowerPanel(
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
