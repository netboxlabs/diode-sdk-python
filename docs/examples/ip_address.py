"""
IPAddress entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPAddress entities:
- ip_address_minimal: Required fields only
- ip_address_extended: Common optional fields
- ip_address_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    FHRPGroup,
    IPAddress,
    Interface,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
    Tenant,
    VMInterface,
    VRF,
    VirtualMachine,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "ip_address-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a IPAddress entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        ip_address = ip_address_minimal()
        # ip_address = ip_address_extended()
        # ip_address = ip_address_explicit()

        response = client.ingest(entities=[Entity(ip_address=ip_address)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPAddress ingested successfully")


def ip_address_minimal() -> IPAddress:
    """Create a IPAddress with only required fields using flat strings."""
    return IPAddress(
        address="192.0.2.1/32",
        metadata={"source": "example"},
    )


def ip_address_extended() -> IPAddress:
    """Create a IPAddress with common optional fields."""
    return IPAddress(
        address="192.0.2.1/32",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        tenant="Example Tenant",
        role="anycast",
        dns_name="example.host.local",
        comments="Example comments",
    )


def ip_address_explicit() -> IPAddress:
    """Create a IPAddress with fully nested objects and all common fields."""
    return IPAddress(
        address="192.0.2.1/32",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        role="anycast",
        dns_name="example.host.local",
        vrf=VRF(name="Example Name", metadata={"source": "example"}),
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        nat_inside=IPAddress(
            address="192.0.2.1/32", status="active", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        # Polymorphic 'assigned_object' — choose ONE of these mutually exclusive variants:
        assigned_object_interface=Interface(
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
            name="Example Name",
            type="1000base-t",
            metadata={"source": "example"},
        ),
        # assigned_object_vm_interface=VMInterface(virtual_machine=VirtualMachine(name="Example Name", status="active", metadata={"source": "example"}), name="Example Name", metadata={"source": "example"}),
        # assigned_object_fhrp_group=FHRPGroup(protocol="carp", group_id=1, metadata={"source": "example"}),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
