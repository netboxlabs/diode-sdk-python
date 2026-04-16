"""
Circuit entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Circuit entities:
- circuit_minimal: Required fields only
- circuit_extended: Common optional fields
- circuit_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Circuit,
    CircuitType,
    Entity,
    Owner,
    OwnerGroup,
    Provider,
    ProviderAccount,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "circuit-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Circuit entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        circuit = circuit_minimal()
        # circuit = circuit_extended()
        # circuit = circuit_explicit()

        response = client.ingest(entities=[Entity(circuit=circuit)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Circuit ingested successfully")


def circuit_minimal() -> Circuit:
    """Create a Circuit with only required fields using flat strings."""
    return Circuit(
        cid="CID-001",
        provider="Example Provider",  # flat string -> Provider
        type="Example Type",  # flat string -> CircuitType
        metadata={"source": "example"},
    )


def circuit_extended() -> Circuit:
    """Create a Circuit with common optional fields."""
    return Circuit(
        cid="CID-001",
        provider="Example Provider",
        type="Example Type",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        tenant="Example Tenant",
        commit_rate=1,
        distance=1.0,
        distance_unit="ft",
        comments="Example comments",
    )


def circuit_explicit() -> Circuit:
    """Create a Circuit with fully nested objects and all common fields."""
    return Circuit(
        cid="CID-001",
        provider=Provider(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        type=CircuitType(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
            metadata={"source": "example"},
        ),
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        commit_rate=1,
        distance=1.0,
        distance_unit="ft",
        provider_account=ProviderAccount(
            provider=Provider(
                name="Example Name", slug="example-slug", metadata={"source": "example"}
            ),
            account="Example Account",
            metadata={"source": "example"},
        ),
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
