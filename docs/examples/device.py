"""
Device entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Device entities:
- device_minimal: Required fields only
- device_extended: Common optional fields
- device_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cluster,
    ClusterType,
    Device,
    DeviceConfig,
    DeviceRole,
    DeviceType,
    Entity,
    IPAddress,
    Location,
    Manufacturer,
    Owner,
    OwnerGroup,
    Platform,
    Rack,
    Site,
    Tag,
    Tenant,
    VirtualChassis,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "device-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Device entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        device = device_minimal()
        # device = device_extended()
        # device = device_explicit()

        response = client.ingest(entities=[Entity(device=device)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Device ingested successfully")


def device_minimal() -> Device:
    """Create a Device with only required fields using flat strings."""
    return Device(
        device_type="Model X",  # flat string -> DeviceType
        role="Example Role",  # flat string -> DeviceRole
        site="Example Site",  # flat string -> Site
        metadata={"source": "example"},
    )


def device_extended() -> Device:
    """Create a Device with common optional fields."""
    return Device(
        device_type="Model X",
        role="Example Role",
        site="Example Site",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        serial="SN-001234",
        description="Example description",
        name="Example Name",
        tenant="Example Tenant",
        platform="Example Platform",
        asset_tag="ASSET-001",
        location="Example Location",
        rack="Example Rack",
        position=1.0,
        face="front",
        latitude=1.0,
        longitude=1.0,
        airflow="bottom-to-top",
        cluster="Example Cluster",
        vc_position=1,
        vc_priority=1,
        comments="Example comments",
    )


def device_explicit() -> Device:
    """Create a Device with fully nested objects and all common fields."""
    return Device(
        device_type=DeviceType(
            manufacturer=Manufacturer(
                name="Example Name", slug="example-slug", metadata={"source": "example"}
            ),
            model="Model X",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        role=DeviceRole(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
            metadata={"source": "example"},
        ),
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        serial="SN-001234",
        description="Example description",
        comments="Example comments",
        asset_tag="ASSET-001",
        name="Example Name",
        position=1.0,
        face="front",
        latitude=1.0,
        longitude=1.0,
        airflow="bottom-to-top",
        vc_position=1,
        vc_priority=1,
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        platform=Platform(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        location=Location(
            name="Example Name",
            slug="example-slug",
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                metadata={"source": "example"},
            ),
            status="active",
            metadata={"source": "example"},
        ),
        rack=Rack(
            name="Example Name",
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                metadata={"source": "example"},
            ),
            status="active",
            metadata={"source": "example"},
        ),
        primary_ip4=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        primary_ip6=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        oob_ip=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        cluster=Cluster(
            name="Example Name",
            type=ClusterType(
                name="Example Name", slug="example-slug", metadata={"source": "example"}
            ),
            status="active",
            metadata={"source": "example"},
        ),
        virtual_chassis=VirtualChassis(
            name="Example Name", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        config=DeviceConfig(
            startup=b"example data",
            running=b"example data",
            candidate=b"example data",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
