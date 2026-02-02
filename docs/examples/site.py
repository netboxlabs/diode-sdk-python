"""
Site entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Site entities:
- site_minimal: Required fields only
- site_extended: Common optional fields
- site_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Site,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "site-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Site entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        site = site_minimal()
        # site = site_extended()
        # site = site_explicit()

        response = client.ingest(entities=[Entity(site=site)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Site ingested successfully")


def site_minimal() -> Site:
    """Create a Site with only required fields using flat strings."""
    return Site(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def site_extended() -> Site:
    """Create a Site with common optional fields."""
    return Site(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        status="active",
        description="Example description",
    )


def site_explicit() -> Site:
    """Create a Site with fully nested objects and all common fields."""
    return Site(
        name="Example Name",
        slug="example-slug",
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
