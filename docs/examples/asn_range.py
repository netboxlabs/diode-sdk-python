"""
ASNRange entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ASNRange entities:
- asn_range_minimal: Required fields only
- asn_range_extended: Common optional fields
- asn_range_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ASNRange,
    Entity,
    RIR,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "asn_range-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ASNRange entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        asn_range = asn_range_minimal()
        # asn_range = asn_range_extended()
        # asn_range = asn_range_explicit()

        response = client.ingest(entities=[Entity(asn_range=asn_range)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ASNRange ingested successfully")


def asn_range_minimal() -> ASNRange:
    """Create a ASNRange with only required fields using flat strings."""
    return ASNRange(
        name="Example Name",
        slug="example-slug",
        rir="Example RIR",  # flat string -> RIR
        start=1,
        end=1,
        metadata={"source": "example"},
    )


def asn_range_extended() -> ASNRange:
    """Create a ASNRange with common optional fields."""
    return ASNRange(
        name="Example Name",
        slug="example-slug",
        rir="Example RIR",
        start=1,
        end=1,
        metadata={"source": "example"},
        description="Example description",
    )


def asn_range_explicit() -> ASNRange:
    """Create a ASNRange with fully nested objects and all common fields."""
    return ASNRange(
        name="Example Name",
        slug="example-slug",
        rir=RIR(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        start=1,
        end=1,
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
