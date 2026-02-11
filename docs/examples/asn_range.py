"""
ASNRange entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ASNRange entities:
- asn_range_minimal: Required fields only
- asn_range_extended: Common optional fields
- asn_range_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ASNRange,
    RIR,
    Tag,
    Tenant,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "asn_range-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an ASNRange entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = asn_range_minimal()
        # entity = asn_range_extended()
        # entity = asn_range_explicit()

        response = client.ingest(entities=[Entity(asn_range=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ASNRange ingested successfully")


def asn_range_minimal() -> ASNRange:
    """Create an ASNRange with only required fields using flat strings."""
    return ASNRange(
        name="Example Name",
        slug="example-slug",
        rir="example-rir",  # flat string -> RIR
        start=1,
        end=1,
        metadata={"source": "example"},
    )


def asn_range_extended() -> ASNRange:
    """Create an ASNRange with common optional fields."""
    return ASNRange(
        name="Example Name",
        slug="example-slug",
        rir="example-rir",
        start=1,
        end=1,
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def asn_range_explicit() -> ASNRange:
    """Create an ASNRange with fully nested objects and all common fields."""
    return ASNRange(
        name="Example Name",
        slug="example-slug",
        rir=RIR(
            name="Example Name",
            slug="example-slug",
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        start=1,
        end=1,
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
