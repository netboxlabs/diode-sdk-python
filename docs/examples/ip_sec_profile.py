"""
IPSecProfile entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting IPSecProfile entities:
- ip_sec_profile_minimal: Required fields only
- ip_sec_profile_extended: Common optional fields
- ip_sec_profile_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    IKEPolicy,
    IPSecPolicy,
    IPSecProfile,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "ip_sec_profile-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a IPSecProfile entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        ip_sec_profile = ip_sec_profile_minimal()
        # ip_sec_profile = ip_sec_profile_extended()
        # ip_sec_profile = ip_sec_profile_explicit()

        response = client.ingest(entities=[Entity(ip_sec_profile=ip_sec_profile)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("IPSecProfile ingested successfully")


def ip_sec_profile_minimal() -> IPSecProfile:
    """Create a IPSecProfile with only required fields using flat strings."""
    return IPSecProfile(
        name="Example Name",
        mode="ah",
        ike_policy="Example Ike Policy",  # flat string -> IKEPolicy
        ipsec_policy="Example Ipsec Policy",  # flat string -> IPSecPolicy
        metadata={"source": "example"},
    )


def ip_sec_profile_extended() -> IPSecProfile:
    """Create a IPSecProfile with common optional fields."""
    return IPSecProfile(
        name="Example Name",
        mode="ah",
        ike_policy="Example Ike Policy",
        ipsec_policy="Example Ipsec Policy",
        metadata={"source": "example"},
        description="Example description",
    )


def ip_sec_profile_explicit() -> IPSecProfile:
    """Create a IPSecProfile with fully nested objects and all common fields."""
    return IPSecProfile(
        name="Example Name",
        mode="ah",
        ike_policy=IKEPolicy(
            name="Example Name", version=1, metadata={"source": "example"}
        ),
        ipsec_policy=IPSecPolicy(name="Example Name", metadata={"source": "example"}),
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
