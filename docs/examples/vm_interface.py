"""
VMInterface entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VMInterface entities:
- vm_interface_minimal: Required fields only
- vm_interface_extended: Common optional fields
- vm_interface_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    MACAddress,
    Owner,
    OwnerGroup,
    Tag,
    VLAN,
    VLANTranslationPolicy,
    VMInterface,
    VRF,
    VirtualMachine,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "vm_interface-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VMInterface entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        vm_interface = vm_interface_minimal()
        # vm_interface = vm_interface_extended()
        # vm_interface = vm_interface_explicit()

        response = client.ingest(entities=[Entity(vm_interface=vm_interface)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VMInterface ingested successfully")


def vm_interface_minimal() -> VMInterface:
    """Create a VMInterface with only required fields using flat strings."""
    return VMInterface(
        virtual_machine="Example Virtual Machine",  # flat string -> VirtualMachine
        name="Example Name",
        metadata={"source": "example"},
    )


def vm_interface_extended() -> VMInterface:
    """Create a VMInterface with common optional fields."""
    return VMInterface(
        virtual_machine="Example Virtual Machine",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        enabled=True,
        mtu=1,
        mode="access",
    )


def vm_interface_explicit() -> VMInterface:
    """Create a VMInterface with fully nested objects and all common fields."""
    return VMInterface(
        virtual_machine=VirtualMachine(
            name="Example Name", status="active", metadata={"source": "example"}
        ),
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        enabled=True,
        mtu=1,
        mode="access",
        parent=VMInterface(
            virtual_machine=VirtualMachine(
                name="Example Name", status="active", metadata={"source": "example"}
            ),
            name="Example Name",
            metadata={"source": "example"},
        ),
        bridge=VMInterface(
            virtual_machine=VirtualMachine(
                name="Example Name", status="active", metadata={"source": "example"}
            ),
            name="Example Name",
            metadata={"source": "example"},
        ),
        primary_mac_address=MACAddress(
            mac_address="00:11:22:33:44:55", metadata={"source": "example"}
        ),
        untagged_vlan=VLAN(
            vid=1, name="Example Name", status="active", metadata={"source": "example"}
        ),
        qinq_svlan=VLAN(
            vid=1, name="Example Name", status="active", metadata={"source": "example"}
        ),
        vlan_translation_policy=VLANTranslationPolicy(
            name="Example Name", metadata={"source": "example"}
        ),
        vrf=VRF(name="Example Name", metadata={"source": "example"}),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
