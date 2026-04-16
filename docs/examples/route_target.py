"""
RouteTarget entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting RouteTarget entities:
- route_target_minimal: Required fields only
- route_target_extended: Common optional fields
- route_target_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Owner,
    OwnerGroup,
    RouteTarget,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "route_target-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a RouteTarget entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        route_target = route_target_minimal()
        # route_target = route_target_extended()
        # route_target = route_target_explicit()

        response = client.ingest(entities=[Entity(route_target=route_target)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("RouteTarget ingested successfully")


def route_target_minimal() -> RouteTarget:
    """Create a RouteTarget with only required fields using flat strings."""
    return RouteTarget(
        name="Example Name",
        metadata={"source": "example"},
    )


def route_target_extended() -> RouteTarget:
    """Create a RouteTarget with common optional fields."""
    return RouteTarget(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
        tenant="Example Tenant",
        comments="Example comments",
    )


def route_target_explicit() -> RouteTarget:
    """Create a RouteTarget with fully nested objects and all common fields."""
    return RouteTarget(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
        comments="Example comments",
        tenant=Tenant(
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
