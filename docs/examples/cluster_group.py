"""
ClusterGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ClusterGroup entities:
- cluster_group_minimal: Required fields only
- cluster_group_extended: Common optional fields
- cluster_group_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ClusterGroup,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "cluster_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = cluster_group_minimal()
        # entity = cluster_group_extended()
        # entity = cluster_group_explicit()

        response = client.ingest(entities=[Entity(cluster_group=entity)])
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
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def cluster_group_explicit() -> ClusterGroup:
    """Create a ClusterGroup with fully nested objects and all common fields."""
    return ClusterGroup(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
