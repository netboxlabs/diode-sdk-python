"""
VirtualCircuit entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting VirtualCircuit entities:
- virtual_circuit_minimal: Required fields only
- virtual_circuit_extended: Common optional fields
- virtual_circuit_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Provider,
    ProviderNetwork,
    Tag,
    Tenant,
    VirtualCircuit,
    VirtualCircuitType,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "virtual_circuit-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a VirtualCircuit entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        virtual_circuit = virtual_circuit_minimal()
        # virtual_circuit = virtual_circuit_extended()
        # virtual_circuit = virtual_circuit_explicit()

        response = client.ingest(entities=[Entity(virtual_circuit=virtual_circuit)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("VirtualCircuit ingested successfully")


def virtual_circuit_minimal() -> VirtualCircuit:
    """Create a VirtualCircuit with only required fields using flat strings."""
    return VirtualCircuit(
        cid="CID-001",
        provider_network="Example Provider Network",  # flat string -> ProviderNetwork
        type="Example Type",  # flat string -> VirtualCircuitType
        metadata={"source": "example"},
    )


def virtual_circuit_extended() -> VirtualCircuit:
    """Create a VirtualCircuit with common optional fields."""
    return VirtualCircuit(
        cid="CID-001",
        provider_network="Example Provider Network",
        type="Example Type",
        metadata={"source": "example"},
        status="active",
        description="Example description",
    )


def virtual_circuit_explicit() -> VirtualCircuit:
    """Create a VirtualCircuit with fully nested objects and all common fields."""
    return VirtualCircuit(
        cid="CID-001",
        provider_network=ProviderNetwork(
            provider=Provider(
                name="Example Name", slug="example-slug", metadata={"source": "example"}
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
        metadata={"source": "example"},
        status="active",
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
