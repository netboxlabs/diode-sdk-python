"""
IPSecPolicy entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPSecPolicy entities:
- ip_sec_policy_minimal: Required fields only
- ip_sec_policy_extended: Common optional fields
- ip_sec_policy_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IPSecPolicy,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "ip_sec_policy-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an IPSecPolicy entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = ip_sec_policy_minimal()
        # entity = ip_sec_policy_extended()
        # entity = ip_sec_policy_explicit()

        response = client.ingest(entities=[Entity(ip_sec_policy=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPSecPolicy ingested successfully")


def ip_sec_policy_minimal() -> IPSecPolicy:
    """Create an IPSecPolicy with only required fields using flat strings."""
    return IPSecPolicy(
        name="Example Name",
        metadata={"source": "example"},
    )


def ip_sec_policy_extended() -> IPSecPolicy:
    """Create an IPSecPolicy with common optional fields."""
    return IPSecPolicy(
        name="Example Name",
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def ip_sec_policy_explicit() -> IPSecPolicy:
    """Create an IPSecPolicy with fully nested objects and all common fields."""
    return IPSecPolicy(
        name="Example Name",
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
