"""
TenantGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting TenantGroup entities:
- tenant_group_minimal: Required fields only
- tenant_group_extended: Common optional fields
- tenant_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    TenantGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "tenant_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a TenantGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        tenant_group = tenant_group_minimal()
        # tenant_group = tenant_group_extended()
        # tenant_group = tenant_group_explicit()

        response = client.ingest(entities=[Entity(tenant_group=tenant_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("TenantGroup ingested successfully")


def tenant_group_minimal() -> TenantGroup:
    """Create a TenantGroup with only required fields using flat strings."""
    return TenantGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def tenant_group_extended() -> TenantGroup:
    """Create a TenantGroup with common optional fields."""
    return TenantGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
    )


def tenant_group_explicit() -> TenantGroup:
    """Create a TenantGroup with fully nested objects and all common fields."""
    return TenantGroup(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        description="Example description",
        comments="Example comments",
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
