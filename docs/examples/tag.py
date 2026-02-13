"""
Tag entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting Tag entities:
- tag_minimal: Required fields only
- tag_extended: Common optional fields
- tag_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "tag-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a Tag entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        tag = tag_minimal()
        # tag = tag_extended()
        # tag = tag_explicit()

        response = client.ingest(entities=[Entity(tag=tag)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("Tag ingested successfully")


def tag_minimal() -> Tag:
    """Create a Tag with only required fields using flat strings."""
    return Tag(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
    )


def tag_extended() -> Tag:
    """Create a Tag with common optional fields."""
    return Tag(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
    )


def tag_explicit() -> Tag:
    """Create a Tag with fully nested objects and all common fields."""
    return Tag(
        name="Example Name",
        slug="example-slug",
        metadata={"source": "example"},
        color="0000ff",
        description="Example description",
    )


if __name__ == "__main__":
    main()
