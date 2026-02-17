"""
Service entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Service entities:
- service_minimal: Required fields only
- service_extended: Common optional fields
- service_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Manufacturer,
    Owner,
    OwnerGroup,
    Service,
    Site,
    Tag,
    VirtualMachine,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "service-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Service entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        service = service_minimal()
        # service = service_extended()
        # service = service_explicit()

        response = client.ingest(entities=[Entity(service=service)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Service ingested successfully")


def service_minimal() -> Service:
    """Create a Service with only required fields using flat strings."""
    return Service(
        name="Example Name",
        metadata={"source": "example"},
    )


def service_extended() -> Service:
    """Create a Service with common optional fields."""
    return Service(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        device="Example Device",
        protocol="sctp",
        comments="Example comments",
    )


def service_explicit() -> Service:
    """Create a Service with fully nested objects and all common fields."""
    return Service(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        protocol="sctp",
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
        virtual_machine=VirtualMachine(
            name="Example Name", status="active", metadata={"source": "example"}
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
