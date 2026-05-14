"""
Module entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Module entities:
- module_minimal: Required fields only
- module_extended: Common optional fields
- module_explicit: Fully nested objects with all fields
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
APP_NAME = "module-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Module entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        module = module_minimal()
        # module = module_extended()
        # module = module_explicit()

        response = client.ingest(entities=[Entity(module=module)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Module ingested successfully")


def module_minimal() -> Module:
    """Create a Module with only required fields using flat strings."""
    return Module(
        device="Example Device",  # flat string -> Device
        module_bay="Example Module Bay",  # flat string -> ModuleBay
        module_type="Example Module Type",  # flat string -> ModuleType
        metadata={"source": "example"},
    )


def module_extended() -> Module:
    """Create a Module with common optional fields."""
    return Module(
        device="Example Device",
        module_bay="Example Module Bay",
        module_type="Example Module Type",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        serial="SN-001234",
        description="Example description",
        asset_tag="ASSET-001",
        comments="Example comments",
        replicate_components=True,
        adopt_components=True,
    )


def module_explicit() -> Module:
    """Create a Module with fully nested objects and all common fields."""
    return Module(
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
                name="Example Name", slug="example-slug", metadata={"source": "example"}
            ),
            model="Model X",
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
        replicate_components=True,
        adopt_components=True,
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
