"""
IPSecPolicy entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPSecPolicy entities:
- ip_sec_policy_minimal: Required fields only
- ip_sec_policy_extended: Common optional fields
- ip_sec_policy_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IPSecPolicy,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "ip_sec_policy-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a IPSecPolicy entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        ip_sec_policy = ip_sec_policy_minimal()
        # ip_sec_policy = ip_sec_policy_extended()
        # ip_sec_policy = ip_sec_policy_explicit()

        response = client.ingest(entities=[Entity(ip_sec_policy=ip_sec_policy)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPSecPolicy ingested successfully")


def ip_sec_policy_minimal() -> IPSecPolicy:
    """Create a IPSecPolicy with only required fields using flat strings."""
    return IPSecPolicy(
        name="Example Name",
        metadata={"source": "example"},
    )


def ip_sec_policy_extended() -> IPSecPolicy:
    """Create a IPSecPolicy with common optional fields."""
    return IPSecPolicy(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        pfs_group=1,
        comments="Example comments",
    )


def ip_sec_policy_explicit() -> IPSecPolicy:
    """Create a IPSecPolicy with fully nested objects and all common fields."""
    return IPSecPolicy(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        pfs_group=1,
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
