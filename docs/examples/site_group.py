"""
SiteGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting SiteGroup entities:
- site_group_minimal: Required fields only
- site_group_extended: Common optional fields
- site_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    SiteGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "site_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a SiteGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        site_group = site_group_minimal()
        # site_group = site_group_extended()
        # site_group = site_group_explicit()

        response = client.ingest(entities=[Entity(site_group=site_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("SiteGroup ingested successfully")


def site_group_minimal() -> SiteGroup:
    """Create a SiteGroup with only required fields using flat strings."""
    return SiteGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def site_group_extended() -> SiteGroup:
    """Create a SiteGroup with common optional fields."""
    return SiteGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def site_group_explicit() -> SiteGroup:
    """Create a SiteGroup with fully nested objects and all common fields."""
    return SiteGroup(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        parent=SiteGroup(
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
