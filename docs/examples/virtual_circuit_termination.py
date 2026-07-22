"""
VirtualCircuitTermination entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualCircuitTermination entities:
- virtual_circuit_termination_minimal: Required fields only
- virtual_circuit_termination_extended: Common optional fields
- virtual_circuit_termination_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    Interface,
    Manufacturer,
    Provider,
    ProviderNetwork,
    Site,
    Tag,
    VirtualCircuit,
    VirtualCircuitTermination,
    VirtualCircuitType,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_circuit_termination-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VirtualCircuitTermination entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        virtual_circuit_termination = virtual_circuit_termination_minimal()
        # virtual_circuit_termination = virtual_circuit_termination_extended()
        # virtual_circuit_termination = virtual_circuit_termination_explicit()

        response = client.ingest(
            entities=[Entity(virtual_circuit_termination=virtual_circuit_termination)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualCircuitTermination ingested successfully")


def virtual_circuit_termination_minimal() -> VirtualCircuitTermination:
    """Create a VirtualCircuitTermination with only required fields using flat strings."""
    return VirtualCircuitTermination(
        virtual_circuit="Example Virtual Circuit",  # flat string -> VirtualCircuit
        interface="Example Interface",  # flat string -> Interface
        metadata={"source": "example"},
    )


def virtual_circuit_termination_extended() -> VirtualCircuitTermination:
    """Create a VirtualCircuitTermination with common optional fields."""
    return VirtualCircuitTermination(
        virtual_circuit="Example Virtual Circuit",
        interface="Example Interface",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        role="hub",
    )


def virtual_circuit_termination_explicit() -> VirtualCircuitTermination:
    """Create a VirtualCircuitTermination with fully nested objects and all common fields."""
    return VirtualCircuitTermination(
        virtual_circuit=VirtualCircuit(
            cid="CID-001",
            provider_network=ProviderNetwork(
                provider=Provider(
                    name="Example Name",
                    slug="example-slug",
                    metadata={"source": "example"},
                ),
                name="Example Name",
                metadata={"source": "example"},
            ),
            type=VirtualCircuitType(
                name="Example Name",
                slug="example-slug",
                color="0000ff",
                metadata={"source": "example"},
            ),
            status="active",
            metadata={"source": "example"},
        ),
        interface=Interface(
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
            type="1000base-t",
            metadata={"source": "example"},
        ),
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        role="hub",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
