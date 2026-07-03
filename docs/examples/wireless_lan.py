"""
WirelessLAN entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting WirelessLAN entities:
- wireless_lan_minimal: Required fields only
- wireless_lan_extended: Common optional fields
- wireless_lan_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Location,
    Owner,
    OwnerGroup,
    Region,
    Site,
    SiteGroup,
    Tag,
    Tenant,
    VLAN,
    WirelessLAN,
    WirelessLANGroup,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "wireless_lan-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a WirelessLAN entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        wireless_lan = wireless_lan_minimal()
        # wireless_lan = wireless_lan_extended()
        # wireless_lan = wireless_lan_explicit()

        response = client.ingest(entities=[Entity(wireless_lan=wireless_lan)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("WirelessLAN ingested successfully")


def wireless_lan_minimal() -> WirelessLAN:
    """Create a WirelessLAN with only required fields using flat strings."""
    return WirelessLAN(
        ssid="ExampleSSID",
        metadata={"source": "example"},
    )


def wireless_lan_extended() -> WirelessLAN:
    """Create a WirelessLAN with common optional fields."""
    return WirelessLAN(
        ssid="ExampleSSID",
        metadata={"source": "example", "custom_key": "custom_value"},
        status="active",
        description="Example description",
        tenant="Example Tenant",
        auth_type="open",
        auth_cipher="aes",
        auth_psk="Example Auth Psk",
        comments="Example comments",
    )


def wireless_lan_explicit() -> WirelessLAN:
    """Create a WirelessLAN with fully nested objects and all common fields."""
    return WirelessLAN(
        ssid="ExampleSSID",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        status="active",
        description="Example description",
        comments="Example comments",
        auth_type="open",
        auth_cipher="aes",
        auth_psk="Example Auth Psk",
        group=WirelessLANGroup(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        vlan=VLAN(
            vid=1, name="Example Name", status="active", metadata={"source": "example"}
        ),
        tenant=Tenant(
            name="Example Name", slug="example-slug", metadata={"source": "example"}
        ),
        owner=Owner(
            name="Example Name",
            group=OwnerGroup(name="Example Name", metadata={"source": "example"}),
            metadata={"source": "example"},
        ),
        # Polymorphic 'scope' — choose ONE of these mutually exclusive variants:
        scope_site=Site(
            name="Example Name",
            slug="example-slug",
            status="active",
            metadata={"source": "example"},
        ),
        # scope_location=Location(name="Example Name", slug="example-slug", site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}),
        # scope_region=Region(name="Example Name", slug="example-slug", metadata={"source": "example"}),
        # scope_site_group=SiteGroup(name="Example Name", slug="example-slug", metadata={"source": "example"}),
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
