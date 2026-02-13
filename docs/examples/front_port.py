"""
FrontPort entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting FrontPort entities:
- front_port_minimal: Required fields only
- front_port_extended: Common optional fields
- front_port_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    FrontPort,
    Manufacturer,
    RearPort,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "front_port-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a FrontPort entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        front_port = front_port_minimal()
        # front_port = front_port_extended()
        # front_port = front_port_explicit()

        response = client.ingest(entities=[Entity(front_port=front_port)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("FrontPort ingested successfully")


def front_port_minimal() -> FrontPort:
    """Create a FrontPort with only required fields using flat strings."""
    return FrontPort(
        device="Example Device",  # flat string -> Device
        name="Example Name",
        type="110-punch",
        rear_port="Example Rear Port",  # flat string -> RearPort
        metadata={"source": "example"},
    )


def front_port_extended() -> FrontPort:
    """Create a FrontPort with common optional fields."""
    return FrontPort(
        device="Example Device",
        name="Example Name",
        type="110-punch",
        rear_port="Example Rear Port",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
    )


def front_port_explicit() -> FrontPort:
    """Create a FrontPort with fully nested objects and all common fields."""
    return FrontPort(
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
        rear_port=RearPort(
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
            color="0000ff",
            metadata={"source": "example"},
        ),
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
