# Supported Entities

## Device

Attributes:

* `name` (str) - device name
* `device_type` (str, [DeviceType](#device-type)) - device type name or DeviceType entity
* `platform` (str, [Platform](#platform)) - platform name or Platform entity
* `manufacturer` (str, [Manufacturer](#manufacturer)) - manufacturer name or Manufacturer entity
* `site` (str, [Site](#site)) - site name or Site entity
* `role` (str, [Role](#role)) - role name or Role entity
* `serial` (str) - serial number
* `asset_tag` (str) - asset tag
* `status` (str) - status (e.g. `active`, `planned`, `staged`, `failed`, `inventory`, `decommissioning`, `offine`)
* `comments` (str) - comments
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceType,
    Entity,
    Manufacturer,
    Platform,
    Role,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Device entity with only a name provided will attempt to create or update a device with
        the given name and placeholders (i.e. "undefined") for other nested objects types
        (e.g. DeviceType, Platform, Site, Role) required by NetBox.
        """

        device = Device(name="Device A")

        entities.append(Entity(device=device))

        """
        Device entity using flat data structure.
        """

        device_flat = Device(
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

        entities.append(Entity(device=device_flat))

        """
        Device entity using explicit data structure.
        """

        device_explicit = Device(
            name="Device A",
            device_type=DeviceType(
                model="Device Type A", manufacturer=Manufacturer(name="Manufacturer A")
            ),
            platform=Platform(
                name="Platform A", manufacturer=Manufacturer(name="Manufacturer A")
            ),
            site=Site(name="Site ABC"),
            role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
            serial="123456",
            asset_tag="123456",
            status="active",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(device=device_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()
```

## Interface

Attributes:

* `name` (str) - interface name
* `device` (str, [Device](#device)) - device name or Device entity
* `device_type` (str, [DeviceType](#device-type)) - device type name or DeviceType entity
* `role` (str, [Role](#role)) - role name or Role entity
* `platform` (str, [Platform](#platform)) - platform name or Platform entity
* `manufacturer` (str, [Manufacturer](#manufacturer)) - manufacturer name or Manufacturer entity
* `site` (str, [Site](#site)) - site name or Site entity
* `type` (str) - interface type (e.g. `virtual`, `other`, etc.)
* `enabled` (bool) - is the interface enabled
* `mtu` (int) - maximum transmission unit
* `mac_address` (str) - MAC address
* `speed` (int) - speed
* `wwn` (str) - world wide name
* `mgmt_only` (bool) - is the interface for management only
* `description` (str) - description
* `mark_connected` (bool) - mark connected
* `mode` (str) - mode (`access`, `tagged`, `tagged-all`)
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceType,
    Entity,
    Interface,
    Manufacturer,
    Platform,
    Role,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Interface entity with only a name provided will attempt to create or update an interface with
        the given name and placeholders (i.e. "undefined") for other nested objects types
        (e.g. Device, DeviceType, Platform, Site, Role) required by NetBox.
        """

        interface = Interface(name="Interface A")

        entities.append(Entity(interface=interface))

        """
        Interface entity using flat data structure.
        """

        interface_flat = Interface(
            name="Interface A",
            device="Device A",
            device_type="Device Type A",
            role="Role ABC",
            platform="Platform A",
            site="Site ABC",
            type="virtual",
            enabled=True,
            mtu=1500,
            mac_address="00:00:00:00:00:00",
            description="Interface A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(interface=interface_flat))

        """
        Interface entity using explicit data structure.
        """

        interface_explicit = Interface(
            name="Interface A",
            device=Device(
                name="Device A",
                device_type=DeviceType(
                    model="Device Type A",
                    manufacturer=Manufacturer(name="Manufacturer A"),
                ),
                platform=Platform(
                    name="Platform A", manufacturer=Manufacturer(name="Manufacturer A")
                ),
                site=Site(name="Site ABC"),
                role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
            ),
            type="virtual",
            enabled=True,
            mtu=1500,
            mac_address="00:00:00:00:00:00",
            description="Interface A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(interface=interface_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Device Type

Attributes:

* `model` (str) - device type model
* `slug` (str) - slug
* `manufacturer` (str, [Manufacturer](#manufacturer)) - manufacturer name or Manufacturer entity
* `description` (str) - description
* `comments` (str) - comments
* `part_number` (str) - part number
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    DeviceType,
    Entity,
    Manufacturer,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        DeviceType entity with only a name provided will attempt to create or update a device type with
        the given name and placeholder (i.e. "undefined") for nested Manufacturer object type
        required by NetBox.
        """

        device_type = DeviceType(model="Device Type A")

        entities.append(Entity(device_type=device_type))

        """
        DeviceType entity using flat data structure.
        """

        device_type_flat = DeviceType(
            model="Device Type A",
            manufacturer="Manufacturer A",
            part_number="123456",
            description="Device Type A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(device_type=device_type_flat))

        """
        DeviceType entity using explicit data structure.
        """

        device_type_explicit = DeviceType(
            model="Device Type A",
            manufacturer=Manufacturer(
                name="Manufacturer A",
                description="Manufacturer A description",
                tags=["tag 1", "tag 2"],
            ),
            part_number="123456",
            description="Device Type A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(device_type=device_type_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Platform

Attributes:

* `name` (str) - platform name
* `slug` (str) - slug
* `manufacturer` (str, [Manufacturer](#manufacturer)) - manufacturer name or Manufacturer entity
* `description` (str) - description
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Manufacturer,
    Platform,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Platform entity with only a name provided will attempt to create or update a platform with
        the given name and placeholders (i.e. "undefined") for other nested objects types (e.g. Manufacturer)
        required by NetBox.
        """

        platform = Platform(
            name="Platform A",
        )

        entities.append(Entity(platform=platform))

        """
        Platform entity using flat data structure.
        """

        platform_flat = Platform(
            name="Platform A",
            manufacturer="Manufacturer A",
            description="Platform A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(platform=platform_flat))

        """
        Platform entity using explicit data structure.
        """

        platform_explicit = Platform(
            name="Platform A",
            manufacturer=Manufacturer(name="Manufacturer A", tags=["tag 1", "tag 3"]),
            description="Platform A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(platform=platform_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Manufacturer

Attributes:

* `name` (str) - manufacturer name
* `slug` (str) - slug
* `description` (str) - description
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Manufacturer,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Manufacturer entity.
        """

        manufacturer = Manufacturer(
            name="Manufacturer A",
            description="Manufacturer A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(manufacturer=manufacturer))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Site

Attributes:

* `name` (str) - site name
* `slug` (str) - slug
* `status` (str) - status (`active`, `planned`, `retired`, `staging`, `decommissioning`)
* `facility` (str) - facility
* `time_zone` (str) - time zone
* `description` (str) - description
* `comments` (str) - comments
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Site entity.
        """

        site = Site(
            name="Site A",
            status="active",
            facility="Data Center 1",
            time_zone="UTC",
            description="Site A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(site=site))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Role

Attributes:

* `name` (str) - role name
* `slug` (str) - slug
* `color` (str) - color
* `description` (str) - description
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Role,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Role entity.
        """

        role = Role(
            name="Role A",
            slug="role-a",
            color="ffffff",
            description="Role A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(device_role=role))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## IP Address

Attributes:

* `address` (str) - IP address
* `interface` (str, [Interface](#interface)) - interface name or Interface entity
* `device` (str, [Device](#device)) - device name or Device entity
* `device_type` (str, [DeviceType](#device-type)) - device type name or DeviceType entity
* `device_role` (str, [Role](#role)) - device role name or Role entity
* `platform` (str, [Platform](#platform)) - platform name or Platform entity
* `manufacturer` (str, [Manufacturer](#manufacturer)) - manufacturer name or Manufacturer entity
* `site` (str, Site) - site name or Site entity
* `status` (str) - status (`active`, `reserved`, `deprecated`, `dhcp`, `slaac`)
* `role` (str) - role (`loopback`, `secondary`, `anycast`, `vip`, `vrrp`, `hsrp`, `glbp`, `carp`)
* `dns_name` (str) - DNS name
* `description` (str) - description
* `comments` (str) - comments
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceType,
    Entity,
    Interface,
    IPAddress,
    Manufacturer,
    Platform,
    Role,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        IPAddress entity with only an address provided will attempt to create or update an IP address with
        the given address and placeholders (i.e. "undefined") for other nested objects types
        (e.g. Interface, Device, DeviceType, Platform, Site, Role) required by NetBox.
        """

        ip_address = IPAddress(
            address="192.168.0.1/24",
        )

        entities.append(Entity(ip_address=ip_address))

        """
        IPAddress entity using flat data structure.
        """

        ip_address_flat = IPAddress(
            address="192.168.0.1/24",
            interface="Interface ABC",
            device="Device ABC",
            device_type="Device Type ABC",
            device_role="Role ABC",
            platform="Platform ABC",
            manufacturer="Cisco",
            site="Site ABC",
            status="active",
            role="Role ABC",
            description="IP Address A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag1", "tag2"],
        )

        entities.append(Entity(ip_address=ip_address_flat))

        """
        IPAddress entity using explicit data structure.
        """

        ip_address_explicit = IPAddress(
            address="192.168.0.1/24",
            interface=Interface(
                name="Interface ABC",
                device=Device(
                    name="Device ABC",
                    device_type=DeviceType(
                        model="Device Type ABC", manufacturer=Manufacturer(name="Cisco")
                    ),
                    platform=Platform(
                        name="Platform ABC", manufacturer=Manufacturer(name="Cisco")
                    ),
                    site=Site(name="Site ABC"),
                    role=Role(name="Role ABC", tags=["tag1", "tag3"]),
                ),
            ),
            status="active",
            role="Role ABC",
            description="IP Address A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag1", "tag2"],
        )

        entities.append(Entity(ip_address=ip_address_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Prefix

Attributes:

* `prefix` (str) - prefix
* `site` (str, [Site](#site)) - site name or Site entity
* `status` (str) - status (`active`, `reserved`, `deprecated`, `container`)
* `is_pool` (bool) - is pool
* `mark_utilized` (bool) - mark utilized
* `description` (str) - description
* `comments` (str) - comments
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Prefix,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Prefix entity with only a prefix provided will attempt to create or update a prefix with
        the given prefix and placeholders (i.e. "undefined") for other nested objects types (e.g. Site)
        required by NetBox.
        """

        prefix = Prefix(
            prefix="192.168.0.0/32",
        )

        entities.append(Entity(prefix=prefix))

        """
        Prefix entity using flat data structure.
        """

        prefix_flat = Prefix(
            prefix="192.168.0.0/32",
            site="Site ABC",
            status="active",
            is_pool=True,
            mark_utilized=True,
            description="Prefix A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(prefix=prefix_flat))

        """
        Prefix entity using explicit data structure.
        """

        prefix_explicit = Prefix(
            prefix="192.168.0.0/32",
            site=Site(
                name="Site ABC",
                status="active",
                facility="Data Center 1",
                time_zone="UTC",
                description="Site A description",
                comments="Lorem ipsum dolor sit amet",
                tags=["tag 1", "tag 2"],
            ),
            is_pool=True,
            mark_utilized=True,
            description="Prefix A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(prefix=prefix_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Cluster Type

Attributes:

* `name` (str) - cluster type name
* `slug` (str) - slug
* `description` (str) - description
* `tags` (list) - tags


### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ClusterType,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        ClusterType entity.
        """

        cluster_type = ClusterType(
            name="Cluster Type A",
            description="Cluster Type A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(cluster_type=cluster_type))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Cluster Group

Attributes:

* `name` (str) - cluster group name
* `slug` (str) - slug
* `description` (str) - description
* `tags` (list) - tags


### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    ClusterGroup,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        ClusterGroup entity.
        """

        cluster_group = ClusterGroup(
            name="Cluster Group A",
            description="Cluster Group A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(cluster_group=cluster_group))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Cluster

Attributes:

* `name` (str) - cluster name
* `type` (str, [ClusterType](#cluster-type)) - cluster type name or ClusterType entity
* `group` (str, [ClusterGroup](#cluster-group)) - cluster group name or ClusterGroup entity
* `site` (str, [Site](#site)) - site name or Site entity
* `status` (str) - status (`offline`, `active`, `planned`, `staged`, `failed`, `decommissioning`)
* `description` (str) - description
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    Cluster,
    ClusterGroup,
    ClusterType,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        Cluster entity with only a name provided will attempt to create or update a cluster with
        the given name and placeholders (i.e. "undefined") for other nested objects types
        (e.g. ClusterGroup, ClusterType, Site) required by NetBox.
        """

        cluster = Cluster(name="Cluster A")

        entities.append(Entity(cluster=cluster))

        """
        Cluster entity using flat data structure.
        """

        cluster_flat = Cluster(
            name="Cluster A",
            type="Cluster Type",
            group="Cluster Group",
            site="Site ABC",
            status="active",
            description="Cluster A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(cluster=cluster_flat))

        """
        Cluster entity using explicit data structure.
        """

        cluster_explicit = Cluster(
            name="Cluster A",
            type = ClusterType(
                name="Cluster Type A",
                description="Cluster Type description",
                tags=["tag 1", "tag 2"],
            ),
            group = ClusterGroup(
                name="Cluster Group A",
                description="Cluster Group description",
                tags=["tag 1", "tag 2"],
            ),
            site=Site(
                name="Site ABC",
                status="active",
                facility="Data Center 1",
                time_zone="UTC",
                description="Site A description",
                comments="Lorem ipsum dolor sit amet",
                tags=["tag 1", "tag 2"],
            ),
            description="Cluster A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(cluster=cluster_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Virtual Machine

Attributes:

* `name` (str) - virtual machine name
* `status` (str) - status (`offline`, `active`, `planned`, `staged`, `failed`, `decommissioning`)
* `site` (str, [Site](#site)) - site name or Site entity
* `cluster` (str, [Cluster](#cluster)) - cluster name or Cluster entity
* `role` (str, [Role](#role)) - role name or Role entity
* `device` (str, [Device](#device)) - device name or Device entity
* `platform` (str, [Platform](#platform)) - platform name or Platform entity
* `vcpus` (int) - virtual machine CPU number
* `memory` (int) - virtual machine memory
* `disk` (int) - virtual machine disk size
* `description` (str) - description
* `comments` (str) - comments
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    VirtualMachine,
    Cluster,
    ClusterGroup,
    ClusterType,
    Device,
    DeviceType,
    Manufacturer,
    Platform,
    Role,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        VirtualMachine entity with only a name provided will attempt to create or update a name with
        the given name and placeholders (i.e. "undefined") for other nested objects types (e.g. Site,
        Role, Cluster, Platform, Device) required by NetBox.
        """

        virtual_machine = VirtualMachine(name="VM A")

        entities.append(Entity(virtual_machine=virtual_machine))

        """
        VirtualMachine entity using flat data structure.
        """

        virtual_machine_flat = VirtualMachine(
            name="VM A",
            status="active",
            cluster="Cluster Type A",
            site="Site ABC",
            role="Role ABC",
            device="Device A",
            platform="Platform A",
            vcpus=8,
            memory=12128,
            disk=16786,
            description="Virtual Machine A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(virtual_machine=virtual_machine_flat))

        """
        VirtualMachine entity using explicit data structure.
        """

        virtual_machine_explicit = VirtualMachine(
            name="VM A",
            status="active",
            cluster=Cluster(
                name="Cluster A",
                type=ClusterType(
                    name="Cluster Type A",
                    description="Cluster Type description",
                    tags=["tag 1", "tag 2"],
                ),
                group=ClusterGroup(
                    name="Cluster Group",
                    description="Cluster Group description",
                    tags=["tag 1", "tag 2"],
                ),
                site=Site(
                    name="Site ABC",
                    status="active",
                    facility="Data Center 1",
                    time_zone="UTC",
                    description="Site A description",
                    comments="Lorem ipsum dolor sit amet",
                    tags=["tag 1", "tag 2"],
                ),
                description="Cluster A description",
                tags=["tag 1", "tag 2"],
            ),
            site=Site(
                name="Site ABC",
                status="active",
                facility="Data Center 1",
                time_zone="UTC",
                description="Site A description",
                comments="Lorem ipsum dolor sit amet",
                tags=["tag 1", "tag 2"],
            ),
            role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
            device=Device(
                name="Device A",
                device_type=DeviceType(
                    model="Device Type A",
                    manufacturer=Manufacturer(name="Manufacturer A"),
                ),
                platform=Platform(
                    name="Platform A", manufacturer=Manufacturer(name="Manufacturer A")
                ),
                site=Site(name="Site ABC"),
                role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
                serial="123456",
                asset_tag="123456",
                status="active",
                comments="Lorem ipsum dolor sit amet",
                tags=["tag 1", "tag 2"],
            ),
            platform=Platform(
                name="Platform A", manufacturer=Manufacturer(name="Manufacturer A")
            ),
            vcpus=8,
            memory=12128,
            disk=16786,
            description="Virtual Machine A description",
            comments="Lorem ipsum dolor sit amet",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(virtual_machine=virtual_machine_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## Virtual Disk

Attributes:

* `name` (str) - virtual disk name
* `virtual_machine` (str, [VirtualMachine](#virtual-machine)) - virtual machine name or VirtualMachine entity
* `size` (int) - disk size
* `description` (str) - description
* `tags` (list) - tags

### Example
```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    VirtualDisk,
    VirtualMachine,
    Cluster,
    ClusterGroup,
    ClusterType,
    Device,
    DeviceType,
    Manufacturer,
    Platform,
    Role,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        VirtualDisk entity with only a name provided will attempt to create or update a name
        with the given name and placeholders (i.e. "undefined") for other nested objects types (e.g.
        VirtualMachine) required by NetBox.
        """

        virtual_disk = VirtualDisk(name="Disk A", size=16480)

        entities.append(Entity(virtual_disk=virtual_disk))

        """
        VirtualDisk entity using flat data structure.
        """

        virtual_disk_flat = VirtualDisk(
            name="Disk A",
            virtual_machine="VM A",
            size=16480,
            description="Disk A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(virtual_disk=virtual_disk_flat))

        """
        VirtualDisk entity using explicit data structure.
        """

        virtual_disk_explicit = VirtualDisk(
            name="Disk A",
            virtual_machine=VirtualMachine(
                name="VM A",
                status="active",
                cluster=Cluster(
                    name="Cluster A",
                    type=ClusterType(
                        name="Cluster Type A",
                        description="Cluster Type description",
                        tags=["tag 1", "tag 2"],
                    ),
                    group=ClusterGroup(
                        name="Cluster Group",
                        description="Cluster Group description",
                        tags=["tag 1", "tag 2"],
                    ),
                    site=Site(
                        name="Site ABC",
                        status="active",
                        facility="Data Center 1",
                        time_zone="UTC",
                        description="Site A description",
                        comments="Lorem ipsum dolor sit amet",
                        tags=["tag 1", "tag 2"],
                    ),
                    description="Cluster A description",
                    tags=["tag 1", "tag 2"],
                ),
                site=Site(
                    name="Site ABC",
                    status="active",
                    facility="Data Center 1",
                    time_zone="UTC",
                    description="Site A description",
                    comments="Lorem ipsum dolor sit amet",
                    tags=["tag 1", "tag 2"],
                ),
                role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
                device=Device(
                    name="Device A",
                    device_type=DeviceType(
                        model="Device Type A",
                        manufacturer=Manufacturer(name="Manufacturer A"),
                    ),
                    platform=Platform(
                        name="Platform A",
                        manufacturer=Manufacturer(name="Manufacturer A"),
                    ),
                    site=Site(name="Site ABC"),
                    role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
                    serial="123456",
                    asset_tag="123456",
                    status="active",
                    comments="Lorem ipsum dolor sit amet",
                    tags=["tag 1", "tag 2"],
                ),
                platform=Platform(
                    name="Platform A", manufacturer=Manufacturer(name="Manufacturer A")
                ),
                vcpus=8,
                memory=12128,
                disk=16480,
                description="Virtual Machine A description",
                comments="Lorem ipsum dolor sit amet",
                tags=["tag 1", "tag 2"],
            ),
            size=16480,
            description="Disk A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(virtual_disk=virtual_disk_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```

## VM Interface

Attributes:

* `name` (str) - virtual interface name
* `virtual_machine` (str, [VirtualMachine](#virtual-machine)) - virtual machine name or VirtualMachine entity
* `enabled` (bool) - is the interface enabled
* `mtu` (int) - maximum transmission unit
* `mac_address` (str) - MAC address
* `description` (str) - description
* `tags` (list) - tags

### Example

```python
from netboxlabs.diode.sdk import DiodeClient
from netboxlabs.diode.sdk.ingester import (
    Entity,
    VMInterface,
    VirtualMachine,
    Cluster,
    ClusterGroup,
    ClusterType,
    Device,
    DeviceType,
    Manufacturer,
    Platform,
    Role,
    Site,
)


def main():
    with DiodeClient(
        target="grpc://localhost:8080/diode",
        app_name="my-test-app",
        app_version="0.0.1",
    ) as client:
        entities = []

        """
        VMInterface entity with only a name provided will attempt to create or update a name
        with the given name and placeholders (i.e. "undefined") for other nested objects types (e.g.
        VirtualMachine) required by NetBox.
        """

        vminterface = VMInterface(name="Interface A")

        entities.append(Entity(vminterface=vminterface))

        """
        VMInterface entity using flat data structure.
        """

        vminterface_flat = VMInterface(
            name="Interface A",
            virtual_machine="VM A",
            enabled=True,
            mtu=1500,
            mac_address="00:00:00:00:00:00",
            description="Interface A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(vminterface=vminterface_flat))

        """
        VMInterface entity using explicit data structure.
        """

        vminterface_explicit = VMInterface(
            name="Interface A",
            virtual_machine=VirtualMachine(
                name="VM A",
                status="active",
                cluster=Cluster(
                    name="Cluster A",
                    type=ClusterType(
                        name="Cluster Type A",
                        description="Cluster Type description",
                        tags=["tag 1", "tag 2"],
                    ),
                    group=ClusterGroup(
                        name="Cluster Group",
                        description="Cluster Group description",
                        tags=["tag 1", "tag 2"],
                    ),
                    site=Site(
                        name="Site ABC",
                        status="active",
                        facility="Data Center 1",
                        time_zone="UTC",
                        description="Site A description",
                        comments="Lorem ipsum dolor sit amet",
                        tags=["tag 1", "tag 2"],
                    ),
                    description="Cluster A description",
                    tags=["tag 1", "tag 2"],
                ),
                site=Site(
                    name="Site ABC",
                    status="active",
                    facility="Data Center 1",
                    time_zone="UTC",
                    description="Site A description",
                    comments="Lorem ipsum dolor sit amet",
                    tags=["tag 1", "tag 2"],
                ),
                role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
                device=Device(
                    name="Device A",
                    device_type=DeviceType(
                        model="Device Type A",
                        manufacturer=Manufacturer(name="Manufacturer A"),
                    ),
                    platform=Platform(
                        name="Platform A",
                        manufacturer=Manufacturer(name="Manufacturer A"),
                    ),
                    site=Site(name="Site ABC"),
                    role=Role(name="Role ABC", tags=["tag 1", "tag 3"]),
                    serial="123456",
                    asset_tag="123456",
                    status="active",
                    comments="Lorem ipsum dolor sit amet",
                    tags=["tag 1", "tag 2"],
                ),
                platform=Platform(
                    name="Platform A", manufacturer=Manufacturer(name="Manufacturer A")
                ),
                vcpus=8,
                memory=12128,
                disk=16480,
                description="Virtual Machine A description",
                comments="Lorem ipsum dolor sit amet",
                tags=["tag 1", "tag 2"],
            ),
            enabled=True,
            mtu=1500,
            mac_address="00:00:00:00:00:00",
            description="Interface A description",
            tags=["tag 1", "tag 2"],
        )

        entities.append(Entity(vminterface=vminterface_explicit))

        response = client.ingest(entities=entities)
        if response.errors:
            print(f"Errors: {response.errors}")


if __name__ == "__main__":
    main()

```