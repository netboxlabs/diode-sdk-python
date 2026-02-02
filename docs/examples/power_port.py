"""
PowerPort entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting PowerPort entities:
- power_port_minimal: Required fields only
- power_port_extended: Common optional fields
- power_port_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    PowerPort,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "power_port-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a PowerPort entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        power_port = power_port_minimal()
        # power_port = power_port_extended()
        # power_port = power_port_explicit()

        response = client.ingest(entities=[Entity(power_port=power_port)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("PowerPort ingested successfully")


def power_port_minimal() -> PowerPort:
    """Create a PowerPort with only required fields using flat strings."""
    return PowerPort(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        metadata={"source": "example"},
    )


def power_port_extended() -> PowerPort:
    """Create a PowerPort with common optional fields."""
    return PowerPort(
        device="Example Device",
        name="Example Name",
        metadata={"source": "example"},
        description="Example description",
    )


def power_port_explicit() -> PowerPort:
    """Create a PowerPort with fully nested objects and all common fields."""
    return PowerPort(
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
