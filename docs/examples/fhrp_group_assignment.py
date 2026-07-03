"""
FHRPGroupAssignment entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting FHRPGroupAssignment entities:
- fhrp_group_assignment_minimal: Required fields only
- fhrp_group_assignment_extended: Common optional fields
- fhrp_group_assignment_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    FHRPGroup,
    FHRPGroupAssignment,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "fhrp_group_assignment-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a FHRPGroupAssignment entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        fhrp_group_assignment = fhrp_group_assignment_minimal()
        # fhrp_group_assignment = fhrp_group_assignment_extended()
        # fhrp_group_assignment = fhrp_group_assignment_explicit()

        response = client.ingest(
            entities=[Entity(fhrp_group_assignment=fhrp_group_assignment)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("FHRPGroupAssignment ingested successfully")


def fhrp_group_assignment_minimal() -> FHRPGroupAssignment:
    """Create a FHRPGroupAssignment with only required fields using flat strings."""
    return FHRPGroupAssignment(
        group="Example Group",  # flat string -> FHRPGroup
        priority=1,
        metadata={"source": "example"},
    )


def fhrp_group_assignment_extended() -> FHRPGroupAssignment:
    """Create a FHRPGroupAssignment with common optional fields."""
    return FHRPGroupAssignment(
        group="Example Group",
        priority=1,
        metadata={"source": "example", "custom_key": "custom_value"},
    )


def fhrp_group_assignment_explicit() -> FHRPGroupAssignment:
    """Create a FHRPGroupAssignment with fully nested objects and all common fields."""
    return FHRPGroupAssignment(
        group=FHRPGroup(protocol="carp", group_id=1, metadata={"source": "example"}),
        priority=1,
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
    )


if __name__ == "__main__":
    main()
