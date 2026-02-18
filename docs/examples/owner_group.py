"""
OwnerGroup entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting OwnerGroup entities:
- owner_group_minimal: Required fields only
- owner_group_extended: Common optional fields
- owner_group_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "owner_group-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a OwnerGroup entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        owner_group = owner_group_minimal()
        # owner_group = owner_group_extended()
        # owner_group = owner_group_explicit()

        response = client.ingest(entities=[Entity(owner_group=owner_group)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("OwnerGroup ingested successfully")


def owner_group_minimal() -> OwnerGroup:
    """Create a OwnerGroup with only required fields using flat strings."""
    return OwnerGroup(
        name="Example Name",
        metadata={"source": "example"},
    )


def owner_group_extended() -> OwnerGroup:
    """Create a OwnerGroup with common optional fields."""
    return OwnerGroup(
        name="Example Name",
        metadata={"source": "example", "custom_key": "custom_value"},
        description="Example description",
    )


def owner_group_explicit() -> OwnerGroup:
    """Create a OwnerGroup with fully nested objects and all common fields."""
    return OwnerGroup(
        name="Example Name",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        description="Example description",
    )


if __name__ == "__main__":
    main()
