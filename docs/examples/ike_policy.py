"""
IKEPolicy entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IKEPolicy entities:
- ike_policy_minimal: Required fields only
- ike_policy_extended: Common optional fields
- ike_policy_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IKEPolicy,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "ike_policy-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an IKEPolicy entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = ike_policy_minimal()
        # entity = ike_policy_extended()
        # entity = ike_policy_explicit()

        response = client.ingest(entities=[Entity(ike_policy=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IKEPolicy ingested successfully")


def ike_policy_minimal() -> IKEPolicy:
    """Create an IKEPolicy with only required fields using flat strings."""
    return IKEPolicy(
        name="Example Name",
        version=1,
        metadata={"source": "example"},
    )


def ike_policy_extended() -> IKEPolicy:
    """Create an IKEPolicy with common optional fields."""
    return IKEPolicy(
        name="Example Name",
        version=1,
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def ike_policy_explicit() -> IKEPolicy:
    """Create an IKEPolicy with fully nested objects and all common fields."""
    return IKEPolicy(
        name="Example Name",
        version=1,
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
