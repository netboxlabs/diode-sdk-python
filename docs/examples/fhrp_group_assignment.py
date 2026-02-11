"""
FHRPGroupAssignment entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting FHRPGroupAssignment entities:
- fhrp_group_assignment_minimal: Required fields only
- fhrp_group_assignment_extended: Common optional fields
- fhrp_group_assignment_explicit: Fully nested objects with all fields
"""

import os

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    FHRPGroup,
    FHRPGroupAssignment,
)

TARGET = os.getenv("DIODE_TARGET", "grpc://localhost:8080/diode")
APP_NAME = "fhrp_group_assignment-example"
APP_VERSION = "1.0.0"
CLIENT_ID = os.getenv("DIODE_CLIENT_ID", "diode")
CLIENT_SECRET = os.getenv("DIODE_CLIENT_SECRET", "changeme")


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
        entity = fhrp_group_assignment_minimal()
        # entity = fhrp_group_assignment_extended()
        # entity = fhrp_group_assignment_explicit()

        response = client.ingest(entities=[Entity(fhrp_group_assignment=entity)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("FHRPGroupAssignment ingested successfully")


def fhrp_group_assignment_minimal() -> FHRPGroupAssignment:
    """Create a FHRPGroupAssignment with only required fields using flat strings."""
    return FHRPGroupAssignment(
        group="example-group",  # flat string -> FHRPGroup
        priority=1,
        metadata={"source": "example"},
    )


def fhrp_group_assignment_extended() -> FHRPGroupAssignment:
    """Create a FHRPGroupAssignment with common optional fields."""
    return FHRPGroupAssignment(
        group="example-group",
        priority=1,
        metadata={"source": "example"},
    )


def fhrp_group_assignment_explicit() -> FHRPGroupAssignment:
    """Create a FHRPGroupAssignment with fully nested objects and all common fields."""
    return FHRPGroupAssignment(
        group=FHRPGroup(
            protocol="carp",
            group_id=1,
            description="Example description",
            comments="Example comments",
            metadata={"source": "example"},
        ),
        priority=1,
        metadata={"source": "example"},
    )


if __name__ == "__main__":
    main()
