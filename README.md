# Diode SDK Python

Diode SDK Python is a Python library for interacting with the Diode ingestion service utilizing gRPC.

Diode is a new [NetBox](https://netboxlabs.com/oss/netbox/) ingestion service that greatly simplifies and enhances the
process to add and update network data
in NetBox, ensuring your network source of truth is always accurate and can be trusted to power your network automation
pipelines. 

More information about Diode can be found
at [https://netboxlabs.com/blog/introducing-diode-streamlining-data-ingestion-in-netbox/](https://netboxlabs.com/blog/introducing-diode-streamlining-data-ingestion-in-netbox/).

## Prerequisites
- Python 3.10 or later installed

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
* `DIODE_CERT_FILE` - Path to custom certificate file for TLS connections
* `DIODE_SKIP_TLS_VERIFY` - Skip TLS verification (default: `false`)
* `DIODE_DRY_RUN_OUTPUT_DIR` - Directory where `DiodeDryRunClient` will write JSON files

### Example

* `target` should be the address of the Diode service.
  * Insecure connections: `grpc://localhost:8080/diode` or `http://localhost:8080/diode`
  * Secure connections: `grpcs://example.com` or `https://example.com`

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

See all [examples](./examples) for reference.

### Using Metadata

Entities support attaching custom metadata as key-value pairs. Metadata can be used to store additional context, tracking information, or custom attributes that don't fit into the standard NetBox fields.

```python
from netboxlabs.diode.sdk import DiodeClient, Entity
from netboxlabs.diode.sdk.ingester import Device, Site, IPAddress

with DiodeClient(
    target="grpc://localhost:8080/diode",
    app_name="my-app",
    app_version="1.0.0",
) as client:
    # Create a device with metadata
    # Note: Both the device and its nested site can have its own metadata
    device = Device(
        name="Device A",
        device_type="Device Type A",
        site=Site(
            name="Site ABC",
            metadata={
                "site_region": "us-west",
                "site_cost_center": "CC-001",
            },
        ),
        role="Role ABC",
        metadata={
            "source": "network_discovery",
            "discovered_at": "2024-01-15T10:30:00Z",
            "import_batch": "batch-123",
            "priority": 1,
            "verified": True,
        },
    )

    # Create an IP address with metadata
    ip_address = IPAddress(
        address="192.168.1.10/24",
        status="active",
        metadata={
            "last_scan": "2024-01-15T12:00:00Z",
            "scan_id": "scan-456",
            "response_time": 23.5,
            "reachable": True,
            "owner_team": "network-ops",
        },
    )

    # Create a site with metadata
    site = Site(
        name="Data Center 1",
        status="active",
        metadata={
            "region": "us-west",
            "cost_center": "CC-001",
            "capacity": 500,
            "is_primary": True,
            "contact_email": "dc1-ops@example.com",
        },
    )

    entities = [Entity(device=device), Entity(ip_address=ip_address), Entity(site=site)]
    response = client.ingest(entities=entities)
    if response.errors:
        print(f"Errors: {response.errors}")
```

#### Adding request-level metadata

In addition to entity-level metadata, you can attach metadata to the entire ingestion request using the `metadata` keyword argument. This is useful for tracking information about the ingestion batch itself, such as the data source, batch ID, or processing context.

```python
from netboxlabs.diode.sdk import DiodeClient, Entity
from netboxlabs.diode.sdk.ingester import Device, Site

with DiodeClient(
    target="grpc://localhost:8080/diode",
    app_name="my-app",
    app_version="1.0.0",
) as client:
    # Create device A
    device_a = Device(
        name="Device A",
        site=Site(name="Site ABC"),
    )

    # Create device B
    device_b = Device(
        name="Device B",
        site=Site(name="Site XYZ"),
    )

    entities = [Entity(device=device_a), Entity(device=device_b)]

    # Add request-level metadata to track the ingestion batch
    response = client.ingest(
        entities=entities,
        metadata={
            "batch_id": "import-2024-01-15",
            "source_system": "network_scanner",
            "import_type": "automated",
            "record_count": len(entities),
            "validated": True,
        },
    )
    if response.errors:
        print(f"Errors: {response.errors}")
```

Request-level metadata is included in the `IngestRequest` and can be useful for:
- Tracking data sources and ingestion pipelines
- Correlating entities within a batch
- Debugging and auditing data imports
- Adding contextual information for downstream processing

### TLS verification and certificates

TLS verification is controlled by the target URL scheme:
- **Secure schemes** (`grpcs://`, `https://`): TLS verification enabled
- **Insecure schemes** (`grpc://`, `http://`): TLS verification disabled

```python
# TLS verification enabled (uses system certificates)
client = DiodeClient(target="grpcs://example.com", ...)

# TLS verification disabled
client = DiodeClient(target="grpc://example.com", ...)
```

### Proxy support

The SDK automatically detects and uses HTTP/HTTPS proxies configured via standard environment variables:

```bash
# For insecure connections
export HTTP_PROXY=http://proxy.example.com:8080

# For secure connections
export HTTPS_PROXY=http://proxy.example.com:8080
# Falls back to HTTP_PROXY if HTTPS_PROXY is not set

# Bypass proxy for specific hosts
export NO_PROXY=localhost,127.0.0.1,.example.com
```

**Important notes for proxy usage:**

1. **Proxy with SKIP_TLS_VERIFY**: When using HTTP(S) proxies, the SDK **always uses secure channels** because proxies require TLS for the CONNECT tunnel. Setting `DIODE_SKIP_TLS_VERIFY=true` with a proxy will log a warning and use a secure channel anyway.

2. **MITM proxies (like mitmproxy)**: To use an intercepting proxy, you must provide the proxy's CA certificate:
   ```bash
   export HTTPS_PROXY=http://127.0.0.1:8080
   export DIODE_CERT_FILE=~/.mitmproxy/mitmproxy-ca-cert.pem
   ```

3. **Non-intercepting proxies**: Regular forwarding proxies work without additional configuration if the target server has a valid certificate trusted by system CAs.

Example with proxy:
```python
import os

# Configure proxy
os.environ["HTTPS_PROXY"] = "http://proxy.example.com:8080"

client = DiodeClient(
    target="grpcs://diode.example.com:443",
    app_name="my-app",
    app_version="1.0.0",
)
```

#### Using custom certificates

```python
# Via constructor parameter
client = DiodeClient(target="grpcs://example.com", cert_file="/path/to/cert.pem", ...)

# Or via environment variable
export DIODE_CERT_FILE=/path/to/cert.pem
```

#### Disabling TLS verification

```bash
export DIODE_SKIP_TLS_VERIFY=true
```

#### For legacy certificates (CN-only, no SANs)

```python
client = DiodeClient(
    target="grpcs://example.com",
    app_name="my-app",
    app_version="1.0.0",
    cert_file="/path/to/cert.pem",
    skip_tls_verify=True,
)
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

#### Adding request-level metadata to dry run output

You can include request-level metadata in the dry run output using the `metadata` keyword argument. This metadata will be included in the JSON output file as part of the `IngestRequest`:

```python
from netboxlabs.diode.sdk import DiodeDryRunClient, Entity
from netboxlabs.diode.sdk.ingester import Device

with DiodeDryRunClient(app_name="my_app", output_dir="/tmp") as client:
    # Add request-level metadata
    client.ingest(
        [Entity(device=Device(name="Device A"))],
        metadata={
            "batch_id": "import-2024-01",
            "source": "csv_import",
            "validated": True,
            "record_count": 150,
        }
    )
```

The resulting JSON file will include the metadata in the `IngestRequest`, making it visible when reviewing the dry run output.

### CLI to replay dry-run files

A small helper command is included to ingest JSON files created by the
`DiodeDryRunClient` and send them to a running Diode service.

Install the helper using `pip`:

```bash
pip install netboxlabs-diode-sdk
```

Run it by providing one or more JSON files and connection details. The command supports replaying multiple dry-run files in a single request:

```bash
diode-replay-dryrun \
  --file /tmp/my_app_92722156890707.json \
  --file /tmp/other.json \
  --target grpc://localhost:8080/diode \
  --app-name my-test-app \
  --app-version 0.0.1 \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET
```

The `--file`, `--target`, `--app-name`, and `--app-version` arguments are required. You may
repeat `--file` to specify multiple files. OAuth2
credentials can be supplied using `--client-id` and `--client-secret` or the
`DIODE_CLIENT_ID` and `DIODE_CLIENT_SECRET` environment variables.

### OTLP client

`DiodeOTLPClient` converts ingestion entities into OpenTelemetry log records and exports them to an OTLP endpoint (gRPC). This is useful when a collector ingests log data and forwards it to Diode.

```python
from netboxlabs.diode.sdk import Entity, DiodeOTLPClient

with DiodeOTLPClient(
    target="grpc://localhost:4317",
    app_name="my-producer",
    app_version="0.0.1",
) as client:
    client.ingest([Entity(site="Site1")])
```

Each entity is serialised to JSON and sent as a log record with producer metadata so downstream collectors can enrich and forward the payload. The client raises `OTLPClientError` when the export fails. TLS behaviour honours the existing `DIODE_SKIP_TLS_VERIFY` and `DIODE_CERT_FILE` environment variables.

#### Adding request-level metadata as OTLP resource attributes

You can add request-level metadata to OTLP exports using the `metadata` keyword argument. This metadata is automatically mapped to OTLP resource attributes with a `diode.metadata.` prefix:

```python
from netboxlabs.diode.sdk import DiodeOTLPClient, Entity
from netboxlabs.diode.sdk.ingester import Site

with DiodeOTLPClient(
    target="grpc://localhost:4317",
    app_name="otlp-producer",
    app_version="1.0.0",
) as client:
    # Add request-level metadata
    client.ingest(
        [Entity(site=Site(name="Site 1"))],
        metadata={
            "environment": "production",
            "deployment": "us-west-2",
            "version": "1.2.3",
            "priority": 5,
        },
    )
```

The resulting OTLP log records will include resource attributes like:
- `diode.metadata.environment="production"`
- `diode.metadata.deployment="us-west-2"`
- `diode.metadata.version="1.2.3"`
- `diode.metadata.priority=5` (as integer)

These attributes are added alongside standard OTLP resource attributes (`service.name`, `service.version`, `diode.stream`, etc.), allowing downstream collectors and observability platforms to filter, route, and enrich the data based on this metadata.

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
