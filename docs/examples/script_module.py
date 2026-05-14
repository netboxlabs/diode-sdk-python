"""
ScriptModule entity examples for the Diode Python SDK.

This module demonstrates three patterns for ingesting ScriptModule entities:
- script_module_minimal: Required fields only
- script_module_extended: Common optional fields
- script_module_explicit: Fully nested objects with all fields
"""

from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ScriptModule,
)

TARGET = "grpc://localhost:8080/diode"
APP_NAME = "script_module-example"
APP_VERSION = "1.0.0"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"


def main():
    """Main execution - demonstrates ingesting a ScriptModule entity."""
    with DiodeClient(
        target=TARGET,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    ) as client:
        # Choose one of the three patterns:
        script_module = script_module_minimal()
        # script_module = script_module_extended()
        # script_module = script_module_explicit()

        response = client.ingest(entities=[Entity(script_module=script_module)])
        if response.errors:
            print(f"Errors: {response.errors}")
        else:
            print("ScriptModule ingested successfully")


def script_module_minimal() -> ScriptModule:
    """Create a ScriptModule with only required fields using flat strings."""
    return ScriptModule(
        file="Example File",
        metadata={"source": "example"},
    )


def script_module_extended() -> ScriptModule:
    """Create a ScriptModule with common optional fields."""
    return ScriptModule(
        file="Example File",
        metadata={"source": "example", "custom_key": "custom_value"},
    )


def script_module_explicit() -> ScriptModule:
    """Create a ScriptModule with fully nested objects and all common fields."""
    return ScriptModule(
        file="Example File",
        metadata={
            "source": "example",
            "custom_key": "custom_value",
            "collected_at": "2024-01-15T10:30:00Z",
        },
    )


if __name__ == "__main__":
    main()
