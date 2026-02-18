"""
Aggregate entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Aggregate entities:
- aggregate_minimal: Required fields only
- aggregate_extended: Common optional fields
- aggregate_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Aggregate,
    Entity,
    Owner,
    OwnerGroup,
    RIR,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "aggregate-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Aggregate entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        aggregate = aggregate_minimal()
        # aggregate = aggregate_extended()
        # aggregate = aggregate_explicit()

        response = client.ingest(entities=[Entity(aggregate=aggregate)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Aggregate ingested successfully")


def aggregate_minimal() -> Aggregate:
    """Create a Aggregate with only required fields using flat strings."""
    return Aggregate(
        prefix="192.0.2.0/24",
        rir="Example RIR",  # flat string -> RIR
        metadata={"source": "example"},
    )


def aggregate_extended() -> Aggregate:
    """Create a Aggregate with common optional fields."""
    return Aggregate(
        prefix="192.0.2.0/24",
        rir="Example RIR",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        tenant="Example Tenant",
        comments="Example comments",
    )


def aggregate_explicit() -> Aggregate:
    """Create a Aggregate with fully nested objects and all common fields."""
    return Aggregate(
        prefix="192.0.2.0/24",
        rir=RIR(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
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
