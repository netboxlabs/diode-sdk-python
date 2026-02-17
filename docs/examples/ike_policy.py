"""
IKEPolicy entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IKEPolicy entities:
- ike_policy_minimal: Required fields only
- ike_policy_extended: Common optional fields
- ike_policy_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IKEPolicy,
    Owner,
    OwnerGroup,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "ike_policy-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a IKEPolicy entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        ike_policy = ike_policy_minimal()
        # ike_policy = ike_policy_extended()
        # ike_policy = ike_policy_explicit()

        response = client.ingest(entities=[Entity(ike_policy=ike_policy)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IKEPolicy ingested successfully")


def ike_policy_minimal() -> IKEPolicy:
    """Create a IKEPolicy with only required fields using flat strings."""
    return IKEPolicy(
        name="Example Name",
        version=1,
        metadata={"source": "example"},
    )


def ike_policy_extended() -> IKEPolicy:
    """Create a IKEPolicy with common optional fields."""
    return IKEPolicy(
        name="Example Name",
        version=1,
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        mode="aggressive",
        preshared_key="Example Preshared Key",
        comments="Example comments",
    )


def ike_policy_explicit() -> IKEPolicy:
    """Create a IKEPolicy with fully nested objects and all common fields."""
    return IKEPolicy(
        name="Example Name",
        version=1,
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        mode="aggressive",
        preshared_key="Example Preshared Key",
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
