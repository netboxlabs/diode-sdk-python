"""
TunnelTermination entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting TunnelTermination entities:
- tunnel_termination_minimal: Required fields only
- tunnel_termination_extended: Common optional fields
- tunnel_termination_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Tag,
    Tunnel,
    TunnelTermination,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "tunnel_termination-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a TunnelTermination entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        tunnel_termination = tunnel_termination_minimal()
        # tunnel_termination = tunnel_termination_extended()
        # tunnel_termination = tunnel_termination_explicit()

        response = client.ingest(
            entities=[Entity(tunnel_termination=tunnel_termination)]
        )
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("TunnelTermination ingested successfully")


def tunnel_termination_minimal() -> TunnelTermination:
    """Create a TunnelTermination with only required fields using flat strings."""
    return TunnelTermination(
        tunnel="Example Tunnel",  # flat string -> Tunnel
        role="hub",
        metadata={"source": "example"},
    )


def tunnel_termination_extended() -> TunnelTermination:
    """Create a TunnelTermination with common optional fields."""
    return TunnelTermination(
        tunnel="Example Tunnel",
        role="hub",
        metadata={"source": "example"},
    )


def tunnel_termination_explicit() -> TunnelTermination:
    """Create a TunnelTermination with fully nested objects and all common fields."""
    return TunnelTermination(
        tunnel=Tunnel(
            name="Example Name",
            status="active",
            encapsulation="Example Encapsulation",
            metadata={"source": "example"},
        ),
        role="hub",
        metadata={"source": "example"},
        tags=[Tag(name="production")],
    )


if __name__ == "__main__":
    main()
