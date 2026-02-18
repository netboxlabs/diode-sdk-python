"""
WirelessLink entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting WirelessLink entities:
- wireless_link_minimal: Required fields only
- wireless_link_extended: Common optional fields
- wireless_link_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Interface,
    Manufacturer,
    Owner,
    OwnerGroup,
    Site,
    Tag,
    Tenant,
    WirelessLink,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "wireless_link-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


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
        wireless_link = wireless_link_minimal()
        # wireless_link = wireless_link_extended()
        # wireless_link = wireless_link_explicit()

        response = client.ingest(entities=[Entity(wireless_link=wireless_link)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("WirelessLink ingested successfully")


def wireless_link_minimal() -> WirelessLink:
    """Create a WirelessLink with only required fields using flat strings."""
    return WirelessLink(
        interface_a="Example Interface A",  # flat string -> Interface
        interface_b="Example Interface B",  # flat string -> Interface
        metadata={"source": "example"},
    )


def wireless_link_extended() -> WirelessLink:
    """Create a WirelessLink with common optional fields."""
    return WirelessLink(
        interface_a="Example Interface A",
        interface_b="Example Interface B",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="connected",
        description="Example description",
        ssid="ExampleSSID",
        tenant="Example Tenant",
        auth_type="open",
        auth_cipher="aes",
        auth_psk="Example Auth Psk",
        distance=1.0,
        distance_unit="ft",
        comments="Example comments",
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
        interface_b=Interface(
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
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="connected",
        description="Example description",
        comments="Example comments",
        ssid="ExampleSSID",
        auth_type="open",
        auth_cipher="aes",
        auth_psk="Example Auth Psk",
        distance=1.0,
        distance_unit="ft",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
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
