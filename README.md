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

* `DIODE_API_KEY` - API key for the Diode service
* `DIODE_SDK_LOG_LEVEL` - Log level for the SDK (default: `INFO`)
* `DIODE_SENTRY_DSN` - Optional Sentry DSN for error reporting

### Example

* `target` should be the address of the Diode service, e.g. `grpc://localhost:8081` for insecure connection
  or `grpcs://example.com` for secure connection.

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    Entity,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8081",
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

## Supported entities (object types)

* [Device](./docs/entities.md#device)
* [Interface](./docs/entities.md#interface)
* [Device Type](./docs/entities.md#device-type)
* [Platform](./docs/entities.md#platform)
* [Manufacturer](./docs/entities.md#manufacturer)
* [Site](./docs/entities.md#site)
* [Role](./docs/entities.md#role)
* [IP Address](./docs/entities.md#ip-address)
* [Prefix](./docs/entities.md#prefix)
* [Cluster Group](./docs/entities.md#cluster-group)
* [Cluster Type](./docs/entities.md#cluster-type)
* [Cluster](./docs/entities.md#cluster)
* [Virtual Machine](./docs/entities.md#virtual-machine)
* [Virtual Disk](./docs/entities.md#virtual-disk)
* [VM Interface](./docs/entities.md#vm-interface)

## Development notes

Code in `netboxlabs/diode/sdk/diode/*` is generated from Protocol Buffers definitions (will be published and referred
here soon).

#### Linting

```shell
ruff netboxlabs/
black netboxlabs/
```

#### Testing

```shell
pytest tests/
```

## License

Distributed under the Apache 2.0 License. See [LICENSE.txt](./LICENSE.txt) for more information.
