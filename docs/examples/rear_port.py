"""
RearPort entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RearPort entities:
- rear_port_minimal: Required fields only
- rear_port_extended: Common optional fields
- rear_port_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    RearPort,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rear_port-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a RearPort entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        rear_port = rear_port_minimal()
        # rear_port = rear_port_extended()
        # rear_port = rear_port_explicit()

        response = client.ingest(entities=[Entity(rear_port=rear_port)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RearPort ingested successfully")


def rear_port_minimal() -> RearPort:
    """Create a RearPort with only required fields using flat strings."""
    return RearPort(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        type="110-punch",
        metadata={"source": "example"},
    )


def rear_port_extended() -> RearPort:
    """Create a RearPort with common optional fields."""
    return RearPort(
        device="Example Device",
        name="Example Name",
        type="110-punch",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
    )


def rear_port_explicit() -> RearPort:
    """Create a RearPort with fully nested objects and all common fields."""
    return RearPort(
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
        type="110-punch",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
