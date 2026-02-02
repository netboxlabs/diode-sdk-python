"""
RIR entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RIR entities:
- rir_minimal: Required fields only
- rir_extended: Common optional fields
- rir_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    RIR,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rir-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a RIR entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        rir = rir_minimal()
        # rir = rir_extended()
        # rir = rir_explicit()

        response = client.ingest(entities=[Entity(rir=rir)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RIR ingested successfully")


def rir_minimal() -> RIR:
    """Create a RIR with only required fields using flat strings."""
    return RIR(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def rir_extended() -> RIR:
    """Create a RIR with common optional fields."""
    return RIR(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def rir_explicit() -> RIR:
    """Create a RIR with fully nested objects and all common fields."""
    return RIR(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
