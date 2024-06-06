#!/usr/bin/env python
# Copyright 2024 NetBox Labs Inc
"""NetBox Labs, Diode - SDK - ingester protobuf message wrappers."""
from typing import Any

from google.protobuf import timestamp_pb2 as _timestamp_pb2

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


def convert_to_protobuf(value: Any, protobuf_class, **kwargs):
    """Convert a value to a protobuf message."""
    if isinstance(value, str):
        return protobuf_class(**kwargs)
    return value


class Tag:
    """Tag message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
    ) -> TagPb:
        """Create a new Tag protobuf message."""
        return TagPb(name=name, slug=slug, color=color)


class Manufacturer:
    """Manufacturer message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> ManufacturerPb:
        """Create a new Manufacturer protobuf message."""
        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return ManufacturerPb(
            name=name,
            slug=slug,
            description=description,
            tags=tags,
        )


class Platform:
    """Platform message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        manufacturer: str | Manufacturer | ManufacturerPb | None = None,
        description: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> PlatformPb:
        """Create a new Platform protobuf message."""
        manufacturer = convert_to_protobuf(
            manufacturer, ManufacturerPb, name=manufacturer
        )

        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return PlatformPb(
            name=name,
            slug=slug,
            manufacturer=manufacturer,
            description=description,
            tags=tags,
        )


class Role:
    """Role message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> RolePb:
        """Create a new Role protobuf message."""
        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return RolePb(
            name=name,
            slug=slug,
            color=color,
            description=description,
            tags=tags,
        )


