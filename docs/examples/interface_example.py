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
    Manufacturer,
    Site,
    Tag,
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
        type="1000base-bx10-d",
        metadata={"source": "example"},
    )


def interface_example_extended() -> Interface:
    """Create a Interface with common optional fields."""
    return Interface(
        device="Example Device",
        name="Example Name",
        type="1000base-bx10-d",
        metadata={"source": "example"},
        description="Example description",
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
        type="1000base-bx10-d",
        metadata={"source": "example"},
        description="Example description",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
