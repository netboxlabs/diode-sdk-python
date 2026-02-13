"""
ASN entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ASN entities:
- asn_minimal: Required fields only
- asn_extended: Common optional fields
- asn_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    ASN,
    Entity,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "asn-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ASN entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        asn = asn_minimal()
        # asn = asn_extended()
        # asn = asn_explicit()

        response = client.ingest(entities=[Entity(asn=asn)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ASN ingested successfully")


def asn_minimal() -> ASN:
    """Create a ASN with only required fields using flat strings."""
    return ASN(
        asn=64512,
        metadata={"source": "example"},
    )


def asn_extended() -> ASN:
    """Create a ASN with common optional fields."""
    return ASN(
        asn=64512,
        metadata={"source": "example"},
        description="Example description",
    )


def asn_explicit() -> ASN:
    """Create a ASN with fully nested objects and all common fields."""
    return ASN(
        asn=64512,
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
