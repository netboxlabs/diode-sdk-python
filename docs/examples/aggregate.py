"""
Aggregate entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Aggregate entities:
- aggregate_minimal: Required fields only
- aggregate_extended: Common optional fields
- aggregate_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Aggregate,
    RIR,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "aggregate-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an Aggregate entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = aggregate_minimal()
        # entity = aggregate_extended()
        # entity = aggregate_explicit()

        response = client.ingest(entities=[Entity(aggregate=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Aggregate ingested successfully")


def aggregate_minimal() -> Aggregate:
    """Create an Aggregate with only required fields using flat strings."""
    return Aggregate(
        prefix="192.0.2.0/24",
        rir="example-rir",  # flat string -> RIR
        metadata={"source": "example"},
    )


def aggregate_extended() -> Aggregate:
    """Create an Aggregate with common optional fields."""
    return Aggregate(
        prefix="192.0.2.0/24",
        rir="example-rir",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def aggregate_explicit() -> Aggregate:
    """Create an Aggregate with fully nested objects and all common fields."""
    return Aggregate(
        prefix="192.0.2.0/24",
        rir=RIR(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
