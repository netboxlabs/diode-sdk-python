"""
ClusterGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ClusterGroup entities:
- cluster_group_minimal: Required fields only
- cluster_group_extended: Common optional fields
- cluster_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ClusterGroup,
    Entity,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cluster_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ClusterGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cluster_group = cluster_group_minimal()
        # cluster_group = cluster_group_extended()
        # cluster_group = cluster_group_explicit()

        response = client.ingest(entities=[Entity(cluster_group=cluster_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ClusterGroup ingested successfully")


def cluster_group_minimal() -> ClusterGroup:
    """Create a ClusterGroup with only required fields using flat strings."""
    return ClusterGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def cluster_group_extended() -> ClusterGroup:
    """Create a ClusterGroup with common optional fields."""
    return ClusterGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def cluster_group_explicit() -> ClusterGroup:
    """Create a ClusterGroup with fully nested objects and all common fields."""
    return ClusterGroup(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
