"""
ClusterType entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ClusterType entities:
- cluster_type_minimal: Required fields only
- cluster_type_extended: Common optional fields
- cluster_type_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ClusterType,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "cluster_type-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a ClusterType entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = cluster_type_minimal()
        # entity = cluster_type_extended()
        # entity = cluster_type_explicit()

        response = client.ingest(entities=[Entity(cluster_type=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ClusterType ingested successfully")


def cluster_type_minimal() -> ClusterType:
    """Create a ClusterType with only required fields using flat strings."""
    return ClusterType(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def cluster_type_extended() -> ClusterType:
    """Create a ClusterType with common optional fields."""
    return ClusterType(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def cluster_type_explicit() -> ClusterType:
    """Create a ClusterType with fully nested objects and all common fields."""
    return ClusterType(
        name="Example Name",
        slug="example-slug",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
