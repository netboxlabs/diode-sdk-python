"""
Interface entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Interface entities:
- interface_example_minimal: Required fields only
- interface_example_extended: Common optional fields
- interface_example_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Interface,
    MACAddress,
    Manufacturer,
    Module,
    ModuleBay,
    ModuleType,
    Owner,
    OwnerGroup,
    Site,
    Tag,
    VLAN,
    VLANTranslationPolicy,
    VRF,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "interface-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Interface entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        interface = interface_example_minimal()
        # interface = interface_example_extended()
        # interface = interface_example_explicit()

        response = client.ingest(entities=[Entity(interface=interface)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Interface ingested successfully")


def interface_example_minimal() -> Interface:
    """Create a Interface with only required fields using flat strings."""
    return Interface(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        type="1.6tbase-cr8",
        metadata={"source": "example"},
    )


def interface_example_extended() -> Interface:
    """Create a Interface with common optional fields."""
    return Interface(
        device="Example Device",
        name="Example Name",
        type="1.6tbase-cr8",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        label="Example Label",
        enabled=True,
        mtu=1,
        speed=1,
        duplex="auto",
        wwn="Example Wwn",
        mgmt_only=True,
        mode="access",
        rf_role="ap",
        rf_channel="2.4g-1-2412-22",
        poe_mode="pd",
        poe_type="passive-24v-2pair",
        rf_channel_frequency=1.0,
        rf_channel_width=1.0,
        tx_power=1,
        mark_connected=True,
    )


def interface_example_explicit() -> Interface:
    """Create a Interface with fully nested objects and all common fields."""
    return Interface(
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
        type="1.6tbase-cr8",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        label="Example Label",
        enabled=True,
        mtu=1,
        speed=1,
        duplex="auto",
        wwn="Example Wwn",
        mgmt_only=True,
        mode="access",
        rf_role="ap",
        rf_channel="2.4g-1-2412-22",
        poe_mode="pd",
        poe_type="passive-24v-2pair",
        rf_channel_frequency=1.0,
        rf_channel_width=1.0,
        tx_power=1,
        mark_connected=True,
        module=Module(
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
            module_bay=ModuleBay(
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
                metadata={"source": "example"},
            ),
            module_type=ModuleType(
                manufacturer=Manufacturer(
                    name="Example Name",
                    slug="example-slug",
                    metadata={"source": "example"},
                ),
                model="Model X",
                metadata={"source": "example"},
            ),
            status="active",
            metadata={"source": "example"},
        ),
        parent=Interface(
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
            type="Example Type",
            metadata={"source": "example"},
        ),
        bridge=Interface(
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
            type="Example Type",
            metadata={"source": "example"},
        ),
        lag=Interface(
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
            type="Example Type",
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
