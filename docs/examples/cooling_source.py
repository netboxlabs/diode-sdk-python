"""
CoolingSource entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CoolingSource entities:
- cooling_source_minimal: Required fields only
- cooling_source_extended: Common optional fields
- cooling_source_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    CoolingSource,
    Entity,
    Location,
    Owner,
    OwnerGroup,
    Site,
    Tag,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cooling_source-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CoolingSource entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cooling_source = cooling_source_minimal()
        # cooling_source = cooling_source_extended()
        # cooling_source = cooling_source_explicit()

        response = client.ingest(entities=[Entity(cooling_source=cooling_source)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CoolingSource ingested successfully")


def cooling_source_minimal() -> CoolingSource:
    """Create a CoolingSource with only required fields using flat strings."""
    return CoolingSource(
        site="Example Site",  # flat string -> Site
        name="Example Name",
        type="chiller",
        metadata={"source": "example"},
    )


def cooling_source_extended() -> CoolingSource:
    """Create a CoolingSource with common optional fields."""
    return CoolingSource(
        site="Example Site",
        name="Example Name",
        type="chiller",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        location="Example Location",
        fluid_type="dielectric",
        cooling_capacity=1.0,
        comments="Example comments",
    )


def cooling_source_explicit() -> CoolingSource:
    """Create a CoolingSource with fully nested objects and all common fields."""
    return CoolingSource(
        site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        name="Example Name",
        type="chiller",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        fluid_type="dielectric",
        cooling_capacity=1.0,
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
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
