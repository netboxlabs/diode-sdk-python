"""
WirelessLink entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting WirelessLink entities:
- wireless_link_minimal: Required fields only
- wireless_link_extended: Common optional fields
- wireless_link_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Device,
    DeviceRole,
    DeviceType,
    Interface,
    Manufacturer,
    Site,
    Tag,
    Tenant,
    WirelessLink,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "wireless_link-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting a WirelessLink entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = wireless_link_minimal()
        # entity = wireless_link_extended()
        # entity = wireless_link_explicit()

        response = client.ingest(entities=[Entity(wireless_link=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("WirelessLink ingested successfully")


def wireless_link_minimal() -> WirelessLink:
    """Create a WirelessLink with only required fields using flat strings."""
    return WirelessLink(
        interface_a="example-interface-a",  # flat string -> Interface
        interface_b="example-interface-b",  # flat string -> Interface
        metadata={"source": "example"},
    )


def wireless_link_extended() -> WirelessLink:
    """Create a WirelessLink with common optional fields."""
    return WirelessLink(
        interface_a="example-interface-a",
        interface_b="example-interface-b",
        status="connected",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def wireless_link_explicit() -> WirelessLink:
    """Create a WirelessLink with fully nested objects and all common fields."""
    return WirelessLink(
        interface_a=Interface(
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
            type="1000base-bx10-d",
            description="Example description",
            metadata={"source": "example"},
        ),
        interface_b=Interface(
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
            type="1000base-bx10-d",
            description="Example description",
            metadata={"source": "example"},
        ),
        status="connected",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
