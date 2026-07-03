"""
VLANGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VLANGroup entities:
- vlan_group_minimal: Required fields only
- vlan_group_extended: Common optional fields
- vlan_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cluster,
    ClusterGroup,
    ClusterType,
    Entity,
    Location,
    Owner,
    OwnerGroup,
    Rack,
    RackGroup,
    Region,
    Site,
    SiteGroup,
    Tag,
    Tenant,
    VLANGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vlan_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VLANGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        vlan_group = vlan_group_minimal()
        # vlan_group = vlan_group_extended()
        # vlan_group = vlan_group_explicit()

        response = client.ingest(entities=[Entity(vlan_group=vlan_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VLANGroup ingested successfully")


def vlan_group_minimal() -> VLANGroup:
    """Create a VLANGroup with only required fields using flat strings."""
    return VLANGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def vlan_group_extended() -> VLANGroup:
    """Create a VLANGroup with common optional fields."""
    return VLANGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        tenant="Example Tenant",
        comments="Example comments",
    )


def vlan_group_explicit() -> VLANGroup:
    """Create a VLANGroup with fully nested objects and all common fields."""
    return VLANGroup(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        # Polymorphic 'scope' — choose ONE of these mutually exclusive variants:
        scope_site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        # scope_cluster=Cluster(name="Example Name", type=ClusterType(name="Example Name", slug="example-slug", metadata={"source": "example"}), status="active", metadata={"source": "example"}),
        # scope_cluster_group=ClusterGroup(name="Example Name", slug="example-slug", metadata={"source": "example"}),
        # scope_location=Location(name="Example Name", slug="example-slug", site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}),
        # scope_rack=Rack(name="Example Name", site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}),
        # scope_region=Region(name="Example Name", slug="example-slug", metadata={"source": "example"}),
        # scope_site_group=SiteGroup(name="Example Name", slug="example-slug", metadata={"source": "example"}),
        # scope_rack_group=RackGroup(name="Example Name", slug="example-slug", metadata={"source": "example"}),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
