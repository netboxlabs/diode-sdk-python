"""
Prefix entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Prefix entities:
- prefix_minimal: Required fields only
- prefix_extended: Common optional fields
- prefix_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Prefix,
    Role,
    Tag,
    Tenant,
    VLAN,
    VRF,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "prefix-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Prefix entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        prefix = prefix_minimal()
        # prefix = prefix_extended()
        # prefix = prefix_explicit()

        response = client.ingest(entities=[Entity(prefix=prefix)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Prefix ingested successfully")


def prefix_minimal() -> Prefix:
    """Create a Prefix with only required fields using flat strings."""
    return Prefix(
        prefix="192.0.2.0/24",
        metadata={"source": "example"},
    )


def prefix_extended() -> Prefix:
    """Create a Prefix with common optional fields."""
    return Prefix(
        prefix="192.0.2.0/24",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        tenant="Example Tenant",
        role="Example Role",
        is_pool=True,
        mark_utilized=True,
        comments="Example comments",
    )


def prefix_explicit() -> Prefix:
    """Create a Prefix with fully nested objects and all common fields."""
    return Prefix(
        prefix="192.0.2.0/24",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        is_pool=True,
        mark_utilized=True,
        vrf=VRF(name="Example Name", metadata={"source": "example"}),
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        vlan=VLAN(
            vid=1, name="Example Name", status="active", metadata={"source": "example"}
        ),
        role=Role(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
