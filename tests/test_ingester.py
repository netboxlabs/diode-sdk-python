#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs - Tests."""

# ruff: noqa: I001
from netboxlabs.diode.sdk.diode.v1.ingester_pb2 import (
    Device as DevicePb,
    DeviceType as DeviceTypePb,
    Entity as EntityPb,
    IPAddress as IPAddressPb,
    Interface as InterfacePb,
    Manufacturer as ManufacturerPb,
    Platform as PlatformPb,
    Prefix as PrefixPb,
    Role as RolePb,
    Site as SitePb,
    Tag as TagPb,
)
from netboxlabs.diode.sdk.ingester import (
    Device,
    DeviceType,
    Entity,
    IPAddress,
    Interface,
    Manufacturer,
    Platform,
    Prefix,
    Role,
    Site,
    Tag,
    convert_to_protobuf,
)


def test_convert_to_protobuf_returns_correct_class_when_value_is_string():
    """Check convert_to_protobuf returns correct class when value is string."""

    class MockProtobufClass:
        def __init__(self, name=None):
            self.name = name

    result = convert_to_protobuf("test", MockProtobufClass, name="test")
    assert isinstance(result, MockProtobufClass)
    assert result.name == "test"


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
    assert platform.name == "Platform1"
    assert platform.slug == "platform1"
    assert isinstance(platform.manufacturer, ManufacturerPb)
    assert platform.manufacturer.name == "Manufacturer1"
    assert platform.description == "This is a platform"
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
    assert platform.name == "Platform1"
    assert platform.slug == "platform1"
    assert isinstance(platform.manufacturer, ManufacturerPb)
    assert platform.manufacturer.name == "Manufacturer1"
    assert len(platform.tags) == 2
    for tag in platform.tags:
        assert isinstance(tag, TagPb)


def test_role_instantiation_with_all_fields():
    """Check Role instantiation with all fields."""
    role = Role(
        name="Admin",
        slug="admin",
        color="blue",
        description="Administrator role",
        tags=["admin", "role"],
    )
    assert isinstance(role, RolePb)
    assert role.name == "Admin"
    assert role.slug == "admin"
    assert role.color == "blue"
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
        device_fqdn="device1.example.com",
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
    assert device.device_fqdn == "device1.example.com"
    assert isinstance(device.role, RolePb)
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
        device_fqdn="device1.example.com",
        role=Role(name="Role1"),
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
    assert isinstance(device.device_type, DeviceTypePb)
    assert isinstance(device.role, RolePb)
    assert isinstance(device.platform, PlatformPb)
    assert isinstance(device.site, SitePb)
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
        mac_address="00:00:00:00:00:00",
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
    assert isinstance(interface.device.role, RolePb)
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
    assert interface.mac_address == "00:00:00:00:00:00"
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
        role=Role(name="Role1"),
        platform=Platform(name="Platform1"),
        site=Site(name="Site1"),
        manufacturer=Manufacturer(name="Manufacturer1"),
    )
    assert isinstance(interface, InterfacePb)
    assert isinstance(interface.device.device_type, DeviceTypePb)
    assert isinstance(interface.device.role, RolePb)
    assert isinstance(interface.device.platform, PlatformPb)
    assert isinstance(interface.device.site, SitePb)
    assert interface.device.platform.manufacturer.name == "Manufacturer1"
    assert interface.device.device_type.manufacturer.name == "Manufacturer1"


def test_ip_address_instantiation_with_all_fields():
    """Check IPAddress instantiation with all fields."""
    ip_address = IPAddress(
        address="192.168.0.1",
        interface="Interface1",
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
    assert isinstance(ip_address.interface, InterfacePb)
    assert ip_address.interface.name == "Interface1"
    assert isinstance(ip_address.interface.device, DevicePb)
    assert ip_address.interface.device.name == "Device1"
    assert isinstance(ip_address.interface.device.device_type, DeviceTypePb)
    assert ip_address.interface.device.device_type.model == "DeviceType1"
    assert isinstance(ip_address.interface.device.role, RolePb)
    assert ip_address.interface.device.role.name == "Role1"
    assert isinstance(ip_address.interface.device.platform, PlatformPb)
    assert ip_address.interface.device.platform.name == "Platform1"
    assert isinstance(ip_address.interface.device.platform.manufacturer, ManufacturerPb)
    assert ip_address.interface.device.platform.manufacturer.name == "Manufacturer1"
    assert isinstance(ip_address.interface.device.site, SitePb)
    assert ip_address.interface.device.site.name == "Site1"
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
        interface=Interface(
            name="Interface1",
            device=Device(
                name="Device1",
                device_type=DeviceType(
                    model="DeviceType1", manufacturer="Manufacturer1"
                ),
                role=Role(name="Role1"),
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
    assert isinstance(ip_address.interface, InterfacePb)
    assert isinstance(ip_address.interface.device, DevicePb)
    assert isinstance(ip_address.interface.device.device_type, DeviceTypePb)
    assert isinstance(ip_address.interface.device.role, RolePb)
    assert isinstance(ip_address.interface.device.platform, PlatformPb)
    assert isinstance(ip_address.interface.device.site, SitePb)
    assert ip_address.interface.device.platform.manufacturer.name == "Manufacturer1"
    assert ip_address.interface.device.device_type.manufacturer.name == "Manufacturer1"
    assert ip_address.status == "active"
    assert ip_address.dns_name == "dns.example.com"
    assert ip_address.description == "This is an IP address"
    assert ip_address.comments == "No comments"
    assert len(ip_address.tags) == 2


def test_ip_address_instantiation_with_manufacturer_populated_to_device_type_and_platform():
    """Check IPAddress instantiation with manufacturer populated to DeviceType and Platform."""
    ip_address = IPAddress(
        address="192.168.0.1",
        interface="Interface1",
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
    assert isinstance(ip_address.interface, InterfacePb)
    assert isinstance(ip_address.interface.device, DevicePb)
    assert isinstance(ip_address.interface.device.device_type, DeviceTypePb)
    assert isinstance(ip_address.interface.device.role, RolePb)
    assert isinstance(ip_address.interface.device.platform, PlatformPb)
    assert isinstance(ip_address.interface.device.site, SitePb)
    assert ip_address.interface.device.platform.manufacturer.name == "Manufacturer1"
    assert ip_address.interface.device.device_type.manufacturer.name == "Manufacturer1"
    assert ip_address.status == "active"
    assert ip_address.dns_name == "dns.example.com"


def test_prefix_instantiation_with_all_fields():
    """Check Prefix instantiation with all fields."""
    prefix = Prefix(
        prefix="192.168.0.0/24",
        site="Site1",
        status="active",
        is_pool=True,
        mark_utilized=False,
        comments="No comments",
        tags=["tag1", "tag2"],
    )
    assert isinstance(prefix, PrefixPb)
    assert prefix.prefix == "192.168.0.0/24"
    assert isinstance(prefix.site, SitePb)
    assert prefix.site.name == "Site1"
    assert prefix.status == "active"
    assert prefix.is_pool is True
    assert prefix.mark_utilized is False
    assert prefix.comments == "No comments"
    assert len(prefix.tags) == 2
    for tag in prefix.tags:
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
    assert isinstance(entity.device_role, RolePb)
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
