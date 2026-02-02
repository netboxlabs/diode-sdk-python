"""
ConsolePort entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ConsolePort entities:
- console_port_minimal: Required fields only
- console_port_extended: Common optional fields
- console_port_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ConsolePort,
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "console_port-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ConsolePort entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        console_port = console_port_minimal()
        # console_port = console_port_extended()
        # console_port = console_port_explicit()

        response = client.ingest(entities=[Entity(console_port=console_port)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ConsolePort ingested successfully")


def console_port_minimal() -> ConsolePort:
    """Create a ConsolePort with only required fields using flat strings."""
    return ConsolePort(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def console_port_extended() -> ConsolePort:
    """Create a ConsolePort with common optional fields."""
    return ConsolePort(
        device="Example Device",
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def console_port_explicit() -> ConsolePort:
    """Create a ConsolePort with fully nested objects and all common fields."""
    return ConsolePort(
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
        description="Example description",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
