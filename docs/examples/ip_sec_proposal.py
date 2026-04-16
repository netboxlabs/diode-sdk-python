"""
IPSecProposal entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPSecProposal entities:
- ip_sec_proposal_minimal: Required fields only
- ip_sec_proposal_extended: Common optional fields
- ip_sec_proposal_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IPSecProposal,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "ip_sec_proposal-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a IPSecProposal entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        ip_sec_proposal = ip_sec_proposal_minimal()
        # ip_sec_proposal = ip_sec_proposal_extended()
        # ip_sec_proposal = ip_sec_proposal_explicit()

        response = client.ingest(entities=[Entity(ip_sec_proposal=ip_sec_proposal)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPSecProposal ingested successfully")


def ip_sec_proposal_minimal() -> IPSecProposal:
    """Create a IPSecProposal with only required fields using flat strings."""
    return IPSecProposal(
        name="Example Name",
        metadata={"source": "example"},
    )


def ip_sec_proposal_extended() -> IPSecProposal:
    """Create a IPSecProposal with common optional fields."""
    return IPSecProposal(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        encryption_algorithm="3des-cbc",
        authentication_algorithm="hmac-md5",
        sa_lifetime_seconds=1,
        sa_lifetime_data=1,
        comments="Example comments",
    )


def ip_sec_proposal_explicit() -> IPSecProposal:
    """Create a IPSecProposal with fully nested objects and all common fields."""
    return IPSecProposal(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        encryption_algorithm="3des-cbc",
        authentication_algorithm="hmac-md5",
        sa_lifetime_seconds=1,
        sa_lifetime_data=1,
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
