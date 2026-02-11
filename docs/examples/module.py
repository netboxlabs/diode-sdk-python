"""
Module entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Module entities:
- module_minimal: Required fields only
- module_extended: Common optional fields
- module_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    Manufacturer,
    Module,
    ModuleBay,
    ModuleType,
    Site,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "module-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = module_minimal()
        # entity = module_extended()
        # entity = module_explicit()

        response = client.ingest(entities=[Entity(module=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Module ingested successfully")


def module_minimal() -> Module:
    """Create a Module with only required fields using flat strings."""
    return Module(
        device="example-device",  # flat string -> Device
        module_bay="example-module-bay",  # flat string -> ModuleBay
        module_type="example-module-type",  # flat string -> ModuleType
        metadata={"source": "example"},
    )


def module_extended() -> Module:
    """Create a Module with common optional fields."""
    return Module(
        device="example-device",
        module_bay="example-module-bay",
        module_type="example-module-type",
        status="active",
        serial="SN-001234",
        asset_tag="ASSET-001",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def module_explicit() -> Module:
    """Create a Module with fully nested objects and all common fields."""
    return Module(
        device=Device(
            device_type=DeviceType(
                manufacturer=Manufacturer(
                    name="Example Name",
                    slug="example-slug",
                    description="Example description",
                    comments="Example comments",
                    metadata={"source": "example"},
                ),
                model="Model X",
                slug="example-slug",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            role=DeviceRole(
                name="Example Name",
                slug="example-slug",
                color="0000ff",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            serial="SN-001234",
            asset_tag="ASSET-001",
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            status="active",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        module_bay=ModuleBay(
            device=Device(
                device_type=DeviceType(
                    manufacturer=Manufacturer(
                        name="Example Name",
                        slug="example-slug",
                        description="Example description",
                        comments="Example comments",
                        metadata={"source": "example"},
                    ),
                    model="Model X",
                    slug="example-slug",
                    description="Example description",
                    comments="Example comments",
                    metadata={"source": "example"},
                ),
                role=DeviceRole(
                    name="Example Name",
                    slug="example-slug",
                    color="0000ff",
                    description="Example description",
                    comments="Example comments",
                    metadata={"source": "example"},
                ),
                serial="SN-001234",
                asset_tag="ASSET-001",
                site=Site(
                    name="Example Name",
                    slug="example-slug",
                    status="active",
                    description="Example description",
                    comments="Example comments",
                    metadata={"source": "example"},
                ),
                status="active",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            name="Example Name",
            label="Example label",
            description="Example description",
            metadata={"source": "example"},
        ),
        module_type=ModuleType(
            manufacturer=Manufacturer(
                name="Example Name",
                slug="example-slug",
                description="Example description",
                comments="Example comments",
                metadata={"source": "example"},
            ),
            model="Model X",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        status="active",
        serial="SN-001234",
        asset_tag="ASSET-001",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
