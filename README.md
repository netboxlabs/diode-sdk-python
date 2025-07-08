# Diode SDK Python

Diode SDK Python is a Python library for interacting with the Diode ingestion service utilizing gRPC.

Diode is a new [NetBox](https://netboxlabs.com/oss/netbox/) ingestion service that greatly simplifies and enhances the
process to add and update network data
in NetBox, ensuring your network source of truth is always accurate and can be trusted to power your network automation
pipelines. 

More information about Diode can be found
at [https://netboxlabs.com/blog/introducing-diode-streamlining-data-ingestion-in-netbox/](https://netboxlabs.com/blog/introducing-diode-streamlining-data-ingestion-in-netbox/).

## Installation

```bash
pip install netboxlabs-diode-sdk
```

## Usage

### Environment variables

* `DIODE_SDK_LOG_LEVEL` - Log level for the SDK (default: `INFO`)
* `DIODE_SENTRY_DSN` - Optional Sentry DSN for error reporting
* `DIODE_CLIENT_ID` - Client ID for OAuth2 authentication
* `DIODE_CLIENT_SECRET` - Client Secret for OAuth2 authentication
* `DIODE_DRY_RUN_OUTPUT_DIR` - Directory where `DiodeDryRunClient` will write JSON files

### Example

* `target` should be the address of the Diode service, e.g. `grpc://localhost:8080/diode` for insecure connection
  or `grpcs://example.com` for secure connection.

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    Entity,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Ingest device with device type, platform, manufacturer, site, role, and tags.
        """

        device = Device(
            name="Device A",
            device_type="Device Type A",
            platform="Platform A",
            manufacturer="Manufacturer A",
            site="Site ABC",
            role="Role ABC",
            serial="123456",
            asset_tag="123456",
            status="active",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(device=device))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

### Dry run mode

`DiodeDryRunClient` generates ingestion requests without contacting a Diode server. Requests are printed to stdout by default, or written to JSON files when `output_dir` (or the `DIODE_DRY_RUN_OUTPUT_DIR` environment variable) is specified. The `app_name` parameter serves as the filename prefix; if not provided, `dryrun` is used as the default prefix. The file name is suffixed with a nanosecond-precision timestamp, resulting in the format `<app_name>_<timestamp_ns>.json`.

```python
from netboxlabs.diode.sdk import DiodeDryRunClient

with DiodeDryRunClient(app_name="my_app", output_dir="/tmp") as client:
    client.ingest([
        Entity(device="Device A"),
    ])
```

The produced file can later be ingested by a real Diode instance using
`load_dryrun_entities` with a standard `DiodeClient` or via the bundled
`diode-replay-dryrun` helper:

```python
from netboxlabs.diode.sdk import DiodeClient, load_dryrun_entities

with DiodeClient(
    target="grpc://localhost:8080/diode",
    app_name="my-test-app",
    app_version="0.0.1",
) as client:
    entities = list(load_dryrun_entities("my_app_92722156890707.json"))
    client.ingest(entities=entities)
```

Alternatively, the same file can be ingested using the `diode-replay-dryrun`
command shipped with the SDK:

```bash
diode-replay-dryrun \
  --target grpc://localhost:8080/diode \
  --app-name my-test-app \
  --app-version 0.0.1 \
  my_app_92722156890707.json
```

## Supported entities (object types)

* ASN
* ASN Range
* Aggregate
* Circuit
* Circuit Group
* Circuit Group Assignment
* Circuit Termination
* Circuit Type
* Cluster
* Cluster Group
* Cluster Type
* Console Port
* Console Server Port
* Contact
* Contact Assignment
* Contact Group
* Contact Role
* Device
* Device Bay
* Device Role
* Device Type
* FHRP Group
* FHRP Group Assignment
* Front Port
* IKE Policy
* IKE Proposal
* IP Address
* IP Range
* IP Sec Policy
* IP Sec Profile
* IP Sec Proposal
* Interface
* Inventory Item
* Inventory Item Role
* L2VPN
* L2VPN Termination
* Location
* MAC Address
* Manufacturer
* Module
* Module Bay
* Module Type
* Platform
* Power Feed
* Power Outlet
* Power Panel
* Power Port
* Prefix
* Provider
* Provider Account
* Provider Network
* RIR
* Rack
* Rack Role
* Rack Type
* Rear Port
* Region
* Role
* Route Target
* Service
* Site
* Site Group
* Tag
* Tenant
* Tenant Group
* Tunnel
* Tunnel Group
* Tunnel Termination
* VLAN
* VLAN Group
* VLAN Translation Policy
* VLAN Translation Rule
* VM Interface
* VRF
* Virtual Chassis
* Virtual Circuit
* Virtual Circuit Termination
* Virtual Circuit Type
* Virtual Device Context
* Virtual Disk
* Virtual Machine
* Wireless Lan
* Wireless Lan Group
* Wireless Link

## Development notes

Code in `netboxlabs/diode/sdk/diode/*` is generated from Protocol Buffers definitions (will be published and referenced here soon).

#### Linting

```shell
ruff netboxlabs/
black netboxlabs/
```

#### Testing

```shell
PYTHONPATH=$(pwd) pytest
```

## License

Distributed under the Apache 2.0 License. See [LICENSE.txt](./LICENSE.txt) for more information.
