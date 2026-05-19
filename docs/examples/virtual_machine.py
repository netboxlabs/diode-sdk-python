"""
VirtualMachine entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualMachine entities:
- virtual_machine_minimal: Required fields only
- virtual_machine_extended: Common optional fields
- virtual_machine_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cluster,
    ClusterType,
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    IPAddress,
    Manufacturer,
    Owner,
    OwnerGroup,
    Platform,
    Site,
    Tag,
    Tenant,
    VirtualMachine,
    VirtualMachineType,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_machine-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VirtualMachine entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        virtual_machine = virtual_machine_minimal()
        # virtual_machine = virtual_machine_extended()
        # virtual_machine = virtual_machine_explicit()

        response = client.ingest(entities=[Entity(virtual_machine=virtual_machine)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualMachine ingested successfully")


def virtual_machine_minimal() -> VirtualMachine:
    """Create a VirtualMachine with only required fields using flat strings."""
    return VirtualMachine(
        name="Example Name",
        metadata={"source": "example"},
    )


def virtual_machine_extended() -> VirtualMachine:
    """Create a VirtualMachine with common optional fields."""
    return VirtualMachine(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        serial="SN-001234",
        description="Example description",
        site="Example Site",
        cluster="Example Cluster",
        device="Example Device",
        role="Example Role",
        tenant="Example Tenant",
        platform="Example Platform",
        vcpus=1.0,
        memory=1,
        disk=1,
        comments="Example comments",
        start_on_boot="laststate",
    )


def virtual_machine_explicit() -> VirtualMachine:
    """Create a VirtualMachine with fully nested objects and all common fields."""
    return VirtualMachine(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        serial="SN-001234",
        description="Example description",
        comments="Example comments",
        vcpus=1.0,
        memory=1,
        disk=1,
        start_on_boot="laststate",
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        cluster=Cluster(
            name="Example Name",
            type=ClusterType(
                name="Example Name", slug="example-slug", metadata={"source": "example"}
            ),
            status="active",
            metadata={"source": "example"},
        ),
        device=Device(
            device_type=DeviceType(
                manufacturer=Manufacturer(
                    name="Example Name",
                    slug="example-slug",
                    metadata={"source": "example"},
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
            status="active",
            metadata={"source": "example"},
        ),
        role=DeviceRole(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
            metadata={"source": "example"},
        ),
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        platform=Platform(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        primary_ip4=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        primary_ip6=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        virtual_machine_type=VirtualMachineType(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
