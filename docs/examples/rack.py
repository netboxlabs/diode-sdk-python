"""
Rack entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Rack entities:
- rack_minimal: Required fields only
- rack_extended: Common optional fields
- rack_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Location,
    Manufacturer,
    Owner,
    OwnerGroup,
    Rack,
    RackGroup,
    RackRole,
    RackType,
    Site,
    Tag,
    Tenant,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "rack-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Rack entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        rack = rack_minimal()
        # rack = rack_extended()
        # rack = rack_explicit()

        response = client.ingest(entities=[Entity(rack=rack)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Rack ingested successfully")


def rack_minimal() -> Rack:
    """Create a Rack with only required fields using flat strings."""
    return Rack(
        name="Example Name",
        site="Example Site",  # flat string -> Site
        metadata={"source": "example"},
    )


def rack_extended() -> Rack:
    """Create a Rack with common optional fields."""
    return Rack(
        name="Example Name",
        site="Example Site",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        serial="SN-001234",
        description="Example description",
        facility_id="Example Facility Id",
        location="Example Location",
        tenant="Example Tenant",
        role="Example Role",
        asset_tag="ASSET-001",
        form_factor="2-post-frame",
        width=1,
        u_height=1,
        starting_unit=1,
        weight=1.0,
        max_weight=1,
        weight_unit="g",
        desc_units=True,
        outer_width=1,
        outer_depth=1,
        outer_unit="in",
        mounting_depth=1,
        airflow="front-to-rear",
        comments="Example comments",
        outer_height=1,
    )


def rack_explicit() -> Rack:
    """Create a Rack with fully nested objects and all common fields."""
    return Rack(
        name="Example Name",
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        serial="SN-001234",
        description="Example description",
        comments="Example comments",
        asset_tag="ASSET-001",
        facility_id="Example Facility Id",
        form_factor="2-post-frame",
        width=1,
        u_height=1,
        starting_unit=1,
        weight=1.0,
        max_weight=1,
        weight_unit="g",
        desc_units=True,
        outer_width=1,
        outer_depth=1,
        outer_unit="in",
        mounting_depth=1,
        airflow="front-to-rear",
        outer_height=1,
        location=Location(
            name="Example Name",
            slug="example-slug",
            site=Site(
                name="Example Name",
                slug="example-slug",
                status="active",
                metadata={"source": "example"},
            ),
            status="active",
            metadata={"source": "example"},
        ),
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        role=RackRole(
            name="Example Name",
            slug="example-slug",
            color="0000ff",
            metadata={"source": "example"},
        ),
        rack_type=RackType(
            manufacturer=Manufacturer(
                name="Example Name", slug="example-slug", metadata={"source": "example"}
            ),
            model="Model X",
            slug="example-slug",
            metadata={"source": "example"},
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        group=RackGroup(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
