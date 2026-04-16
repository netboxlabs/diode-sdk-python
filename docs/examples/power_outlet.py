"""
PowerOutlet entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting PowerOutlet entities:
- power_outlet_minimal: Required fields only
- power_outlet_extended: Common optional fields
- power_outlet_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    Module,
    ModuleBay,
    ModuleType,
    Owner,
    OwnerGroup,
    PowerOutlet,
    PowerPort,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "power_outlet-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a PowerOutlet entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        power_outlet = power_outlet_minimal()
        # power_outlet = power_outlet_extended()
        # power_outlet = power_outlet_explicit()

        response = client.ingest(entities=[Entity(power_outlet=power_outlet)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("PowerOutlet ingested successfully")


def power_outlet_minimal() -> PowerOutlet:
    """Create a PowerOutlet with only required fields using flat strings."""
    return PowerOutlet(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def power_outlet_extended() -> PowerOutlet:
    """Create a PowerOutlet with common optional fields."""
    return PowerOutlet(
        device="Example Device",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="disabled",
        description="Example description",
        color="0000ff",
        label="Example Label",
        type="CS6360C",
        feed_leg="A",
        mark_connected=True,
    )


def power_outlet_explicit() -> PowerOutlet:
    """Create a PowerOutlet with fully nested objects and all common fields."""
    return PowerOutlet(
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
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="disabled",
        description="Example description",
        color="0000ff",
        label="Example Label",
        type="CS6360C",
        feed_leg="A",
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
        power_port=PowerPort(
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
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
