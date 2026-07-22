"""
CableTermination entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting CableTermination entities:
- cable_termination_minimal: Required fields only
- cable_termination_extended: Common optional fields
- cable_termination_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Cable,
    CableTermination,
    Circuit,
    CircuitTermination,
    CircuitType,
    ConsolePort,
    ConsoleServerPort,
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    FrontPort,
    Interface,
    Manufacturer,
    PowerFeed,
    PowerOutlet,
    PowerPanel,
    PowerPort,
    Provider,
    RearPort,
    Site,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "cable_termination-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a CableTermination entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        cable_termination = cable_termination_minimal()
        # cable_termination = cable_termination_extended()
        # cable_termination = cable_termination_explicit()

        response = client.ingest(entities=[Entity(cable_termination=cable_termination)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("CableTermination ingested successfully")


def cable_termination_minimal() -> CableTermination:
    """Create a CableTermination with only required fields using flat strings."""
    return CableTermination(
        cable="Example Cable",  # flat string -> Cable
        cable_end="A",
        metadata={"source": "example"},
    )


def cable_termination_extended() -> CableTermination:
    """Create a CableTermination with common optional fields."""
    return CableTermination(
        cable="Example Cable",
        cable_end="A",
        metadata={"source": "example", "custom_key": "custom_value"},
    )


def cable_termination_explicit() -> CableTermination:
    """Create a CableTermination with fully nested objects and all common fields."""
    return CableTermination(
        cable=Cable(status="planned", color="0000ff", metadata={"source": "example"}),
        cable_end="A",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
        # Polymorphic 'termination' — choose ONE of these mutually exclusive variants:
        termination_interface=Interface(
            device=Device(
                device_type=DeviceType(
                    manufacturer=Manufacturer(
                        name="Example Name",
                        slug="example-slug",
                        metadata={"source": "example"},
                    ),
                    model="Model X",
                    slug="example-slug",
                    metadata={"source": "example"},
                ),
                role=DeviceRole(
                    name="Example Name",
                    slug="example-slug",
                    color="0000ff",
                    metadata={"source": "example"},
                ),
                site=Site(
                    name="Example Name",
                    slug="example-slug",
                    status="active",
                    metadata={"source": "example"},
                ),
                status="active",
                metadata={"source": "example"},
            ),
            name="Example Name",
            type="1000base-t",
            metadata={"source": "example"},
        ),
        # termination_circuit_termination=CircuitTermination(circuit=Circuit(cid="CID-001", provider=Provider(name="Example Name", slug="example-slug", metadata={"source": "example"}), type=CircuitType(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), status="active", metadata={"source": "example"}), term_side="A", metadata={"source": "example"}),
        # termination_console_port=ConsolePort(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", metadata={"source": "example"}),
        # termination_console_server_port=ConsoleServerPort(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", metadata={"source": "example"}),
        # termination_front_port=FrontPort(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", type="110-punch", color="0000ff", rear_port=RearPort(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", type="110-punch", color="0000ff", metadata={"source": "example"}), metadata={"source": "example"}),
        # termination_power_feed=PowerFeed(power_panel=PowerPanel(site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), name="Example Name", metadata={"source": "example"}), name="Example Name", status="active", metadata={"source": "example"}),
        # termination_power_outlet=PowerOutlet(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", color="0000ff", status="disabled", metadata={"source": "example"}),
        # termination_power_port=PowerPort(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", metadata={"source": "example"}),
        # termination_rear_port=RearPort(device=Device(device_type=DeviceType(manufacturer=Manufacturer(name="Example Name", slug="example-slug", metadata={"source": "example"}), model="Model X", slug="example-slug", metadata={"source": "example"}), role=DeviceRole(name="Example Name", slug="example-slug", color="0000ff", metadata={"source": "example"}), site=Site(name="Example Name", slug="example-slug", status="active", metadata={"source": "example"}), status="active", metadata={"source": "example"}), name="Example Name", type="110-punch", color="0000ff", metadata={"source": "example"}),
    )


if __name__ == "__main__":
    main()
