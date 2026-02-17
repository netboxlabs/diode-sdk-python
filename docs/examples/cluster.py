"""
Cluster entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Cluster entities:
- cluster_minimal: Required fields only
- cluster_extended: Common optional fields
- cluster_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cluster,
    ClusterGroup,
    ClusterType,
    Entity,
    Owner,
    OwnerGroup,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cluster-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Cluster entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cluster = cluster_minimal()
        # cluster = cluster_extended()
        # cluster = cluster_explicit()

        response = client.ingest(entities=[Entity(cluster=cluster)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Cluster ingested successfully")


def cluster_minimal() -> Cluster:
    """Create a Cluster with only required fields using flat strings."""
    return Cluster(
        name="Example Name",
        type="Example Type",  # flat string -> ClusterType
        metadata={"source": "example"},
    )


def cluster_extended() -> Cluster:
    """Create a Cluster with common optional fields."""
    return Cluster(
        name="Example Name",
        type="Example Type",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        tenant="Example Tenant",
        comments="Example comments",
    )


def cluster_explicit() -> Cluster:
    """Create a Cluster with fully nested objects and all common fields."""
    return Cluster(
        name="Example Name",
        type=ClusterType(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        group=ClusterGroup(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
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