class DeviceType:
    """DeviceType message wrapper."""

    def __new__(
        cls,
        model: str | None = None,
        slug: str | None = None,
        manufacturer: str | Manufacturer | ManufacturerPb | None = None,
        description: str | None = None,
        comments: str | None = None,
        part_number: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> DeviceTypePb:
        """Create a new DeviceType protobuf message."""
        manufacturer = convert_to_protobuf(
            manufacturer, ManufacturerPb, name=manufacturer
        )

        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return DeviceTypePb(
            model=model,
            slug=slug,
            manufacturer=manufacturer,
            description=description,
            comments=comments,
            part_number=part_number,
            tags=tags,
        )


class Device:
    """Device message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        device_type: str | DeviceType | DeviceTypePb | None = None,
        device_fqdn: str | None = None,
        role: str | Role | RolePb | None = None,
        platform: str | Platform | PlatformPb | None = None,
        serial: str | None = None,
        site: str | SitePb | None = None,
        asset_tag: str | None = None,
        status: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
        primary_ip4: str | IPAddressPb | None = None,
        primary_ip6: str | IPAddressPb | None = None,
        manufacturer: str | Manufacturer | ManufacturerPb | None = None,
    ) -> DevicePb:
        """Create a new Device protobuf message."""
        manufacturer = convert_to_protobuf(
            manufacturer, ManufacturerPb, name=manufacturer
        )
        platform = convert_to_protobuf(
            platform, PlatformPb, name=platform, manufacturer=manufacturer
        )

        if (
            isinstance(platform, PlatformPb)
            and not platform.HasField("manufacturer")
            and manufacturer is not None
        ):
            platform.manufacturer.CopyFrom(manufacturer)

        site = convert_to_protobuf(site, SitePb, name=site)
        device_type = convert_to_protobuf(
            device_type, DeviceTypePb, model=device_type, manufacturer=manufacturer
        )

        if (
            isinstance(device_type, DeviceTypePb)
            and not device_type.HasField("manufacturer")
            and manufacturer is not None
        ):
            device_type.manufacturer.CopyFrom(manufacturer)

        role = convert_to_protobuf(role, RolePb, name=role)

        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        primary_ip4 = convert_to_protobuf(primary_ip4, IPAddressPb, address=primary_ip4)
        primary_ip6 = convert_to_protobuf(primary_ip6, IPAddressPb, address=primary_ip6)

        return DevicePb(
            name=name,
            device_fqdn=device_fqdn,
            device_type=device_type,
            role=role,
            platform=platform,
            serial=serial,
            site=site,
            asset_tag=asset_tag,
            status=status,
            description=description,
            comments=comments,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            tags=tags,
        )


class Interface:
    """Interface message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        device: str | Device | DevicePb | None = None,
        device_type: str | DeviceType | DeviceTypePb | None = None,
        role: str | Role | RolePb | None = None,
        platform: str | Platform | PlatformPb | None = None,
        manufacturer: str | Manufacturer | ManufacturerPb | None = None,
        site: str | SitePb | None = None,
        type: str | None = None,
        enabled: bool | None = None,
        mtu: int | None = None,
        mac_address: str | None = None,
        speed: int | None = None,
        wwn: str | None = None,
        mgmt_only: bool | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        mode: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> InterfacePb:
        """Create a new Interface protobuf message."""
        manufacturer = convert_to_protobuf(
            manufacturer, ManufacturerPb, name=manufacturer
        )

        platform = convert_to_protobuf(
            platform, PlatformPb, name=platform, manufacturer=manufacturer
        )

        if (
            isinstance(platform, PlatformPb)
            and not platform.HasField("manufacturer")
            and manufacturer is not None
        ):
            platform.manufacturer.CopyFrom(manufacturer)

        site = convert_to_protobuf(site, SitePb, name=site)

        device_type = convert_to_protobuf(
            device_type, DeviceTypePb, model=device_type, manufacturer=manufacturer
        )

        if (
            isinstance(device_type, DeviceTypePb)
            and not device_type.HasField("manufacturer")
            and manufacturer is not None
        ):
            device_type.manufacturer.CopyFrom(manufacturer)

        role = convert_to_protobuf(role, RolePb, name=role)

        device = convert_to_protobuf(
            device,
            DevicePb,
            name=device,
            device_type=device_type,
            platform=platform,
            site=site,
            role=role,
        )

        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return InterfacePb(
            name=name,
            device=device,
            type=type,
            enabled=enabled,
            mtu=mtu,
            mac_address=mac_address,
            speed=speed,
            wwn=wwn,
            mgmt_only=mgmt_only,
            description=description,
            mark_connected=mark_connected,
            mode=mode,
            tags=tags,
        )


class IPAddress:
    """IPAddress message wrapper."""

    def __new__(
        cls,
        address: str | None = None,
        interface: str | Interface | InterfacePb | None = None,
        device: str | Device | DevicePb | None = None,
        device_type: str | DeviceType | DeviceTypePb | None = None,
        device_role: str | Role | RolePb | None = None,
        platform: str | Platform | PlatformPb | None = None,
        manufacturer: str | Manufacturer | ManufacturerPb | None = None,
        site: str | SitePb | None = None,
        status: str | None = None,
        role: str | None = None,
        dns_name: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> IPAddressPb:
        """Create a new IPAddress protobuf message."""
        manufacturer = convert_to_protobuf(
            manufacturer, ManufacturerPb, name=manufacturer
        )

        platform = convert_to_protobuf(
            platform, PlatformPb, name=platform, manufacturer=manufacturer
        )

        if (
            isinstance(platform, PlatformPb)
            and not platform.HasField("manufacturer")
            and manufacturer is not None
        ):
            platform.manufacturer.CopyFrom(manufacturer)

        site = convert_to_protobuf(site, SitePb, name=site)

        device_type = convert_to_protobuf(
            device_type, DeviceTypePb, model=device_type, manufacturer=manufacturer
        )

        if (
            isinstance(device_type, DeviceTypePb)
            and not device_type.HasField("manufacturer")
            and manufacturer is not None
        ):
            device_type.manufacturer.CopyFrom(manufacturer)

        device_role = convert_to_protobuf(device_role, RolePb, name=device_role)

        device = convert_to_protobuf(
            device,
            DevicePb,
            name=device,
            device_type=device_type,
            platform=platform,
            site=site,
            role=device_role,
        )

        interface = convert_to_protobuf(
            interface,
            InterfacePb,
            name=interface,
            device=device,
        )

        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return IPAddressPb(
            address=address,
            interface=interface,
            status=status,
            role=role,
            dns_name=dns_name,
            description=description,
            comments=comments,
            tags=tags,
        )


class Prefix:
    """Prefix message wrapper."""

    def __new__(
        cls,
        prefix: str | None = None,
        site: str | SitePb | None = None,
        status: str | None = None,
        is_pool: bool | None = None,
        mark_utilized: bool | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> PrefixPb:
        """Create a new Prefix protobuf message."""
        site = convert_to_protobuf(site, SitePb, name=site)

        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return PrefixPb(
            prefix=prefix,
            site=site,
            status=status,
            is_pool=is_pool,
            mark_utilized=mark_utilized,
            description=description,
            comments=comments,
            tags=tags,
        )


class Site:
    """Site message wrapper."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        status: str | None = None,
        facility: str | None = None,
        time_zone: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | TagPb] | None = None,
    ) -> SitePb:
        """Create a new Site protobuf message."""
        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = [TagPb(name=tag) for tag in tags]

        return SitePb(
            name=name,
            slug=slug,
            status=status,
            facility=facility,
            time_zone=time_zone,
            description=description,
            comments=comments,
            tags=tags,
        )


class Entity:
    """Entity message wrapper."""

    def __new__(
        cls,
        site: str | Site | SitePb | None = None,
        platform: str | Platform | PlatformPb | None = None,
        manufacturer: str | Manufacturer | ManufacturerPb | None = None,
        device: str | Device | DevicePb | None = None,
        device_role: str | Role | RolePb | None = None,
        device_type: str | DeviceType | DeviceTypePb | None = None,
        interface: str | Interface | InterfacePb | None = None,
        ip_address: str | IPAddress | IPAddressPb | None = None,
        prefix: str | Prefix | PrefixPb | None = None,
        timestamp: _timestamp_pb2.Timestamp | None = None,
    ):
        """Create a new Entity protobuf message."""
        site = convert_to_protobuf(site, SitePb, name=site)
        platform = convert_to_protobuf(platform, PlatformPb, name=platform)
        manufacturer = convert_to_protobuf(
            manufacturer, ManufacturerPb, name=manufacturer
        )
        device = convert_to_protobuf(device, DevicePb, name=device)
        device_role = convert_to_protobuf(device_role, RolePb, name=device_role)
        device_type = convert_to_protobuf(device_type, DeviceTypePb, model=device_type)
        ip_address = convert_to_protobuf(ip_address, IPAddressPb, address=ip_address)
        interface = convert_to_protobuf(interface, InterfacePb, name=interface)
        prefix = convert_to_protobuf(prefix, PrefixPb, prefix=prefix)

        return EntityPb(
            site=site,
            platform=platform,
            manufacturer=manufacturer,
            device=device,
            device_role=device_role,
            device_type=device_type,
            interface=interface,
            ip_address=ip_address,
            prefix=prefix,
            timestamp=timestamp,
        )
