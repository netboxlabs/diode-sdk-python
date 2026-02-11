"""
Rack entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Rack entities:
- rack_minimal: Required fields only
- rack_extended: Common optional fields
- rack_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Rack,
    Site,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "rack-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a Rack entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = rack_minimal()
        # entity = rack_extended()
        # entity = rack_explicit()

        response = client.ingest(entities=[Entity(rack=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Rack ingested successfully")


def rack_minimal() -> Rack:
    """Create a Rack with only required fields using flat strings."""
    return Rack(
        name="Example Name",
        site="example-site",  # flat string -> Site
        metadata={"source": "example"},
    )


def rack_extended() -> Rack:
    """Create a Rack with common optional fields."""
    return Rack(
        name="Example Name",
        site="example-site",
        status="active",
        serial="SN-001234",
        asset_tag="ASSET-001",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def rack_explicit() -> Rack:
    """Create a Rack with fully nested objects and all common fields."""
    return Rack(
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
