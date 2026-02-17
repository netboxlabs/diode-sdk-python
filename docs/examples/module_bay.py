"""
ModuleBay entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ModuleBay entities:
- module_bay_minimal: Required fields only
- module_bay_extended: Common optional fields
- module_bay_explicit: Fully nested objects with all fields
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
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "module_bay-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ModuleBay entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        module_bay = module_bay_minimal()
        # module_bay = module_bay_extended()
        # module_bay = module_bay_explicit()

        response = client.ingest(entities=[Entity(module_bay=module_bay)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ModuleBay ingested successfully")


def module_bay_minimal() -> ModuleBay:
    """Create a ModuleBay with only required fields using flat strings."""
    return ModuleBay(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def module_bay_extended() -> ModuleBay:
    """Create a ModuleBay with common optional fields."""
    return ModuleBay(
        device="Example Device",
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        label="Example Label",
        position="Example Position",
    )


def module_bay_explicit() -> ModuleBay:
    """Create a ModuleBay with fully nested objects and all common fields."""
    return ModuleBay(
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
        description="Example description",
        label="Example Label",
        position="Example Position",
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
        installed_module=Module(
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
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
