"""
IKEProposal entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IKEProposal entities:
- ike_proposal_minimal: Required fields only
- ike_proposal_extended: Common optional fields
- ike_proposal_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IKEProposal,
    Tag,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "ike_proposal-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


def main():
    """Main execution - demonstrates ingesting an IKEProposal entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        entity = ike_proposal_minimal()
        # entity = ike_proposal_extended()
        # entity = ike_proposal_explicit()

        response = client.ingest(entities=[Entity(ike_proposal=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IKEProposal ingested successfully")


def ike_proposal_minimal() -> IKEProposal:
    """Create an IKEProposal with only required fields using flat strings."""
    return IKEProposal(
        name="Example Name",
        authentication_method="certificates",
        encryption_algorithm="3des-cbc",
        group=1,
        metadata={"source": "example"},
    )


def ike_proposal_extended() -> IKEProposal:
    """Create an IKEProposal with common optional fields."""
    return IKEProposal(
        name="Example Name",
        authentication_method="certificates",
        encryption_algorithm="3des-cbc",
        group=1,
        description="Example description",
        comments="Example comments",
        metadata={"source": "example"},
    )


def ike_proposal_explicit() -> IKEProposal:
    """Create an IKEProposal with fully nested objects and all common fields."""
    return IKEProposal(
        name="Example Name",
        authentication_method="certificates",
        encryption_algorithm="3des-cbc",
        group=1,
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
