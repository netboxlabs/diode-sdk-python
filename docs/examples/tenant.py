"""
Tenant entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Tenant entities:
- tenant_minimal: Required fields only
- tenant_extended: Common optional fields
- tenant_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    Tag,
    Tenant,
    TenantGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "tenant-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Tenant entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        tenant = tenant_minimal()
        # tenant = tenant_extended()
        # tenant = tenant_explicit()

        response = client.ingest(entities=[Entity(tenant=tenant)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Tenant ingested successfully")


def tenant_minimal() -> Tenant:
    """Create a Tenant with only required fields using flat strings."""
    return Tenant(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def tenant_extended() -> Tenant:
    """Create a Tenant with common optional fields."""
    return Tenant(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        comments="Example comments",
    )


def tenant_explicit() -> Tenant:
    """Create a Tenant with fully nested objects and all common fields."""
    return Tenant(
        name="Example Name",
        slug="example-slug",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        group=TenantGroup(
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
