"""Python SDK wrappers for the Diode protobuf schema."""

#
# Generated code. DO NOT EDIT.
# Timestamp: 2025-04-10 14:44:19Z
#
# ruff: noqa: C901

from __future__ import annotations

import datetime
import re
from typing import Any

from google.protobuf import timestamp_pb2 as _timestamp_pb2

import netboxlabs.diode.sdk.diode.v1.ingester_pb2 as pb

PRIMARY_VALUE_MAP = {
    'ASN': 'asn',
    'ASNRange': 'name',
    'Circuit': 'cid',
    'CircuitGroup': 'name',
    'CircuitType': 'name',
    'Cluster': 'name',
    'ClusterGroup': 'name',
    'ClusterType': 'name',
    'ConsolePort': 'name',
    'ConsoleServerPort': 'name',
    'Contact': 'name',
    'ContactGroup': 'name',
    'ContactRole': 'name',
    'Device': 'name',
    'DeviceBay': 'name',
    'DeviceRole': 'name',
    'DeviceType': 'model',
    'FHRPGroup': 'name',
    'FrontPort': 'name',
    'IKEPolicy': 'name',
    'IKEProposal': 'name',
    'IPAddress': 'address',
    'IPSecPolicy': 'name',
    'IPSecProfile': 'name',
    'IPSecProposal': 'name',
    'Interface': 'name',
    'InventoryItem': 'name',
    'InventoryItemRole': 'name',
    'L2VPN': 'name',
    'Location': 'name',
    'MACAddress': 'mac_address',
    'Manufacturer': 'name',
    'ModuleBay': 'name',
    'ModuleType': 'model',
    'Platform': 'name',
    'PowerFeed': 'name',
    'PowerOutlet': 'name',
    'PowerPanel': 'name',
    'PowerPort': 'name',
    'Prefix': 'prefix',
    'Provider': 'name',
    'ProviderAccount': 'name',
    'ProviderNetwork': 'name',
    'RIR': 'name',
    'Rack': 'name',
    'RackRole': 'name',
    'RackType': 'model',
    'RearPort': 'name',
    'Region': 'name',
    'Role': 'name',
    'RouteTarget': 'name',
    'Service': 'name',
    'Site': 'name',
    'SiteGroup': 'name',
    'Tag': 'name',
    'Tenant': 'name',
    'TenantGroup': 'name',
    'Tunnel': 'name',
    'TunnelGroup': 'name',
    'VLAN': 'name',
    'VLANGroup': 'name',
    'VLANTranslationPolicy': 'name',
    'VMInterface': 'name',
    'VRF': 'name',
    'VirtualChassis': 'name',
    'VirtualCircuit': 'cid',
    'VirtualCircuitType': 'name',
    'VirtualDeviceContext': 'name',
    'VirtualDisk': 'name',
    'VirtualMachine': 'name',
    'WirelessLAN': 'ssid',
    'WirelessLANGroup': 'name',
}


def slugify(value: Any) -> str:
    """Utility to convert a value to a slug."""
    value = str(value).strip().strip('_').lower()
    value = re.sub(r'[^\w\s-]', '', value)
    return re.sub(r'[-\s]+', '-', value)


def is_field_set(value: Any, field_name: str) -> bool:
    """Check if a protobuf field is set. HasField() only works for message fields in proto3."""
    if value is None:
        return False
    for field_descriptor, _ in value.ListFields():
        if field_descriptor.name == field_name:
            return True
    return False


def convert_to_protobuf(value: Any, protobuf_class):
    """Convert a value to a protobuf message."""
    if value is None:
        return None
    if isinstance(value, str|int|float):
        pvk = PRIMARY_VALUE_MAP.get(protobuf_class.__name__)
        if pvk is None:
            raise ValueError(f'{protobuf_class.__name__} cannot be initialized with {type(value)}')
        kwargs = {pvk: value}
        value = protobuf_class(**kwargs)
    return value


def convert_to_protobuf_list(value: list | None, protobuf_class):
    """Convert a list of values to a list of protobuf messages."""
    if value is None:
        return None
    return [convert_to_protobuf(x, protobuf_class) for x in value]


def convert_to_protobuf_dict(value: dict | None, protobuf_class):
    """Convert a dictionary of values to a dictionary of protobuf messages."""
    if value is None:
        return None
    return {k: convert_to_protobuf(v, protobuf_class) for k, v in value.items()}


