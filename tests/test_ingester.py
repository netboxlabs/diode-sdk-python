#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs - Tests."""
from google.protobuf import timestamp_pb2

# ruff: noqa: I001
from netboxlabs.diode.sdk.diode.v1.ingester_pb2 import (
    Cluster as ClusterPb,
    ClusterGroup as ClusterGroupPb,
    ClusterType as ClusterTypePb,
    Device as DevicePb,
    DeviceRole as DeviceRolePb,
    DeviceType as DeviceTypePb,
    Entity as EntityPb,
    IPAddress as IPAddressPb,
    Interface as InterfacePb,
    Manufacturer as ManufacturerPb,
    Owner as OwnerPb,
    OwnerGroup as OwnerGroupPb,
    Platform as PlatformPb,
    Prefix as PrefixPb,
    Role as RolePb,
    Site as SitePb,
    Tag as TagPb,
    VirtualDisk as VirtualDiskPb,
    VMInterface as VMInterfacePb,
    VirtualMachine as VirtualMachinePb,
)
from netboxlabs.diode.sdk.ingester import (
    Cluster,
    ClusterGroup,
    ClusterType,
    Device,
    DeviceRole,
    DeviceType,
    Entity,
    IPAddress,
    Interface,
    Manufacturer,
    Owner,
    OwnerGroup,
    Platform,
    Prefix,
    Role,
    Site,
    Tag,
    VirtualDisk,
    VMInterface,
    VirtualMachine,
    convert_to_protobuf,
)


def test_convert_to_protobuf_returns_correct_class_when_value_is_string():
    """Check convert_to_protobuf returns correct class when value is string."""
    result = convert_to_protobuf("Test Site", SitePb)
    assert isinstance(result, SitePb)
    assert result.name == "Test Site"


def test_convert_to_protobuf_returns_value_when_value_is_not_string():
    """Check convert_to_protobuf returns value when value is not string."""

    class MockProtobufClass:
        def __init__(self, name=None):
            self.name = name

    mock_instance = MockProtobufClass(name="test")
    result = convert_to_protobuf(mock_instance, MockProtobufClass)
    assert result is mock_instance


def test_tag_instantiation_with_all_fields():
    """Check Tag instantiation with all fields."""
    tag = Tag(name="networking", slug="networking-slug", color="blue")
    assert isinstance(tag, TagPb)
    assert tag.name == "networking"
    assert tag.slug == "networking-slug"
    assert tag.color == "blue"


def test_tag_instantiation_with_only_name():
    """Check Tag instantiation with only name."""
    tag = Tag(name="networking")
    assert isinstance(tag, TagPb)
    assert tag.name == "networking"
    assert tag.slug == ""
    assert tag.color == ""


def test_tag_instantiation_with_no_fields():
    """Check Tag instantiation with no fields."""
    tag = Tag()
    assert isinstance(tag, TagPb)
    assert tag.name == ""
    assert tag.slug == ""
    assert tag.color == ""


def test_manufacturer_instantiation_with_tags_as_strings():
    """Check Manufacturer instantiation with tags as strings."""
    manufacturer = Manufacturer(
        name="Cisco",
        slug="cisco",
        description="Networking equipment manufacturer",
        tags=["networking", "equipment"],
    )
    assert isinstance(manufacturer, ManufacturerPb)
    assert manufacturer.name == "Cisco"
    assert manufacturer.slug == "cisco"
    assert manufacturer.description == "Networking equipment manufacturer"
    assert len(manufacturer.tags) == 2
    for tag in manufacturer.tags:
        assert isinstance(tag, TagPb)


def test_manufacturer_instantiation_with_tags_as_protobufs():
    """Check Manufacturer instantiation with tags as protobufs."""
    tags = [TagPb(name="networking"), TagPb(name="equipment")]
    manufacturer = Manufacturer(
        name="Cisco",
        slug="cisco",
        description="Networking equipment manufacturer",
        tags=tags,
    )
    assert isinstance(manufacturer, ManufacturerPb)
    assert manufacturer.name == "Cisco"
    assert manufacturer.slug == "cisco"
    assert manufacturer.description == "Networking equipment manufacturer"
    assert len(manufacturer.tags) == 2
    for tag in manufacturer.tags:
        assert isinstance(tag, TagPb)


def test_platform_instantiation_with_all_fields():
    """Check Platform instantiation with all fields."""
    platform = Platform(
        name="Platform1",
        slug="platform1",
        manufacturer="Manufacturer1",
        description="This is a platform",
        tags=["tag1", "tag2"],
    )
    assert isinstance(platform, PlatformPb)
    assert hasattr(platform, "metadata")
    assert platform.name == "Platform1"
    assert platform.slug == "platform1"
    assert platform.description == "This is a platform"
    assert isinstance(platform.manufacturer, ManufacturerPb)
    assert platform.manufacturer.name == "Manufacturer1"
    assert len(platform.tags) == 2
    for tag in platform.tags:
        assert isinstance(tag, TagPb)


def test_platform_instantiation_with_explicit_manufacturer():
    """Check Platform instantiation with explicit Manufacturer."""
    platform = Platform(
        name="Platform1",
        slug="platform1",
        manufacturer=Manufacturer(name="Manufacturer1"),
        tags=["tag1", "tag2"],
    )
    assert isinstance(platform, PlatformPb)
    assert hasattr(platform, "metadata")

    # Test user-facing API: works like protobuf
    assert platform.name == "Platform1"
    assert platform.slug == "platform1"
    assert platform.manufacturer.name == "Manufacturer1"
    assert len(platform.tags) == 2
    for tag in platform.tags:
        assert isinstance(tag, TagPb)


def test_role_instantiation_with_all_fields():
    """Check Role instantiation with all fields."""
    role = Role(
        name="Admin",
        slug="admin",
        description="Administrator role",
        tags=["admin", "role"],
    )
    assert isinstance(role, RolePb)
    assert role.name == "Admin"
    assert role.slug == "admin"
    assert role.description == "Administrator role"
    assert len(role.tags) == 2
    for tag in role.tags:
        assert isinstance(tag, TagPb)


def test_device_type_instantiation_with_all_fields():
    """Check DeviceType instantiation with all fields."""
    device_type = DeviceType(
        model="Model1",
        slug="model1",
        manufacturer="Manufacturer1",
        description="This is a device type",
        comments="No comments",
        part_number="1234",
        tags=["tag1", "tag2"],
    )
    assert isinstance(device_type, DeviceTypePb)
    assert device_type.model == "Model1"
    assert device_type.slug == "model1"
    assert isinstance(device_type.manufacturer, ManufacturerPb)
    assert device_type.manufacturer.name == "Manufacturer1"
    assert device_type.description == "This is a device type"
    assert device_type.comments == "No comments"
    assert device_type.part_number == "1234"
    assert len(device_type.tags) == 2
    for tag in device_type.tags:
        assert isinstance(tag, TagPb)


def test_device_instantiation_with_all_fields():
    """Check Device instantiation with all fields."""
    device = Device(
        name="Device1",
        device_type="DeviceType1",
        role="Role1",
        platform="Platform1",
        serial="123456",
        site="Site1",
        asset_tag="123456",
        status="active",
        description="This is a device",
        comments="No comments",
        tags=["tag1", "tag2"],
        primary_ip4="192.168.0.1",
        primary_ip6="2001:db8::1",
        manufacturer="Manufacturer1",
    )
    assert isinstance(device, DevicePb)
    assert device.name == "Device1"
    assert isinstance(device.device_type, DeviceTypePb)
    assert isinstance(device.role, DeviceRolePb)
    assert isinstance(device.platform, PlatformPb)
    assert device.serial == "123456"
    assert isinstance(device.site, SitePb)
    assert device.asset_tag == "123456"
    assert device.status == "active"
    assert device.description == "This is a device"
    assert device.comments == "No comments"
    assert len(device.tags) == 2
    for tag in device.tags:
        assert isinstance(tag, TagPb)
    assert isinstance(device.primary_ip4, IPAddressPb)
    assert isinstance(device.primary_ip6, IPAddressPb)


def test_device_instantiation_with_explicit_nested_object_types():
    """Check Device instantiation with explicit nested object types."""
    device = Device(
        name="Device1",
        device_type=DeviceType(model="DeviceType1"),
        role=DeviceRole(name="Role1"),
        platform=Platform(name="Platform1"),
        serial="123456",
        site=Site(name="Site1"),
        asset_tag="123456",
        status="active",
        comments="No comments",
        tags=["tag1", "tag2"],
        primary_ip4="192.168.0.1",
        primary_ip6="2001:db8::1",
        manufacturer=Manufacturer(name="Manufacturer1"),
    )
    assert isinstance(device, DevicePb)
    assert isinstance(device.primary_ip4, IPAddressPb)
    assert isinstance(device.primary_ip6, IPAddressPb)
    assert device.device_type.manufacturer.name == "Manufacturer1"
    assert device.platform.manufacturer.name == "Manufacturer1"


def test_interface_instantiation_with_all_fields():
    """Check Interface instantiation with all fields."""
    interface = Interface(
        name="Interface1",
        device="Device1",
        device_type="DeviceType1",
        role="Role1",
        platform="Platform1",
        manufacturer="Manufacturer1",
        site="Site1",
        type="type1",
        enabled=True,
        mtu=1500,
        primary_mac_address="00:00:00:00:00:00",
        speed=1000,
        wwn="wwn1",
        mgmt_only=True,
        description="This is an interface",
        mark_connected=True,
        mode="mode1",
        tags=["tag1", "tag2"],
    )
    assert isinstance(interface, InterfacePb)
    assert interface.name == "Interface1"
    assert isinstance(interface.device, DevicePb)
    assert interface.device.name == "Device1"
    assert isinstance(interface.device.device_type, DeviceTypePb)
    assert interface.device.device_type.model == "DeviceType1"
    assert isinstance(interface.device.role, DeviceRolePb)
    assert interface.device.role.name == "Role1"
    assert isinstance(interface.device.platform, PlatformPb)
    assert interface.device.platform.name == "Platform1"
    assert isinstance(interface.device.platform.manufacturer, ManufacturerPb)
    assert interface.device.platform.manufacturer.name == "Manufacturer1"
    assert isinstance(interface.device.site, SitePb)
    assert interface.device.site.name == "Site1"
    assert interface.type == "type1"
    assert interface.enabled is True
    assert interface.mtu == 1500
    assert interface.primary_mac_address.mac_address == "00:00:00:00:00:00"
    assert interface.speed == 1000
    assert interface.wwn == "wwn1"
    assert interface.mgmt_only is True
    assert interface.description == "This is an interface"
    assert interface.mark_connected is True
    assert interface.mode == "mode1"
    assert len(interface.tags) == 2
    for tag in interface.tags:
        assert isinstance(tag, TagPb)


def test_interface_instantiation_with_explicit_nested_object_types():
    """Check Interface instantiation with explicit nested object types."""
    interface = Interface(
        name="Interface1",
        device="Device1",
        device_type=DeviceType(model="DeviceType1"),
        role=DeviceRole(name="Role1"),
        platform=Platform(name="Platform1"),
        site=Site(name="Site1"),
        manufacturer=Manufacturer(name="Manufacturer1"),
    )
    assert isinstance(interface, InterfacePb)
    assert isinstance(interface.device.device_type, DeviceTypePb)
    assert isinstance(interface.device.role, DeviceRolePb)
    assert isinstance(interface.device.platform, PlatformPb)
    assert isinstance(interface.device.site, SitePb)
    assert interface.device.platform.manufacturer.name == "Manufacturer1"
    assert interface.device.device_type.manufacturer.name == "Manufacturer1"


def test_ip_address_instantiation_with_all_fields():
    """Check IPAddress instantiation with all fields."""
    ip_address = IPAddress(
        address="192.168.0.1",
        assigned_object_interface="Interface1",
        device="Device1",
        device_type="DeviceType1",
        device_role="Role1",
        platform="Platform1",
        manufacturer="Manufacturer1",
        site="Site1",
        status="active",
        role="admin",
        dns_name="dns.example.com",
        description="This is an IP address",
        comments="No comments",
        tags=["tag1", "tag2"],
    )
    assert isinstance(ip_address, IPAddressPb)
    assert ip_address.address == "192.168.0.1"
    assert isinstance(ip_address.assigned_object_interface, InterfacePb)
    assert ip_address.assigned_object_interface.name == "Interface1"
    assert isinstance(ip_address.assigned_object_interface.device, DevicePb)
    assert ip_address.assigned_object_interface.device.name == "Device1"
    assert isinstance(
        ip_address.assigned_object_interface.device.device_type, DeviceTypePb
    )
    assert (
        ip_address.assigned_object_interface.device.device_type.model == "DeviceType1"
    )
    assert isinstance(ip_address.assigned_object_interface.device.role, DeviceRolePb)
    assert ip_address.assigned_object_interface.device.role.name == "Role1"
    assert isinstance(ip_address.assigned_object_interface.device.platform, PlatformPb)
    assert ip_address.assigned_object_interface.device.platform.name == "Platform1"
    assert isinstance(
        ip_address.assigned_object_interface.device.platform.manufacturer,
        ManufacturerPb,
    )
    assert (
        ip_address.assigned_object_interface.device.platform.manufacturer.name
        == "Manufacturer1"
    )
    assert isinstance(ip_address.assigned_object_interface.device.site, SitePb)
    assert ip_address.assigned_object_interface.device.site.name == "Site1"
    assert ip_address.status == "active"
    assert ip_address.role == "admin"
    assert ip_address.dns_name == "dns.example.com"
    assert ip_address.description == "This is an IP address"
    assert ip_address.comments == "No comments"
    assert len(ip_address.tags) == 2
    for tag in ip_address.tags:
        assert isinstance(tag, TagPb)


def test_ip_address_instantiation_with_explicit_nested_object_types():
    """Check IPAddress instantiation with explicit nested object types."""
    ip_address = IPAddress(
        address="192.168.0.1",
        assigned_object_interface=Interface(
            name="Interface1",
            device=Device(
                name="Device1",
                device_type=DeviceType(
                    model="DeviceType1", manufacturer="Manufacturer1"
                ),
                role=DeviceRole(name="Role1"),
                platform=Platform(name="Platform1", manufacturer="Manufacturer1"),
                site=Site(name="Site1"),
            ),
        ),
        status="active",
        dns_name="dns.example.com",
        description="This is an IP address",
        comments="No comments",
        tags=["tag1", "tag2"],
    )
    assert isinstance(ip_address, IPAddressPb)
    assert (
        ip_address.assigned_object_interface.device.platform.manufacturer.name
        == "Manufacturer1"
    )
    assert (
        ip_address.assigned_object_interface.device.device_type.manufacturer.name
        == "Manufacturer1"
    )
    assert ip_address.status == "active"
    assert ip_address.dns_name == "dns.example.com"
    assert ip_address.description == "This is an IP address"
    assert ip_address.comments == "No comments"
    assert len(ip_address.tags) == 2


def test_ip_address_instantiation_with_manufacturer_populated_to_device_type_and_platform():
    """Check IPAddress instantiation with manufacturer populated to DeviceType and Platform."""
    ip_address = IPAddress(
        address="192.168.0.1",
        assigned_object_interface="Interface1",
        device="Device1",
        device_type=DeviceType(model="DeviceType1"),
        device_role="Role1",
        platform=Platform(name="Platform1"),
        manufacturer="Manufacturer1",
        site="Site1",
        status="active",
        role="admin",
        dns_name="dns.example.com",
    )
    assert isinstance(ip_address, IPAddressPb)
    assert isinstance(ip_address.assigned_object_interface, InterfacePb)
    assert isinstance(ip_address.assigned_object_interface.device, DevicePb)
    assert isinstance(
        ip_address.assigned_object_interface.device.device_type, DeviceTypePb
    )
    assert isinstance(ip_address.assigned_object_interface.device.role, DeviceRolePb)
    assert isinstance(ip_address.assigned_object_interface.device.platform, PlatformPb)
    assert isinstance(ip_address.assigned_object_interface.device.site, SitePb)
    assert (
        ip_address.assigned_object_interface.device.platform.manufacturer.name
        == "Manufacturer1"
    )
    assert (
        ip_address.assigned_object_interface.device.device_type.manufacturer.name
        == "Manufacturer1"
    )
    assert ip_address.status == "active"
    assert ip_address.dns_name == "dns.example.com"


def test_prefix_instantiation_with_all_fields():
    """Check Prefix instantiation with all fields."""
    prefix = Prefix(
        prefix="192.168.0.0/24",
        scope_site="Site1",
        status="active",
        is_pool=True,
        mark_utilized=False,
        comments="No comments",
        tags=["tag1", "tag2"],
    )
    assert isinstance(prefix, PrefixPb)
    assert prefix.prefix == "192.168.0.0/24"
    assert isinstance(prefix.scope_site, SitePb)
    assert prefix.scope_site.name == "Site1"
    assert prefix.status == "active"
    assert prefix.is_pool is True
    assert prefix.mark_utilized is False
    assert prefix.comments == "No comments"
    assert len(prefix.tags) == 2
    for tag in prefix.tags:
        assert isinstance(tag, TagPb)


def test_cluster_group_instantiation_with_all_fields():
    """Check ClusterGroup instantiation with all fields."""
    cluster_group = ClusterGroup(
        name="Group",
        slug="group",
        description="Cluster group",
        tags=["clusters", "grouping"],
    )
    assert isinstance(cluster_group, ClusterGroupPb)
    assert cluster_group.name == "Group"
    assert cluster_group.slug == "group"
    assert cluster_group.description == "Cluster group"
    assert len(cluster_group.tags) == 2
    for tag in cluster_group.tags:
        assert isinstance(tag, TagPb)


def test_cluster_type_instantiation_with_all_fields():
    """Check ClusterType instantiation with all fields."""
    cluster_type = ClusterType(
        name="VMWare",
        slug="vmware",
        description="Cluster type for virtual machine",
        tags=["clusters", "types"],
    )
    assert isinstance(cluster_type, ClusterTypePb)
    assert cluster_type.name == "VMWare"
    assert cluster_type.slug == "vmware"
    assert cluster_type.description == "Cluster type for virtual machine"
    assert len(cluster_type.tags) == 2
    for tag in cluster_type.tags:
        assert isinstance(tag, TagPb)


def test_cluster_instantiation_with_all_fields():
    """Check Cluster instantiation with all fields."""
    cluster = Cluster(
        name="gc-us-east1",
        status="active",
        group=ClusterGroup(name="North America"),
        type="Google Cloud",
        scope_site="Site1",
        description="Cluster on gc us east",
        tags=["us", "gc"],
    )
    assert isinstance(cluster, ClusterPb)
    assert isinstance(cluster.type, ClusterTypePb)
    assert isinstance(cluster.scope_site, SitePb)
    assert cluster.name == "gc-us-east1"
    assert cluster.status == "active"
    assert cluster.scope_site.name == "Site1"
    assert cluster.description == "Cluster on gc us east"
    assert len(cluster.tags) == 2
    for tag in cluster.tags:
        assert isinstance(tag, TagPb)


def test_virtual_machine_instantiation_with_all_fields():
    """Check VirtualMachine instantiation with all fields."""
    virtual_machine = VirtualMachine(
        name="vm1",
        status="active",
        cluster="gc-us-east1",
        site="Site1",
        role="admin",
        device="dev01",
        platform="Platform1",
        vcpus=12,
        memory=16572,
        disk=1225798,
        primary_ip4="192.168.0.1",
        primary_ip6="2001:db8::1",
        description="VM on google cloud",
        tags=["vm", "gc"],
    )
    assert isinstance(virtual_machine, VirtualMachinePb)
    assert isinstance(virtual_machine.cluster, ClusterPb)
    assert isinstance(virtual_machine.site, SitePb)
    assert isinstance(virtual_machine.role, DeviceRolePb)
    assert isinstance(virtual_machine.device, DevicePb)
    assert isinstance(virtual_machine.platform, PlatformPb)
    assert isinstance(virtual_machine.primary_ip4, IPAddressPb)
    assert isinstance(virtual_machine.primary_ip6, IPAddressPb)
    assert virtual_machine.name == "vm1"
    assert virtual_machine.status == "active"
    assert virtual_machine.site.name == "Site1"
    assert virtual_machine.device.site.name == "Site1"
    assert virtual_machine.memory == 16572
    assert virtual_machine.description == "VM on google cloud"
    assert len(virtual_machine.tags) == 2
    for tag in virtual_machine.tags:
        assert isinstance(tag, TagPb)


def test_virtual_machine_instantiation_with_cluster_without_site():
    """Check VirtualMachine instantiation with cluster without explicit site."""
    virtual_machine = VirtualMachine(
        name="vm1",
        status="active",
        cluster=Cluster(name="gc-us-east1"),
        site=Site(name="Site1"),
        description="VM on google cloud",
    )
    assert isinstance(virtual_machine, VirtualMachinePb)
    assert isinstance(virtual_machine.role, DeviceRolePb)
    assert virtual_machine.name == "vm1"
    assert virtual_machine.status == "active"
    assert virtual_machine.site.name == "Site1"
    assert virtual_machine.cluster.scope_site.name == "Site1"


def test_virtual_disk_instantiation_with_all_fields():
    """Check VirtualDisk instantiation with all fields."""
    virtual_disk = VirtualDisk(
        name="Disk",
        virtual_machine="vm1",
        size=16512,
        description="Virtual disk",
        tags=["vm", "disk"],
    )
    assert isinstance(virtual_disk, VirtualDiskPb)
    assert isinstance(virtual_disk.virtual_machine, VirtualMachinePb)
    assert virtual_disk.name == "Disk"
    assert virtual_disk.virtual_machine.name == "vm1"
    assert virtual_disk.description == "Virtual disk"
    assert len(virtual_disk.tags) == 2
    for tag in virtual_disk.tags:
        assert isinstance(tag, TagPb)


def test_vm_interface_instantiation_with_all_fields():
    """Check VMInterface instantiation with all fields."""
    vm_interface = VMInterface(
        name="eth01",
        virtual_machine="vm1",
        enabled=True,
        mtu=1500,
        primary_mac_address="00:00:00:01:02:03",
        description="Virtual interface",
        tags=["vm", "interface"],
    )
    assert isinstance(vm_interface, VMInterfacePb)
    assert isinstance(vm_interface.virtual_machine, VirtualMachinePb)
    assert vm_interface.name == "eth01"
    assert vm_interface.virtual_machine.name == "vm1"
    assert vm_interface.mtu == 1500
    assert vm_interface.primary_mac_address.mac_address == "00:00:00:01:02:03"
    assert vm_interface.description == "Virtual interface"
    assert len(vm_interface.tags) == 2
    for tag in vm_interface.tags:
        assert isinstance(tag, TagPb)


def test_site_instantiation_with_all_fields():
    """Check Site instantiation with all fields."""
    site = Site(
        name="Site1",
        slug="site1",
        status="active",
        comments="No comments",
        tags=["tag1", "tag2"],
    )
    assert isinstance(site, SitePb)
    assert site.name == "Site1"
    assert site.slug == "site1"
    assert site.status == "active"
    assert site.comments == "No comments"
    assert len(site.tags) == 2
    for tag in site.tags:
        assert isinstance(tag, TagPb)


def test_entity_instantiation_with_no_timestamp_provided():
    """Check Entity instantiation with no timestamp provided."""
    entity = Entity(
        site="Site1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.site, SitePb)
    assert entity.site.name == "Site1"
    assert entity.timestamp is not None
    assert entity.timestamp.seconds > 0
    assert entity.timestamp.nanos > 0


def test_entity_instantiation_with_timestamp_provided():
    """Check Entity instantiation with timestamp provided."""
    current_ts = timestamp_pb2.Timestamp()
    current_ts.GetCurrentTime()

    entity = Entity(
        site="Site1",
        timestamp=current_ts,
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.site, SitePb)
    assert entity.site.name == "Site1"
    assert entity.timestamp is not None
    assert entity.timestamp.seconds > 0
    assert entity.timestamp.nanos > 0
    assert entity.timestamp.seconds == current_ts.seconds
    assert entity.timestamp.nanos == current_ts.nanos


def test_entity_instantiation_with_site():
    """Check Entity instantiation with site."""
    entity = Entity(
        site="Site1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.site, SitePb)
    assert entity.site.name == "Site1"


def test_entity_instantiation_with_platform():
    """Check Entity instantiation with platform."""
    entity = Entity(
        platform="Platform1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.platform, PlatformPb)
    assert entity.platform.name == "Platform1"


def test_entity_instantiation_with_manufacturer():
    """Check Entity instantiation with manufacturer."""
    entity = Entity(
        manufacturer="Manufacturer1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.manufacturer, ManufacturerPb)
    assert entity.manufacturer.name == "Manufacturer1"


def test_entity_instantiation_with_device():
    """Check Entity instantiation with device."""
    entity = Entity(
        device="Device1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.device, DevicePb)
    assert entity.device.name == "Device1"


def test_entity_instantiation_with_device_type():
    """Check Entity instantiation with device type."""
    entity = Entity(
        device_type="DeviceType1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.device_type, DeviceTypePb)
    assert entity.device_type.model == "DeviceType1"


def test_entity_instantiation_with_role():
    """Check Entity instantiation with role."""
    entity = Entity(
        device_role="Role1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.device_role, DeviceRolePb)
    assert entity.device_role.name == "Role1"


def test_entity_instantiation_with_interface():
    """Check Entity instantiation with interface."""
    entity = Entity(
        interface="Interface1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.interface, InterfacePb)
    assert entity.interface.name == "Interface1"


def test_entity_instantiation_with_ip_address():
    """Check Entity instantiation with IP address."""
    entity = Entity(
        ip_address="192.168.0.1/24",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.ip_address, IPAddressPb)
    assert entity.ip_address.address == "192.168.0.1/24"


def test_entity_instantiation_with_prefix():
    """Check Entity instantiation with prefix."""
    entity = Entity(
        prefix="192.168.0.0/24",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.prefix, PrefixPb)
    assert entity.prefix.prefix == "192.168.0.0/24"


def test_entity_instantiation_with_cluster_group():
    """Check Entity instantiation with cluster group."""
    entity = Entity(
        cluster_group="ClusterGroup1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.cluster_group, ClusterGroupPb)
    assert entity.cluster_group.name == "ClusterGroup1"


def test_entity_instantiation_with_cluster_type():
    """Check Entity instantiation with cluster type."""
    entity = Entity(
        cluster_type="ClusterType1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.cluster_type, ClusterTypePb)
    assert entity.cluster_type.name == "ClusterType1"


def test_entity_instantiation_with_cluster():
    """Check Entity instantiation with cluster."""
    entity = Entity(
        cluster="Cluster1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.cluster, ClusterPb)
    assert entity.cluster.name == "Cluster1"


def test_entity_instantiation_with_virtual_machine():
    """Check Entity instantiation with virtual machine."""
    entity = Entity(
        virtual_machine="VM1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.virtual_machine, VirtualMachinePb)
    assert entity.virtual_machine.name == "VM1"


def test_entity_instantiation_with_virtual_disk():
    """Check Entity instantiation with virtual disk."""
    entity = Entity(
        virtual_disk="VirtualDisk1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.virtual_disk, VirtualDiskPb)
    assert entity.virtual_disk.name == "VirtualDisk1"


def test_entity_instantiation_with_vm_interface():
    """Check Entity instantiation with virtual interface."""
    entity = Entity(
        vm_interface="VMInterface1",
    )
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.vm_interface, VMInterfacePb)
    assert entity.vm_interface.name == "VMInterface1"


def test_entity_with_metadata():
    """Test Entity with entity-level metadata."""
    metadata = {
        "source": "import-script",
        "import_id": "batch-123",
        "priority": 5,
    }

    site = Site(name="TestSite", metadata=metadata)
    entity = Entity(site=site)

    assert isinstance(entity, EntityPb)
    assert entity.HasField("site")
    assert entity.site.name == "TestSite"

    assert entity.site.HasField("metadata")
    assert "source" in entity.site.metadata.fields
    assert entity.site.metadata.fields["source"].string_value == "import-script"
    assert "import_id" in entity.site.metadata.fields
    assert entity.site.metadata.fields["import_id"].string_value == "batch-123"
    assert "priority" in entity.site.metadata.fields
    assert entity.site.metadata.fields["priority"].number_value == 5


def test_entity_with_nested_metadata():
    """Test Entity with nested metadata structures."""
    metadata = {
        "tags": ["production", "critical"],
        "config": {
            "auto_sync": True,
            "retry_count": 3,
        },
    }

    device = Device(name="TestDevice", metadata=metadata)
    entity = Entity(device=device)

    assert isinstance(entity, EntityPb)
    assert entity.HasField("device")
    assert entity.device.name == "TestDevice"

    assert entity.device.HasField("metadata")
    assert "tags" in entity.device.metadata.fields
    assert entity.device.metadata.fields["tags"].HasField("list_value")
    tags_list = entity.device.metadata.fields["tags"].list_value.values
    assert len(tags_list) == 2
    assert tags_list[0].string_value == "production"
    assert tags_list[1].string_value == "critical"

    assert "config" in entity.device.metadata.fields
    assert entity.device.metadata.fields["config"].HasField("struct_value")
    config_struct = entity.device.metadata.fields["config"].struct_value.fields
    assert "auto_sync" in config_struct
    assert config_struct["auto_sync"].bool_value is True
    assert "retry_count" in config_struct
    assert config_struct["retry_count"].number_value == 3


def test_entity_without_metadata():
    """Test Entity without metadata (backward compatibility)."""
    entity = Entity(site="TestSite")

    assert isinstance(entity, EntityPb)
    assert entity.HasField("site")
    assert entity.site.name == "TestSite"

    assert not entity.site.HasField("metadata") or len(entity.site.metadata.fields) == 0


def test_entity_metadata_type_conversion():
    """Test entity type metadata with different Python types."""
    metadata = {
        "string_val": "test",
        "int_val": 42,
        "float_val": 3.14,
        "bool_true": True,
        "bool_false": False,
        "null_val": None,
    }

    site = Site(name="TestSite", metadata=metadata)
    entity = Entity(site=site)

    assert isinstance(entity, EntityPb)
    assert entity.site.HasField("metadata")

    assert entity.site.metadata.fields["string_val"].string_value == "test"
    assert entity.site.metadata.fields["int_val"].number_value == 42
    assert entity.site.metadata.fields["float_val"].number_value == 3.14
    assert entity.site.metadata.fields["bool_true"].bool_value is True
    assert entity.site.metadata.fields["bool_false"].bool_value is False
    assert entity.site.metadata.fields["null_val"].HasField("null_value")


def test_device_with_metadata():
    """Test Device entity with metadata."""
    metadata = {
        "rack_position": "A1",
        "warranty_expires": "2025-12-31",
    }

    device = Device(
        name="switch-01",
        device_type="Catalyst 9300",
        site="DC1",
        metadata=metadata,
    )
    entity = Entity(device=device)

    assert isinstance(entity, EntityPb)
    assert entity.HasField("device")
    assert entity.device.name == "switch-01"
    assert entity.device.HasField("metadata")
    assert entity.device.metadata.fields["rack_position"].string_value == "A1"
    assert (
        entity.device.metadata.fields["warranty_expires"].string_value == "2025-12-31"
    )


def test_multiple_entities_with_different_metadata():
    """Test multiple entities each with metadata."""
    entities = [
        Entity(site=Site(name="Site1", metadata={"region": "us-west", "priority": 1})),
        Entity(site=Site(name="Site2", metadata={"region": "us-east", "priority": 2})),
        Entity(
            device=Device(
                name="Device1", metadata={"rack": "A1", "power_source": "UPS-1"}
            )
        ),
    ]

    assert entities[0].site.metadata.fields["region"].string_value == "us-west"
    assert entities[0].site.metadata.fields["priority"].number_value == 1

    assert entities[1].site.metadata.fields["region"].string_value == "us-east"
    assert entities[1].site.metadata.fields["priority"].number_value == 2

    assert entities[2].device.metadata.fields["rack"].string_value == "A1"
    assert entities[2].device.metadata.fields["power_source"].string_value == "UPS-1"


def test_entity_with_nested_entity_both_with_metadata():
    """Test that nested entity metadata is embedded in protobufs."""
    manufacturer = Manufacturer(
        name="Cisco Systems",
        metadata={
            "vendor_id": "CSCO-001",
            "support_tier": "platinum",
            "contract_number": "SUP-12345",
        },
    )

    platform = Platform(
        name="Cisco IOS XE",
        manufacturer=manufacturer,
        metadata={
            "platform_version": "17.3.4",
            "certified": True,
            "eol_date": "2030-12-31",
        },
    )

    assert isinstance(platform, PlatformPb)
    assert platform.HasField("metadata")
    assert platform.metadata.fields["platform_version"].string_value == "17.3.4"
    assert platform.metadata.fields["certified"].bool_value is True
    assert platform.metadata.fields["eol_date"].string_value == "2030-12-31"

    assert isinstance(platform.manufacturer, ManufacturerPb)
    assert platform.manufacturer.HasField("metadata")
    assert platform.manufacturer.metadata.fields["vendor_id"].string_value == "CSCO-001"
    assert (
        platform.manufacturer.metadata.fields["support_tier"].string_value == "platinum"
    )
    assert (
        platform.manufacturer.metadata.fields["contract_number"].string_value
        == "SUP-12345"
    )
    assert platform.manufacturer.name == "Cisco Systems"

    platform_entity = Entity(platform=platform)
    assert isinstance(platform_entity, EntityPb)
    assert platform_entity.HasField("platform")
    assert platform_entity.platform.name == "Cisco IOS XE"
    assert platform_entity.platform.HasField("manufacturer")
    assert platform_entity.platform.manufacturer.name == "Cisco Systems"


def test_owner_group_instantiation_with_all_fields():
    """Check OwnerGroup instantiation with all fields."""
    owner_group = OwnerGroup(
        name="Network Team",
        description="Team responsible for network infrastructure",
        metadata={"department": "IT", "cost_center": "CC001"},
    )
    assert isinstance(owner_group, OwnerGroupPb)
    assert owner_group.name == "Network Team"
    assert owner_group.description == "Team responsible for network infrastructure"
    assert owner_group.HasField("metadata")
    assert owner_group.metadata.fields["department"].string_value == "IT"
    assert owner_group.metadata.fields["cost_center"].string_value == "CC001"


def test_owner_group_instantiation_with_only_name():
    """Check OwnerGroup instantiation with only name."""
    owner_group = OwnerGroup(name="Network Team")
    assert isinstance(owner_group, OwnerGroupPb)
    assert owner_group.name == "Network Team"
    assert owner_group.description == ""


def test_owner_instantiation_with_all_fields():
    """Check Owner instantiation with all fields."""
    owner = Owner(
        name="John Doe",
        group="Network Team",
        description="Primary network administrator",
        metadata={"email": "john.doe@example.com", "employee_id": "E12345"},
    )
    assert isinstance(owner, OwnerPb)
    assert owner.name == "John Doe"
    assert isinstance(owner.group, OwnerGroupPb)
    assert owner.group.name == "Network Team"
    assert owner.description == "Primary network administrator"
    assert owner.HasField("metadata")
    assert owner.metadata.fields["email"].string_value == "john.doe@example.com"
    assert owner.metadata.fields["employee_id"].string_value == "E12345"


def test_owner_instantiation_with_only_name():
    """Check Owner instantiation with only name."""
    owner = Owner(name="John Doe")
    assert isinstance(owner, OwnerPb)
    assert owner.name == "John Doe"
    assert owner.description == ""


def test_owner_instantiation_with_explicit_owner_group():
    """Check Owner instantiation with explicit OwnerGroup object."""
    owner_group = OwnerGroup(
        name="Network Team", description="Network infrastructure team"
    )
    owner = Owner(
        name="Jane Smith",
        group=owner_group,
        description="Backup network administrator",
    )
    assert isinstance(owner, OwnerPb)
    assert owner.name == "Jane Smith"
    assert isinstance(owner.group, OwnerGroupPb)
    assert owner.group.name == "Network Team"
    assert owner.group.description == "Network infrastructure team"


def test_owner_instantiation_with_protobuf_owner_group():
    """Check Owner instantiation with protobuf OwnerGroup."""
    owner_group_pb = OwnerGroupPb(name="Security Team")
    owner = Owner(name="Bob Wilson", group=owner_group_pb)
    assert isinstance(owner, OwnerPb)
    assert owner.name == "Bob Wilson"
    assert isinstance(owner.group, OwnerGroupPb)
    assert owner.group.name == "Security Team"


def test_entity_instantiation_with_owner():
    """Check Entity instantiation with owner as string."""
    entity = Entity(owner="John Doe")
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.owner, OwnerPb)
    assert entity.owner.name == "John Doe"


def test_entity_instantiation_with_owner_object():
    """Check Entity instantiation with Owner object."""
    owner = Owner(name="Jane Smith", group="Network Team")
    entity = Entity(owner=owner)
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.owner, OwnerPb)
    assert entity.owner.name == "Jane Smith"
    assert entity.owner.group.name == "Network Team"


def test_entity_instantiation_with_owner_group():
    """Check Entity instantiation with owner_group as string."""
    entity = Entity(owner_group="Network Team")
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.owner_group, OwnerGroupPb)
    assert entity.owner_group.name == "Network Team"


def test_entity_instantiation_with_owner_group_object():
    """Check Entity instantiation with OwnerGroup object."""
    owner_group = OwnerGroup(name="Security Team", description="Security operations")
    entity = Entity(owner_group=owner_group)
    assert isinstance(entity, EntityPb)
    assert isinstance(entity.owner_group, OwnerGroupPb)
    assert entity.owner_group.name == "Security Team"
    assert entity.owner_group.description == "Security operations"


def test_site_with_owner():
    """Check Site instantiation with owner."""
    site = Site(name="Site1", owner="Site Admin")
    assert isinstance(site, SitePb)
    assert site.name == "Site1"
    assert isinstance(site.owner, OwnerPb)
    assert site.owner.name == "Site Admin"


def test_device_with_owner():
    """Check Device instantiation with owner."""
    device = Device(
        name="Device1",
        device_type="DeviceType1",
        site="Site1",
        owner="Device Admin",
    )
    assert isinstance(device, DevicePb)
    assert device.name == "Device1"
    assert isinstance(device.owner, OwnerPb)
    assert device.owner.name == "Device Admin"


def test_device_with_owner_object():
    """Check Device instantiation with Owner object."""
    owner = Owner(name="Network Admin", group="Network Team")
    device = Device(name="Switch01", device_type="Catalyst 9300", owner=owner)
    assert isinstance(device, DevicePb)
    assert device.name == "Switch01"
    assert isinstance(device.owner, OwnerPb)
    assert device.owner.name == "Network Admin"
    assert device.owner.group.name == "Network Team"


def test_interface_with_owner():
    """Check Interface instantiation with owner."""
    interface = Interface(
        name="eth0",
        device="Device1",
        owner="Interface Owner",
    )
    assert isinstance(interface, InterfacePb)
    assert interface.name == "eth0"
    assert isinstance(interface.owner, OwnerPb)
    assert interface.owner.name == "Interface Owner"


def test_prefix_with_owner():
    """Check Prefix instantiation with owner."""
    prefix = Prefix(
        prefix="192.168.0.0/24",
        owner="Network Team",
    )
    assert isinstance(prefix, PrefixPb)
    assert prefix.prefix == "192.168.0.0/24"
    assert isinstance(prefix.owner, OwnerPb)
    assert prefix.owner.name == "Network Team"


def test_virtual_machine_with_owner():
    """Check VirtualMachine instantiation with owner."""
    vm = VirtualMachine(
        name="vm1",
        status="active",
        owner="VM Admin",
    )
    assert isinstance(vm, VirtualMachinePb)
    assert vm.name == "vm1"
    assert isinstance(vm.owner, OwnerPb)
    assert vm.owner.name == "VM Admin"


def test_cluster_with_owner():
    """Check Cluster instantiation with owner."""
    cluster = Cluster(
        name="production-cluster",
        type="Kubernetes",
        owner="Platform Team",
    )
    assert isinstance(cluster, ClusterPb)
    assert cluster.name == "production-cluster"
    assert isinstance(cluster.owner, OwnerPb)
    assert cluster.owner.name == "Platform Team"


def test_manufacturer_with_owner():
    """Check Manufacturer instantiation with owner."""
    manufacturer = Manufacturer(
        name="Cisco",
        owner="Vendor Management",
    )
    assert isinstance(manufacturer, ManufacturerPb)
    assert manufacturer.name == "Cisco"
    assert isinstance(manufacturer.owner, OwnerPb)
    assert manufacturer.owner.name == "Vendor Management"


def test_platform_with_owner():
    """Check Platform instantiation with owner."""
    platform = Platform(
        name="IOS-XE",
        owner="Platform Team",
    )
    assert isinstance(platform, PlatformPb)
    assert platform.name == "IOS-XE"
    assert isinstance(platform.owner, OwnerPb)
    assert platform.owner.name == "Platform Team"


def test_convert_to_protobuf_owner():
    """Check convert_to_protobuf works with Owner."""
    result = convert_to_protobuf("Test Owner", OwnerPb)
    assert isinstance(result, OwnerPb)
    assert result.name == "Test Owner"


def test_convert_to_protobuf_owner_group():
    """Check convert_to_protobuf works with OwnerGroup."""
    result = convert_to_protobuf("Test Group", OwnerGroupPb)
    assert isinstance(result, OwnerGroupPb)
    assert result.name == "Test Group"