class Entity:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Entity."""

    def __new__(
        cls,
        timestamp: datetime.datetime | None = None,
        asn: str | ASN | pb.ASN | None = None,
        asn_range: str | ASNRange | pb.ASNRange | None = None,
        aggregate: str | Aggregate | pb.Aggregate | None = None,
        cable: str | Cable | pb.Cable | None = None,
        cable_path: str | CablePath | pb.CablePath | None = None,
        cable_termination: str | CableTermination | pb.CableTermination | None = None,
        circuit: str | Circuit | pb.Circuit | None = None,
        circuit_group: str | CircuitGroup | pb.CircuitGroup | None = None,
        circuit_group_assignment: str | CircuitGroupAssignment | pb.CircuitGroupAssignment | None = None,
        circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        circuit_type: str | CircuitType | pb.CircuitType | None = None,
        cluster: str | Cluster | pb.Cluster | None = None,
        cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        cluster_type: str | ClusterType | pb.ClusterType | None = None,
        console_port: str | ConsolePort | pb.ConsolePort | None = None,
        console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        contact: str | Contact | pb.Contact | None = None,
        contact_assignment: str | ContactAssignment | pb.ContactAssignment | None = None,
        contact_group: str | ContactGroup | pb.ContactGroup | None = None,
        contact_role: str | ContactRole | pb.ContactRole | None = None,
        device: str | Device | pb.Device | None = None,
        device_bay: str | DeviceBay | pb.DeviceBay | None = None,
        device_role: str | DeviceRole | pb.DeviceRole | None = None,
        device_type: str | DeviceType | pb.DeviceType | None = None,
        fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        fhrp_group_assignment: str | FHRPGroupAssignment | pb.FHRPGroupAssignment | None = None,
        front_port: str | FrontPort | pb.FrontPort | None = None,
        ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        ike_proposal: str | IKEProposal | pb.IKEProposal | None = None,
        ip_address: str | IPAddress | pb.IPAddress | None = None,
        ip_range: str | IPRange | pb.IPRange | None = None,
        ip_sec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        ip_sec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        ip_sec_proposal: str | IPSecProposal | pb.IPSecProposal | None = None,
        interface: str | Interface | pb.Interface | None = None,
        inventory_item: str | InventoryItem | pb.InventoryItem | None = None,
        inventory_item_role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        l2vpn: str | L2VPN | pb.L2VPN | None = None,
        l2vpn_termination: str | L2VPNTermination | pb.L2VPNTermination | None = None,
        location: str | Location | pb.Location | None = None,
        mac_address: str | MACAddress | pb.MACAddress | None = None,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        module: str | Module | pb.Module | None = None,
        module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        module_type: str | ModuleType | pb.ModuleType | None = None,
        platform: str | Platform | pb.Platform | None = None,
        power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        power_port: str | PowerPort | pb.PowerPort | None = None,
        prefix: str | Prefix | pb.Prefix | None = None,
        provider: str | Provider | pb.Provider | None = None,
        provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        rir: str | RIR | pb.RIR | None = None,
        rack: str | Rack | pb.Rack | None = None,
        rack_reservation: str | RackReservation | pb.RackReservation | None = None,
        rack_role: str | RackRole | pb.RackRole | None = None,
        rack_type: str | RackType | pb.RackType | None = None,
        rear_port: str | RearPort | pb.RearPort | None = None,
        region: str | Region | pb.Region | None = None,
        role: str | Role | pb.Role | None = None,
        route_target: str | RouteTarget | pb.RouteTarget | None = None,
        service: str | Service | pb.Service | None = None,
        site: str | Site | pb.Site | None = None,
        site_group: str | SiteGroup | pb.SiteGroup | None = None,
        tag: str | Tag | pb.Tag | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        tenant_group: str | TenantGroup | pb.TenantGroup | None = None,
        tunnel: str | Tunnel | pb.Tunnel | None = None,
        tunnel_group: str | TunnelGroup | pb.TunnelGroup | None = None,
        tunnel_termination: str | TunnelTermination | pb.TunnelTermination | None = None,
        vlan: str | VLAN | pb.VLAN | None = None,
        vlan_group: str | VLANGroup | pb.VLANGroup | None = None,
        vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        vlan_translation_rule: str | VLANTranslationRule | pb.VLANTranslationRule | None = None,
        vm_interface: str | VMInterface | pb.VMInterface | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        virtual_circuit_termination: str | VirtualCircuitTermination | pb.VirtualCircuitTermination | None = None,
        virtual_circuit_type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        virtual_device_context: str | VirtualDeviceContext | pb.VirtualDeviceContext | None = None,
        virtual_disk: str | VirtualDisk | pb.VirtualDisk | None = None,
        virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        wireless_lan: str | WirelessLAN | pb.WirelessLAN | None = None,
        wireless_lan_group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        wireless_link: str | WirelessLink | pb.WirelessLink | None = None,
    ) -> pb.Entity:
        """Create a new Entity."""
        asn = convert_to_protobuf(asn, pb.ASN)
        asn_range = convert_to_protobuf(asn_range, pb.ASNRange)
        aggregate = convert_to_protobuf(aggregate, pb.Aggregate)
        cable = convert_to_protobuf(cable, pb.Cable)
        cable_path = convert_to_protobuf(cable_path, pb.CablePath)
        cable_termination = convert_to_protobuf(cable_termination, pb.CableTermination)
        circuit = convert_to_protobuf(circuit, pb.Circuit)
        circuit_group = convert_to_protobuf(circuit_group, pb.CircuitGroup)
        circuit_group_assignment = convert_to_protobuf(circuit_group_assignment, pb.CircuitGroupAssignment)
        circuit_termination = convert_to_protobuf(circuit_termination, pb.CircuitTermination)
        circuit_type = convert_to_protobuf(circuit_type, pb.CircuitType)
        cluster = convert_to_protobuf(cluster, pb.Cluster)
        cluster_group = convert_to_protobuf(cluster_group, pb.ClusterGroup)
        cluster_type = convert_to_protobuf(cluster_type, pb.ClusterType)
        console_port = convert_to_protobuf(console_port, pb.ConsolePort)
        console_server_port = convert_to_protobuf(console_server_port, pb.ConsoleServerPort)
        contact = convert_to_protobuf(contact, pb.Contact)
        contact_assignment = convert_to_protobuf(contact_assignment, pb.ContactAssignment)
        contact_group = convert_to_protobuf(contact_group, pb.ContactGroup)
        contact_role = convert_to_protobuf(contact_role, pb.ContactRole)
        device = convert_to_protobuf(device, pb.Device)
        device_bay = convert_to_protobuf(device_bay, pb.DeviceBay)
        device_role = convert_to_protobuf(device_role, pb.DeviceRole)
        device_type = convert_to_protobuf(device_type, pb.DeviceType)
        fhrp_group = convert_to_protobuf(fhrp_group, pb.FHRPGroup)
        fhrp_group_assignment = convert_to_protobuf(fhrp_group_assignment, pb.FHRPGroupAssignment)
        front_port = convert_to_protobuf(front_port, pb.FrontPort)
        ike_policy = convert_to_protobuf(ike_policy, pb.IKEPolicy)
        ike_proposal = convert_to_protobuf(ike_proposal, pb.IKEProposal)
        ip_address = convert_to_protobuf(ip_address, pb.IPAddress)
        ip_range = convert_to_protobuf(ip_range, pb.IPRange)
        ip_sec_policy = convert_to_protobuf(ip_sec_policy, pb.IPSecPolicy)
        ip_sec_profile = convert_to_protobuf(ip_sec_profile, pb.IPSecProfile)
        ip_sec_proposal = convert_to_protobuf(ip_sec_proposal, pb.IPSecProposal)
        interface = convert_to_protobuf(interface, pb.Interface)
        inventory_item = convert_to_protobuf(inventory_item, pb.InventoryItem)
        inventory_item_role = convert_to_protobuf(inventory_item_role, pb.InventoryItemRole)
        l2vpn = convert_to_protobuf(l2vpn, pb.L2VPN)
        l2vpn_termination = convert_to_protobuf(l2vpn_termination, pb.L2VPNTermination)
        location = convert_to_protobuf(location, pb.Location)
        mac_address = convert_to_protobuf(mac_address, pb.MACAddress)
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        module = convert_to_protobuf(module, pb.Module)
        module_bay = convert_to_protobuf(module_bay, pb.ModuleBay)
        module_type = convert_to_protobuf(module_type, pb.ModuleType)
        platform = convert_to_protobuf(platform, pb.Platform)
        power_feed = convert_to_protobuf(power_feed, pb.PowerFeed)
        power_outlet = convert_to_protobuf(power_outlet, pb.PowerOutlet)
        power_panel = convert_to_protobuf(power_panel, pb.PowerPanel)
        power_port = convert_to_protobuf(power_port, pb.PowerPort)
        prefix = convert_to_protobuf(prefix, pb.Prefix)
        provider = convert_to_protobuf(provider, pb.Provider)
        provider_account = convert_to_protobuf(provider_account, pb.ProviderAccount)
        provider_network = convert_to_protobuf(provider_network, pb.ProviderNetwork)
        rir = convert_to_protobuf(rir, pb.RIR)
        rack = convert_to_protobuf(rack, pb.Rack)
        rack_reservation = convert_to_protobuf(rack_reservation, pb.RackReservation)
        rack_role = convert_to_protobuf(rack_role, pb.RackRole)
        rack_type = convert_to_protobuf(rack_type, pb.RackType)
        rear_port = convert_to_protobuf(rear_port, pb.RearPort)
        region = convert_to_protobuf(region, pb.Region)
        role = convert_to_protobuf(role, pb.Role)
        route_target = convert_to_protobuf(route_target, pb.RouteTarget)
        service = convert_to_protobuf(service, pb.Service)
        site = convert_to_protobuf(site, pb.Site)
        site_group = convert_to_protobuf(site_group, pb.SiteGroup)
        tag = convert_to_protobuf(tag, pb.Tag)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tenant_group = convert_to_protobuf(tenant_group, pb.TenantGroup)
        tunnel = convert_to_protobuf(tunnel, pb.Tunnel)
        tunnel_group = convert_to_protobuf(tunnel_group, pb.TunnelGroup)
        tunnel_termination = convert_to_protobuf(tunnel_termination, pb.TunnelTermination)
        vlan = convert_to_protobuf(vlan, pb.VLAN)
        vlan_group = convert_to_protobuf(vlan_group, pb.VLANGroup)
        vlan_translation_policy = convert_to_protobuf(vlan_translation_policy, pb.VLANTranslationPolicy)
        vlan_translation_rule = convert_to_protobuf(vlan_translation_rule, pb.VLANTranslationRule)
        vm_interface = convert_to_protobuf(vm_interface, pb.VMInterface)
        vrf = convert_to_protobuf(vrf, pb.VRF)
        virtual_chassis = convert_to_protobuf(virtual_chassis, pb.VirtualChassis)
        virtual_circuit = convert_to_protobuf(virtual_circuit, pb.VirtualCircuit)
        virtual_circuit_termination = convert_to_protobuf(virtual_circuit_termination, pb.VirtualCircuitTermination)
        virtual_circuit_type = convert_to_protobuf(virtual_circuit_type, pb.VirtualCircuitType)
        virtual_device_context = convert_to_protobuf(virtual_device_context, pb.VirtualDeviceContext)
        virtual_disk = convert_to_protobuf(virtual_disk, pb.VirtualDisk)
        virtual_machine = convert_to_protobuf(virtual_machine, pb.VirtualMachine)
        wireless_lan = convert_to_protobuf(wireless_lan, pb.WirelessLAN)
        wireless_lan_group = convert_to_protobuf(wireless_lan_group, pb.WirelessLANGroup)
        wireless_link = convert_to_protobuf(wireless_link, pb.WirelessLink)
        if timestamp is None:
            ts = _timestamp_pb2.Timestamp()
            ts.GetCurrentTime()
            timestamp = ts
        return pb.Entity(
            timestamp=timestamp,
            asn=asn,
            asn_range=asn_range,
            aggregate=aggregate,
            cable=cable,
            cable_path=cable_path,
            cable_termination=cable_termination,
            circuit=circuit,
            circuit_group=circuit_group,
            circuit_group_assignment=circuit_group_assignment,
            circuit_termination=circuit_termination,
            circuit_type=circuit_type,
            cluster=cluster,
            cluster_group=cluster_group,
            cluster_type=cluster_type,
            console_port=console_port,
            console_server_port=console_server_port,
            contact=contact,
            contact_assignment=contact_assignment,
            contact_group=contact_group,
            contact_role=contact_role,
            device=device,
            device_bay=device_bay,
            device_role=device_role,
            device_type=device_type,
            fhrp_group=fhrp_group,
            fhrp_group_assignment=fhrp_group_assignment,
            front_port=front_port,
            ike_policy=ike_policy,
            ike_proposal=ike_proposal,
            ip_address=ip_address,
            ip_range=ip_range,
            ip_sec_policy=ip_sec_policy,
            ip_sec_profile=ip_sec_profile,
            ip_sec_proposal=ip_sec_proposal,
            interface=interface,
            inventory_item=inventory_item,
            inventory_item_role=inventory_item_role,
            l2vpn=l2vpn,
            l2vpn_termination=l2vpn_termination,
            location=location,
            mac_address=mac_address,
            manufacturer=manufacturer,
            module=module,
            module_bay=module_bay,
            module_type=module_type,
            platform=platform,
            power_feed=power_feed,
            power_outlet=power_outlet,
            power_panel=power_panel,
            power_port=power_port,
            prefix=prefix,
            provider=provider,
            provider_account=provider_account,
            provider_network=provider_network,
            rir=rir,
            rack=rack,
            rack_reservation=rack_reservation,
            rack_role=rack_role,
            rack_type=rack_type,
            rear_port=rear_port,
            region=region,
            role=role,
            route_target=route_target,
            service=service,
            site=site,
            site_group=site_group,
            tag=tag,
            tenant=tenant,
            tenant_group=tenant_group,
            tunnel=tunnel,
            tunnel_group=tunnel_group,
            tunnel_termination=tunnel_termination,
            vlan=vlan,
            vlan_group=vlan_group,
            vlan_translation_policy=vlan_translation_policy,
            vlan_translation_rule=vlan_translation_rule,
            vm_interface=vm_interface,
            vrf=vrf,
            virtual_chassis=virtual_chassis,
            virtual_circuit=virtual_circuit,
            virtual_circuit_termination=virtual_circuit_termination,
            virtual_circuit_type=virtual_circuit_type,
            virtual_device_context=virtual_device_context,
            virtual_disk=virtual_disk,
            virtual_machine=virtual_machine,
            wireless_lan=wireless_lan,
            wireless_lan_group=wireless_lan_group,
            wireless_link=wireless_link,
        )


class ASN:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ASN."""

    def __new__(
        cls,
        asn: int | None = None,
        rir: str | RIR | pb.RIR | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ASN:
        """Create a new ASN."""
        rir = convert_to_protobuf(rir, pb.RIR)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ASN(
            asn=asn,
            rir=rir,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class ASNRange:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ASNRange."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        rir: str | RIR | pb.RIR | None = None,
        start: int | None = None,
        end: int | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ASNRange:
        """Create a new ASNRange."""
        rir = convert_to_protobuf(rir, pb.RIR)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ASNRange(
            name=name,
            slug=slug,
            rir=rir,
            start=start,
            end=end,
            tenant=tenant,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Aggregate:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Aggregate."""

    def __new__(
        cls,
        prefix: str | None = None,
        rir: str | RIR | pb.RIR | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        date_added: datetime.datetime | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Aggregate:
        """Create a new Aggregate."""
        rir = convert_to_protobuf(rir, pb.RIR)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Aggregate(
            prefix=prefix,
            rir=rir,
            tenant=tenant,
            date_added=date_added,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class Cable:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Cable."""

    def __new__(
        cls,
        type: str | None = None,
        a_terminations: list[str | GenericObject | pb.GenericObject] | None = None,
        b_terminations: list[str | GenericObject | pb.GenericObject] | None = None,
        status: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        label: str | None = None,
        color: str | None = None,
        length: float | None = None,
        length_unit: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Cable:
        """Create a new Cable."""
        a_terminations = convert_to_protobuf_list(a_terminations, pb.GenericObject)
        b_terminations = convert_to_protobuf_list(b_terminations, pb.GenericObject)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Cable(
            type=type,
            a_terminations=a_terminations,
            b_terminations=b_terminations,
            status=status,
            tenant=tenant,
            label=label,
            color=color,
            length=length,
            length_unit=length_unit,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class CablePath:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CablePath."""

    def __new__(
        cls,
        is_active: bool | None = None,
        is_complete: bool | None = None,
        is_split: bool | None = None,
    ) -> pb.CablePath:
        """Create a new CablePath."""
        return pb.CablePath(
            is_active=is_active,
            is_complete=is_complete,
            is_split=is_split,
        )


class CableTermination:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CableTermination."""

    def __new__(
        cls,
        cable: str | Cable | pb.Cable | None = None,
        cable_end: str | None = None,
        termination_circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        termination_console_port: str | ConsolePort | pb.ConsolePort | None = None,
        termination_console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        termination_front_port: str | FrontPort | pb.FrontPort | None = None,
        termination_interface: str | Interface | pb.Interface | None = None,
        termination_power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        termination_power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        termination_power_port: str | PowerPort | pb.PowerPort | None = None,
        termination_rear_port: str | RearPort | pb.RearPort | None = None,
    ) -> pb.CableTermination:
        """Create a new CableTermination."""
        cable = convert_to_protobuf(cable, pb.Cable)
        termination_circuit_termination = convert_to_protobuf(termination_circuit_termination, pb.CircuitTermination)
        termination_console_port = convert_to_protobuf(termination_console_port, pb.ConsolePort)
        termination_console_server_port = convert_to_protobuf(termination_console_server_port, pb.ConsoleServerPort)
        termination_front_port = convert_to_protobuf(termination_front_port, pb.FrontPort)
        termination_interface = convert_to_protobuf(termination_interface, pb.Interface)
        termination_power_feed = convert_to_protobuf(termination_power_feed, pb.PowerFeed)
        termination_power_outlet = convert_to_protobuf(termination_power_outlet, pb.PowerOutlet)
        termination_power_port = convert_to_protobuf(termination_power_port, pb.PowerPort)
        termination_rear_port = convert_to_protobuf(termination_rear_port, pb.RearPort)
        return pb.CableTermination(
            cable=cable,
            cable_end=cable_end,
            termination_circuit_termination=termination_circuit_termination,
            termination_console_port=termination_console_port,
            termination_console_server_port=termination_console_server_port,
            termination_front_port=termination_front_port,
            termination_interface=termination_interface,
            termination_power_feed=termination_power_feed,
            termination_power_outlet=termination_power_outlet,
            termination_power_port=termination_power_port,
            termination_rear_port=termination_rear_port,
        )


class Circuit:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Circuit."""

    def __new__(
        cls,
        cid: str | None = None,
        provider: str | Provider | pb.Provider | None = None,
        provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        type: str | CircuitType | pb.CircuitType | None = None,
        status: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        install_date: datetime.datetime | None = None,
        termination_date: datetime.datetime | None = None,
        commit_rate: int | None = None,
        description: str | None = None,
        distance: float | None = None,
        distance_unit: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        assignments: list[str | CircuitGroupAssignment | pb.CircuitGroupAssignment] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Circuit:
        """Create a new Circuit."""
        provider = convert_to_protobuf(provider, pb.Provider)
        provider_account = convert_to_protobuf(provider_account, pb.ProviderAccount)
        type = convert_to_protobuf(type, pb.CircuitType)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        assignments = convert_to_protobuf_list(assignments, pb.CircuitGroupAssignment)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Circuit(
            cid=cid,
            provider=provider,
            provider_account=provider_account,
            type=type,
            status=status,
            tenant=tenant,
            install_date=install_date,
            termination_date=termination_date,
            commit_rate=commit_rate,
            description=description,
            distance=distance,
            distance_unit=distance_unit,
            comments=comments,
            tags=tags,
            assignments=assignments,
            custom_fields=custom_fields,
        )


class CircuitGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CircuitGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.CircuitGroup:
        """Create a new CircuitGroup."""
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.CircuitGroup(
            name=name,
            slug=slug,
            description=description,
            tenant=tenant,
            tags=tags,
            custom_fields=custom_fields,
        )


class CircuitGroupAssignment:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CircuitGroupAssignment."""

    def __new__(
        cls,
        group: str | CircuitGroup | pb.CircuitGroup | None = None,
        member_circuit: str | Circuit | pb.Circuit | None = None,
        member_virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        priority: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
    ) -> pb.CircuitGroupAssignment:
        """Create a new CircuitGroupAssignment."""
        group = convert_to_protobuf(group, pb.CircuitGroup)
        member_circuit = convert_to_protobuf(member_circuit, pb.Circuit)
        member_virtual_circuit = convert_to_protobuf(member_virtual_circuit, pb.VirtualCircuit)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        return pb.CircuitGroupAssignment(
            group=group,
            member_circuit=member_circuit,
            member_virtual_circuit=member_virtual_circuit,
            priority=priority,
            tags=tags,
        )


class CircuitTermination:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CircuitTermination."""

    def __new__(
        cls,
        circuit: str | Circuit | pb.Circuit | None = None,
        term_side: str | None = None,
        termination_location: str | Location | pb.Location | None = None,
        termination_provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        termination_region: str | Region | pb.Region | None = None,
        termination_site: str | Site | pb.Site | None = None,
        termination_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        port_speed: int | None = None,
        upstream_speed: int | None = None,
        xconnect_id: str | None = None,
        pp_info: str | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.CircuitTermination:
        """Create a new CircuitTermination."""
        circuit = convert_to_protobuf(circuit, pb.Circuit)
        termination_location = convert_to_protobuf(termination_location, pb.Location)
        termination_provider_network = convert_to_protobuf(termination_provider_network, pb.ProviderNetwork)
        termination_region = convert_to_protobuf(termination_region, pb.Region)
        termination_site = convert_to_protobuf(termination_site, pb.Site)
        termination_site_group = convert_to_protobuf(termination_site_group, pb.SiteGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.CircuitTermination(
            circuit=circuit,
            term_side=term_side,
            termination_location=termination_location,
            termination_provider_network=termination_provider_network,
            termination_region=termination_region,
            termination_site=termination_site,
            termination_site_group=termination_site_group,
            port_speed=port_speed,
            upstream_speed=upstream_speed,
            xconnect_id=xconnect_id,
            pp_info=pp_info,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class CircuitType:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CircuitType."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.CircuitType:
        """Create a new CircuitType."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.CircuitType(
            name=name,
            slug=slug,
            color=color,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Cluster:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Cluster."""

    def __new__(
        cls,
        name: str | None = None,
        type: str | ClusterType | pb.ClusterType | None = None,
        group: str | ClusterGroup | pb.ClusterGroup | None = None,
        status: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        scope_location: str | Location | pb.Location | None = None,
        scope_region: str | Region | pb.Region | None = None,
        scope_site: str | Site | pb.Site | None = None,
        scope_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Cluster:
        """Create a new Cluster."""
        type = convert_to_protobuf(type, pb.ClusterType)
        group = convert_to_protobuf(group, pb.ClusterGroup)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        scope_location = convert_to_protobuf(scope_location, pb.Location)
        scope_region = convert_to_protobuf(scope_region, pb.Region)
        scope_site = convert_to_protobuf(scope_site, pb.Site)
        scope_site_group = convert_to_protobuf(scope_site_group, pb.SiteGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Cluster(
            name=name,
            type=type,
            group=group,
            status=status,
            tenant=tenant,
            scope_location=scope_location,
            scope_region=scope_region,
            scope_site=scope_site,
            scope_site_group=scope_site_group,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class ClusterGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ClusterGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ClusterGroup:
        """Create a new ClusterGroup."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ClusterGroup(
            name=name,
            slug=slug,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class ClusterType:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ClusterType."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ClusterType:
        """Create a new ClusterType."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ClusterType(
            name=name,
            slug=slug,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class ConsolePort:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ConsolePort."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        speed: int | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ConsolePort:
        """Create a new ConsolePort."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ConsolePort(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            speed=speed,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class ConsoleServerPort:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ConsoleServerPort."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        speed: int | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ConsoleServerPort:
        """Create a new ConsoleServerPort."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ConsoleServerPort(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            speed=speed,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class Contact:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Contact."""

    def __new__(
        cls,
        group: str | ContactGroup | pb.ContactGroup | None = None,
        name: str | None = None,
        title: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        address: str | None = None,
        link: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Contact:
        """Create a new Contact."""
        group = convert_to_protobuf(group, pb.ContactGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Contact(
            group=group,
            name=name,
            title=title,
            phone=phone,
            email=email,
            address=address,
            link=link,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class ContactAssignment:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ContactAssignment."""

    def __new__(
        cls,
        object_asn: str | ASN | pb.ASN | None = None,
        object_asn_range: str | ASNRange | pb.ASNRange | None = None,
        object_aggregate: str | Aggregate | pb.Aggregate | None = None,
        object_cable: str | Cable | pb.Cable | None = None,
        object_cable_path: str | CablePath | pb.CablePath | None = None,
        object_cable_termination: str | CableTermination | pb.CableTermination | None = None,
        object_circuit: str | Circuit | pb.Circuit | None = None,
        object_circuit_group: str | CircuitGroup | pb.CircuitGroup | None = None,
        object_circuit_group_assignment: str | CircuitGroupAssignment | pb.CircuitGroupAssignment | None = None,
        object_circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        object_circuit_type: str | CircuitType | pb.CircuitType | None = None,
        object_cluster: str | Cluster | pb.Cluster | None = None,
        object_cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        object_cluster_type: str | ClusterType | pb.ClusterType | None = None,
        object_console_port: str | ConsolePort | pb.ConsolePort | None = None,
        object_console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        object_contact: str | Contact | pb.Contact | None = None,
        object_contact_assignment: str | ContactAssignment | pb.ContactAssignment | None = None,
        object_contact_group: str | ContactGroup | pb.ContactGroup | None = None,
        object_contact_role: str | ContactRole | pb.ContactRole | None = None,
        object_device: str | Device | pb.Device | None = None,
        object_device_bay: str | DeviceBay | pb.DeviceBay | None = None,
        object_device_role: str | DeviceRole | pb.DeviceRole | None = None,
        object_device_type: str | DeviceType | pb.DeviceType | None = None,
        object_fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        object_fhrp_group_assignment: str | FHRPGroupAssignment | pb.FHRPGroupAssignment | None = None,
        object_front_port: str | FrontPort | pb.FrontPort | None = None,
        object_ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        object_ike_proposal: str | IKEProposal | pb.IKEProposal | None = None,
        object_ip_address: str | IPAddress | pb.IPAddress | None = None,
        object_ip_range: str | IPRange | pb.IPRange | None = None,
        object_ip_sec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        object_ip_sec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        object_ip_sec_proposal: str | IPSecProposal | pb.IPSecProposal | None = None,
        object_interface: str | Interface | pb.Interface | None = None,
        object_inventory_item: str | InventoryItem | pb.InventoryItem | None = None,
        object_inventory_item_role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        object_l2vpn: str | L2VPN | pb.L2VPN | None = None,
        object_l2vpn_termination: str | L2VPNTermination | pb.L2VPNTermination | None = None,
        object_location: str | Location | pb.Location | None = None,
        object_mac_address: str | MACAddress | pb.MACAddress | None = None,
        object_manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        object_module: str | Module | pb.Module | None = None,
        object_module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        object_module_type: str | ModuleType | pb.ModuleType | None = None,
        object_platform: str | Platform | pb.Platform | None = None,
        object_power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        object_power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        object_power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        object_power_port: str | PowerPort | pb.PowerPort | None = None,
        object_prefix: str | Prefix | pb.Prefix | None = None,
        object_provider: str | Provider | pb.Provider | None = None,
        object_provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        object_provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        object_rir: str | RIR | pb.RIR | None = None,
        object_rack: str | Rack | pb.Rack | None = None,
        object_rack_reservation: str | RackReservation | pb.RackReservation | None = None,
        object_rack_role: str | RackRole | pb.RackRole | None = None,
        object_rack_type: str | RackType | pb.RackType | None = None,
        object_rear_port: str | RearPort | pb.RearPort | None = None,
        object_region: str | Region | pb.Region | None = None,
        object_role: str | Role | pb.Role | None = None,
        object_route_target: str | RouteTarget | pb.RouteTarget | None = None,
        object_service: str | Service | pb.Service | None = None,
        object_site: str | Site | pb.Site | None = None,
        object_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        object_tag: str | Tag | pb.Tag | None = None,
        object_tenant: str | Tenant | pb.Tenant | None = None,
        object_tenant_group: str | TenantGroup | pb.TenantGroup | None = None,
        object_tunnel: str | Tunnel | pb.Tunnel | None = None,
        object_tunnel_group: str | TunnelGroup | pb.TunnelGroup | None = None,
        object_tunnel_termination: str | TunnelTermination | pb.TunnelTermination | None = None,
        object_vlan: str | VLAN | pb.VLAN | None = None,
        object_vlan_group: str | VLANGroup | pb.VLANGroup | None = None,
        object_vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        object_vlan_translation_rule: str | VLANTranslationRule | pb.VLANTranslationRule | None = None,
        object_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        object_vrf: str | VRF | pb.VRF | None = None,
        object_virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        object_virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        object_virtual_circuit_termination: str | VirtualCircuitTermination | pb.VirtualCircuitTermination | None = None,
        object_virtual_circuit_type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        object_virtual_device_context: str | VirtualDeviceContext | pb.VirtualDeviceContext | None = None,
        object_virtual_disk: str | VirtualDisk | pb.VirtualDisk | None = None,
        object_virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        object_wireless_lan: str | WirelessLAN | pb.WirelessLAN | None = None,
        object_wireless_lan_group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        object_wireless_link: str | WirelessLink | pb.WirelessLink | None = None,
        contact: str | Contact | pb.Contact | None = None,
        role: str | ContactRole | pb.ContactRole | None = None,
        priority: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ContactAssignment:
        """Create a new ContactAssignment."""
        object_asn = convert_to_protobuf(object_asn, pb.ASN)
        object_asn_range = convert_to_protobuf(object_asn_range, pb.ASNRange)
        object_aggregate = convert_to_protobuf(object_aggregate, pb.Aggregate)
        object_cable = convert_to_protobuf(object_cable, pb.Cable)
        object_cable_path = convert_to_protobuf(object_cable_path, pb.CablePath)
        object_cable_termination = convert_to_protobuf(object_cable_termination, pb.CableTermination)
        object_circuit = convert_to_protobuf(object_circuit, pb.Circuit)
        object_circuit_group = convert_to_protobuf(object_circuit_group, pb.CircuitGroup)
        object_circuit_group_assignment = convert_to_protobuf(object_circuit_group_assignment, pb.CircuitGroupAssignment)
        object_circuit_termination = convert_to_protobuf(object_circuit_termination, pb.CircuitTermination)
        object_circuit_type = convert_to_protobuf(object_circuit_type, pb.CircuitType)
        object_cluster = convert_to_protobuf(object_cluster, pb.Cluster)
        object_cluster_group = convert_to_protobuf(object_cluster_group, pb.ClusterGroup)
        object_cluster_type = convert_to_protobuf(object_cluster_type, pb.ClusterType)
        object_console_port = convert_to_protobuf(object_console_port, pb.ConsolePort)
        object_console_server_port = convert_to_protobuf(object_console_server_port, pb.ConsoleServerPort)
        object_contact = convert_to_protobuf(object_contact, pb.Contact)
        object_contact_assignment = convert_to_protobuf(object_contact_assignment, pb.ContactAssignment)
        object_contact_group = convert_to_protobuf(object_contact_group, pb.ContactGroup)
        object_contact_role = convert_to_protobuf(object_contact_role, pb.ContactRole)
        object_device = convert_to_protobuf(object_device, pb.Device)
        object_device_bay = convert_to_protobuf(object_device_bay, pb.DeviceBay)
        object_device_role = convert_to_protobuf(object_device_role, pb.DeviceRole)
        object_device_type = convert_to_protobuf(object_device_type, pb.DeviceType)
        object_fhrp_group = convert_to_protobuf(object_fhrp_group, pb.FHRPGroup)
        object_fhrp_group_assignment = convert_to_protobuf(object_fhrp_group_assignment, pb.FHRPGroupAssignment)
        object_front_port = convert_to_protobuf(object_front_port, pb.FrontPort)
        object_ike_policy = convert_to_protobuf(object_ike_policy, pb.IKEPolicy)
        object_ike_proposal = convert_to_protobuf(object_ike_proposal, pb.IKEProposal)
        object_ip_address = convert_to_protobuf(object_ip_address, pb.IPAddress)
        object_ip_range = convert_to_protobuf(object_ip_range, pb.IPRange)
        object_ip_sec_policy = convert_to_protobuf(object_ip_sec_policy, pb.IPSecPolicy)
        object_ip_sec_profile = convert_to_protobuf(object_ip_sec_profile, pb.IPSecProfile)
        object_ip_sec_proposal = convert_to_protobuf(object_ip_sec_proposal, pb.IPSecProposal)
        object_interface = convert_to_protobuf(object_interface, pb.Interface)
        object_inventory_item = convert_to_protobuf(object_inventory_item, pb.InventoryItem)
        object_inventory_item_role = convert_to_protobuf(object_inventory_item_role, pb.InventoryItemRole)
        object_l2vpn = convert_to_protobuf(object_l2vpn, pb.L2VPN)
        object_l2vpn_termination = convert_to_protobuf(object_l2vpn_termination, pb.L2VPNTermination)
        object_location = convert_to_protobuf(object_location, pb.Location)
        object_mac_address = convert_to_protobuf(object_mac_address, pb.MACAddress)
        object_manufacturer = convert_to_protobuf(object_manufacturer, pb.Manufacturer)
        object_module = convert_to_protobuf(object_module, pb.Module)
        object_module_bay = convert_to_protobuf(object_module_bay, pb.ModuleBay)
        object_module_type = convert_to_protobuf(object_module_type, pb.ModuleType)
        object_platform = convert_to_protobuf(object_platform, pb.Platform)
        object_power_feed = convert_to_protobuf(object_power_feed, pb.PowerFeed)
        object_power_outlet = convert_to_protobuf(object_power_outlet, pb.PowerOutlet)
        object_power_panel = convert_to_protobuf(object_power_panel, pb.PowerPanel)
        object_power_port = convert_to_protobuf(object_power_port, pb.PowerPort)
        object_prefix = convert_to_protobuf(object_prefix, pb.Prefix)
        object_provider = convert_to_protobuf(object_provider, pb.Provider)
        object_provider_account = convert_to_protobuf(object_provider_account, pb.ProviderAccount)
        object_provider_network = convert_to_protobuf(object_provider_network, pb.ProviderNetwork)
        object_rir = convert_to_protobuf(object_rir, pb.RIR)
        object_rack = convert_to_protobuf(object_rack, pb.Rack)
        object_rack_reservation = convert_to_protobuf(object_rack_reservation, pb.RackReservation)
        object_rack_role = convert_to_protobuf(object_rack_role, pb.RackRole)
        object_rack_type = convert_to_protobuf(object_rack_type, pb.RackType)
        object_rear_port = convert_to_protobuf(object_rear_port, pb.RearPort)
        object_region = convert_to_protobuf(object_region, pb.Region)
        object_role = convert_to_protobuf(object_role, pb.Role)
        object_route_target = convert_to_protobuf(object_route_target, pb.RouteTarget)
        object_service = convert_to_protobuf(object_service, pb.Service)
        object_site = convert_to_protobuf(object_site, pb.Site)
        object_site_group = convert_to_protobuf(object_site_group, pb.SiteGroup)
        object_tag = convert_to_protobuf(object_tag, pb.Tag)
        object_tenant = convert_to_protobuf(object_tenant, pb.Tenant)
        object_tenant_group = convert_to_protobuf(object_tenant_group, pb.TenantGroup)
        object_tunnel = convert_to_protobuf(object_tunnel, pb.Tunnel)
        object_tunnel_group = convert_to_protobuf(object_tunnel_group, pb.TunnelGroup)
        object_tunnel_termination = convert_to_protobuf(object_tunnel_termination, pb.TunnelTermination)
        object_vlan = convert_to_protobuf(object_vlan, pb.VLAN)
        object_vlan_group = convert_to_protobuf(object_vlan_group, pb.VLANGroup)
        object_vlan_translation_policy = convert_to_protobuf(object_vlan_translation_policy, pb.VLANTranslationPolicy)
        object_vlan_translation_rule = convert_to_protobuf(object_vlan_translation_rule, pb.VLANTranslationRule)
        object_vm_interface = convert_to_protobuf(object_vm_interface, pb.VMInterface)
        object_vrf = convert_to_protobuf(object_vrf, pb.VRF)
        object_virtual_chassis = convert_to_protobuf(object_virtual_chassis, pb.VirtualChassis)
        object_virtual_circuit = convert_to_protobuf(object_virtual_circuit, pb.VirtualCircuit)
        object_virtual_circuit_termination = convert_to_protobuf(object_virtual_circuit_termination, pb.VirtualCircuitTermination)
        object_virtual_circuit_type = convert_to_protobuf(object_virtual_circuit_type, pb.VirtualCircuitType)
        object_virtual_device_context = convert_to_protobuf(object_virtual_device_context, pb.VirtualDeviceContext)
        object_virtual_disk = convert_to_protobuf(object_virtual_disk, pb.VirtualDisk)
        object_virtual_machine = convert_to_protobuf(object_virtual_machine, pb.VirtualMachine)
        object_wireless_lan = convert_to_protobuf(object_wireless_lan, pb.WirelessLAN)
        object_wireless_lan_group = convert_to_protobuf(object_wireless_lan_group, pb.WirelessLANGroup)
        object_wireless_link = convert_to_protobuf(object_wireless_link, pb.WirelessLink)
        contact = convert_to_protobuf(contact, pb.Contact)
        role = convert_to_protobuf(role, pb.ContactRole)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ContactAssignment(
            object_asn=object_asn,
            object_asn_range=object_asn_range,
            object_aggregate=object_aggregate,
            object_cable=object_cable,
            object_cable_path=object_cable_path,
            object_cable_termination=object_cable_termination,
            object_circuit=object_circuit,
            object_circuit_group=object_circuit_group,
            object_circuit_group_assignment=object_circuit_group_assignment,
            object_circuit_termination=object_circuit_termination,
            object_circuit_type=object_circuit_type,
            object_cluster=object_cluster,
            object_cluster_group=object_cluster_group,
            object_cluster_type=object_cluster_type,
            object_console_port=object_console_port,
            object_console_server_port=object_console_server_port,
            object_contact=object_contact,
            object_contact_assignment=object_contact_assignment,
            object_contact_group=object_contact_group,
            object_contact_role=object_contact_role,
            object_device=object_device,
            object_device_bay=object_device_bay,
            object_device_role=object_device_role,
            object_device_type=object_device_type,
            object_fhrp_group=object_fhrp_group,
            object_fhrp_group_assignment=object_fhrp_group_assignment,
            object_front_port=object_front_port,
            object_ike_policy=object_ike_policy,
            object_ike_proposal=object_ike_proposal,
            object_ip_address=object_ip_address,
            object_ip_range=object_ip_range,
            object_ip_sec_policy=object_ip_sec_policy,
            object_ip_sec_profile=object_ip_sec_profile,
            object_ip_sec_proposal=object_ip_sec_proposal,
            object_interface=object_interface,
            object_inventory_item=object_inventory_item,
            object_inventory_item_role=object_inventory_item_role,
            object_l2vpn=object_l2vpn,
            object_l2vpn_termination=object_l2vpn_termination,
            object_location=object_location,
            object_mac_address=object_mac_address,
            object_manufacturer=object_manufacturer,
            object_module=object_module,
            object_module_bay=object_module_bay,
            object_module_type=object_module_type,
            object_platform=object_platform,
            object_power_feed=object_power_feed,
            object_power_outlet=object_power_outlet,
            object_power_panel=object_power_panel,
            object_power_port=object_power_port,
            object_prefix=object_prefix,
            object_provider=object_provider,
            object_provider_account=object_provider_account,
            object_provider_network=object_provider_network,
            object_rir=object_rir,
            object_rack=object_rack,
            object_rack_reservation=object_rack_reservation,
            object_rack_role=object_rack_role,
            object_rack_type=object_rack_type,
            object_rear_port=object_rear_port,
            object_region=object_region,
            object_role=object_role,
            object_route_target=object_route_target,
            object_service=object_service,
            object_site=object_site,
            object_site_group=object_site_group,
            object_tag=object_tag,
            object_tenant=object_tenant,
            object_tenant_group=object_tenant_group,
            object_tunnel=object_tunnel,
            object_tunnel_group=object_tunnel_group,
            object_tunnel_termination=object_tunnel_termination,
            object_vlan=object_vlan,
            object_vlan_group=object_vlan_group,
            object_vlan_translation_policy=object_vlan_translation_policy,
            object_vlan_translation_rule=object_vlan_translation_rule,
            object_vm_interface=object_vm_interface,
            object_vrf=object_vrf,
            object_virtual_chassis=object_virtual_chassis,
            object_virtual_circuit=object_virtual_circuit,
            object_virtual_circuit_termination=object_virtual_circuit_termination,
            object_virtual_circuit_type=object_virtual_circuit_type,
            object_virtual_device_context=object_virtual_device_context,
            object_virtual_disk=object_virtual_disk,
            object_virtual_machine=object_virtual_machine,
            object_wireless_lan=object_wireless_lan,
            object_wireless_lan_group=object_wireless_lan_group,
            object_wireless_link=object_wireless_link,
            contact=contact,
            role=role,
            priority=priority,
            tags=tags,
            custom_fields=custom_fields,
        )


class ContactGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ContactGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        parent: str | ContactGroup | pb.ContactGroup | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ContactGroup:
        """Create a new ContactGroup."""
        parent = convert_to_protobuf(parent, pb.ContactGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ContactGroup(
            name=name,
            slug=slug,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class ContactRole:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ContactRole."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ContactRole:
        """Create a new ContactRole."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ContactRole(
            name=name,
            slug=slug,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class CustomFieldObjectReference:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CustomFieldObjectReference."""

    def __new__(
        cls,
        asn: str | ASN | pb.ASN | None = None,
        asn_range: str | ASNRange | pb.ASNRange | None = None,
        aggregate: str | Aggregate | pb.Aggregate | None = None,
        cable: str | Cable | pb.Cable | None = None,
        cable_path: str | CablePath | pb.CablePath | None = None,
        cable_termination: str | CableTermination | pb.CableTermination | None = None,
        circuit: str | Circuit | pb.Circuit | None = None,
        circuit_group: str | CircuitGroup | pb.CircuitGroup | None = None,
        circuit_group_assignment: str | CircuitGroupAssignment | pb.CircuitGroupAssignment | None = None,
        circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        circuit_type: str | CircuitType | pb.CircuitType | None = None,
        cluster: str | Cluster | pb.Cluster | None = None,
        cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        cluster_type: str | ClusterType | pb.ClusterType | None = None,
        console_port: str | ConsolePort | pb.ConsolePort | None = None,
        console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        contact: str | Contact | pb.Contact | None = None,
        contact_assignment: str | ContactAssignment | pb.ContactAssignment | None = None,
        contact_group: str | ContactGroup | pb.ContactGroup | None = None,
        contact_role: str | ContactRole | pb.ContactRole | None = None,
        device: str | Device | pb.Device | None = None,
        device_bay: str | DeviceBay | pb.DeviceBay | None = None,
        device_role: str | DeviceRole | pb.DeviceRole | None = None,
        device_type: str | DeviceType | pb.DeviceType | None = None,
        fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        fhrp_group_assignment: str | FHRPGroupAssignment | pb.FHRPGroupAssignment | None = None,
        front_port: str | FrontPort | pb.FrontPort | None = None,
        ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        ike_proposal: str | IKEProposal | pb.IKEProposal | None = None,
        ip_address: str | IPAddress | pb.IPAddress | None = None,
        ip_range: str | IPRange | pb.IPRange | None = None,
        ip_sec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        ip_sec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        ip_sec_proposal: str | IPSecProposal | pb.IPSecProposal | None = None,
        interface: str | Interface | pb.Interface | None = None,
        inventory_item: str | InventoryItem | pb.InventoryItem | None = None,
        inventory_item_role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        l2vpn: str | L2VPN | pb.L2VPN | None = None,
        l2vpn_termination: str | L2VPNTermination | pb.L2VPNTermination | None = None,
        location: str | Location | pb.Location | None = None,
        mac_address: str | MACAddress | pb.MACAddress | None = None,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        module: str | Module | pb.Module | None = None,
        module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        module_type: str | ModuleType | pb.ModuleType | None = None,
        platform: str | Platform | pb.Platform | None = None,
        power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        power_port: str | PowerPort | pb.PowerPort | None = None,
        prefix: str | Prefix | pb.Prefix | None = None,
        provider: str | Provider | pb.Provider | None = None,
        provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        rir: str | RIR | pb.RIR | None = None,
        rack: str | Rack | pb.Rack | None = None,
        rack_reservation: str | RackReservation | pb.RackReservation | None = None,
        rack_role: str | RackRole | pb.RackRole | None = None,
        rack_type: str | RackType | pb.RackType | None = None,
        rear_port: str | RearPort | pb.RearPort | None = None,
        region: str | Region | pb.Region | None = None,
        role: str | Role | pb.Role | None = None,
        route_target: str | RouteTarget | pb.RouteTarget | None = None,
        service: str | Service | pb.Service | None = None,
        site: str | Site | pb.Site | None = None,
        site_group: str | SiteGroup | pb.SiteGroup | None = None,
        tag: str | Tag | pb.Tag | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        tenant_group: str | TenantGroup | pb.TenantGroup | None = None,
        tunnel: str | Tunnel | pb.Tunnel | None = None,
        tunnel_group: str | TunnelGroup | pb.TunnelGroup | None = None,
        tunnel_termination: str | TunnelTermination | pb.TunnelTermination | None = None,
        vlan: str | VLAN | pb.VLAN | None = None,
        vlan_group: str | VLANGroup | pb.VLANGroup | None = None,
        vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        vlan_translation_rule: str | VLANTranslationRule | pb.VLANTranslationRule | None = None,
        vm_interface: str | VMInterface | pb.VMInterface | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        virtual_circuit_termination: str | VirtualCircuitTermination | pb.VirtualCircuitTermination | None = None,
        virtual_circuit_type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        virtual_device_context: str | VirtualDeviceContext | pb.VirtualDeviceContext | None = None,
        virtual_disk: str | VirtualDisk | pb.VirtualDisk | None = None,
        virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        wireless_lan: str | WirelessLAN | pb.WirelessLAN | None = None,
        wireless_lan_group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        wireless_link: str | WirelessLink | pb.WirelessLink | None = None,
    ) -> pb.CustomFieldObjectReference:
        """Create a new CustomFieldObjectReference."""
        asn = convert_to_protobuf(asn, pb.ASN)
        asn_range = convert_to_protobuf(asn_range, pb.ASNRange)
        aggregate = convert_to_protobuf(aggregate, pb.Aggregate)
        cable = convert_to_protobuf(cable, pb.Cable)
        cable_path = convert_to_protobuf(cable_path, pb.CablePath)
        cable_termination = convert_to_protobuf(cable_termination, pb.CableTermination)
        circuit = convert_to_protobuf(circuit, pb.Circuit)
        circuit_group = convert_to_protobuf(circuit_group, pb.CircuitGroup)
        circuit_group_assignment = convert_to_protobuf(circuit_group_assignment, pb.CircuitGroupAssignment)
        circuit_termination = convert_to_protobuf(circuit_termination, pb.CircuitTermination)
        circuit_type = convert_to_protobuf(circuit_type, pb.CircuitType)
        cluster = convert_to_protobuf(cluster, pb.Cluster)
        cluster_group = convert_to_protobuf(cluster_group, pb.ClusterGroup)
        cluster_type = convert_to_protobuf(cluster_type, pb.ClusterType)
        console_port = convert_to_protobuf(console_port, pb.ConsolePort)
        console_server_port = convert_to_protobuf(console_server_port, pb.ConsoleServerPort)
        contact = convert_to_protobuf(contact, pb.Contact)
        contact_assignment = convert_to_protobuf(contact_assignment, pb.ContactAssignment)
        contact_group = convert_to_protobuf(contact_group, pb.ContactGroup)
        contact_role = convert_to_protobuf(contact_role, pb.ContactRole)
        device = convert_to_protobuf(device, pb.Device)
        device_bay = convert_to_protobuf(device_bay, pb.DeviceBay)
        device_role = convert_to_protobuf(device_role, pb.DeviceRole)
        device_type = convert_to_protobuf(device_type, pb.DeviceType)
        fhrp_group = convert_to_protobuf(fhrp_group, pb.FHRPGroup)
        fhrp_group_assignment = convert_to_protobuf(fhrp_group_assignment, pb.FHRPGroupAssignment)
        front_port = convert_to_protobuf(front_port, pb.FrontPort)
        ike_policy = convert_to_protobuf(ike_policy, pb.IKEPolicy)
        ike_proposal = convert_to_protobuf(ike_proposal, pb.IKEProposal)
        ip_address = convert_to_protobuf(ip_address, pb.IPAddress)
        ip_range = convert_to_protobuf(ip_range, pb.IPRange)
        ip_sec_policy = convert_to_protobuf(ip_sec_policy, pb.IPSecPolicy)
        ip_sec_profile = convert_to_protobuf(ip_sec_profile, pb.IPSecProfile)
        ip_sec_proposal = convert_to_protobuf(ip_sec_proposal, pb.IPSecProposal)
        interface = convert_to_protobuf(interface, pb.Interface)
        inventory_item = convert_to_protobuf(inventory_item, pb.InventoryItem)
        inventory_item_role = convert_to_protobuf(inventory_item_role, pb.InventoryItemRole)
        l2vpn = convert_to_protobuf(l2vpn, pb.L2VPN)
        l2vpn_termination = convert_to_protobuf(l2vpn_termination, pb.L2VPNTermination)
        location = convert_to_protobuf(location, pb.Location)
        mac_address = convert_to_protobuf(mac_address, pb.MACAddress)
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        module = convert_to_protobuf(module, pb.Module)
        module_bay = convert_to_protobuf(module_bay, pb.ModuleBay)
        module_type = convert_to_protobuf(module_type, pb.ModuleType)
        platform = convert_to_protobuf(platform, pb.Platform)
        power_feed = convert_to_protobuf(power_feed, pb.PowerFeed)
        power_outlet = convert_to_protobuf(power_outlet, pb.PowerOutlet)
        power_panel = convert_to_protobuf(power_panel, pb.PowerPanel)
        power_port = convert_to_protobuf(power_port, pb.PowerPort)
        prefix = convert_to_protobuf(prefix, pb.Prefix)
        provider = convert_to_protobuf(provider, pb.Provider)
        provider_account = convert_to_protobuf(provider_account, pb.ProviderAccount)
        provider_network = convert_to_protobuf(provider_network, pb.ProviderNetwork)
        rir = convert_to_protobuf(rir, pb.RIR)
        rack = convert_to_protobuf(rack, pb.Rack)
        rack_reservation = convert_to_protobuf(rack_reservation, pb.RackReservation)
        rack_role = convert_to_protobuf(rack_role, pb.RackRole)
        rack_type = convert_to_protobuf(rack_type, pb.RackType)
        rear_port = convert_to_protobuf(rear_port, pb.RearPort)
        region = convert_to_protobuf(region, pb.Region)
        role = convert_to_protobuf(role, pb.Role)
        route_target = convert_to_protobuf(route_target, pb.RouteTarget)
        service = convert_to_protobuf(service, pb.Service)
        site = convert_to_protobuf(site, pb.Site)
        site_group = convert_to_protobuf(site_group, pb.SiteGroup)
        tag = convert_to_protobuf(tag, pb.Tag)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tenant_group = convert_to_protobuf(tenant_group, pb.TenantGroup)
        tunnel = convert_to_protobuf(tunnel, pb.Tunnel)
        tunnel_group = convert_to_protobuf(tunnel_group, pb.TunnelGroup)
        tunnel_termination = convert_to_protobuf(tunnel_termination, pb.TunnelTermination)
        vlan = convert_to_protobuf(vlan, pb.VLAN)
        vlan_group = convert_to_protobuf(vlan_group, pb.VLANGroup)
        vlan_translation_policy = convert_to_protobuf(vlan_translation_policy, pb.VLANTranslationPolicy)
        vlan_translation_rule = convert_to_protobuf(vlan_translation_rule, pb.VLANTranslationRule)
        vm_interface = convert_to_protobuf(vm_interface, pb.VMInterface)
        vrf = convert_to_protobuf(vrf, pb.VRF)
        virtual_chassis = convert_to_protobuf(virtual_chassis, pb.VirtualChassis)
        virtual_circuit = convert_to_protobuf(virtual_circuit, pb.VirtualCircuit)
        virtual_circuit_termination = convert_to_protobuf(virtual_circuit_termination, pb.VirtualCircuitTermination)
        virtual_circuit_type = convert_to_protobuf(virtual_circuit_type, pb.VirtualCircuitType)
        virtual_device_context = convert_to_protobuf(virtual_device_context, pb.VirtualDeviceContext)
        virtual_disk = convert_to_protobuf(virtual_disk, pb.VirtualDisk)
        virtual_machine = convert_to_protobuf(virtual_machine, pb.VirtualMachine)
        wireless_lan = convert_to_protobuf(wireless_lan, pb.WirelessLAN)
        wireless_lan_group = convert_to_protobuf(wireless_lan_group, pb.WirelessLANGroup)
        wireless_link = convert_to_protobuf(wireless_link, pb.WirelessLink)
        return pb.CustomFieldObjectReference(
            asn=asn,
            asn_range=asn_range,
            aggregate=aggregate,
            cable=cable,
            cable_path=cable_path,
            cable_termination=cable_termination,
            circuit=circuit,
            circuit_group=circuit_group,
            circuit_group_assignment=circuit_group_assignment,
            circuit_termination=circuit_termination,
            circuit_type=circuit_type,
            cluster=cluster,
            cluster_group=cluster_group,
            cluster_type=cluster_type,
            console_port=console_port,
            console_server_port=console_server_port,
            contact=contact,
            contact_assignment=contact_assignment,
            contact_group=contact_group,
            contact_role=contact_role,
            device=device,
            device_bay=device_bay,
            device_role=device_role,
            device_type=device_type,
            fhrp_group=fhrp_group,
            fhrp_group_assignment=fhrp_group_assignment,
            front_port=front_port,
            ike_policy=ike_policy,
            ike_proposal=ike_proposal,
            ip_address=ip_address,
            ip_range=ip_range,
            ip_sec_policy=ip_sec_policy,
            ip_sec_profile=ip_sec_profile,
            ip_sec_proposal=ip_sec_proposal,
            interface=interface,
            inventory_item=inventory_item,
            inventory_item_role=inventory_item_role,
            l2vpn=l2vpn,
            l2vpn_termination=l2vpn_termination,
            location=location,
            mac_address=mac_address,
            manufacturer=manufacturer,
            module=module,
            module_bay=module_bay,
            module_type=module_type,
            platform=platform,
            power_feed=power_feed,
            power_outlet=power_outlet,
            power_panel=power_panel,
            power_port=power_port,
            prefix=prefix,
            provider=provider,
            provider_account=provider_account,
            provider_network=provider_network,
            rir=rir,
            rack=rack,
            rack_reservation=rack_reservation,
            rack_role=rack_role,
            rack_type=rack_type,
            rear_port=rear_port,
            region=region,
            role=role,
            route_target=route_target,
            service=service,
            site=site,
            site_group=site_group,
            tag=tag,
            tenant=tenant,
            tenant_group=tenant_group,
            tunnel=tunnel,
            tunnel_group=tunnel_group,
            tunnel_termination=tunnel_termination,
            vlan=vlan,
            vlan_group=vlan_group,
            vlan_translation_policy=vlan_translation_policy,
            vlan_translation_rule=vlan_translation_rule,
            vm_interface=vm_interface,
            vrf=vrf,
            virtual_chassis=virtual_chassis,
            virtual_circuit=virtual_circuit,
            virtual_circuit_termination=virtual_circuit_termination,
            virtual_circuit_type=virtual_circuit_type,
            virtual_device_context=virtual_device_context,
            virtual_disk=virtual_disk,
            virtual_machine=virtual_machine,
            wireless_lan=wireless_lan,
            wireless_lan_group=wireless_lan_group,
            wireless_link=wireless_link,
        )


class CustomFieldValue:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.CustomFieldValue."""

    def __new__(
        cls,
        multiple_selection: list[str] | None = None,
        multiple_objects: list[str | CustomFieldObjectReference | pb.CustomFieldObjectReference] | None = None,
        text: str | None = None,
        long_text: str | None = None,
        integer: int | None = None,
        decimal: float | None = None,
        boolean: bool | None = None,
        date: datetime.datetime | None = None,
        datetime: datetime.datetime | None = None,
        url: str | None = None,
        json: str | None = None,
        selection: str | None = None,
        object: str | CustomFieldObjectReference | pb.CustomFieldObjectReference | None = None,
    ) -> pb.CustomFieldValue:
        """Create a new CustomFieldValue."""
        multiple_objects = convert_to_protobuf_list(multiple_objects, pb.CustomFieldObjectReference)
        object = convert_to_protobuf(object, pb.CustomFieldObjectReference)
        return pb.CustomFieldValue(
            multiple_selection=multiple_selection,
            multiple_objects=multiple_objects,
            text=text,
            long_text=long_text,
            integer=integer,
            decimal=decimal,
            boolean=boolean,
            date=date,
            datetime=datetime,
            url=url,
            json=json,
            selection=selection,
            object=object,
        )


class Device:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Device."""

    def __new__(
        cls,
        name: str | None = None,
        device_type: str | DeviceType | pb.DeviceType | None = None,
        role: str | DeviceRole | pb.DeviceRole | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        platform: str | Platform | pb.Platform | None = None,
        serial: str | None = None,
        asset_tag: str | None = None,
        site: str | Site | pb.Site | None = None,
        location: str | Location | pb.Location | None = None,
        rack: str | Rack | pb.Rack | None = None,
        position: float | None = None,
        face: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        status: str | None = None,
        airflow: str | None = None,
        primary_ip4: str | IPAddress | pb.IPAddress | None = None,
        primary_ip6: str | IPAddress | pb.IPAddress | None = None,
        oob_ip: str | IPAddress | pb.IPAddress | None = None,
        cluster: str | Cluster | pb.Cluster | None = None,
        virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        vc_position: int | None = None,
        vc_priority: int | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        # shortcuts
        manufacturer: str | Manufacturer | pb.Manufacturer = None,
    ) -> pb.Device:
        """Create a new Device."""
        device_type = convert_to_protobuf(device_type, pb.DeviceType)
        role = convert_to_protobuf(role, pb.DeviceRole)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        platform = convert_to_protobuf(platform, pb.Platform)
        site = convert_to_protobuf(site, pb.Site)
        location = convert_to_protobuf(location, pb.Location)
        rack = convert_to_protobuf(rack, pb.Rack)
        primary_ip4 = convert_to_protobuf(primary_ip4, pb.IPAddress)
        primary_ip6 = convert_to_protobuf(primary_ip6, pb.IPAddress)
        oob_ip = convert_to_protobuf(oob_ip, pb.IPAddress)
        cluster = convert_to_protobuf(cluster, pb.Cluster)
        virtual_chassis = convert_to_protobuf(virtual_chassis, pb.VirtualChassis)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)

        # shortcut types (not directly used)
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)

        # apply shortcuts
        if manufacturer is not None:
            if platform is not None and not platform.HasField('manufacturer'):
                platform.manufacturer.CopyFrom(manufacturer)
            if device_type is not None and not device_type.HasField('manufacturer'):
                device_type.manufacturer.CopyFrom(manufacturer)
        return pb.Device(
            name=name,
            device_type=device_type,
            role=role,
            tenant=tenant,
            platform=platform,
            serial=serial,
            asset_tag=asset_tag,
            site=site,
            location=location,
            rack=rack,
            position=position,
            face=face,
            latitude=latitude,
            longitude=longitude,
            status=status,
            airflow=airflow,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            oob_ip=oob_ip,
            cluster=cluster,
            virtual_chassis=virtual_chassis,
            vc_position=vc_position,
            vc_priority=vc_priority,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class DeviceBay:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.DeviceBay."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        name: str | None = None,
        label: str | None = None,
        description: str | None = None,
        installed_device: str | Device | pb.Device | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.DeviceBay:
        """Create a new DeviceBay."""
        device = convert_to_protobuf(device, pb.Device)
        installed_device = convert_to_protobuf(installed_device, pb.Device)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.DeviceBay(
            device=device,
            name=name,
            label=label,
            description=description,
            installed_device=installed_device,
            tags=tags,
            custom_fields=custom_fields,
        )


class DeviceRole:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.DeviceRole."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
        vm_role: bool | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.DeviceRole:
        """Create a new DeviceRole."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.DeviceRole(
            name=name,
            slug=slug,
            color=color,
            vm_role=vm_role,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class DeviceType:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.DeviceType."""

    def __new__(
        cls,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        default_platform: str | Platform | pb.Platform | None = None,
        model: str | None = None,
        slug: str | None = None,
        part_number: str | None = None,
        u_height: float | None = None,
        exclude_from_utilization: bool | None = None,
        is_full_depth: bool | None = None,
        subdevice_role: str | None = None,
        airflow: str | None = None,
        weight: float | None = None,
        weight_unit: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.DeviceType:
        """Create a new DeviceType."""
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        default_platform = convert_to_protobuf(default_platform, pb.Platform)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.DeviceType(
            manufacturer=manufacturer,
            default_platform=default_platform,
            model=model,
            slug=slug,
            part_number=part_number,
            u_height=u_height,
            exclude_from_utilization=exclude_from_utilization,
            is_full_depth=is_full_depth,
            subdevice_role=subdevice_role,
            airflow=airflow,
            weight=weight,
            weight_unit=weight_unit,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class FHRPGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.FHRPGroup."""

    def __new__(
        cls,
        name: str | None = None,
        protocol: str | None = None,
        group_id: int | None = None,
        auth_type: str | None = None,
        auth_key: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.FHRPGroup:
        """Create a new FHRPGroup."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.FHRPGroup(
            name=name,
            protocol=protocol,
            group_id=group_id,
            auth_type=auth_type,
            auth_key=auth_key,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class FHRPGroupAssignment:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.FHRPGroupAssignment."""

    def __new__(
        cls,
        group: str | FHRPGroup | pb.FHRPGroup | None = None,
        interface_asn: str | ASN | pb.ASN | None = None,
        interface_asn_range: str | ASNRange | pb.ASNRange | None = None,
        interface_aggregate: str | Aggregate | pb.Aggregate | None = None,
        interface_cable: str | Cable | pb.Cable | None = None,
        interface_cable_path: str | CablePath | pb.CablePath | None = None,
        interface_cable_termination: str | CableTermination | pb.CableTermination | None = None,
        interface_circuit: str | Circuit | pb.Circuit | None = None,
        interface_circuit_group: str | CircuitGroup | pb.CircuitGroup | None = None,
        interface_circuit_group_assignment: str | CircuitGroupAssignment | pb.CircuitGroupAssignment | None = None,
        interface_circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        interface_circuit_type: str | CircuitType | pb.CircuitType | None = None,
        interface_cluster: str | Cluster | pb.Cluster | None = None,
        interface_cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        interface_cluster_type: str | ClusterType | pb.ClusterType | None = None,
        interface_console_port: str | ConsolePort | pb.ConsolePort | None = None,
        interface_console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        interface_contact: str | Contact | pb.Contact | None = None,
        interface_contact_assignment: str | ContactAssignment | pb.ContactAssignment | None = None,
        interface_contact_group: str | ContactGroup | pb.ContactGroup | None = None,
        interface_contact_role: str | ContactRole | pb.ContactRole | None = None,
        interface_device: str | Device | pb.Device | None = None,
        interface_device_bay: str | DeviceBay | pb.DeviceBay | None = None,
        interface_device_role: str | DeviceRole | pb.DeviceRole | None = None,
        interface_device_type: str | DeviceType | pb.DeviceType | None = None,
        interface_fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        interface_fhrp_group_assignment: str | FHRPGroupAssignment | pb.FHRPGroupAssignment | None = None,
        interface_front_port: str | FrontPort | pb.FrontPort | None = None,
        interface_ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        interface_ike_proposal: str | IKEProposal | pb.IKEProposal | None = None,
        interface_ip_address: str | IPAddress | pb.IPAddress | None = None,
        interface_ip_range: str | IPRange | pb.IPRange | None = None,
        interface_ip_sec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        interface_ip_sec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        interface_ip_sec_proposal: str | IPSecProposal | pb.IPSecProposal | None = None,
        interface_interface: str | Interface | pb.Interface | None = None,
        interface_inventory_item: str | InventoryItem | pb.InventoryItem | None = None,
        interface_inventory_item_role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        interface_l2vpn: str | L2VPN | pb.L2VPN | None = None,
        interface_l2vpn_termination: str | L2VPNTermination | pb.L2VPNTermination | None = None,
        interface_location: str | Location | pb.Location | None = None,
        interface_mac_address: str | MACAddress | pb.MACAddress | None = None,
        interface_manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        interface_module: str | Module | pb.Module | None = None,
        interface_module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        interface_module_type: str | ModuleType | pb.ModuleType | None = None,
        interface_platform: str | Platform | pb.Platform | None = None,
        interface_power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        interface_power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        interface_power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        interface_power_port: str | PowerPort | pb.PowerPort | None = None,
        interface_prefix: str | Prefix | pb.Prefix | None = None,
        interface_provider: str | Provider | pb.Provider | None = None,
        interface_provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        interface_provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        interface_rir: str | RIR | pb.RIR | None = None,
        interface_rack: str | Rack | pb.Rack | None = None,
        interface_rack_reservation: str | RackReservation | pb.RackReservation | None = None,
        interface_rack_role: str | RackRole | pb.RackRole | None = None,
        interface_rack_type: str | RackType | pb.RackType | None = None,
        interface_rear_port: str | RearPort | pb.RearPort | None = None,
        interface_region: str | Region | pb.Region | None = None,
        interface_role: str | Role | pb.Role | None = None,
        interface_route_target: str | RouteTarget | pb.RouteTarget | None = None,
        interface_service: str | Service | pb.Service | None = None,
        interface_site: str | Site | pb.Site | None = None,
        interface_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        interface_tag: str | Tag | pb.Tag | None = None,
        interface_tenant: str | Tenant | pb.Tenant | None = None,
        interface_tenant_group: str | TenantGroup | pb.TenantGroup | None = None,
        interface_tunnel: str | Tunnel | pb.Tunnel | None = None,
        interface_tunnel_group: str | TunnelGroup | pb.TunnelGroup | None = None,
        interface_tunnel_termination: str | TunnelTermination | pb.TunnelTermination | None = None,
        interface_vlan: str | VLAN | pb.VLAN | None = None,
        interface_vlan_group: str | VLANGroup | pb.VLANGroup | None = None,
        interface_vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        interface_vlan_translation_rule: str | VLANTranslationRule | pb.VLANTranslationRule | None = None,
        interface_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        interface_vrf: str | VRF | pb.VRF | None = None,
        interface_virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        interface_virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        interface_virtual_circuit_termination: str | VirtualCircuitTermination | pb.VirtualCircuitTermination | None = None,
        interface_virtual_circuit_type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        interface_virtual_device_context: str | VirtualDeviceContext | pb.VirtualDeviceContext | None = None,
        interface_virtual_disk: str | VirtualDisk | pb.VirtualDisk | None = None,
        interface_virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        interface_wireless_lan: str | WirelessLAN | pb.WirelessLAN | None = None,
        interface_wireless_lan_group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        interface_wireless_link: str | WirelessLink | pb.WirelessLink | None = None,
        priority: int | None = None,
    ) -> pb.FHRPGroupAssignment:
        """Create a new FHRPGroupAssignment."""
        group = convert_to_protobuf(group, pb.FHRPGroup)
        interface_asn = convert_to_protobuf(interface_asn, pb.ASN)
        interface_asn_range = convert_to_protobuf(interface_asn_range, pb.ASNRange)
        interface_aggregate = convert_to_protobuf(interface_aggregate, pb.Aggregate)
        interface_cable = convert_to_protobuf(interface_cable, pb.Cable)
        interface_cable_path = convert_to_protobuf(interface_cable_path, pb.CablePath)
        interface_cable_termination = convert_to_protobuf(interface_cable_termination, pb.CableTermination)
        interface_circuit = convert_to_protobuf(interface_circuit, pb.Circuit)
        interface_circuit_group = convert_to_protobuf(interface_circuit_group, pb.CircuitGroup)
        interface_circuit_group_assignment = convert_to_protobuf(interface_circuit_group_assignment, pb.CircuitGroupAssignment)
        interface_circuit_termination = convert_to_protobuf(interface_circuit_termination, pb.CircuitTermination)
        interface_circuit_type = convert_to_protobuf(interface_circuit_type, pb.CircuitType)
        interface_cluster = convert_to_protobuf(interface_cluster, pb.Cluster)
        interface_cluster_group = convert_to_protobuf(interface_cluster_group, pb.ClusterGroup)
        interface_cluster_type = convert_to_protobuf(interface_cluster_type, pb.ClusterType)
        interface_console_port = convert_to_protobuf(interface_console_port, pb.ConsolePort)
        interface_console_server_port = convert_to_protobuf(interface_console_server_port, pb.ConsoleServerPort)
        interface_contact = convert_to_protobuf(interface_contact, pb.Contact)
        interface_contact_assignment = convert_to_protobuf(interface_contact_assignment, pb.ContactAssignment)
        interface_contact_group = convert_to_protobuf(interface_contact_group, pb.ContactGroup)
        interface_contact_role = convert_to_protobuf(interface_contact_role, pb.ContactRole)
        interface_device = convert_to_protobuf(interface_device, pb.Device)
        interface_device_bay = convert_to_protobuf(interface_device_bay, pb.DeviceBay)
        interface_device_role = convert_to_protobuf(interface_device_role, pb.DeviceRole)
        interface_device_type = convert_to_protobuf(interface_device_type, pb.DeviceType)
        interface_fhrp_group = convert_to_protobuf(interface_fhrp_group, pb.FHRPGroup)
        interface_fhrp_group_assignment = convert_to_protobuf(interface_fhrp_group_assignment, pb.FHRPGroupAssignment)
        interface_front_port = convert_to_protobuf(interface_front_port, pb.FrontPort)
        interface_ike_policy = convert_to_protobuf(interface_ike_policy, pb.IKEPolicy)
        interface_ike_proposal = convert_to_protobuf(interface_ike_proposal, pb.IKEProposal)
        interface_ip_address = convert_to_protobuf(interface_ip_address, pb.IPAddress)
        interface_ip_range = convert_to_protobuf(interface_ip_range, pb.IPRange)
        interface_ip_sec_policy = convert_to_protobuf(interface_ip_sec_policy, pb.IPSecPolicy)
        interface_ip_sec_profile = convert_to_protobuf(interface_ip_sec_profile, pb.IPSecProfile)
        interface_ip_sec_proposal = convert_to_protobuf(interface_ip_sec_proposal, pb.IPSecProposal)
        interface_interface = convert_to_protobuf(interface_interface, pb.Interface)
        interface_inventory_item = convert_to_protobuf(interface_inventory_item, pb.InventoryItem)
        interface_inventory_item_role = convert_to_protobuf(interface_inventory_item_role, pb.InventoryItemRole)
        interface_l2vpn = convert_to_protobuf(interface_l2vpn, pb.L2VPN)
        interface_l2vpn_termination = convert_to_protobuf(interface_l2vpn_termination, pb.L2VPNTermination)
        interface_location = convert_to_protobuf(interface_location, pb.Location)
        interface_mac_address = convert_to_protobuf(interface_mac_address, pb.MACAddress)
        interface_manufacturer = convert_to_protobuf(interface_manufacturer, pb.Manufacturer)
        interface_module = convert_to_protobuf(interface_module, pb.Module)
        interface_module_bay = convert_to_protobuf(interface_module_bay, pb.ModuleBay)
        interface_module_type = convert_to_protobuf(interface_module_type, pb.ModuleType)
        interface_platform = convert_to_protobuf(interface_platform, pb.Platform)
        interface_power_feed = convert_to_protobuf(interface_power_feed, pb.PowerFeed)
        interface_power_outlet = convert_to_protobuf(interface_power_outlet, pb.PowerOutlet)
        interface_power_panel = convert_to_protobuf(interface_power_panel, pb.PowerPanel)
        interface_power_port = convert_to_protobuf(interface_power_port, pb.PowerPort)
        interface_prefix = convert_to_protobuf(interface_prefix, pb.Prefix)
        interface_provider = convert_to_protobuf(interface_provider, pb.Provider)
        interface_provider_account = convert_to_protobuf(interface_provider_account, pb.ProviderAccount)
        interface_provider_network = convert_to_protobuf(interface_provider_network, pb.ProviderNetwork)
        interface_rir = convert_to_protobuf(interface_rir, pb.RIR)
        interface_rack = convert_to_protobuf(interface_rack, pb.Rack)
        interface_rack_reservation = convert_to_protobuf(interface_rack_reservation, pb.RackReservation)
        interface_rack_role = convert_to_protobuf(interface_rack_role, pb.RackRole)
        interface_rack_type = convert_to_protobuf(interface_rack_type, pb.RackType)
        interface_rear_port = convert_to_protobuf(interface_rear_port, pb.RearPort)
        interface_region = convert_to_protobuf(interface_region, pb.Region)
        interface_role = convert_to_protobuf(interface_role, pb.Role)
        interface_route_target = convert_to_protobuf(interface_route_target, pb.RouteTarget)
        interface_service = convert_to_protobuf(interface_service, pb.Service)
        interface_site = convert_to_protobuf(interface_site, pb.Site)
        interface_site_group = convert_to_protobuf(interface_site_group, pb.SiteGroup)
        interface_tag = convert_to_protobuf(interface_tag, pb.Tag)
        interface_tenant = convert_to_protobuf(interface_tenant, pb.Tenant)
        interface_tenant_group = convert_to_protobuf(interface_tenant_group, pb.TenantGroup)
        interface_tunnel = convert_to_protobuf(interface_tunnel, pb.Tunnel)
        interface_tunnel_group = convert_to_protobuf(interface_tunnel_group, pb.TunnelGroup)
        interface_tunnel_termination = convert_to_protobuf(interface_tunnel_termination, pb.TunnelTermination)
        interface_vlan = convert_to_protobuf(interface_vlan, pb.VLAN)
        interface_vlan_group = convert_to_protobuf(interface_vlan_group, pb.VLANGroup)
        interface_vlan_translation_policy = convert_to_protobuf(interface_vlan_translation_policy, pb.VLANTranslationPolicy)
        interface_vlan_translation_rule = convert_to_protobuf(interface_vlan_translation_rule, pb.VLANTranslationRule)
        interface_vm_interface = convert_to_protobuf(interface_vm_interface, pb.VMInterface)
        interface_vrf = convert_to_protobuf(interface_vrf, pb.VRF)
        interface_virtual_chassis = convert_to_protobuf(interface_virtual_chassis, pb.VirtualChassis)
        interface_virtual_circuit = convert_to_protobuf(interface_virtual_circuit, pb.VirtualCircuit)
        interface_virtual_circuit_termination = convert_to_protobuf(interface_virtual_circuit_termination, pb.VirtualCircuitTermination)
        interface_virtual_circuit_type = convert_to_protobuf(interface_virtual_circuit_type, pb.VirtualCircuitType)
        interface_virtual_device_context = convert_to_protobuf(interface_virtual_device_context, pb.VirtualDeviceContext)
        interface_virtual_disk = convert_to_protobuf(interface_virtual_disk, pb.VirtualDisk)
        interface_virtual_machine = convert_to_protobuf(interface_virtual_machine, pb.VirtualMachine)
        interface_wireless_lan = convert_to_protobuf(interface_wireless_lan, pb.WirelessLAN)
        interface_wireless_lan_group = convert_to_protobuf(interface_wireless_lan_group, pb.WirelessLANGroup)
        interface_wireless_link = convert_to_protobuf(interface_wireless_link, pb.WirelessLink)
        return pb.FHRPGroupAssignment(
            group=group,
            interface_asn=interface_asn,
            interface_asn_range=interface_asn_range,
            interface_aggregate=interface_aggregate,
            interface_cable=interface_cable,
            interface_cable_path=interface_cable_path,
            interface_cable_termination=interface_cable_termination,
            interface_circuit=interface_circuit,
            interface_circuit_group=interface_circuit_group,
            interface_circuit_group_assignment=interface_circuit_group_assignment,
            interface_circuit_termination=interface_circuit_termination,
            interface_circuit_type=interface_circuit_type,
            interface_cluster=interface_cluster,
            interface_cluster_group=interface_cluster_group,
            interface_cluster_type=interface_cluster_type,
            interface_console_port=interface_console_port,
            interface_console_server_port=interface_console_server_port,
            interface_contact=interface_contact,
            interface_contact_assignment=interface_contact_assignment,
            interface_contact_group=interface_contact_group,
            interface_contact_role=interface_contact_role,
            interface_device=interface_device,
            interface_device_bay=interface_device_bay,
            interface_device_role=interface_device_role,
            interface_device_type=interface_device_type,
            interface_fhrp_group=interface_fhrp_group,
            interface_fhrp_group_assignment=interface_fhrp_group_assignment,
            interface_front_port=interface_front_port,
            interface_ike_policy=interface_ike_policy,
            interface_ike_proposal=interface_ike_proposal,
            interface_ip_address=interface_ip_address,
            interface_ip_range=interface_ip_range,
            interface_ip_sec_policy=interface_ip_sec_policy,
            interface_ip_sec_profile=interface_ip_sec_profile,
            interface_ip_sec_proposal=interface_ip_sec_proposal,
            interface_interface=interface_interface,
            interface_inventory_item=interface_inventory_item,
            interface_inventory_item_role=interface_inventory_item_role,
            interface_l2vpn=interface_l2vpn,
            interface_l2vpn_termination=interface_l2vpn_termination,
            interface_location=interface_location,
            interface_mac_address=interface_mac_address,
            interface_manufacturer=interface_manufacturer,
            interface_module=interface_module,
            interface_module_bay=interface_module_bay,
            interface_module_type=interface_module_type,
            interface_platform=interface_platform,
            interface_power_feed=interface_power_feed,
            interface_power_outlet=interface_power_outlet,
            interface_power_panel=interface_power_panel,
            interface_power_port=interface_power_port,
            interface_prefix=interface_prefix,
            interface_provider=interface_provider,
            interface_provider_account=interface_provider_account,
            interface_provider_network=interface_provider_network,
            interface_rir=interface_rir,
            interface_rack=interface_rack,
            interface_rack_reservation=interface_rack_reservation,
            interface_rack_role=interface_rack_role,
            interface_rack_type=interface_rack_type,
            interface_rear_port=interface_rear_port,
            interface_region=interface_region,
            interface_role=interface_role,
            interface_route_target=interface_route_target,
            interface_service=interface_service,
            interface_site=interface_site,
            interface_site_group=interface_site_group,
            interface_tag=interface_tag,
            interface_tenant=interface_tenant,
            interface_tenant_group=interface_tenant_group,
            interface_tunnel=interface_tunnel,
            interface_tunnel_group=interface_tunnel_group,
            interface_tunnel_termination=interface_tunnel_termination,
            interface_vlan=interface_vlan,
            interface_vlan_group=interface_vlan_group,
            interface_vlan_translation_policy=interface_vlan_translation_policy,
            interface_vlan_translation_rule=interface_vlan_translation_rule,
            interface_vm_interface=interface_vm_interface,
            interface_vrf=interface_vrf,
            interface_virtual_chassis=interface_virtual_chassis,
            interface_virtual_circuit=interface_virtual_circuit,
            interface_virtual_circuit_termination=interface_virtual_circuit_termination,
            interface_virtual_circuit_type=interface_virtual_circuit_type,
            interface_virtual_device_context=interface_virtual_device_context,
            interface_virtual_disk=interface_virtual_disk,
            interface_virtual_machine=interface_virtual_machine,
            interface_wireless_lan=interface_wireless_lan,
            interface_wireless_lan_group=interface_wireless_lan_group,
            interface_wireless_link=interface_wireless_link,
            priority=priority,
        )


class FrontPort:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.FrontPort."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        color: str | None = None,
        rear_port: str | RearPort | pb.RearPort | None = None,
        rear_port_position: int | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.FrontPort:
        """Create a new FrontPort."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        rear_port = convert_to_protobuf(rear_port, pb.RearPort)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.FrontPort(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            color=color,
            rear_port=rear_port,
            rear_port_position=rear_port_position,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class GenericObject:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.GenericObject."""

    def __new__(
        cls,
        object_asn: str | ASN | pb.ASN | None = None,
        object_asn_range: str | ASNRange | pb.ASNRange | None = None,
        object_aggregate: str | Aggregate | pb.Aggregate | None = None,
        object_cable: str | Cable | pb.Cable | None = None,
        object_cable_path: str | CablePath | pb.CablePath | None = None,
        object_cable_termination: str | CableTermination | pb.CableTermination | None = None,
        object_circuit: str | Circuit | pb.Circuit | None = None,
        object_circuit_group: str | CircuitGroup | pb.CircuitGroup | None = None,
        object_circuit_group_assignment: str | CircuitGroupAssignment | pb.CircuitGroupAssignment | None = None,
        object_circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        object_circuit_type: str | CircuitType | pb.CircuitType | None = None,
        object_cluster: str | Cluster | pb.Cluster | None = None,
        object_cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        object_cluster_type: str | ClusterType | pb.ClusterType | None = None,
        object_console_port: str | ConsolePort | pb.ConsolePort | None = None,
        object_console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        object_contact: str | Contact | pb.Contact | None = None,
        object_contact_assignment: str | ContactAssignment | pb.ContactAssignment | None = None,
        object_contact_group: str | ContactGroup | pb.ContactGroup | None = None,
        object_contact_role: str | ContactRole | pb.ContactRole | None = None,
        object_device: str | Device | pb.Device | None = None,
        object_device_bay: str | DeviceBay | pb.DeviceBay | None = None,
        object_device_role: str | DeviceRole | pb.DeviceRole | None = None,
        object_device_type: str | DeviceType | pb.DeviceType | None = None,
        object_fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        object_fhrp_group_assignment: str | FHRPGroupAssignment | pb.FHRPGroupAssignment | None = None,
        object_front_port: str | FrontPort | pb.FrontPort | None = None,
        object_ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        object_ike_proposal: str | IKEProposal | pb.IKEProposal | None = None,
        object_ip_address: str | IPAddress | pb.IPAddress | None = None,
        object_ip_range: str | IPRange | pb.IPRange | None = None,
        object_ip_sec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        object_ip_sec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        object_ip_sec_proposal: str | IPSecProposal | pb.IPSecProposal | None = None,
        object_interface: str | Interface | pb.Interface | None = None,
        object_inventory_item: str | InventoryItem | pb.InventoryItem | None = None,
        object_inventory_item_role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        object_l2vpn: str | L2VPN | pb.L2VPN | None = None,
        object_l2vpn_termination: str | L2VPNTermination | pb.L2VPNTermination | None = None,
        object_location: str | Location | pb.Location | None = None,
        object_mac_address: str | MACAddress | pb.MACAddress | None = None,
        object_manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        object_module: str | Module | pb.Module | None = None,
        object_module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        object_module_type: str | ModuleType | pb.ModuleType | None = None,
        object_platform: str | Platform | pb.Platform | None = None,
        object_power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        object_power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        object_power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        object_power_port: str | PowerPort | pb.PowerPort | None = None,
        object_prefix: str | Prefix | pb.Prefix | None = None,
        object_provider: str | Provider | pb.Provider | None = None,
        object_provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        object_provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        object_rir: str | RIR | pb.RIR | None = None,
        object_rack: str | Rack | pb.Rack | None = None,
        object_rack_reservation: str | RackReservation | pb.RackReservation | None = None,
        object_rack_role: str | RackRole | pb.RackRole | None = None,
        object_rack_type: str | RackType | pb.RackType | None = None,
        object_rear_port: str | RearPort | pb.RearPort | None = None,
        object_region: str | Region | pb.Region | None = None,
        object_role: str | Role | pb.Role | None = None,
        object_route_target: str | RouteTarget | pb.RouteTarget | None = None,
        object_service: str | Service | pb.Service | None = None,
        object_site: str | Site | pb.Site | None = None,
        object_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        object_tag: str | Tag | pb.Tag | None = None,
        object_tenant: str | Tenant | pb.Tenant | None = None,
        object_tenant_group: str | TenantGroup | pb.TenantGroup | None = None,
        object_tunnel: str | Tunnel | pb.Tunnel | None = None,
        object_tunnel_group: str | TunnelGroup | pb.TunnelGroup | None = None,
        object_tunnel_termination: str | TunnelTermination | pb.TunnelTermination | None = None,
        object_vlan: str | VLAN | pb.VLAN | None = None,
        object_vlan_group: str | VLANGroup | pb.VLANGroup | None = None,
        object_vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        object_vlan_translation_rule: str | VLANTranslationRule | pb.VLANTranslationRule | None = None,
        object_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        object_vrf: str | VRF | pb.VRF | None = None,
        object_virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        object_virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        object_virtual_circuit_termination: str | VirtualCircuitTermination | pb.VirtualCircuitTermination | None = None,
        object_virtual_circuit_type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        object_virtual_device_context: str | VirtualDeviceContext | pb.VirtualDeviceContext | None = None,
        object_virtual_disk: str | VirtualDisk | pb.VirtualDisk | None = None,
        object_virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        object_wireless_lan: str | WirelessLAN | pb.WirelessLAN | None = None,
        object_wireless_lan_group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        object_wireless_link: str | WirelessLink | pb.WirelessLink | None = None,
    ) -> pb.GenericObject:
        """Create a new GenericObject."""
        object_asn = convert_to_protobuf(object_asn, pb.ASN)
        object_asn_range = convert_to_protobuf(object_asn_range, pb.ASNRange)
        object_aggregate = convert_to_protobuf(object_aggregate, pb.Aggregate)
        object_cable = convert_to_protobuf(object_cable, pb.Cable)
        object_cable_path = convert_to_protobuf(object_cable_path, pb.CablePath)
        object_cable_termination = convert_to_protobuf(object_cable_termination, pb.CableTermination)
        object_circuit = convert_to_protobuf(object_circuit, pb.Circuit)
        object_circuit_group = convert_to_protobuf(object_circuit_group, pb.CircuitGroup)
        object_circuit_group_assignment = convert_to_protobuf(object_circuit_group_assignment, pb.CircuitGroupAssignment)
        object_circuit_termination = convert_to_protobuf(object_circuit_termination, pb.CircuitTermination)
        object_circuit_type = convert_to_protobuf(object_circuit_type, pb.CircuitType)
        object_cluster = convert_to_protobuf(object_cluster, pb.Cluster)
        object_cluster_group = convert_to_protobuf(object_cluster_group, pb.ClusterGroup)
        object_cluster_type = convert_to_protobuf(object_cluster_type, pb.ClusterType)
        object_console_port = convert_to_protobuf(object_console_port, pb.ConsolePort)
        object_console_server_port = convert_to_protobuf(object_console_server_port, pb.ConsoleServerPort)
        object_contact = convert_to_protobuf(object_contact, pb.Contact)
        object_contact_assignment = convert_to_protobuf(object_contact_assignment, pb.ContactAssignment)
        object_contact_group = convert_to_protobuf(object_contact_group, pb.ContactGroup)
        object_contact_role = convert_to_protobuf(object_contact_role, pb.ContactRole)
        object_device = convert_to_protobuf(object_device, pb.Device)
        object_device_bay = convert_to_protobuf(object_device_bay, pb.DeviceBay)
        object_device_role = convert_to_protobuf(object_device_role, pb.DeviceRole)
        object_device_type = convert_to_protobuf(object_device_type, pb.DeviceType)
        object_fhrp_group = convert_to_protobuf(object_fhrp_group, pb.FHRPGroup)
        object_fhrp_group_assignment = convert_to_protobuf(object_fhrp_group_assignment, pb.FHRPGroupAssignment)
        object_front_port = convert_to_protobuf(object_front_port, pb.FrontPort)
        object_ike_policy = convert_to_protobuf(object_ike_policy, pb.IKEPolicy)
        object_ike_proposal = convert_to_protobuf(object_ike_proposal, pb.IKEProposal)
        object_ip_address = convert_to_protobuf(object_ip_address, pb.IPAddress)
        object_ip_range = convert_to_protobuf(object_ip_range, pb.IPRange)
        object_ip_sec_policy = convert_to_protobuf(object_ip_sec_policy, pb.IPSecPolicy)
        object_ip_sec_profile = convert_to_protobuf(object_ip_sec_profile, pb.IPSecProfile)
        object_ip_sec_proposal = convert_to_protobuf(object_ip_sec_proposal, pb.IPSecProposal)
        object_interface = convert_to_protobuf(object_interface, pb.Interface)
        object_inventory_item = convert_to_protobuf(object_inventory_item, pb.InventoryItem)
        object_inventory_item_role = convert_to_protobuf(object_inventory_item_role, pb.InventoryItemRole)
        object_l2vpn = convert_to_protobuf(object_l2vpn, pb.L2VPN)
        object_l2vpn_termination = convert_to_protobuf(object_l2vpn_termination, pb.L2VPNTermination)
        object_location = convert_to_protobuf(object_location, pb.Location)
        object_mac_address = convert_to_protobuf(object_mac_address, pb.MACAddress)
        object_manufacturer = convert_to_protobuf(object_manufacturer, pb.Manufacturer)
        object_module = convert_to_protobuf(object_module, pb.Module)
        object_module_bay = convert_to_protobuf(object_module_bay, pb.ModuleBay)
        object_module_type = convert_to_protobuf(object_module_type, pb.ModuleType)
        object_platform = convert_to_protobuf(object_platform, pb.Platform)
        object_power_feed = convert_to_protobuf(object_power_feed, pb.PowerFeed)
        object_power_outlet = convert_to_protobuf(object_power_outlet, pb.PowerOutlet)
        object_power_panel = convert_to_protobuf(object_power_panel, pb.PowerPanel)
        object_power_port = convert_to_protobuf(object_power_port, pb.PowerPort)
        object_prefix = convert_to_protobuf(object_prefix, pb.Prefix)
        object_provider = convert_to_protobuf(object_provider, pb.Provider)
        object_provider_account = convert_to_protobuf(object_provider_account, pb.ProviderAccount)
        object_provider_network = convert_to_protobuf(object_provider_network, pb.ProviderNetwork)
        object_rir = convert_to_protobuf(object_rir, pb.RIR)
        object_rack = convert_to_protobuf(object_rack, pb.Rack)
        object_rack_reservation = convert_to_protobuf(object_rack_reservation, pb.RackReservation)
        object_rack_role = convert_to_protobuf(object_rack_role, pb.RackRole)
        object_rack_type = convert_to_protobuf(object_rack_type, pb.RackType)
        object_rear_port = convert_to_protobuf(object_rear_port, pb.RearPort)
        object_region = convert_to_protobuf(object_region, pb.Region)
        object_role = convert_to_protobuf(object_role, pb.Role)
        object_route_target = convert_to_protobuf(object_route_target, pb.RouteTarget)
        object_service = convert_to_protobuf(object_service, pb.Service)
        object_site = convert_to_protobuf(object_site, pb.Site)
        object_site_group = convert_to_protobuf(object_site_group, pb.SiteGroup)
        object_tag = convert_to_protobuf(object_tag, pb.Tag)
        object_tenant = convert_to_protobuf(object_tenant, pb.Tenant)
        object_tenant_group = convert_to_protobuf(object_tenant_group, pb.TenantGroup)
        object_tunnel = convert_to_protobuf(object_tunnel, pb.Tunnel)
        object_tunnel_group = convert_to_protobuf(object_tunnel_group, pb.TunnelGroup)
        object_tunnel_termination = convert_to_protobuf(object_tunnel_termination, pb.TunnelTermination)
        object_vlan = convert_to_protobuf(object_vlan, pb.VLAN)
        object_vlan_group = convert_to_protobuf(object_vlan_group, pb.VLANGroup)
        object_vlan_translation_policy = convert_to_protobuf(object_vlan_translation_policy, pb.VLANTranslationPolicy)
        object_vlan_translation_rule = convert_to_protobuf(object_vlan_translation_rule, pb.VLANTranslationRule)
        object_vm_interface = convert_to_protobuf(object_vm_interface, pb.VMInterface)
        object_vrf = convert_to_protobuf(object_vrf, pb.VRF)
        object_virtual_chassis = convert_to_protobuf(object_virtual_chassis, pb.VirtualChassis)
        object_virtual_circuit = convert_to_protobuf(object_virtual_circuit, pb.VirtualCircuit)
        object_virtual_circuit_termination = convert_to_protobuf(object_virtual_circuit_termination, pb.VirtualCircuitTermination)
        object_virtual_circuit_type = convert_to_protobuf(object_virtual_circuit_type, pb.VirtualCircuitType)
        object_virtual_device_context = convert_to_protobuf(object_virtual_device_context, pb.VirtualDeviceContext)
        object_virtual_disk = convert_to_protobuf(object_virtual_disk, pb.VirtualDisk)
        object_virtual_machine = convert_to_protobuf(object_virtual_machine, pb.VirtualMachine)
        object_wireless_lan = convert_to_protobuf(object_wireless_lan, pb.WirelessLAN)
        object_wireless_lan_group = convert_to_protobuf(object_wireless_lan_group, pb.WirelessLANGroup)
        object_wireless_link = convert_to_protobuf(object_wireless_link, pb.WirelessLink)
        return pb.GenericObject(
            object_asn=object_asn,
            object_asn_range=object_asn_range,
            object_aggregate=object_aggregate,
            object_cable=object_cable,
            object_cable_path=object_cable_path,
            object_cable_termination=object_cable_termination,
            object_circuit=object_circuit,
            object_circuit_group=object_circuit_group,
            object_circuit_group_assignment=object_circuit_group_assignment,
            object_circuit_termination=object_circuit_termination,
            object_circuit_type=object_circuit_type,
            object_cluster=object_cluster,
            object_cluster_group=object_cluster_group,
            object_cluster_type=object_cluster_type,
            object_console_port=object_console_port,
            object_console_server_port=object_console_server_port,
            object_contact=object_contact,
            object_contact_assignment=object_contact_assignment,
            object_contact_group=object_contact_group,
            object_contact_role=object_contact_role,
            object_device=object_device,
            object_device_bay=object_device_bay,
            object_device_role=object_device_role,
            object_device_type=object_device_type,
            object_fhrp_group=object_fhrp_group,
            object_fhrp_group_assignment=object_fhrp_group_assignment,
            object_front_port=object_front_port,
            object_ike_policy=object_ike_policy,
            object_ike_proposal=object_ike_proposal,
            object_ip_address=object_ip_address,
            object_ip_range=object_ip_range,
            object_ip_sec_policy=object_ip_sec_policy,
            object_ip_sec_profile=object_ip_sec_profile,
            object_ip_sec_proposal=object_ip_sec_proposal,
            object_interface=object_interface,
            object_inventory_item=object_inventory_item,
            object_inventory_item_role=object_inventory_item_role,
            object_l2vpn=object_l2vpn,
            object_l2vpn_termination=object_l2vpn_termination,
            object_location=object_location,
            object_mac_address=object_mac_address,
            object_manufacturer=object_manufacturer,
            object_module=object_module,
            object_module_bay=object_module_bay,
            object_module_type=object_module_type,
            object_platform=object_platform,
            object_power_feed=object_power_feed,
            object_power_outlet=object_power_outlet,
            object_power_panel=object_power_panel,
            object_power_port=object_power_port,
            object_prefix=object_prefix,
            object_provider=object_provider,
            object_provider_account=object_provider_account,
            object_provider_network=object_provider_network,
            object_rir=object_rir,
            object_rack=object_rack,
            object_rack_reservation=object_rack_reservation,
            object_rack_role=object_rack_role,
            object_rack_type=object_rack_type,
            object_rear_port=object_rear_port,
            object_region=object_region,
            object_role=object_role,
            object_route_target=object_route_target,
            object_service=object_service,
            object_site=object_site,
            object_site_group=object_site_group,
            object_tag=object_tag,
            object_tenant=object_tenant,
            object_tenant_group=object_tenant_group,
            object_tunnel=object_tunnel,
            object_tunnel_group=object_tunnel_group,
            object_tunnel_termination=object_tunnel_termination,
            object_vlan=object_vlan,
            object_vlan_group=object_vlan_group,
            object_vlan_translation_policy=object_vlan_translation_policy,
            object_vlan_translation_rule=object_vlan_translation_rule,
            object_vm_interface=object_vm_interface,
            object_vrf=object_vrf,
            object_virtual_chassis=object_virtual_chassis,
            object_virtual_circuit=object_virtual_circuit,
            object_virtual_circuit_termination=object_virtual_circuit_termination,
            object_virtual_circuit_type=object_virtual_circuit_type,
            object_virtual_device_context=object_virtual_device_context,
            object_virtual_disk=object_virtual_disk,
            object_virtual_machine=object_virtual_machine,
            object_wireless_lan=object_wireless_lan,
            object_wireless_lan_group=object_wireless_lan_group,
            object_wireless_link=object_wireless_link,
        )


class IKEPolicy:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IKEPolicy."""

    def __new__(
        cls,
        name: str | None = None,
        description: str | None = None,
        version: int | None = None,
        mode: str | None = None,
        preshared_key: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        proposals: list[str | IKEProposal | pb.IKEProposal] | None = None,
    ) -> pb.IKEPolicy:
        """Create a new IKEPolicy."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        proposals = convert_to_protobuf_list(proposals, pb.IKEProposal)
        return pb.IKEPolicy(
            name=name,
            description=description,
            version=version,
            mode=mode,
            preshared_key=preshared_key,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            proposals=proposals,
        )


class IKEProposal:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IKEProposal."""

    def __new__(
        cls,
        name: str | None = None,
        description: str | None = None,
        authentication_method: str | None = None,
        encryption_algorithm: str | None = None,
        authentication_algorithm: str | None = None,
        group: int | None = None,
        sa_lifetime: int | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.IKEProposal:
        """Create a new IKEProposal."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.IKEProposal(
            name=name,
            description=description,
            authentication_method=authentication_method,
            encryption_algorithm=encryption_algorithm,
            authentication_algorithm=authentication_algorithm,
            group=group,
            sa_lifetime=sa_lifetime,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class IPAddress:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IPAddress."""

    def __new__(
        cls,
        address: str | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        status: str | None = None,
        role: str | None = None,
        assigned_object_fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        assigned_object_interface: str | Interface | pb.Interface | None = None,
        assigned_object_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        nat_inside: str | IPAddress | pb.IPAddress | None = None,
        dns_name: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        # shortcuts
        manufacturer: str | Manufacturer | pb.Manufacturer = None,
        device_type: str | DeviceType | pb.DeviceType = None,
        platform: str | Platform | pb.Platform = None,
        site: str | Site | pb.Site = None,
        device_role: str | DeviceRole | pb.DeviceRole = None,
        device: str | Device | pb.Device = None,
    ) -> pb.IPAddress:
        """Create a new IPAddress."""
        vrf = convert_to_protobuf(vrf, pb.VRF)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        assigned_object_fhrp_group = convert_to_protobuf(assigned_object_fhrp_group, pb.FHRPGroup)
        assigned_object_interface = convert_to_protobuf(assigned_object_interface, pb.Interface)
        assigned_object_vm_interface = convert_to_protobuf(assigned_object_vm_interface, pb.VMInterface)
        nat_inside = convert_to_protobuf(nat_inside, pb.IPAddress)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)

        # shortcut types (not directly used)
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        device_type = convert_to_protobuf(device_type, pb.DeviceType)
        platform = convert_to_protobuf(platform, pb.Platform)
        site = convert_to_protobuf(site, pb.Site)
        device_role = convert_to_protobuf(device_role, pb.DeviceRole)
        device = convert_to_protobuf(device, pb.Device)

        # apply shortcuts
        if manufacturer is not None:
            if platform is not None and not platform.HasField('manufacturer'):
                platform.manufacturer.CopyFrom(manufacturer)
            if device_type is not None and not device_type.HasField('manufacturer'):
                device_type.manufacturer.CopyFrom(manufacturer)
        if device_type is not None:
            if device is not None and not device.HasField('device_type'):
                device.device_type.CopyFrom(device_type)
        if platform is not None:
            if device is not None and not device.HasField('platform'):
                device.platform.CopyFrom(platform)
        if site is not None:
            if device is not None and not device.HasField('site'):
                device.site.CopyFrom(site)
        if device_role is not None:
            if device is not None and not device.HasField('role'):
                device.role.CopyFrom(device_role)
        if device is not None:
            if assigned_object_interface is not None and not assigned_object_interface.HasField('device'):
                assigned_object_interface.device.CopyFrom(device)
            if assigned_object_vm_interface is not None and not assigned_object_vm_interface.HasField('device'):
                assigned_object_vm_interface.device.CopyFrom(device)
        return pb.IPAddress(
            address=address,
            vrf=vrf,
            tenant=tenant,
            status=status,
            role=role,
            assigned_object_fhrp_group=assigned_object_fhrp_group,
            assigned_object_interface=assigned_object_interface,
            assigned_object_vm_interface=assigned_object_vm_interface,
            nat_inside=nat_inside,
            dns_name=dns_name,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class IPRange:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IPRange."""

    def __new__(
        cls,
        start_address: str | None = None,
        end_address: str | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        status: str | None = None,
        role: str | Role | pb.Role | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        mark_utilized: bool | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.IPRange:
        """Create a new IPRange."""
        vrf = convert_to_protobuf(vrf, pb.VRF)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        role = convert_to_protobuf(role, pb.Role)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.IPRange(
            start_address=start_address,
            end_address=end_address,
            vrf=vrf,
            tenant=tenant,
            status=status,
            role=role,
            description=description,
            comments=comments,
            tags=tags,
            mark_utilized=mark_utilized,
            custom_fields=custom_fields,
        )


class IPSecPolicy:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IPSecPolicy."""

    def __new__(
        cls,
        name: str | None = None,
        description: str | None = None,
        pfs_group: int | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        proposals: list[str | IPSecProposal | pb.IPSecProposal] | None = None,
    ) -> pb.IPSecPolicy:
        """Create a new IPSecPolicy."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        proposals = convert_to_protobuf_list(proposals, pb.IPSecProposal)
        return pb.IPSecPolicy(
            name=name,
            description=description,
            pfs_group=pfs_group,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            proposals=proposals,
        )


class IPSecProfile:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IPSecProfile."""

    def __new__(
        cls,
        name: str | None = None,
        description: str | None = None,
        mode: str | None = None,
        ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        ipsec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.IPSecProfile:
        """Create a new IPSecProfile."""
        ike_policy = convert_to_protobuf(ike_policy, pb.IKEPolicy)
        ipsec_policy = convert_to_protobuf(ipsec_policy, pb.IPSecPolicy)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.IPSecProfile(
            name=name,
            description=description,
            mode=mode,
            ike_policy=ike_policy,
            ipsec_policy=ipsec_policy,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class IPSecProposal:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.IPSecProposal."""

    def __new__(
        cls,
        name: str | None = None,
        description: str | None = None,
        encryption_algorithm: str | None = None,
        authentication_algorithm: str | None = None,
        sa_lifetime_seconds: int | None = None,
        sa_lifetime_data: int | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.IPSecProposal:
        """Create a new IPSecProposal."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.IPSecProposal(
            name=name,
            description=description,
            encryption_algorithm=encryption_algorithm,
            authentication_algorithm=authentication_algorithm,
            sa_lifetime_seconds=sa_lifetime_seconds,
            sa_lifetime_data=sa_lifetime_data,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class Interface:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Interface."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        enabled: bool | None = None,
        parent: str | Interface | pb.Interface | None = None,
        bridge: str | Interface | pb.Interface | None = None,
        lag: str | Interface | pb.Interface | None = None,
        mtu: int | None = None,
        primary_mac_address: str | MACAddress | pb.MACAddress | None = None,
        speed: int | None = None,
        duplex: str | None = None,
        wwn: str | None = None,
        mgmt_only: bool | None = None,
        description: str | None = None,
        mode: str | None = None,
        rf_role: str | None = None,
        rf_channel: str | None = None,
        poe_mode: str | None = None,
        poe_type: str | None = None,
        rf_channel_frequency: float | None = None,
        rf_channel_width: float | None = None,
        tx_power: int | None = None,
        untagged_vlan: str | VLAN | pb.VLAN | None = None,
        qinq_svlan: str | VLAN | pb.VLAN | None = None,
        vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        mark_connected: bool | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        vdcs: list[str | VirtualDeviceContext | pb.VirtualDeviceContext] | None = None,
        tagged_vlans: list[str | VLAN | pb.VLAN] | None = None,
        wireless_lans: list[str | WirelessLAN | pb.WirelessLAN] | None = None,
        # shortcuts
        manufacturer: str | Manufacturer | pb.Manufacturer = None,
        device_type: str | DeviceType | pb.DeviceType = None,
        platform: str | Platform | pb.Platform = None,
        site: str | Site | pb.Site = None,
        role: str | DeviceRole | pb.DeviceRole = None,
    ) -> pb.Interface:
        """Create a new Interface."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        parent = convert_to_protobuf(parent, pb.Interface)
        bridge = convert_to_protobuf(bridge, pb.Interface)
        lag = convert_to_protobuf(lag, pb.Interface)
        primary_mac_address = convert_to_protobuf(primary_mac_address, pb.MACAddress)
        untagged_vlan = convert_to_protobuf(untagged_vlan, pb.VLAN)
        qinq_svlan = convert_to_protobuf(qinq_svlan, pb.VLAN)
        vlan_translation_policy = convert_to_protobuf(vlan_translation_policy, pb.VLANTranslationPolicy)
        vrf = convert_to_protobuf(vrf, pb.VRF)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        vdcs = convert_to_protobuf_list(vdcs, pb.VirtualDeviceContext)
        tagged_vlans = convert_to_protobuf_list(tagged_vlans, pb.VLAN)
        wireless_lans = convert_to_protobuf_list(wireless_lans, pb.WirelessLAN)

        # shortcut types (not directly used)
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        device_type = convert_to_protobuf(device_type, pb.DeviceType)
        platform = convert_to_protobuf(platform, pb.Platform)
        site = convert_to_protobuf(site, pb.Site)
        role = convert_to_protobuf(role, pb.DeviceRole)

        # apply shortcuts
        if manufacturer is not None:
            if platform is not None and not platform.HasField('manufacturer'):
                platform.manufacturer.CopyFrom(manufacturer)
            if device_type is not None and not device_type.HasField('manufacturer'):
                device_type.manufacturer.CopyFrom(manufacturer)
        if device_type is not None:
            if device is not None and not device.HasField('device_type'):
                device.device_type.CopyFrom(device_type)
        if platform is not None:
            if device is not None and not device.HasField('platform'):
                device.platform.CopyFrom(platform)
        if site is not None:
            if device is not None and not device.HasField('site'):
                device.site.CopyFrom(site)
        if role is not None:
            if device is not None and not device.HasField('role'):
                device.role.CopyFrom(role)
        return pb.Interface(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            enabled=enabled,
            parent=parent,
            bridge=bridge,
            lag=lag,
            mtu=mtu,
            primary_mac_address=primary_mac_address,
            speed=speed,
            duplex=duplex,
            wwn=wwn,
            mgmt_only=mgmt_only,
            description=description,
            mode=mode,
            rf_role=rf_role,
            rf_channel=rf_channel,
            poe_mode=poe_mode,
            poe_type=poe_type,
            rf_channel_frequency=rf_channel_frequency,
            rf_channel_width=rf_channel_width,
            tx_power=tx_power,
            untagged_vlan=untagged_vlan,
            qinq_svlan=qinq_svlan,
            vlan_translation_policy=vlan_translation_policy,
            mark_connected=mark_connected,
            vrf=vrf,
            tags=tags,
            custom_fields=custom_fields,
            vdcs=vdcs,
            tagged_vlans=tagged_vlans,
            wireless_lans=wireless_lans,
        )


class InventoryItem:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.InventoryItem."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        parent: str | InventoryItem | pb.InventoryItem | None = None,
        name: str | None = None,
        label: str | None = None,
        status: str | None = None,
        role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        part_id: str | None = None,
        serial: str | None = None,
        asset_tag: str | None = None,
        discovered: bool | None = None,
        description: str | None = None,
        component_console_port: str | ConsolePort | pb.ConsolePort | None = None,
        component_console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        component_front_port: str | FrontPort | pb.FrontPort | None = None,
        component_interface: str | Interface | pb.Interface | None = None,
        component_power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        component_power_port: str | PowerPort | pb.PowerPort | None = None,
        component_rear_port: str | RearPort | pb.RearPort | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.InventoryItem:
        """Create a new InventoryItem."""
        device = convert_to_protobuf(device, pb.Device)
        parent = convert_to_protobuf(parent, pb.InventoryItem)
        role = convert_to_protobuf(role, pb.InventoryItemRole)
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        component_console_port = convert_to_protobuf(component_console_port, pb.ConsolePort)
        component_console_server_port = convert_to_protobuf(component_console_server_port, pb.ConsoleServerPort)
        component_front_port = convert_to_protobuf(component_front_port, pb.FrontPort)
        component_interface = convert_to_protobuf(component_interface, pb.Interface)
        component_power_outlet = convert_to_protobuf(component_power_outlet, pb.PowerOutlet)
        component_power_port = convert_to_protobuf(component_power_port, pb.PowerPort)
        component_rear_port = convert_to_protobuf(component_rear_port, pb.RearPort)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.InventoryItem(
            device=device,
            parent=parent,
            name=name,
            label=label,
            status=status,
            role=role,
            manufacturer=manufacturer,
            part_id=part_id,
            serial=serial,
            asset_tag=asset_tag,
            discovered=discovered,
            description=description,
            component_console_port=component_console_port,
            component_console_server_port=component_console_server_port,
            component_front_port=component_front_port,
            component_interface=component_interface,
            component_power_outlet=component_power_outlet,
            component_power_port=component_power_port,
            component_rear_port=component_rear_port,
            tags=tags,
            custom_fields=custom_fields,
        )


class InventoryItemRole:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.InventoryItemRole."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.InventoryItemRole:
        """Create a new InventoryItemRole."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.InventoryItemRole(
            name=name,
            slug=slug,
            color=color,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class L2VPN:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.L2VPN."""

    def __new__(
        cls,
        identifier: int | None = None,
        name: str | None = None,
        slug: str | None = None,
        type: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        import_targets: list[str | RouteTarget | pb.RouteTarget] | None = None,
        export_targets: list[str | RouteTarget | pb.RouteTarget] | None = None,
    ) -> pb.L2VPN:
        """Create a new L2VPN."""
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        import_targets = convert_to_protobuf_list(import_targets, pb.RouteTarget)
        export_targets = convert_to_protobuf_list(export_targets, pb.RouteTarget)
        return pb.L2VPN(
            identifier=identifier,
            name=name,
            slug=slug,
            type=type,
            description=description,
            comments=comments,
            tenant=tenant,
            tags=tags,
            custom_fields=custom_fields,
            import_targets=import_targets,
            export_targets=export_targets,
        )


class L2VPNTermination:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.L2VPNTermination."""

    def __new__(
        cls,
        l2vpn: str | L2VPN | pb.L2VPN | None = None,
        assigned_object_interface: str | Interface | pb.Interface | None = None,
        assigned_object_vlan: str | VLAN | pb.VLAN | None = None,
        assigned_object_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.L2VPNTermination:
        """Create a new L2VPNTermination."""
        l2vpn = convert_to_protobuf(l2vpn, pb.L2VPN)
        assigned_object_interface = convert_to_protobuf(assigned_object_interface, pb.Interface)
        assigned_object_vlan = convert_to_protobuf(assigned_object_vlan, pb.VLAN)
        assigned_object_vm_interface = convert_to_protobuf(assigned_object_vm_interface, pb.VMInterface)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.L2VPNTermination(
            l2vpn=l2vpn,
            assigned_object_interface=assigned_object_interface,
            assigned_object_vlan=assigned_object_vlan,
            assigned_object_vm_interface=assigned_object_vm_interface,
            tags=tags,
            custom_fields=custom_fields,
        )


class Location:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Location."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        site: str | Site | pb.Site | None = None,
        parent: str | Location | pb.Location | None = None,
        status: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        facility: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Location:
        """Create a new Location."""
        site = convert_to_protobuf(site, pb.Site)
        parent = convert_to_protobuf(parent, pb.Location)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Location(
            name=name,
            slug=slug,
            site=site,
            parent=parent,
            status=status,
            tenant=tenant,
            facility=facility,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class MACAddress:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.MACAddress."""

    def __new__(
        cls,
        mac_address: str | None = None,
        assigned_object_interface: str | Interface | pb.Interface | None = None,
        assigned_object_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.MACAddress:
        """Create a new MACAddress."""
        assigned_object_interface = convert_to_protobuf(assigned_object_interface, pb.Interface)
        assigned_object_vm_interface = convert_to_protobuf(assigned_object_vm_interface, pb.VMInterface)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.MACAddress(
            mac_address=mac_address,
            assigned_object_interface=assigned_object_interface,
            assigned_object_vm_interface=assigned_object_vm_interface,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class Manufacturer:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Manufacturer."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Manufacturer:
        """Create a new Manufacturer."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Manufacturer(
            name=name,
            slug=slug,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Module:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Module."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        module_type: str | ModuleType | pb.ModuleType | None = None,
        status: str | None = None,
        serial: str | None = None,
        asset_tag: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Module:
        """Create a new Module."""
        device = convert_to_protobuf(device, pb.Device)
        module_bay = convert_to_protobuf(module_bay, pb.ModuleBay)
        module_type = convert_to_protobuf(module_type, pb.ModuleType)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Module(
            device=device,
            module_bay=module_bay,
            module_type=module_type,
            status=status,
            serial=serial,
            asset_tag=asset_tag,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class ModuleBay:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ModuleBay."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        installed_module: str | Module | pb.Module | None = None,
        label: str | None = None,
        position: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ModuleBay:
        """Create a new ModuleBay."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        installed_module = convert_to_protobuf(installed_module, pb.Module)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ModuleBay(
            device=device,
            module=module,
            name=name,
            installed_module=installed_module,
            label=label,
            position=position,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class ModuleType:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ModuleType."""

    def __new__(
        cls,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        model: str | None = None,
        part_number: str | None = None,
        airflow: str | None = None,
        weight: float | None = None,
        weight_unit: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ModuleType:
        """Create a new ModuleType."""
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ModuleType(
            manufacturer=manufacturer,
            model=model,
            part_number=part_number,
            airflow=airflow,
            weight=weight,
            weight_unit=weight_unit,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class Platform:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Platform."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Platform:
        """Create a new Platform."""
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Platform(
            name=name,
            slug=slug,
            manufacturer=manufacturer,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class PowerFeed:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.PowerFeed."""

    def __new__(
        cls,
        power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        rack: str | Rack | pb.Rack | None = None,
        name: str | None = None,
        status: str | None = None,
        type: str | None = None,
        supply: str | None = None,
        phase: str | None = None,
        voltage: int | None = None,
        amperage: int | None = None,
        max_utilization: int | None = None,
        mark_connected: bool | None = None,
        description: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.PowerFeed:
        """Create a new PowerFeed."""
        power_panel = convert_to_protobuf(power_panel, pb.PowerPanel)
        rack = convert_to_protobuf(rack, pb.Rack)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.PowerFeed(
            power_panel=power_panel,
            rack=rack,
            name=name,
            status=status,
            type=type,
            supply=supply,
            phase=phase,
            voltage=voltage,
            amperage=amperage,
            max_utilization=max_utilization,
            mark_connected=mark_connected,
            description=description,
            tenant=tenant,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class PowerOutlet:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.PowerOutlet."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        color: str | None = None,
        power_port: str | PowerPort | pb.PowerPort | None = None,
        feed_leg: str | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.PowerOutlet:
        """Create a new PowerOutlet."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        power_port = convert_to_protobuf(power_port, pb.PowerPort)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.PowerOutlet(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            color=color,
            power_port=power_port,
            feed_leg=feed_leg,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class PowerPanel:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.PowerPanel."""

    def __new__(
        cls,
        site: str | Site | pb.Site | None = None,
        location: str | Location | pb.Location | None = None,
        name: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.PowerPanel:
        """Create a new PowerPanel."""
        site = convert_to_protobuf(site, pb.Site)
        location = convert_to_protobuf(location, pb.Location)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.PowerPanel(
            site=site,
            location=location,
            name=name,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class PowerPort:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.PowerPort."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        maximum_draw: int | None = None,
        allocated_draw: int | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.PowerPort:
        """Create a new PowerPort."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.PowerPort(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            maximum_draw=maximum_draw,
            allocated_draw=allocated_draw,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class Prefix:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Prefix."""

    def __new__(
        cls,
        prefix: str | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        scope_location: str | Location | pb.Location | None = None,
        scope_region: str | Region | pb.Region | None = None,
        scope_site: str | Site | pb.Site | None = None,
        scope_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        vlan: str | VLAN | pb.VLAN | None = None,
        status: str | None = None,
        role: str | Role | pb.Role | None = None,
        is_pool: bool | None = None,
        mark_utilized: bool | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Prefix:
        """Create a new Prefix."""
        vrf = convert_to_protobuf(vrf, pb.VRF)
        scope_location = convert_to_protobuf(scope_location, pb.Location)
        scope_region = convert_to_protobuf(scope_region, pb.Region)
        scope_site = convert_to_protobuf(scope_site, pb.Site)
        scope_site_group = convert_to_protobuf(scope_site_group, pb.SiteGroup)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        vlan = convert_to_protobuf(vlan, pb.VLAN)
        role = convert_to_protobuf(role, pb.Role)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Prefix(
            prefix=prefix,
            vrf=vrf,
            scope_location=scope_location,
            scope_region=scope_region,
            scope_site=scope_site,
            scope_site_group=scope_site_group,
            tenant=tenant,
            vlan=vlan,
            status=status,
            role=role,
            is_pool=is_pool,
            mark_utilized=mark_utilized,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class Provider:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Provider."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        accounts: list[str | ProviderAccount | pb.ProviderAccount] | None = None,
        asns: list[str | ASN | pb.ASN] | None = None,
    ) -> pb.Provider:
        """Create a new Provider."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        accounts = convert_to_protobuf_list(accounts, pb.ProviderAccount)
        asns = convert_to_protobuf_list(asns, pb.ASN)
        return pb.Provider(
            name=name,
            slug=slug,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            accounts=accounts,
            asns=asns,
        )


class ProviderAccount:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ProviderAccount."""

    def __new__(
        cls,
        provider: str | Provider | pb.Provider | None = None,
        name: str | None = None,
        account: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ProviderAccount:
        """Create a new ProviderAccount."""
        provider = convert_to_protobuf(provider, pb.Provider)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ProviderAccount(
            provider=provider,
            name=name,
            account=account,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class ProviderNetwork:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.ProviderNetwork."""

    def __new__(
        cls,
        provider: str | Provider | pb.Provider | None = None,
        name: str | None = None,
        service_id: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.ProviderNetwork:
        """Create a new ProviderNetwork."""
        provider = convert_to_protobuf(provider, pb.Provider)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.ProviderNetwork(
            provider=provider,
            name=name,
            service_id=service_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class RIR:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.RIR."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        is_private: bool | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.RIR:
        """Create a new RIR."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.RIR(
            name=name,
            slug=slug,
            is_private=is_private,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Rack:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Rack."""

    def __new__(
        cls,
        name: str | None = None,
        facility_id: str | None = None,
        site: str | Site | pb.Site | None = None,
        location: str | Location | pb.Location | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        status: str | None = None,
        role: str | RackRole | pb.RackRole | None = None,
        serial: str | None = None,
        asset_tag: str | None = None,
        rack_type: str | RackType | pb.RackType | None = None,
        form_factor: str | None = None,
        width: int | None = None,
        u_height: int | None = None,
        starting_unit: int | None = None,
        weight: float | None = None,
        max_weight: int | None = None,
        weight_unit: str | None = None,
        desc_units: bool | None = None,
        outer_width: int | None = None,
        outer_depth: int | None = None,
        outer_unit: str | None = None,
        mounting_depth: int | None = None,
        airflow: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Rack:
        """Create a new Rack."""
        site = convert_to_protobuf(site, pb.Site)
        location = convert_to_protobuf(location, pb.Location)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        role = convert_to_protobuf(role, pb.RackRole)
        rack_type = convert_to_protobuf(rack_type, pb.RackType)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Rack(
            name=name,
            facility_id=facility_id,
            site=site,
            location=location,
            tenant=tenant,
            status=status,
            role=role,
            serial=serial,
            asset_tag=asset_tag,
            rack_type=rack_type,
            form_factor=form_factor,
            width=width,
            u_height=u_height,
            starting_unit=starting_unit,
            weight=weight,
            max_weight=max_weight,
            weight_unit=weight_unit,
            desc_units=desc_units,
            outer_width=outer_width,
            outer_depth=outer_depth,
            outer_unit=outer_unit,
            mounting_depth=mounting_depth,
            airflow=airflow,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class RackReservation:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.RackReservation."""

    def __new__(
        cls,
        rack: str | Rack | pb.Rack | None = None,
        units: list[int] | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.RackReservation:
        """Create a new RackReservation."""
        rack = convert_to_protobuf(rack, pb.Rack)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.RackReservation(
            rack=rack,
            units=units,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class RackRole:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.RackRole."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.RackRole:
        """Create a new RackRole."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.RackRole(
            name=name,
            slug=slug,
            color=color,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class RackType:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.RackType."""

    def __new__(
        cls,
        manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        model: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        form_factor: str | None = None,
        width: int | None = None,
        u_height: int | None = None,
        starting_unit: int | None = None,
        desc_units: bool | None = None,
        outer_width: int | None = None,
        outer_depth: int | None = None,
        outer_unit: str | None = None,
        weight: float | None = None,
        max_weight: int | None = None,
        weight_unit: str | None = None,
        mounting_depth: int | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.RackType:
        """Create a new RackType."""
        manufacturer = convert_to_protobuf(manufacturer, pb.Manufacturer)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.RackType(
            manufacturer=manufacturer,
            model=model,
            slug=slug,
            description=description,
            form_factor=form_factor,
            width=width,
            u_height=u_height,
            starting_unit=starting_unit,
            desc_units=desc_units,
            outer_width=outer_width,
            outer_depth=outer_depth,
            outer_unit=outer_unit,
            weight=weight,
            max_weight=max_weight,
            weight_unit=weight_unit,
            mounting_depth=mounting_depth,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class RearPort:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.RearPort."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        module: str | Module | pb.Module | None = None,
        name: str | None = None,
        label: str | None = None,
        type: str | None = None,
        color: str | None = None,
        positions: int | None = None,
        description: str | None = None,
        mark_connected: bool | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.RearPort:
        """Create a new RearPort."""
        device = convert_to_protobuf(device, pb.Device)
        module = convert_to_protobuf(module, pb.Module)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.RearPort(
            device=device,
            module=module,
            name=name,
            label=label,
            type=type,
            color=color,
            positions=positions,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )


class Region:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Region."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        parent: str | Region | pb.Region | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Region:
        """Create a new Region."""
        parent = convert_to_protobuf(parent, pb.Region)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Region(
            name=name,
            slug=slug,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Role:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Role."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        weight: int | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Role:
        """Create a new Role."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Role(
            name=name,
            slug=slug,
            weight=weight,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class RouteTarget:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.RouteTarget."""

    def __new__(
        cls,
        name: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.RouteTarget:
        """Create a new RouteTarget."""
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.RouteTarget(
            name=name,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class Service:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Service."""

    def __new__(
        cls,
        device: str | Device | pb.Device | None = None,
        virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        name: str | None = None,
        protocol: str | None = None,
        ports: list[int] | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        ipaddresses: list[str | IPAddress | pb.IPAddress] | None = None,
    ) -> pb.Service:
        """Create a new Service."""
        device = convert_to_protobuf(device, pb.Device)
        virtual_machine = convert_to_protobuf(virtual_machine, pb.VirtualMachine)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        ipaddresses = convert_to_protobuf_list(ipaddresses, pb.IPAddress)
        return pb.Service(
            device=device,
            virtual_machine=virtual_machine,
            name=name,
            protocol=protocol,
            ports=ports,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            ipaddresses=ipaddresses,
        )


class Site:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Site."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        status: str | None = None,
        region: str | Region | pb.Region | None = None,
        group: str | SiteGroup | pb.SiteGroup | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        facility: str | None = None,
        time_zone: str | None = None,
        description: str | None = None,
        physical_address: str | None = None,
        shipping_address: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        asns: list[str | ASN | pb.ASN] | None = None,
    ) -> pb.Site:
        """Create a new Site."""
        region = convert_to_protobuf(region, pb.Region)
        group = convert_to_protobuf(group, pb.SiteGroup)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        asns = convert_to_protobuf_list(asns, pb.ASN)
        return pb.Site(
            name=name,
            slug=slug,
            status=status,
            region=region,
            group=group,
            tenant=tenant,
            facility=facility,
            time_zone=time_zone,
            description=description,
            physical_address=physical_address,
            shipping_address=shipping_address,
            latitude=latitude,
            longitude=longitude,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            asns=asns,
        )


class SiteGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.SiteGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        parent: str | SiteGroup | pb.SiteGroup | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.SiteGroup:
        """Create a new SiteGroup."""
        parent = convert_to_protobuf(parent, pb.SiteGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.SiteGroup(
            name=name,
            slug=slug,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Tag:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Tag."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
    ) -> pb.Tag:
        """Create a new Tag."""
        return pb.Tag(
            name=name,
            slug=slug,
            color=color,
        )


class Tenant:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Tenant."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        group: str | TenantGroup | pb.TenantGroup | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Tenant:
        """Create a new Tenant."""
        group = convert_to_protobuf(group, pb.TenantGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Tenant(
            name=name,
            slug=slug,
            group=group,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class TenantGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.TenantGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        parent: str | TenantGroup | pb.TenantGroup | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.TenantGroup:
        """Create a new TenantGroup."""
        parent = convert_to_protobuf(parent, pb.TenantGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.TenantGroup(
            name=name,
            slug=slug,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class Tunnel:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.Tunnel."""

    def __new__(
        cls,
        name: str | None = None,
        status: str | None = None,
        group: str | TunnelGroup | pb.TunnelGroup | None = None,
        encapsulation: str | None = None,
        ipsec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        tunnel_id: int | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.Tunnel:
        """Create a new Tunnel."""
        group = convert_to_protobuf(group, pb.TunnelGroup)
        ipsec_profile = convert_to_protobuf(ipsec_profile, pb.IPSecProfile)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.Tunnel(
            name=name,
            status=status,
            group=group,
            encapsulation=encapsulation,
            ipsec_profile=ipsec_profile,
            tenant=tenant,
            tunnel_id=tunnel_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class TunnelGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.TunnelGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.TunnelGroup:
        """Create a new TunnelGroup."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.TunnelGroup(
            name=name,
            slug=slug,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class TunnelTermination:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.TunnelTermination."""

    def __new__(
        cls,
        tunnel: str | Tunnel | pb.Tunnel | None = None,
        role: str | None = None,
        termination_asn: str | ASN | pb.ASN | None = None,
        termination_asn_range: str | ASNRange | pb.ASNRange | None = None,
        termination_aggregate: str | Aggregate | pb.Aggregate | None = None,
        termination_cable: str | Cable | pb.Cable | None = None,
        termination_cable_path: str | CablePath | pb.CablePath | None = None,
        termination_cable_termination: str | CableTermination | pb.CableTermination | None = None,
        termination_circuit: str | Circuit | pb.Circuit | None = None,
        termination_circuit_group: str | CircuitGroup | pb.CircuitGroup | None = None,
        termination_circuit_group_assignment: str | CircuitGroupAssignment | pb.CircuitGroupAssignment | None = None,
        termination_circuit_termination: str | CircuitTermination | pb.CircuitTermination | None = None,
        termination_circuit_type: str | CircuitType | pb.CircuitType | None = None,
        termination_cluster: str | Cluster | pb.Cluster | None = None,
        termination_cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        termination_cluster_type: str | ClusterType | pb.ClusterType | None = None,
        termination_console_port: str | ConsolePort | pb.ConsolePort | None = None,
        termination_console_server_port: str | ConsoleServerPort | pb.ConsoleServerPort | None = None,
        termination_contact: str | Contact | pb.Contact | None = None,
        termination_contact_assignment: str | ContactAssignment | pb.ContactAssignment | None = None,
        termination_contact_group: str | ContactGroup | pb.ContactGroup | None = None,
        termination_contact_role: str | ContactRole | pb.ContactRole | None = None,
        termination_device: str | Device | pb.Device | None = None,
        termination_device_bay: str | DeviceBay | pb.DeviceBay | None = None,
        termination_device_role: str | DeviceRole | pb.DeviceRole | None = None,
        termination_device_type: str | DeviceType | pb.DeviceType | None = None,
        termination_fhrp_group: str | FHRPGroup | pb.FHRPGroup | None = None,
        termination_fhrp_group_assignment: str | FHRPGroupAssignment | pb.FHRPGroupAssignment | None = None,
        termination_front_port: str | FrontPort | pb.FrontPort | None = None,
        termination_ike_policy: str | IKEPolicy | pb.IKEPolicy | None = None,
        termination_ike_proposal: str | IKEProposal | pb.IKEProposal | None = None,
        termination_ip_address: str | IPAddress | pb.IPAddress | None = None,
        termination_ip_range: str | IPRange | pb.IPRange | None = None,
        termination_ip_sec_policy: str | IPSecPolicy | pb.IPSecPolicy | None = None,
        termination_ip_sec_profile: str | IPSecProfile | pb.IPSecProfile | None = None,
        termination_ip_sec_proposal: str | IPSecProposal | pb.IPSecProposal | None = None,
        termination_interface: str | Interface | pb.Interface | None = None,
        termination_inventory_item: str | InventoryItem | pb.InventoryItem | None = None,
        termination_inventory_item_role: str | InventoryItemRole | pb.InventoryItemRole | None = None,
        termination_l2vpn: str | L2VPN | pb.L2VPN | None = None,
        termination_l2vpn_termination: str | L2VPNTermination | pb.L2VPNTermination | None = None,
        termination_location: str | Location | pb.Location | None = None,
        termination_mac_address: str | MACAddress | pb.MACAddress | None = None,
        termination_manufacturer: str | Manufacturer | pb.Manufacturer | None = None,
        termination_module: str | Module | pb.Module | None = None,
        termination_module_bay: str | ModuleBay | pb.ModuleBay | None = None,
        termination_module_type: str | ModuleType | pb.ModuleType | None = None,
        termination_platform: str | Platform | pb.Platform | None = None,
        termination_power_feed: str | PowerFeed | pb.PowerFeed | None = None,
        termination_power_outlet: str | PowerOutlet | pb.PowerOutlet | None = None,
        termination_power_panel: str | PowerPanel | pb.PowerPanel | None = None,
        termination_power_port: str | PowerPort | pb.PowerPort | None = None,
        termination_prefix: str | Prefix | pb.Prefix | None = None,
        termination_provider: str | Provider | pb.Provider | None = None,
        termination_provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        termination_provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        termination_rir: str | RIR | pb.RIR | None = None,
        termination_rack: str | Rack | pb.Rack | None = None,
        termination_rack_reservation: str | RackReservation | pb.RackReservation | None = None,
        termination_rack_role: str | RackRole | pb.RackRole | None = None,
        termination_rack_type: str | RackType | pb.RackType | None = None,
        termination_rear_port: str | RearPort | pb.RearPort | None = None,
        termination_region: str | Region | pb.Region | None = None,
        termination_role: str | Role | pb.Role | None = None,
        termination_route_target: str | RouteTarget | pb.RouteTarget | None = None,
        termination_service: str | Service | pb.Service | None = None,
        termination_site: str | Site | pb.Site | None = None,
        termination_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        termination_tag: str | Tag | pb.Tag | None = None,
        termination_tenant: str | Tenant | pb.Tenant | None = None,
        termination_tenant_group: str | TenantGroup | pb.TenantGroup | None = None,
        termination_tunnel: str | Tunnel | pb.Tunnel | None = None,
        termination_tunnel_group: str | TunnelGroup | pb.TunnelGroup | None = None,
        termination_tunnel_termination: str | TunnelTermination | pb.TunnelTermination | None = None,
        termination_vlan: str | VLAN | pb.VLAN | None = None,
        termination_vlan_group: str | VLANGroup | pb.VLANGroup | None = None,
        termination_vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        termination_vlan_translation_rule: str | VLANTranslationRule | pb.VLANTranslationRule | None = None,
        termination_vm_interface: str | VMInterface | pb.VMInterface | None = None,
        termination_vrf: str | VRF | pb.VRF | None = None,
        termination_virtual_chassis: str | VirtualChassis | pb.VirtualChassis | None = None,
        termination_virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        termination_virtual_circuit_termination: str | VirtualCircuitTermination | pb.VirtualCircuitTermination | None = None,
        termination_virtual_circuit_type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        termination_virtual_device_context: str | VirtualDeviceContext | pb.VirtualDeviceContext | None = None,
        termination_virtual_disk: str | VirtualDisk | pb.VirtualDisk | None = None,
        termination_virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        termination_wireless_lan: str | WirelessLAN | pb.WirelessLAN | None = None,
        termination_wireless_lan_group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        termination_wireless_link: str | WirelessLink | pb.WirelessLink | None = None,
        outside_ip: str | IPAddress | pb.IPAddress | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.TunnelTermination:
        """Create a new TunnelTermination."""
        tunnel = convert_to_protobuf(tunnel, pb.Tunnel)
        termination_asn = convert_to_protobuf(termination_asn, pb.ASN)
        termination_asn_range = convert_to_protobuf(termination_asn_range, pb.ASNRange)
        termination_aggregate = convert_to_protobuf(termination_aggregate, pb.Aggregate)
        termination_cable = convert_to_protobuf(termination_cable, pb.Cable)
        termination_cable_path = convert_to_protobuf(termination_cable_path, pb.CablePath)
        termination_cable_termination = convert_to_protobuf(termination_cable_termination, pb.CableTermination)
        termination_circuit = convert_to_protobuf(termination_circuit, pb.Circuit)
        termination_circuit_group = convert_to_protobuf(termination_circuit_group, pb.CircuitGroup)
        termination_circuit_group_assignment = convert_to_protobuf(termination_circuit_group_assignment, pb.CircuitGroupAssignment)
        termination_circuit_termination = convert_to_protobuf(termination_circuit_termination, pb.CircuitTermination)
        termination_circuit_type = convert_to_protobuf(termination_circuit_type, pb.CircuitType)
        termination_cluster = convert_to_protobuf(termination_cluster, pb.Cluster)
        termination_cluster_group = convert_to_protobuf(termination_cluster_group, pb.ClusterGroup)
        termination_cluster_type = convert_to_protobuf(termination_cluster_type, pb.ClusterType)
        termination_console_port = convert_to_protobuf(termination_console_port, pb.ConsolePort)
        termination_console_server_port = convert_to_protobuf(termination_console_server_port, pb.ConsoleServerPort)
        termination_contact = convert_to_protobuf(termination_contact, pb.Contact)
        termination_contact_assignment = convert_to_protobuf(termination_contact_assignment, pb.ContactAssignment)
        termination_contact_group = convert_to_protobuf(termination_contact_group, pb.ContactGroup)
        termination_contact_role = convert_to_protobuf(termination_contact_role, pb.ContactRole)
        termination_device = convert_to_protobuf(termination_device, pb.Device)
        termination_device_bay = convert_to_protobuf(termination_device_bay, pb.DeviceBay)
        termination_device_role = convert_to_protobuf(termination_device_role, pb.DeviceRole)
        termination_device_type = convert_to_protobuf(termination_device_type, pb.DeviceType)
        termination_fhrp_group = convert_to_protobuf(termination_fhrp_group, pb.FHRPGroup)
        termination_fhrp_group_assignment = convert_to_protobuf(termination_fhrp_group_assignment, pb.FHRPGroupAssignment)
        termination_front_port = convert_to_protobuf(termination_front_port, pb.FrontPort)
        termination_ike_policy = convert_to_protobuf(termination_ike_policy, pb.IKEPolicy)
        termination_ike_proposal = convert_to_protobuf(termination_ike_proposal, pb.IKEProposal)
        termination_ip_address = convert_to_protobuf(termination_ip_address, pb.IPAddress)
        termination_ip_range = convert_to_protobuf(termination_ip_range, pb.IPRange)
        termination_ip_sec_policy = convert_to_protobuf(termination_ip_sec_policy, pb.IPSecPolicy)
        termination_ip_sec_profile = convert_to_protobuf(termination_ip_sec_profile, pb.IPSecProfile)
        termination_ip_sec_proposal = convert_to_protobuf(termination_ip_sec_proposal, pb.IPSecProposal)
        termination_interface = convert_to_protobuf(termination_interface, pb.Interface)
        termination_inventory_item = convert_to_protobuf(termination_inventory_item, pb.InventoryItem)
        termination_inventory_item_role = convert_to_protobuf(termination_inventory_item_role, pb.InventoryItemRole)
        termination_l2vpn = convert_to_protobuf(termination_l2vpn, pb.L2VPN)
        termination_l2vpn_termination = convert_to_protobuf(termination_l2vpn_termination, pb.L2VPNTermination)
        termination_location = convert_to_protobuf(termination_location, pb.Location)
        termination_mac_address = convert_to_protobuf(termination_mac_address, pb.MACAddress)
        termination_manufacturer = convert_to_protobuf(termination_manufacturer, pb.Manufacturer)
        termination_module = convert_to_protobuf(termination_module, pb.Module)
        termination_module_bay = convert_to_protobuf(termination_module_bay, pb.ModuleBay)
        termination_module_type = convert_to_protobuf(termination_module_type, pb.ModuleType)
        termination_platform = convert_to_protobuf(termination_platform, pb.Platform)
        termination_power_feed = convert_to_protobuf(termination_power_feed, pb.PowerFeed)
        termination_power_outlet = convert_to_protobuf(termination_power_outlet, pb.PowerOutlet)
        termination_power_panel = convert_to_protobuf(termination_power_panel, pb.PowerPanel)
        termination_power_port = convert_to_protobuf(termination_power_port, pb.PowerPort)
        termination_prefix = convert_to_protobuf(termination_prefix, pb.Prefix)
        termination_provider = convert_to_protobuf(termination_provider, pb.Provider)
        termination_provider_account = convert_to_protobuf(termination_provider_account, pb.ProviderAccount)
        termination_provider_network = convert_to_protobuf(termination_provider_network, pb.ProviderNetwork)
        termination_rir = convert_to_protobuf(termination_rir, pb.RIR)
        termination_rack = convert_to_protobuf(termination_rack, pb.Rack)
        termination_rack_reservation = convert_to_protobuf(termination_rack_reservation, pb.RackReservation)
        termination_rack_role = convert_to_protobuf(termination_rack_role, pb.RackRole)
        termination_rack_type = convert_to_protobuf(termination_rack_type, pb.RackType)
        termination_rear_port = convert_to_protobuf(termination_rear_port, pb.RearPort)
        termination_region = convert_to_protobuf(termination_region, pb.Region)
        termination_role = convert_to_protobuf(termination_role, pb.Role)
        termination_route_target = convert_to_protobuf(termination_route_target, pb.RouteTarget)
        termination_service = convert_to_protobuf(termination_service, pb.Service)
        termination_site = convert_to_protobuf(termination_site, pb.Site)
        termination_site_group = convert_to_protobuf(termination_site_group, pb.SiteGroup)
        termination_tag = convert_to_protobuf(termination_tag, pb.Tag)
        termination_tenant = convert_to_protobuf(termination_tenant, pb.Tenant)
        termination_tenant_group = convert_to_protobuf(termination_tenant_group, pb.TenantGroup)
        termination_tunnel = convert_to_protobuf(termination_tunnel, pb.Tunnel)
        termination_tunnel_group = convert_to_protobuf(termination_tunnel_group, pb.TunnelGroup)
        termination_tunnel_termination = convert_to_protobuf(termination_tunnel_termination, pb.TunnelTermination)
        termination_vlan = convert_to_protobuf(termination_vlan, pb.VLAN)
        termination_vlan_group = convert_to_protobuf(termination_vlan_group, pb.VLANGroup)
        termination_vlan_translation_policy = convert_to_protobuf(termination_vlan_translation_policy, pb.VLANTranslationPolicy)
        termination_vlan_translation_rule = convert_to_protobuf(termination_vlan_translation_rule, pb.VLANTranslationRule)
        termination_vm_interface = convert_to_protobuf(termination_vm_interface, pb.VMInterface)
        termination_vrf = convert_to_protobuf(termination_vrf, pb.VRF)
        termination_virtual_chassis = convert_to_protobuf(termination_virtual_chassis, pb.VirtualChassis)
        termination_virtual_circuit = convert_to_protobuf(termination_virtual_circuit, pb.VirtualCircuit)
        termination_virtual_circuit_termination = convert_to_protobuf(termination_virtual_circuit_termination, pb.VirtualCircuitTermination)
        termination_virtual_circuit_type = convert_to_protobuf(termination_virtual_circuit_type, pb.VirtualCircuitType)
        termination_virtual_device_context = convert_to_protobuf(termination_virtual_device_context, pb.VirtualDeviceContext)
        termination_virtual_disk = convert_to_protobuf(termination_virtual_disk, pb.VirtualDisk)
        termination_virtual_machine = convert_to_protobuf(termination_virtual_machine, pb.VirtualMachine)
        termination_wireless_lan = convert_to_protobuf(termination_wireless_lan, pb.WirelessLAN)
        termination_wireless_lan_group = convert_to_protobuf(termination_wireless_lan_group, pb.WirelessLANGroup)
        termination_wireless_link = convert_to_protobuf(termination_wireless_link, pb.WirelessLink)
        outside_ip = convert_to_protobuf(outside_ip, pb.IPAddress)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.TunnelTermination(
            tunnel=tunnel,
            role=role,
            termination_asn=termination_asn,
            termination_asn_range=termination_asn_range,
            termination_aggregate=termination_aggregate,
            termination_cable=termination_cable,
            termination_cable_path=termination_cable_path,
            termination_cable_termination=termination_cable_termination,
            termination_circuit=termination_circuit,
            termination_circuit_group=termination_circuit_group,
            termination_circuit_group_assignment=termination_circuit_group_assignment,
            termination_circuit_termination=termination_circuit_termination,
            termination_circuit_type=termination_circuit_type,
            termination_cluster=termination_cluster,
            termination_cluster_group=termination_cluster_group,
            termination_cluster_type=termination_cluster_type,
            termination_console_port=termination_console_port,
            termination_console_server_port=termination_console_server_port,
            termination_contact=termination_contact,
            termination_contact_assignment=termination_contact_assignment,
            termination_contact_group=termination_contact_group,
            termination_contact_role=termination_contact_role,
            termination_device=termination_device,
            termination_device_bay=termination_device_bay,
            termination_device_role=termination_device_role,
            termination_device_type=termination_device_type,
            termination_fhrp_group=termination_fhrp_group,
            termination_fhrp_group_assignment=termination_fhrp_group_assignment,
            termination_front_port=termination_front_port,
            termination_ike_policy=termination_ike_policy,
            termination_ike_proposal=termination_ike_proposal,
            termination_ip_address=termination_ip_address,
            termination_ip_range=termination_ip_range,
            termination_ip_sec_policy=termination_ip_sec_policy,
            termination_ip_sec_profile=termination_ip_sec_profile,
            termination_ip_sec_proposal=termination_ip_sec_proposal,
            termination_interface=termination_interface,
            termination_inventory_item=termination_inventory_item,
            termination_inventory_item_role=termination_inventory_item_role,
            termination_l2vpn=termination_l2vpn,
            termination_l2vpn_termination=termination_l2vpn_termination,
            termination_location=termination_location,
            termination_mac_address=termination_mac_address,
            termination_manufacturer=termination_manufacturer,
            termination_module=termination_module,
            termination_module_bay=termination_module_bay,
            termination_module_type=termination_module_type,
            termination_platform=termination_platform,
            termination_power_feed=termination_power_feed,
            termination_power_outlet=termination_power_outlet,
            termination_power_panel=termination_power_panel,
            termination_power_port=termination_power_port,
            termination_prefix=termination_prefix,
            termination_provider=termination_provider,
            termination_provider_account=termination_provider_account,
            termination_provider_network=termination_provider_network,
            termination_rir=termination_rir,
            termination_rack=termination_rack,
            termination_rack_reservation=termination_rack_reservation,
            termination_rack_role=termination_rack_role,
            termination_rack_type=termination_rack_type,
            termination_rear_port=termination_rear_port,
            termination_region=termination_region,
            termination_role=termination_role,
            termination_route_target=termination_route_target,
            termination_service=termination_service,
            termination_site=termination_site,
            termination_site_group=termination_site_group,
            termination_tag=termination_tag,
            termination_tenant=termination_tenant,
            termination_tenant_group=termination_tenant_group,
            termination_tunnel=termination_tunnel,
            termination_tunnel_group=termination_tunnel_group,
            termination_tunnel_termination=termination_tunnel_termination,
            termination_vlan=termination_vlan,
            termination_vlan_group=termination_vlan_group,
            termination_vlan_translation_policy=termination_vlan_translation_policy,
            termination_vlan_translation_rule=termination_vlan_translation_rule,
            termination_vm_interface=termination_vm_interface,
            termination_vrf=termination_vrf,
            termination_virtual_chassis=termination_virtual_chassis,
            termination_virtual_circuit=termination_virtual_circuit,
            termination_virtual_circuit_termination=termination_virtual_circuit_termination,
            termination_virtual_circuit_type=termination_virtual_circuit_type,
            termination_virtual_device_context=termination_virtual_device_context,
            termination_virtual_disk=termination_virtual_disk,
            termination_virtual_machine=termination_virtual_machine,
            termination_wireless_lan=termination_wireless_lan,
            termination_wireless_lan_group=termination_wireless_lan_group,
            termination_wireless_link=termination_wireless_link,
            outside_ip=outside_ip,
            tags=tags,
            custom_fields=custom_fields,
        )


class VLAN:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VLAN."""

    def __new__(
        cls,
        site: str | Site | pb.Site | None = None,
        group: str | VLANGroup | pb.VLANGroup | None = None,
        vid: int | None = None,
        name: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        status: str | None = None,
        role: str | Role | pb.Role | None = None,
        description: str | None = None,
        qinq_role: str | None = None,
        qinq_svlan: str | VLAN | pb.VLAN | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VLAN:
        """Create a new VLAN."""
        site = convert_to_protobuf(site, pb.Site)
        group = convert_to_protobuf(group, pb.VLANGroup)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        role = convert_to_protobuf(role, pb.Role)
        qinq_svlan = convert_to_protobuf(qinq_svlan, pb.VLAN)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VLAN(
            site=site,
            group=group,
            vid=vid,
            name=name,
            tenant=tenant,
            status=status,
            role=role,
            description=description,
            qinq_role=qinq_role,
            qinq_svlan=qinq_svlan,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class VLANGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VLANGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        scope_cluster: str | Cluster | pb.Cluster | None = None,
        scope_cluster_group: str | ClusterGroup | pb.ClusterGroup | None = None,
        scope_location: str | Location | pb.Location | None = None,
        scope_rack: str | Rack | pb.Rack | None = None,
        scope_region: str | Region | pb.Region | None = None,
        scope_site: str | Site | pb.Site | None = None,
        scope_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        vid_ranges: list[int] | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VLANGroup:
        """Create a new VLANGroup."""
        scope_cluster = convert_to_protobuf(scope_cluster, pb.Cluster)
        scope_cluster_group = convert_to_protobuf(scope_cluster_group, pb.ClusterGroup)
        scope_location = convert_to_protobuf(scope_location, pb.Location)
        scope_rack = convert_to_protobuf(scope_rack, pb.Rack)
        scope_region = convert_to_protobuf(scope_region, pb.Region)
        scope_site = convert_to_protobuf(scope_site, pb.Site)
        scope_site_group = convert_to_protobuf(scope_site_group, pb.SiteGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VLANGroup(
            name=name,
            slug=slug,
            scope_cluster=scope_cluster,
            scope_cluster_group=scope_cluster_group,
            scope_location=scope_location,
            scope_rack=scope_rack,
            scope_region=scope_region,
            scope_site=scope_site,
            scope_site_group=scope_site_group,
            vid_ranges=vid_ranges,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class VLANTranslationPolicy:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VLANTranslationPolicy."""

    def __new__(
        cls,
        name: str | None = None,
        description: str | None = None,
    ) -> pb.VLANTranslationPolicy:
        """Create a new VLANTranslationPolicy."""
        return pb.VLANTranslationPolicy(
            name=name,
            description=description,
        )


class VLANTranslationRule:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VLANTranslationRule."""

    def __new__(
        cls,
        policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        local_vid: int | None = None,
        remote_vid: int | None = None,
        description: str | None = None,
    ) -> pb.VLANTranslationRule:
        """Create a new VLANTranslationRule."""
        policy = convert_to_protobuf(policy, pb.VLANTranslationPolicy)
        return pb.VLANTranslationRule(
            policy=policy,
            local_vid=local_vid,
            remote_vid=remote_vid,
            description=description,
        )


class VMInterface:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VMInterface."""

    def __new__(
        cls,
        virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        name: str | None = None,
        enabled: bool | None = None,
        parent: str | VMInterface | pb.VMInterface | None = None,
        bridge: str | VMInterface | pb.VMInterface | None = None,
        mtu: int | None = None,
        primary_mac_address: str | MACAddress | pb.MACAddress | None = None,
        description: str | None = None,
        mode: str | None = None,
        untagged_vlan: str | VLAN | pb.VLAN | None = None,
        qinq_svlan: str | VLAN | pb.VLAN | None = None,
        vlan_translation_policy: str | VLANTranslationPolicy | pb.VLANTranslationPolicy | None = None,
        vrf: str | VRF | pb.VRF | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        tagged_vlans: list[str | VLAN | pb.VLAN] | None = None,
    ) -> pb.VMInterface:
        """Create a new VMInterface."""
        virtual_machine = convert_to_protobuf(virtual_machine, pb.VirtualMachine)
        parent = convert_to_protobuf(parent, pb.VMInterface)
        bridge = convert_to_protobuf(bridge, pb.VMInterface)
        primary_mac_address = convert_to_protobuf(primary_mac_address, pb.MACAddress)
        untagged_vlan = convert_to_protobuf(untagged_vlan, pb.VLAN)
        qinq_svlan = convert_to_protobuf(qinq_svlan, pb.VLAN)
        vlan_translation_policy = convert_to_protobuf(vlan_translation_policy, pb.VLANTranslationPolicy)
        vrf = convert_to_protobuf(vrf, pb.VRF)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        tagged_vlans = convert_to_protobuf_list(tagged_vlans, pb.VLAN)
        return pb.VMInterface(
            virtual_machine=virtual_machine,
            name=name,
            enabled=enabled,
            parent=parent,
            bridge=bridge,
            mtu=mtu,
            primary_mac_address=primary_mac_address,
            description=description,
            mode=mode,
            untagged_vlan=untagged_vlan,
            qinq_svlan=qinq_svlan,
            vlan_translation_policy=vlan_translation_policy,
            vrf=vrf,
            tags=tags,
            custom_fields=custom_fields,
            tagged_vlans=tagged_vlans,
        )


class VRF:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VRF."""

    def __new__(
        cls,
        name: str | None = None,
        rd: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        enforce_unique: bool | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
        import_targets: list[str | RouteTarget | pb.RouteTarget] | None = None,
        export_targets: list[str | RouteTarget | pb.RouteTarget] | None = None,
    ) -> pb.VRF:
        """Create a new VRF."""
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        import_targets = convert_to_protobuf_list(import_targets, pb.RouteTarget)
        export_targets = convert_to_protobuf_list(export_targets, pb.RouteTarget)
        return pb.VRF(
            name=name,
            rd=rd,
            tenant=tenant,
            enforce_unique=enforce_unique,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            import_targets=import_targets,
            export_targets=export_targets,
        )


class VirtualChassis:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualChassis."""

    def __new__(
        cls,
        name: str | None = None,
        domain: str | None = None,
        master: str | Device | pb.Device | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualChassis:
        """Create a new VirtualChassis."""
        master = convert_to_protobuf(master, pb.Device)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VirtualChassis(
            name=name,
            domain=domain,
            master=master,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class VirtualCircuit:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualCircuit."""

    def __new__(
        cls,
        cid: str | None = None,
        provider_network: str | ProviderNetwork | pb.ProviderNetwork | None = None,
        provider_account: str | ProviderAccount | pb.ProviderAccount | None = None,
        type: str | VirtualCircuitType | pb.VirtualCircuitType | None = None,
        status: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualCircuit:
        """Create a new VirtualCircuit."""
        provider_network = convert_to_protobuf(provider_network, pb.ProviderNetwork)
        provider_account = convert_to_protobuf(provider_account, pb.ProviderAccount)
        type = convert_to_protobuf(type, pb.VirtualCircuitType)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VirtualCircuit(
            cid=cid,
            provider_network=provider_network,
            provider_account=provider_account,
            type=type,
            status=status,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class VirtualCircuitTermination:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualCircuitTermination."""

    def __new__(
        cls,
        virtual_circuit: str | VirtualCircuit | pb.VirtualCircuit | None = None,
        role: str | None = None,
        interface: str | Interface | pb.Interface | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualCircuitTermination:
        """Create a new VirtualCircuitTermination."""
        virtual_circuit = convert_to_protobuf(virtual_circuit, pb.VirtualCircuit)
        interface = convert_to_protobuf(interface, pb.Interface)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VirtualCircuitTermination(
            virtual_circuit=virtual_circuit,
            role=role,
            interface=interface,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class VirtualCircuitType:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualCircuitType."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        color: str | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualCircuitType:
        """Create a new VirtualCircuitType."""
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VirtualCircuitType(
            name=name,
            slug=slug,
            color=color,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class VirtualDeviceContext:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualDeviceContext."""

    def __new__(
        cls,
        name: str | None = None,
        device: str | Device | pb.Device | None = None,
        identifier: int | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        primary_ip4: str | IPAddress | pb.IPAddress | None = None,
        primary_ip6: str | IPAddress | pb.IPAddress | None = None,
        status: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualDeviceContext:
        """Create a new VirtualDeviceContext."""
        device = convert_to_protobuf(device, pb.Device)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        primary_ip4 = convert_to_protobuf(primary_ip4, pb.IPAddress)
        primary_ip6 = convert_to_protobuf(primary_ip6, pb.IPAddress)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VirtualDeviceContext(
            name=name,
            device=device,
            identifier=identifier,
            tenant=tenant,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            status=status,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class VirtualDisk:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualDisk."""

    def __new__(
        cls,
        virtual_machine: str | VirtualMachine | pb.VirtualMachine | None = None,
        name: str | None = None,
        description: str | None = None,
        size: int | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualDisk:
        """Create a new VirtualDisk."""
        virtual_machine = convert_to_protobuf(virtual_machine, pb.VirtualMachine)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.VirtualDisk(
            virtual_machine=virtual_machine,
            name=name,
            description=description,
            size=size,
            tags=tags,
            custom_fields=custom_fields,
        )


class VirtualMachine:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.VirtualMachine."""

    def __new__(
        cls,
        name: str | None = None,
        status: str | None = None,
        site: str | Site | pb.Site | None = None,
        cluster: str | Cluster | pb.Cluster | None = None,
        device: str | Device | pb.Device | None = None,
        serial: str | None = None,
        role: str | DeviceRole | pb.DeviceRole | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        platform: str | Platform | pb.Platform | None = None,
        primary_ip4: str | IPAddress | pb.IPAddress | None = None,
        primary_ip6: str | IPAddress | pb.IPAddress | None = None,
        vcpus: float | None = None,
        memory: int | None = None,
        disk: int | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.VirtualMachine:
        """Create a new VirtualMachine."""
        site = convert_to_protobuf(site, pb.Site)
        cluster = convert_to_protobuf(cluster, pb.Cluster)
        device = convert_to_protobuf(device, pb.Device)
        role = convert_to_protobuf(role, pb.DeviceRole)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        platform = convert_to_protobuf(platform, pb.Platform)
        primary_ip4 = convert_to_protobuf(primary_ip4, pb.IPAddress)
        primary_ip6 = convert_to_protobuf(primary_ip6, pb.IPAddress)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)

        # apply shortcuts
        if platform is not None:
            if device is not None and not device.HasField('platform'):
                device.platform.CopyFrom(platform)
        if site is not None:
            if device is not None and not device.HasField('site'):
                device.site.CopyFrom(site)
            if cluster is not None and not cluster.HasField('scope_site'):
                cluster.scope_site.CopyFrom(site)
        if role is not None:
            if device is not None and not device.HasField('role'):
                device.role.CopyFrom(role)
        return pb.VirtualMachine(
            name=name,
            status=status,
            site=site,
            cluster=cluster,
            device=device,
            serial=serial,
            role=role,
            tenant=tenant,
            platform=platform,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            vcpus=vcpus,
            memory=memory,
            disk=disk,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class WirelessLAN:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.WirelessLAN."""

    def __new__(
        cls,
        ssid: str | None = None,
        description: str | None = None,
        group: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        status: str | None = None,
        vlan: str | VLAN | pb.VLAN | None = None,
        scope_location: str | Location | pb.Location | None = None,
        scope_region: str | Region | pb.Region | None = None,
        scope_site: str | Site | pb.Site | None = None,
        scope_site_group: str | SiteGroup | pb.SiteGroup | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        auth_type: str | None = None,
        auth_cipher: str | None = None,
        auth_psk: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.WirelessLAN:
        """Create a new WirelessLAN."""
        group = convert_to_protobuf(group, pb.WirelessLANGroup)
        vlan = convert_to_protobuf(vlan, pb.VLAN)
        scope_location = convert_to_protobuf(scope_location, pb.Location)
        scope_region = convert_to_protobuf(scope_region, pb.Region)
        scope_site = convert_to_protobuf(scope_site, pb.Site)
        scope_site_group = convert_to_protobuf(scope_site_group, pb.SiteGroup)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.WirelessLAN(
            ssid=ssid,
            description=description,
            group=group,
            status=status,
            vlan=vlan,
            scope_location=scope_location,
            scope_region=scope_region,
            scope_site=scope_site,
            scope_site_group=scope_site_group,
            tenant=tenant,
            auth_type=auth_type,
            auth_cipher=auth_cipher,
            auth_psk=auth_psk,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )


class WirelessLANGroup:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.WirelessLANGroup."""

    def __new__(
        cls,
        name: str | None = None,
        slug: str | None = None,
        parent: str | WirelessLANGroup | pb.WirelessLANGroup | None = None,
        description: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.WirelessLANGroup:
        """Create a new WirelessLANGroup."""
        parent = convert_to_protobuf(parent, pb.WirelessLANGroup)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.WirelessLANGroup(
            name=name,
            slug=slug,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )


class WirelessLink:
    """wrapper for netboxlabs.diode.sdk.diode.v1.ingester_pb2.WirelessLink."""

    def __new__(
        cls,
        interface_a: str | Interface | pb.Interface | None = None,
        interface_b: str | Interface | pb.Interface | None = None,
        ssid: str | None = None,
        status: str | None = None,
        tenant: str | Tenant | pb.Tenant | None = None,
        auth_type: str | None = None,
        auth_cipher: str | None = None,
        auth_psk: str | None = None,
        distance: float | None = None,
        distance_unit: str | None = None,
        description: str | None = None,
        comments: str | None = None,
        tags: list[str | Tag | pb.Tag] | None = None,
        custom_fields: dict[str, str | CustomFieldValue | pb.CustomFieldValue] | None = None,
    ) -> pb.WirelessLink:
        """Create a new WirelessLink."""
        interface_a = convert_to_protobuf(interface_a, pb.Interface)
        interface_b = convert_to_protobuf(interface_b, pb.Interface)
        tenant = convert_to_protobuf(tenant, pb.Tenant)
        tags = convert_to_protobuf_list(tags, pb.Tag)
        custom_fields = convert_to_protobuf_dict(custom_fields, pb.CustomFieldValue)
        return pb.WirelessLink(
            interface_a=interface_a,
            interface_b=interface_b,
            ssid=ssid,
            status=status,
            tenant=tenant,
            auth_type=auth_type,
            auth_cipher=auth_cipher,
            auth_psk=auth_psk,
            distance=distance,
            distance_unit=distance_unit,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )
