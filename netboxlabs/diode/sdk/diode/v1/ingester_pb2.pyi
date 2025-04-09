from google.protobuf import timestamp_pb2 as _timestamp_pb2
from netboxlabs.diode.sdk.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("timestamp", "asn", "asn_range", "aggregate", "cable", "cable_path", "cable_termination", "circuit", "circuit_group", "circuit_group_assignment", "circuit_termination", "circuit_type", "cluster", "cluster_group", "cluster_type", "console_port", "console_server_port", "contact", "contact_assignment", "contact_group", "contact_role", "device", "device_bay", "device_role", "device_type", "fhrp_group", "fhrp_group_assignment", "front_port", "ike_policy", "ike_proposal", "ip_address", "ip_range", "ip_sec_policy", "ip_sec_profile", "ip_sec_proposal", "interface", "inventory_item", "inventory_item_role", "l2vpn", "l2vpn_termination", "location", "mac_address", "manufacturer", "module", "module_bay", "module_type", "platform", "power_feed", "power_outlet", "power_panel", "power_port", "prefix", "provider", "provider_account", "provider_network", "rir", "rack", "rack_reservation", "rack_role", "rack_type", "rear_port", "region", "role", "route_target", "service", "site", "site_group", "tag", "tenant", "tenant_group", "tunnel", "tunnel_group", "tunnel_termination", "vlan", "vlan_group", "vlan_translation_policy", "vlan_translation_rule", "vm_interface", "vrf", "virtual_chassis", "virtual_circuit", "virtual_circuit_termination", "virtual_circuit_type", "virtual_device_context", "virtual_disk", "virtual_machine", "wireless_lan", "wireless_lan_group", "wireless_link")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ASN_FIELD_NUMBER: _ClassVar[int]
    ASN_RANGE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    CABLE_FIELD_NUMBER: _ClassVar[int]
    CABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    CABLE_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BAY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    FHRP_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    IKE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    IP_SEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    IP_SEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IP_SEC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_ITEM_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_ITEM_ROLE_FIELD_NUMBER: _ClassVar[int]
    L2VPN_FIELD_NUMBER: _ClassVar[int]
    L2VPN_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    RIR_FIELD_NUMBER: _ClassVar[int]
    RACK_FIELD_NUMBER: _ClassVar[int]
    RACK_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    RACK_ROLE_FIELD_NUMBER: _ClassVar[int]
    RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TARGET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    TENANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    VLAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    VLAN_TRANSLATION_RULE_FIELD_NUMBER: _ClassVar[int]
    VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DEVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LAN_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    asn: ASN
    asn_range: ASNRange
    aggregate: Aggregate
    cable: Cable
    cable_path: CablePath
    cable_termination: CableTermination
    circuit: Circuit
    circuit_group: CircuitGroup
    circuit_group_assignment: CircuitGroupAssignment
    circuit_termination: CircuitTermination
    circuit_type: CircuitType
    cluster: Cluster
    cluster_group: ClusterGroup
    cluster_type: ClusterType
    console_port: ConsolePort
    console_server_port: ConsoleServerPort
    contact: Contact
    contact_assignment: ContactAssignment
    contact_group: ContactGroup
    contact_role: ContactRole
    device: Device
    device_bay: DeviceBay
    device_role: DeviceRole
    device_type: DeviceType
    fhrp_group: FHRPGroup
    fhrp_group_assignment: FHRPGroupAssignment
    front_port: FrontPort
    ike_policy: IKEPolicy
    ike_proposal: IKEProposal
    ip_address: IPAddress
    ip_range: IPRange
    ip_sec_policy: IPSecPolicy
    ip_sec_profile: IPSecProfile
    ip_sec_proposal: IPSecProposal
    interface: Interface
    inventory_item: InventoryItem
    inventory_item_role: InventoryItemRole
    l2vpn: L2VPN
    l2vpn_termination: L2VPNTermination
    location: Location
    mac_address: MACAddress
    manufacturer: Manufacturer
    module: Module
    module_bay: ModuleBay
    module_type: ModuleType
    platform: Platform
    power_feed: PowerFeed
    power_outlet: PowerOutlet
    power_panel: PowerPanel
    power_port: PowerPort
    prefix: Prefix
    provider: Provider
    provider_account: ProviderAccount
    provider_network: ProviderNetwork
    rir: RIR
    rack: Rack
    rack_reservation: RackReservation
    rack_role: RackRole
    rack_type: RackType
    rear_port: RearPort
    region: Region
    role: Role
    route_target: RouteTarget
    service: Service
    site: Site
    site_group: SiteGroup
    tag: Tag
    tenant: Tenant
    tenant_group: TenantGroup
    tunnel: Tunnel
    tunnel_group: TunnelGroup
    tunnel_termination: TunnelTermination
    vlan: VLAN
    vlan_group: VLANGroup
    vlan_translation_policy: VLANTranslationPolicy
    vlan_translation_rule: VLANTranslationRule
    vm_interface: VMInterface
    vrf: VRF
    virtual_chassis: VirtualChassis
    virtual_circuit: VirtualCircuit
    virtual_circuit_termination: VirtualCircuitTermination
    virtual_circuit_type: VirtualCircuitType
    virtual_device_context: VirtualDeviceContext
    virtual_disk: VirtualDisk
    virtual_machine: VirtualMachine
    wireless_lan: WirelessLAN
    wireless_lan_group: WirelessLANGroup
    wireless_link: WirelessLink
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., asn: _Optional[_Union[ASN, _Mapping]] = ..., asn_range: _Optional[_Union[ASNRange, _Mapping]] = ..., aggregate: _Optional[_Union[Aggregate, _Mapping]] = ..., cable: _Optional[_Union[Cable, _Mapping]] = ..., cable_path: _Optional[_Union[CablePath, _Mapping]] = ..., cable_termination: _Optional[_Union[CableTermination, _Mapping]] = ..., circuit: _Optional[_Union[Circuit, _Mapping]] = ..., circuit_group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., circuit_group_assignment: _Optional[_Union[CircuitGroupAssignment, _Mapping]] = ..., circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., circuit_type: _Optional[_Union[CircuitType, _Mapping]] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., cluster_type: _Optional[_Union[ClusterType, _Mapping]] = ..., console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ..., contact_assignment: _Optional[_Union[ContactAssignment, _Mapping]] = ..., contact_group: _Optional[_Union[ContactGroup, _Mapping]] = ..., contact_role: _Optional[_Union[ContactRole, _Mapping]] = ..., device: _Optional[_Union[Device, _Mapping]] = ..., device_bay: _Optional[_Union[DeviceBay, _Mapping]] = ..., device_role: _Optional[_Union[DeviceRole, _Mapping]] = ..., device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., fhrp_group_assignment: _Optional[_Union[FHRPGroupAssignment, _Mapping]] = ..., front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., ike_proposal: _Optional[_Union[IKEProposal, _Mapping]] = ..., ip_address: _Optional[_Union[IPAddress, _Mapping]] = ..., ip_range: _Optional[_Union[IPRange, _Mapping]] = ..., ip_sec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., ip_sec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., ip_sec_proposal: _Optional[_Union[IPSecProposal, _Mapping]] = ..., interface: _Optional[_Union[Interface, _Mapping]] = ..., inventory_item: _Optional[_Union[InventoryItem, _Mapping]] = ..., inventory_item_role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., l2vpn_termination: _Optional[_Union[L2VPNTermination, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., platform: _Optional[_Union[Platform, _Mapping]] = ..., power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., prefix: _Optional[_Union[Prefix, _Mapping]] = ..., provider: _Optional[_Union[Provider, _Mapping]] = ..., provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., rir: _Optional[_Union[RIR, _Mapping]] = ..., rack: _Optional[_Union[Rack, _Mapping]] = ..., rack_reservation: _Optional[_Union[RackReservation, _Mapping]] = ..., rack_role: _Optional[_Union[RackRole, _Mapping]] = ..., rack_type: _Optional[_Union[RackType, _Mapping]] = ..., rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., region: _Optional[_Union[Region, _Mapping]] = ..., role: _Optional[_Union[Role, _Mapping]] = ..., route_target: _Optional[_Union[RouteTarget, _Mapping]] = ..., service: _Optional[_Union[Service, _Mapping]] = ..., site: _Optional[_Union[Site, _Mapping]] = ..., site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., tag: _Optional[_Union[Tag, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., tenant_group: _Optional[_Union[TenantGroup, _Mapping]] = ..., tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., tunnel_group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., tunnel_termination: _Optional[_Union[TunnelTermination, _Mapping]] = ..., vlan: _Optional[_Union[VLAN, _Mapping]] = ..., vlan_group: _Optional[_Union[VLANGroup, _Mapping]] = ..., vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., vlan_translation_rule: _Optional[_Union[VLANTranslationRule, _Mapping]] = ..., vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., virtual_circuit_termination: _Optional[_Union[VirtualCircuitTermination, _Mapping]] = ..., virtual_circuit_type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., virtual_device_context: _Optional[_Union[VirtualDeviceContext, _Mapping]] = ..., virtual_disk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., wireless_lan: _Optional[_Union[WirelessLAN, _Mapping]] = ..., wireless_lan_group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., wireless_link: _Optional[_Union[WirelessLink, _Mapping]] = ...) -> None: ...

class IngestRequest(_message.Message):
    __slots__ = ("stream", "entities", "id", "producer_app_name", "producer_app_version", "sdk_name", "sdk_version")
    STREAM_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_APP_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    SDK_NAME_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    stream: str
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    id: str
    producer_app_name: str
    producer_app_version: str
    sdk_name: str
    sdk_version: str
    def __init__(self, stream: _Optional[str] = ..., entities: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., id: _Optional[str] = ..., producer_app_name: _Optional[str] = ..., producer_app_version: _Optional[str] = ..., sdk_name: _Optional[str] = ..., sdk_version: _Optional[str] = ...) -> None: ...

class IngestResponse(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, errors: _Optional[_Iterable[str]] = ...) -> None: ...

class ASN(_message.Message):
    __slots__ = ("asn", "rir", "tenant", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    ASN_FIELD_NUMBER: _ClassVar[int]
    RIR_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    asn: int
    rir: RIR
    tenant: Tenant
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, asn: _Optional[int] = ..., rir: _Optional[_Union[RIR, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ASNRange(_message.Message):
    __slots__ = ("name", "slug", "rir", "start", "end", "tenant", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    RIR_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    rir: RIR
    start: int
    end: int
    tenant: Tenant
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., rir: _Optional[_Union[RIR, _Mapping]] = ..., start: _Optional[int] = ..., end: _Optional[int] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Aggregate(_message.Message):
    __slots__ = ("prefix", "rir", "tenant", "date_added", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    RIR_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    DATE_ADDED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    rir: RIR
    tenant: Tenant
    date_added: _timestamp_pb2.Timestamp
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, prefix: _Optional[str] = ..., rir: _Optional[_Union[RIR, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., date_added: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Cable(_message.Message):
    __slots__ = ("type", "a_terminations", "b_terminations", "status", "tenant", "label", "color", "length", "length_unit", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    A_TERMINATIONS_FIELD_NUMBER: _ClassVar[int]
    B_TERMINATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    LENGTH_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    type: str
    a_terminations: _containers.RepeatedCompositeFieldContainer[GenericObject]
    b_terminations: _containers.RepeatedCompositeFieldContainer[GenericObject]
    status: str
    tenant: Tenant
    label: str
    color: str
    length: float
    length_unit: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, type: _Optional[str] = ..., a_terminations: _Optional[_Iterable[_Union[GenericObject, _Mapping]]] = ..., b_terminations: _Optional[_Iterable[_Union[GenericObject, _Mapping]]] = ..., status: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., label: _Optional[str] = ..., color: _Optional[str] = ..., length: _Optional[float] = ..., length_unit: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class CablePath(_message.Message):
    __slots__ = ("is_active", "is_complete", "is_split")
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    IS_SPLIT_FIELD_NUMBER: _ClassVar[int]
    is_active: bool
    is_complete: bool
    is_split: bool
    def __init__(self, is_active: bool = ..., is_complete: bool = ..., is_split: bool = ...) -> None: ...

class CableTermination(_message.Message):
    __slots__ = ("cable", "cable_end", "termination_circuit_termination", "termination_console_port", "termination_console_server_port", "termination_front_port", "termination_interface", "termination_power_feed", "termination_power_outlet", "termination_power_port", "termination_rear_port")
    CABLE_FIELD_NUMBER: _ClassVar[int]
    CABLE_END_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    cable: Cable
    cable_end: str
    termination_circuit_termination: CircuitTermination
    termination_console_port: ConsolePort
    termination_console_server_port: ConsoleServerPort
    termination_front_port: FrontPort
    termination_interface: Interface
    termination_power_feed: PowerFeed
    termination_power_outlet: PowerOutlet
    termination_power_port: PowerPort
    termination_rear_port: RearPort
    def __init__(self, cable: _Optional[_Union[Cable, _Mapping]] = ..., cable_end: _Optional[str] = ..., termination_circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., termination_console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., termination_console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., termination_front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., termination_interface: _Optional[_Union[Interface, _Mapping]] = ..., termination_power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., termination_power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., termination_power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., termination_rear_port: _Optional[_Union[RearPort, _Mapping]] = ...) -> None: ...

class Circuit(_message.Message):
    __slots__ = ("cid", "provider", "provider_account", "type", "status", "tenant", "install_date", "termination_date", "commit_rate", "description", "distance", "distance_unit", "comments", "tags", "assignments", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    CID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    INSTALL_DATE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_DATE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_RATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    cid: str
    provider: Provider
    provider_account: ProviderAccount
    type: CircuitType
    status: str
    tenant: Tenant
    install_date: _timestamp_pb2.Timestamp
    termination_date: _timestamp_pb2.Timestamp
    commit_rate: int
    description: str
    distance: float
    distance_unit: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    assignments: _containers.RepeatedCompositeFieldContainer[CircuitGroupAssignment]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, cid: _Optional[str] = ..., provider: _Optional[_Union[Provider, _Mapping]] = ..., provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., type: _Optional[_Union[CircuitType, _Mapping]] = ..., status: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., install_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., termination_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., commit_rate: _Optional[int] = ..., description: _Optional[str] = ..., distance: _Optional[float] = ..., distance_unit: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., assignments: _Optional[_Iterable[_Union[CircuitGroupAssignment, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class CircuitGroup(_message.Message):
    __slots__ = ("name", "slug", "description", "tenant", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    tenant: Tenant
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class CircuitGroupAssignment(_message.Message):
    __slots__ = ("group", "member_circuit", "member_virtual_circuit", "priority", "tags")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    group: CircuitGroup
    member_circuit: Circuit
    member_virtual_circuit: VirtualCircuit
    priority: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., member_circuit: _Optional[_Union[Circuit, _Mapping]] = ..., member_virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., priority: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class CircuitTermination(_message.Message):
    __slots__ = ("circuit", "term_side", "termination_location", "termination_provider_network", "termination_region", "termination_site", "termination_site_group", "port_speed", "upstream_speed", "xconnect_id", "pp_info", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    TERM_SIDE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_REGION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_SITE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    PORT_SPEED_FIELD_NUMBER: _ClassVar[int]
    UPSTREAM_SPEED_FIELD_NUMBER: _ClassVar[int]
    XCONNECT_ID_FIELD_NUMBER: _ClassVar[int]
    PP_INFO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    circuit: Circuit
    term_side: str
    termination_location: Location
    termination_provider_network: ProviderNetwork
    termination_region: Region
    termination_site: Site
    termination_site_group: SiteGroup
    port_speed: int
    upstream_speed: int
    xconnect_id: str
    pp_info: str
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, circuit: _Optional[_Union[Circuit, _Mapping]] = ..., term_side: _Optional[str] = ..., termination_location: _Optional[_Union[Location, _Mapping]] = ..., termination_provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., termination_region: _Optional[_Union[Region, _Mapping]] = ..., termination_site: _Optional[_Union[Site, _Mapping]] = ..., termination_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., port_speed: _Optional[int] = ..., upstream_speed: _Optional[int] = ..., xconnect_id: _Optional[str] = ..., pp_info: _Optional[str] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class CircuitType(_message.Message):
    __slots__ = ("name", "slug", "color", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    color: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., color: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("name", "type", "group", "status", "tenant", "scope_location", "scope_region", "scope_site", "scope_site_group", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_REGION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: ClusterType
    group: ClusterGroup
    status: str
    tenant: Tenant
    scope_location: Location
    scope_region: Region
    scope_site: Site
    scope_site_group: SiteGroup
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[ClusterType, _Mapping]] = ..., group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., status: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., scope_location: _Optional[_Union[Location, _Mapping]] = ..., scope_region: _Optional[_Union[Region, _Mapping]] = ..., scope_site: _Optional[_Union[Site, _Mapping]] = ..., scope_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ClusterGroup(_message.Message):
    __slots__ = ("name", "slug", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ClusterType(_message.Message):
    __slots__ = ("name", "slug", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ConsolePort(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "speed", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    speed: int
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., speed: _Optional[int] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ConsoleServerPort(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "speed", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    speed: int
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., speed: _Optional[int] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ("group", "name", "title", "phone", "email", "address", "link", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    GROUP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    group: ContactGroup
    name: str
    title: str
    phone: str
    email: str
    address: str
    link: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, group: _Optional[_Union[ContactGroup, _Mapping]] = ..., name: _Optional[str] = ..., title: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ..., address: _Optional[str] = ..., link: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ContactAssignment(_message.Message):
    __slots__ = ("object_asn", "object_asn_range", "object_aggregate", "object_cable", "object_cable_path", "object_cable_termination", "object_circuit", "object_circuit_group", "object_circuit_group_assignment", "object_circuit_termination", "object_circuit_type", "object_cluster", "object_cluster_group", "object_cluster_type", "object_console_port", "object_console_server_port", "object_contact", "object_contact_assignment", "object_contact_group", "object_contact_role", "object_device", "object_device_bay", "object_device_role", "object_device_type", "object_fhrp_group", "object_fhrp_group_assignment", "object_front_port", "object_ike_policy", "object_ike_proposal", "object_ip_address", "object_ip_range", "object_ip_sec_policy", "object_ip_sec_profile", "object_ip_sec_proposal", "object_interface", "object_inventory_item", "object_inventory_item_role", "object_l2vpn", "object_l2vpn_termination", "object_location", "object_mac_address", "object_manufacturer", "object_module", "object_module_bay", "object_module_type", "object_platform", "object_power_feed", "object_power_outlet", "object_power_panel", "object_power_port", "object_prefix", "object_provider", "object_provider_account", "object_provider_network", "object_rir", "object_rack", "object_rack_reservation", "object_rack_role", "object_rack_type", "object_rear_port", "object_region", "object_role", "object_route_target", "object_service", "object_site", "object_site_group", "object_tag", "object_tenant", "object_tenant_group", "object_tunnel", "object_tunnel_group", "object_tunnel_termination", "object_vlan", "object_vlan_group", "object_vlan_translation_policy", "object_vlan_translation_rule", "object_vm_interface", "object_vrf", "object_virtual_chassis", "object_virtual_circuit", "object_virtual_circuit_termination", "object_virtual_circuit_type", "object_virtual_device_context", "object_virtual_disk", "object_virtual_machine", "object_wireless_lan", "object_wireless_lan_group", "object_wireless_link", "contact", "role", "priority", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    OBJECT_ASN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ASN_RANGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CABLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CABLE_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_BAY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FHRP_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IKE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_SEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_SEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_SEC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INVENTORY_ITEM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INVENTORY_ITEM_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_L2VPN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_L2VPN_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MODULE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RIR_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_REGION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ROUTE_TARGET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SERVICE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SITE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TAG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TENANT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TENANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TUNNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TUNNEL_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_TRANSLATION_RULE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VRF_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_DEVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WIRELESS_LAN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WIRELESS_LAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    object_asn: ASN
    object_asn_range: ASNRange
    object_aggregate: Aggregate
    object_cable: Cable
    object_cable_path: CablePath
    object_cable_termination: CableTermination
    object_circuit: Circuit
    object_circuit_group: CircuitGroup
    object_circuit_group_assignment: CircuitGroupAssignment
    object_circuit_termination: CircuitTermination
    object_circuit_type: CircuitType
    object_cluster: Cluster
    object_cluster_group: ClusterGroup
    object_cluster_type: ClusterType
    object_console_port: ConsolePort
    object_console_server_port: ConsoleServerPort
    object_contact: Contact
    object_contact_assignment: ContactAssignment
    object_contact_group: ContactGroup
    object_contact_role: ContactRole
    object_device: Device
    object_device_bay: DeviceBay
    object_device_role: DeviceRole
    object_device_type: DeviceType
    object_fhrp_group: FHRPGroup
    object_fhrp_group_assignment: FHRPGroupAssignment
    object_front_port: FrontPort
    object_ike_policy: IKEPolicy
    object_ike_proposal: IKEProposal
    object_ip_address: IPAddress
    object_ip_range: IPRange
    object_ip_sec_policy: IPSecPolicy
    object_ip_sec_profile: IPSecProfile
    object_ip_sec_proposal: IPSecProposal
    object_interface: Interface
    object_inventory_item: InventoryItem
    object_inventory_item_role: InventoryItemRole
    object_l2vpn: L2VPN
    object_l2vpn_termination: L2VPNTermination
    object_location: Location
    object_mac_address: MACAddress
    object_manufacturer: Manufacturer
    object_module: Module
    object_module_bay: ModuleBay
    object_module_type: ModuleType
    object_platform: Platform
    object_power_feed: PowerFeed
    object_power_outlet: PowerOutlet
    object_power_panel: PowerPanel
    object_power_port: PowerPort
    object_prefix: Prefix
    object_provider: Provider
    object_provider_account: ProviderAccount
    object_provider_network: ProviderNetwork
    object_rir: RIR
    object_rack: Rack
    object_rack_reservation: RackReservation
    object_rack_role: RackRole
    object_rack_type: RackType
    object_rear_port: RearPort
    object_region: Region
    object_role: Role
    object_route_target: RouteTarget
    object_service: Service
    object_site: Site
    object_site_group: SiteGroup
    object_tag: Tag
    object_tenant: Tenant
    object_tenant_group: TenantGroup
    object_tunnel: Tunnel
    object_tunnel_group: TunnelGroup
    object_tunnel_termination: TunnelTermination
    object_vlan: VLAN
    object_vlan_group: VLANGroup
    object_vlan_translation_policy: VLANTranslationPolicy
    object_vlan_translation_rule: VLANTranslationRule
    object_vm_interface: VMInterface
    object_vrf: VRF
    object_virtual_chassis: VirtualChassis
    object_virtual_circuit: VirtualCircuit
    object_virtual_circuit_termination: VirtualCircuitTermination
    object_virtual_circuit_type: VirtualCircuitType
    object_virtual_device_context: VirtualDeviceContext
    object_virtual_disk: VirtualDisk
    object_virtual_machine: VirtualMachine
    object_wireless_lan: WirelessLAN
    object_wireless_lan_group: WirelessLANGroup
    object_wireless_link: WirelessLink
    contact: Contact
    role: ContactRole
    priority: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, object_asn: _Optional[_Union[ASN, _Mapping]] = ..., object_asn_range: _Optional[_Union[ASNRange, _Mapping]] = ..., object_aggregate: _Optional[_Union[Aggregate, _Mapping]] = ..., object_cable: _Optional[_Union[Cable, _Mapping]] = ..., object_cable_path: _Optional[_Union[CablePath, _Mapping]] = ..., object_cable_termination: _Optional[_Union[CableTermination, _Mapping]] = ..., object_circuit: _Optional[_Union[Circuit, _Mapping]] = ..., object_circuit_group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., object_circuit_group_assignment: _Optional[_Union[CircuitGroupAssignment, _Mapping]] = ..., object_circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., object_circuit_type: _Optional[_Union[CircuitType, _Mapping]] = ..., object_cluster: _Optional[_Union[Cluster, _Mapping]] = ..., object_cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., object_cluster_type: _Optional[_Union[ClusterType, _Mapping]] = ..., object_console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., object_console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., object_contact: _Optional[_Union[Contact, _Mapping]] = ..., object_contact_assignment: _Optional[_Union[ContactAssignment, _Mapping]] = ..., object_contact_group: _Optional[_Union[ContactGroup, _Mapping]] = ..., object_contact_role: _Optional[_Union[ContactRole, _Mapping]] = ..., object_device: _Optional[_Union[Device, _Mapping]] = ..., object_device_bay: _Optional[_Union[DeviceBay, _Mapping]] = ..., object_device_role: _Optional[_Union[DeviceRole, _Mapping]] = ..., object_device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., object_fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., object_fhrp_group_assignment: _Optional[_Union[FHRPGroupAssignment, _Mapping]] = ..., object_front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., object_ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., object_ike_proposal: _Optional[_Union[IKEProposal, _Mapping]] = ..., object_ip_address: _Optional[_Union[IPAddress, _Mapping]] = ..., object_ip_range: _Optional[_Union[IPRange, _Mapping]] = ..., object_ip_sec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., object_ip_sec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., object_ip_sec_proposal: _Optional[_Union[IPSecProposal, _Mapping]] = ..., object_interface: _Optional[_Union[Interface, _Mapping]] = ..., object_inventory_item: _Optional[_Union[InventoryItem, _Mapping]] = ..., object_inventory_item_role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., object_l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., object_l2vpn_termination: _Optional[_Union[L2VPNTermination, _Mapping]] = ..., object_location: _Optional[_Union[Location, _Mapping]] = ..., object_mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., object_manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., object_module: _Optional[_Union[Module, _Mapping]] = ..., object_module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., object_module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., object_platform: _Optional[_Union[Platform, _Mapping]] = ..., object_power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., object_power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., object_power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., object_power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., object_prefix: _Optional[_Union[Prefix, _Mapping]] = ..., object_provider: _Optional[_Union[Provider, _Mapping]] = ..., object_provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., object_provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., object_rir: _Optional[_Union[RIR, _Mapping]] = ..., object_rack: _Optional[_Union[Rack, _Mapping]] = ..., object_rack_reservation: _Optional[_Union[RackReservation, _Mapping]] = ..., object_rack_role: _Optional[_Union[RackRole, _Mapping]] = ..., object_rack_type: _Optional[_Union[RackType, _Mapping]] = ..., object_rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., object_region: _Optional[_Union[Region, _Mapping]] = ..., object_role: _Optional[_Union[Role, _Mapping]] = ..., object_route_target: _Optional[_Union[RouteTarget, _Mapping]] = ..., object_service: _Optional[_Union[Service, _Mapping]] = ..., object_site: _Optional[_Union[Site, _Mapping]] = ..., object_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., object_tag: _Optional[_Union[Tag, _Mapping]] = ..., object_tenant: _Optional[_Union[Tenant, _Mapping]] = ..., object_tenant_group: _Optional[_Union[TenantGroup, _Mapping]] = ..., object_tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., object_tunnel_group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., object_tunnel_termination: _Optional[_Union[TunnelTermination, _Mapping]] = ..., object_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., object_vlan_group: _Optional[_Union[VLANGroup, _Mapping]] = ..., object_vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., object_vlan_translation_rule: _Optional[_Union[VLANTranslationRule, _Mapping]] = ..., object_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., object_vrf: _Optional[_Union[VRF, _Mapping]] = ..., object_virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., object_virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., object_virtual_circuit_termination: _Optional[_Union[VirtualCircuitTermination, _Mapping]] = ..., object_virtual_circuit_type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., object_virtual_device_context: _Optional[_Union[VirtualDeviceContext, _Mapping]] = ..., object_virtual_disk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., object_virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., object_wireless_lan: _Optional[_Union[WirelessLAN, _Mapping]] = ..., object_wireless_lan_group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., object_wireless_link: _Optional[_Union[WirelessLink, _Mapping]] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ..., role: _Optional[_Union[ContactRole, _Mapping]] = ..., priority: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ContactGroup(_message.Message):
    __slots__ = ("name", "slug", "parent", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    parent: ContactGroup
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., parent: _Optional[_Union[ContactGroup, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ContactRole(_message.Message):
    __slots__ = ("name", "slug", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class CustomFieldObjectReference(_message.Message):
    __slots__ = ("asn", "asn_range", "aggregate", "cable", "cable_path", "cable_termination", "circuit", "circuit_group", "circuit_group_assignment", "circuit_termination", "circuit_type", "cluster", "cluster_group", "cluster_type", "console_port", "console_server_port", "contact", "contact_assignment", "contact_group", "contact_role", "device", "device_bay", "device_role", "device_type", "fhrp_group", "fhrp_group_assignment", "front_port", "ike_policy", "ike_proposal", "ip_address", "ip_range", "ip_sec_policy", "ip_sec_profile", "ip_sec_proposal", "interface", "inventory_item", "inventory_item_role", "l2vpn", "l2vpn_termination", "location", "mac_address", "manufacturer", "module", "module_bay", "module_type", "platform", "power_feed", "power_outlet", "power_panel", "power_port", "prefix", "provider", "provider_account", "provider_network", "rir", "rack", "rack_reservation", "rack_role", "rack_type", "rear_port", "region", "role", "route_target", "service", "site", "site_group", "tag", "tenant", "tenant_group", "tunnel", "tunnel_group", "tunnel_termination", "vlan", "vlan_group", "vlan_translation_policy", "vlan_translation_rule", "vm_interface", "vrf", "virtual_chassis", "virtual_circuit", "virtual_circuit_termination", "virtual_circuit_type", "virtual_device_context", "virtual_disk", "virtual_machine", "wireless_lan", "wireless_lan_group", "wireless_link")
    ASN_FIELD_NUMBER: _ClassVar[int]
    ASN_RANGE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    CABLE_FIELD_NUMBER: _ClassVar[int]
    CABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    CABLE_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BAY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    FHRP_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    IKE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    IP_SEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    IP_SEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IP_SEC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_ITEM_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_ITEM_ROLE_FIELD_NUMBER: _ClassVar[int]
    L2VPN_FIELD_NUMBER: _ClassVar[int]
    L2VPN_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    RIR_FIELD_NUMBER: _ClassVar[int]
    RACK_FIELD_NUMBER: _ClassVar[int]
    RACK_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    RACK_ROLE_FIELD_NUMBER: _ClassVar[int]
    RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TARGET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    TENANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    VLAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    VLAN_TRANSLATION_RULE_FIELD_NUMBER: _ClassVar[int]
    VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DEVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LAN_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    asn: ASN
    asn_range: ASNRange
    aggregate: Aggregate
    cable: Cable
    cable_path: CablePath
    cable_termination: CableTermination
    circuit: Circuit
    circuit_group: CircuitGroup
    circuit_group_assignment: CircuitGroupAssignment
    circuit_termination: CircuitTermination
    circuit_type: CircuitType
    cluster: Cluster
    cluster_group: ClusterGroup
    cluster_type: ClusterType
    console_port: ConsolePort
    console_server_port: ConsoleServerPort
    contact: Contact
    contact_assignment: ContactAssignment
    contact_group: ContactGroup
    contact_role: ContactRole
    device: Device
    device_bay: DeviceBay
    device_role: DeviceRole
    device_type: DeviceType
    fhrp_group: FHRPGroup
    fhrp_group_assignment: FHRPGroupAssignment
    front_port: FrontPort
    ike_policy: IKEPolicy
    ike_proposal: IKEProposal
    ip_address: IPAddress
    ip_range: IPRange
    ip_sec_policy: IPSecPolicy
    ip_sec_profile: IPSecProfile
    ip_sec_proposal: IPSecProposal
    interface: Interface
    inventory_item: InventoryItem
    inventory_item_role: InventoryItemRole
    l2vpn: L2VPN
    l2vpn_termination: L2VPNTermination
    location: Location
    mac_address: MACAddress
    manufacturer: Manufacturer
    module: Module
    module_bay: ModuleBay
    module_type: ModuleType
    platform: Platform
    power_feed: PowerFeed
    power_outlet: PowerOutlet
    power_panel: PowerPanel
    power_port: PowerPort
    prefix: Prefix
    provider: Provider
    provider_account: ProviderAccount
    provider_network: ProviderNetwork
    rir: RIR
    rack: Rack
    rack_reservation: RackReservation
    rack_role: RackRole
    rack_type: RackType
    rear_port: RearPort
    region: Region
    role: Role
    route_target: RouteTarget
    service: Service
    site: Site
    site_group: SiteGroup
    tag: Tag
    tenant: Tenant
    tenant_group: TenantGroup
    tunnel: Tunnel
    tunnel_group: TunnelGroup
    tunnel_termination: TunnelTermination
    vlan: VLAN
    vlan_group: VLANGroup
    vlan_translation_policy: VLANTranslationPolicy
    vlan_translation_rule: VLANTranslationRule
    vm_interface: VMInterface
    vrf: VRF
    virtual_chassis: VirtualChassis
    virtual_circuit: VirtualCircuit
    virtual_circuit_termination: VirtualCircuitTermination
    virtual_circuit_type: VirtualCircuitType
    virtual_device_context: VirtualDeviceContext
    virtual_disk: VirtualDisk
    virtual_machine: VirtualMachine
    wireless_lan: WirelessLAN
    wireless_lan_group: WirelessLANGroup
    wireless_link: WirelessLink
    def __init__(self, asn: _Optional[_Union[ASN, _Mapping]] = ..., asn_range: _Optional[_Union[ASNRange, _Mapping]] = ..., aggregate: _Optional[_Union[Aggregate, _Mapping]] = ..., cable: _Optional[_Union[Cable, _Mapping]] = ..., cable_path: _Optional[_Union[CablePath, _Mapping]] = ..., cable_termination: _Optional[_Union[CableTermination, _Mapping]] = ..., circuit: _Optional[_Union[Circuit, _Mapping]] = ..., circuit_group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., circuit_group_assignment: _Optional[_Union[CircuitGroupAssignment, _Mapping]] = ..., circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., circuit_type: _Optional[_Union[CircuitType, _Mapping]] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., cluster_type: _Optional[_Union[ClusterType, _Mapping]] = ..., console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ..., contact_assignment: _Optional[_Union[ContactAssignment, _Mapping]] = ..., contact_group: _Optional[_Union[ContactGroup, _Mapping]] = ..., contact_role: _Optional[_Union[ContactRole, _Mapping]] = ..., device: _Optional[_Union[Device, _Mapping]] = ..., device_bay: _Optional[_Union[DeviceBay, _Mapping]] = ..., device_role: _Optional[_Union[DeviceRole, _Mapping]] = ..., device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., fhrp_group_assignment: _Optional[_Union[FHRPGroupAssignment, _Mapping]] = ..., front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., ike_proposal: _Optional[_Union[IKEProposal, _Mapping]] = ..., ip_address: _Optional[_Union[IPAddress, _Mapping]] = ..., ip_range: _Optional[_Union[IPRange, _Mapping]] = ..., ip_sec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., ip_sec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., ip_sec_proposal: _Optional[_Union[IPSecProposal, _Mapping]] = ..., interface: _Optional[_Union[Interface, _Mapping]] = ..., inventory_item: _Optional[_Union[InventoryItem, _Mapping]] = ..., inventory_item_role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., l2vpn_termination: _Optional[_Union[L2VPNTermination, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., platform: _Optional[_Union[Platform, _Mapping]] = ..., power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., prefix: _Optional[_Union[Prefix, _Mapping]] = ..., provider: _Optional[_Union[Provider, _Mapping]] = ..., provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., rir: _Optional[_Union[RIR, _Mapping]] = ..., rack: _Optional[_Union[Rack, _Mapping]] = ..., rack_reservation: _Optional[_Union[RackReservation, _Mapping]] = ..., rack_role: _Optional[_Union[RackRole, _Mapping]] = ..., rack_type: _Optional[_Union[RackType, _Mapping]] = ..., rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., region: _Optional[_Union[Region, _Mapping]] = ..., role: _Optional[_Union[Role, _Mapping]] = ..., route_target: _Optional[_Union[RouteTarget, _Mapping]] = ..., service: _Optional[_Union[Service, _Mapping]] = ..., site: _Optional[_Union[Site, _Mapping]] = ..., site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., tag: _Optional[_Union[Tag, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., tenant_group: _Optional[_Union[TenantGroup, _Mapping]] = ..., tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., tunnel_group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., tunnel_termination: _Optional[_Union[TunnelTermination, _Mapping]] = ..., vlan: _Optional[_Union[VLAN, _Mapping]] = ..., vlan_group: _Optional[_Union[VLANGroup, _Mapping]] = ..., vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., vlan_translation_rule: _Optional[_Union[VLANTranslationRule, _Mapping]] = ..., vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., virtual_circuit_termination: _Optional[_Union[VirtualCircuitTermination, _Mapping]] = ..., virtual_circuit_type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., virtual_device_context: _Optional[_Union[VirtualDeviceContext, _Mapping]] = ..., virtual_disk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., wireless_lan: _Optional[_Union[WirelessLAN, _Mapping]] = ..., wireless_lan_group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., wireless_link: _Optional[_Union[WirelessLink, _Mapping]] = ...) -> None: ...

class CustomFieldValue(_message.Message):
    __slots__ = ("multiple_selection", "multiple_objects", "text", "long_text", "integer", "decimal", "boolean", "date", "datetime", "url", "json", "selection", "object")
    MULTIPLE_SELECTION_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LONG_TEXT_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    multiple_selection: _containers.RepeatedScalarFieldContainer[str]
    multiple_objects: _containers.RepeatedCompositeFieldContainer[CustomFieldObjectReference]
    text: str
    long_text: str
    integer: int
    decimal: float
    boolean: bool
    date: _timestamp_pb2.Timestamp
    datetime: _timestamp_pb2.Timestamp
    url: str
    json: str
    selection: str
    object: CustomFieldObjectReference
    def __init__(self, multiple_selection: _Optional[_Iterable[str]] = ..., multiple_objects: _Optional[_Iterable[_Union[CustomFieldObjectReference, _Mapping]]] = ..., text: _Optional[str] = ..., long_text: _Optional[str] = ..., integer: _Optional[int] = ..., decimal: _Optional[float] = ..., boolean: bool = ..., date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., url: _Optional[str] = ..., json: _Optional[str] = ..., selection: _Optional[str] = ..., object: _Optional[_Union[CustomFieldObjectReference, _Mapping]] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("name", "device_type", "role", "tenant", "platform", "serial", "asset_tag", "site", "location", "rack", "position", "face", "latitude", "longitude", "status", "airflow", "primary_ip4", "primary_ip6", "oob_ip", "cluster", "virtual_chassis", "vc_position", "vc_priority", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_TAG_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RACK_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IP4_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IP6_FIELD_NUMBER: _ClassVar[int]
    OOB_IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    VC_POSITION_FIELD_NUMBER: _ClassVar[int]
    VC_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    device_type: DeviceType
    role: DeviceRole
    tenant: Tenant
    platform: Platform
    serial: str
    asset_tag: str
    site: Site
    location: Location
    rack: Rack
    position: float
    face: str
    latitude: float
    longitude: float
    status: str
    airflow: str
    primary_ip4: IPAddress
    primary_ip6: IPAddress
    oob_ip: IPAddress
    cluster: Cluster
    virtual_chassis: VirtualChassis
    vc_position: int
    vc_priority: int
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., role: _Optional[_Union[DeviceRole, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., platform: _Optional[_Union[Platform, _Mapping]] = ..., serial: _Optional[str] = ..., asset_tag: _Optional[str] = ..., site: _Optional[_Union[Site, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., rack: _Optional[_Union[Rack, _Mapping]] = ..., position: _Optional[float] = ..., face: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., status: _Optional[str] = ..., airflow: _Optional[str] = ..., primary_ip4: _Optional[_Union[IPAddress, _Mapping]] = ..., primary_ip6: _Optional[_Union[IPAddress, _Mapping]] = ..., oob_ip: _Optional[_Union[IPAddress, _Mapping]] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., vc_position: _Optional[int] = ..., vc_priority: _Optional[int] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class DeviceBay(_message.Message):
    __slots__ = ("device", "name", "label", "description", "installed_device", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_DEVICE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    name: str
    label: str
    description: str
    installed_device: Device
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., description: _Optional[str] = ..., installed_device: _Optional[_Union[Device, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class DeviceRole(_message.Message):
    __slots__ = ("name", "slug", "color", "vm_role", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    VM_ROLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    color: str
    vm_role: bool
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., color: _Optional[str] = ..., vm_role: bool = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class DeviceType(_message.Message):
    __slots__ = ("manufacturer", "default_platform", "model", "slug", "part_number", "u_height", "exclude_from_utilization", "is_full_depth", "subdevice_role", "airflow", "weight", "weight_unit", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    U_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FROM_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_DEPTH_FIELD_NUMBER: _ClassVar[int]
    SUBDEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    manufacturer: Manufacturer
    default_platform: Platform
    model: str
    slug: str
    part_number: str
    u_height: float
    exclude_from_utilization: bool
    is_full_depth: bool
    subdevice_role: str
    airflow: str
    weight: float
    weight_unit: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., default_platform: _Optional[_Union[Platform, _Mapping]] = ..., model: _Optional[str] = ..., slug: _Optional[str] = ..., part_number: _Optional[str] = ..., u_height: _Optional[float] = ..., exclude_from_utilization: bool = ..., is_full_depth: bool = ..., subdevice_role: _Optional[str] = ..., airflow: _Optional[str] = ..., weight: _Optional[float] = ..., weight_unit: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class FHRPGroup(_message.Message):
    __slots__ = ("name", "protocol", "group_id", "auth_type", "auth_key", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    protocol: str
    group_id: int
    auth_type: str
    auth_key: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., protocol: _Optional[str] = ..., group_id: _Optional[int] = ..., auth_type: _Optional[str] = ..., auth_key: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class FHRPGroupAssignment(_message.Message):
    __slots__ = ("group", "interface_asn", "interface_asn_range", "interface_aggregate", "interface_cable", "interface_cable_path", "interface_cable_termination", "interface_circuit", "interface_circuit_group", "interface_circuit_group_assignment", "interface_circuit_termination", "interface_circuit_type", "interface_cluster", "interface_cluster_group", "interface_cluster_type", "interface_console_port", "interface_console_server_port", "interface_contact", "interface_contact_assignment", "interface_contact_group", "interface_contact_role", "interface_device", "interface_device_bay", "interface_device_role", "interface_device_type", "interface_fhrp_group", "interface_fhrp_group_assignment", "interface_front_port", "interface_ike_policy", "interface_ike_proposal", "interface_ip_address", "interface_ip_range", "interface_ip_sec_policy", "interface_ip_sec_profile", "interface_ip_sec_proposal", "interface_interface", "interface_inventory_item", "interface_inventory_item_role", "interface_l2vpn", "interface_l2vpn_termination", "interface_location", "interface_mac_address", "interface_manufacturer", "interface_module", "interface_module_bay", "interface_module_type", "interface_platform", "interface_power_feed", "interface_power_outlet", "interface_power_panel", "interface_power_port", "interface_prefix", "interface_provider", "interface_provider_account", "interface_provider_network", "interface_rir", "interface_rack", "interface_rack_reservation", "interface_rack_role", "interface_rack_type", "interface_rear_port", "interface_region", "interface_role", "interface_route_target", "interface_service", "interface_site", "interface_site_group", "interface_tag", "interface_tenant", "interface_tenant_group", "interface_tunnel", "interface_tunnel_group", "interface_tunnel_termination", "interface_vlan", "interface_vlan_group", "interface_vlan_translation_policy", "interface_vlan_translation_rule", "interface_vm_interface", "interface_vrf", "interface_virtual_chassis", "interface_virtual_circuit", "interface_virtual_circuit_termination", "interface_virtual_circuit_type", "interface_virtual_device_context", "interface_virtual_disk", "interface_virtual_machine", "interface_wireless_lan", "interface_wireless_lan_group", "interface_wireless_link", "priority")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ASN_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ASN_RANGE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CABLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CABLE_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CIRCUIT_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CIRCUIT_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CONTACT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CONTACT_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_CONTACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_DEVICE_BAY_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_DEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FHRP_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IKE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IP_SEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IP_SEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_IP_SEC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INVENTORY_ITEM_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_INVENTORY_ITEM_ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_L2VPN_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_L2VPN_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_MODULE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_RIR_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_RACK_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_RACK_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_RACK_ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_REGION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ROUTE_TARGET_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_SITE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TAG_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TENANT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TENANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TUNNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TUNNEL_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VLAN_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VLAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VLAN_TRANSLATION_RULE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VRF_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_DEVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_WIRELESS_LAN_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_WIRELESS_LAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    group: FHRPGroup
    interface_asn: ASN
    interface_asn_range: ASNRange
    interface_aggregate: Aggregate
    interface_cable: Cable
    interface_cable_path: CablePath
    interface_cable_termination: CableTermination
    interface_circuit: Circuit
    interface_circuit_group: CircuitGroup
    interface_circuit_group_assignment: CircuitGroupAssignment
    interface_circuit_termination: CircuitTermination
    interface_circuit_type: CircuitType
    interface_cluster: Cluster
    interface_cluster_group: ClusterGroup
    interface_cluster_type: ClusterType
    interface_console_port: ConsolePort
    interface_console_server_port: ConsoleServerPort
    interface_contact: Contact
    interface_contact_assignment: ContactAssignment
    interface_contact_group: ContactGroup
    interface_contact_role: ContactRole
    interface_device: Device
    interface_device_bay: DeviceBay
    interface_device_role: DeviceRole
    interface_device_type: DeviceType
    interface_fhrp_group: FHRPGroup
    interface_fhrp_group_assignment: FHRPGroupAssignment
    interface_front_port: FrontPort
    interface_ike_policy: IKEPolicy
    interface_ike_proposal: IKEProposal
    interface_ip_address: IPAddress
    interface_ip_range: IPRange
    interface_ip_sec_policy: IPSecPolicy
    interface_ip_sec_profile: IPSecProfile
    interface_ip_sec_proposal: IPSecProposal
    interface_interface: Interface
    interface_inventory_item: InventoryItem
    interface_inventory_item_role: InventoryItemRole
    interface_l2vpn: L2VPN
    interface_l2vpn_termination: L2VPNTermination
    interface_location: Location
    interface_mac_address: MACAddress
    interface_manufacturer: Manufacturer
    interface_module: Module
    interface_module_bay: ModuleBay
    interface_module_type: ModuleType
    interface_platform: Platform
    interface_power_feed: PowerFeed
    interface_power_outlet: PowerOutlet
    interface_power_panel: PowerPanel
    interface_power_port: PowerPort
    interface_prefix: Prefix
    interface_provider: Provider
    interface_provider_account: ProviderAccount
    interface_provider_network: ProviderNetwork
    interface_rir: RIR
    interface_rack: Rack
    interface_rack_reservation: RackReservation
    interface_rack_role: RackRole
    interface_rack_type: RackType
    interface_rear_port: RearPort
    interface_region: Region
    interface_role: Role
    interface_route_target: RouteTarget
    interface_service: Service
    interface_site: Site
    interface_site_group: SiteGroup
    interface_tag: Tag
    interface_tenant: Tenant
    interface_tenant_group: TenantGroup
    interface_tunnel: Tunnel
    interface_tunnel_group: TunnelGroup
    interface_tunnel_termination: TunnelTermination
    interface_vlan: VLAN
    interface_vlan_group: VLANGroup
    interface_vlan_translation_policy: VLANTranslationPolicy
    interface_vlan_translation_rule: VLANTranslationRule
    interface_vm_interface: VMInterface
    interface_vrf: VRF
    interface_virtual_chassis: VirtualChassis
    interface_virtual_circuit: VirtualCircuit
    interface_virtual_circuit_termination: VirtualCircuitTermination
    interface_virtual_circuit_type: VirtualCircuitType
    interface_virtual_device_context: VirtualDeviceContext
    interface_virtual_disk: VirtualDisk
    interface_virtual_machine: VirtualMachine
    interface_wireless_lan: WirelessLAN
    interface_wireless_lan_group: WirelessLANGroup
    interface_wireless_link: WirelessLink
    priority: int
    def __init__(self, group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., interface_asn: _Optional[_Union[ASN, _Mapping]] = ..., interface_asn_range: _Optional[_Union[ASNRange, _Mapping]] = ..., interface_aggregate: _Optional[_Union[Aggregate, _Mapping]] = ..., interface_cable: _Optional[_Union[Cable, _Mapping]] = ..., interface_cable_path: _Optional[_Union[CablePath, _Mapping]] = ..., interface_cable_termination: _Optional[_Union[CableTermination, _Mapping]] = ..., interface_circuit: _Optional[_Union[Circuit, _Mapping]] = ..., interface_circuit_group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., interface_circuit_group_assignment: _Optional[_Union[CircuitGroupAssignment, _Mapping]] = ..., interface_circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., interface_circuit_type: _Optional[_Union[CircuitType, _Mapping]] = ..., interface_cluster: _Optional[_Union[Cluster, _Mapping]] = ..., interface_cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., interface_cluster_type: _Optional[_Union[ClusterType, _Mapping]] = ..., interface_console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., interface_console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., interface_contact: _Optional[_Union[Contact, _Mapping]] = ..., interface_contact_assignment: _Optional[_Union[ContactAssignment, _Mapping]] = ..., interface_contact_group: _Optional[_Union[ContactGroup, _Mapping]] = ..., interface_contact_role: _Optional[_Union[ContactRole, _Mapping]] = ..., interface_device: _Optional[_Union[Device, _Mapping]] = ..., interface_device_bay: _Optional[_Union[DeviceBay, _Mapping]] = ..., interface_device_role: _Optional[_Union[DeviceRole, _Mapping]] = ..., interface_device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., interface_fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., interface_fhrp_group_assignment: _Optional[_Union[FHRPGroupAssignment, _Mapping]] = ..., interface_front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., interface_ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., interface_ike_proposal: _Optional[_Union[IKEProposal, _Mapping]] = ..., interface_ip_address: _Optional[_Union[IPAddress, _Mapping]] = ..., interface_ip_range: _Optional[_Union[IPRange, _Mapping]] = ..., interface_ip_sec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., interface_ip_sec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., interface_ip_sec_proposal: _Optional[_Union[IPSecProposal, _Mapping]] = ..., interface_interface: _Optional[_Union[Interface, _Mapping]] = ..., interface_inventory_item: _Optional[_Union[InventoryItem, _Mapping]] = ..., interface_inventory_item_role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., interface_l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., interface_l2vpn_termination: _Optional[_Union[L2VPNTermination, _Mapping]] = ..., interface_location: _Optional[_Union[Location, _Mapping]] = ..., interface_mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., interface_manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., interface_module: _Optional[_Union[Module, _Mapping]] = ..., interface_module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., interface_module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., interface_platform: _Optional[_Union[Platform, _Mapping]] = ..., interface_power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., interface_power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., interface_power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., interface_power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., interface_prefix: _Optional[_Union[Prefix, _Mapping]] = ..., interface_provider: _Optional[_Union[Provider, _Mapping]] = ..., interface_provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., interface_provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., interface_rir: _Optional[_Union[RIR, _Mapping]] = ..., interface_rack: _Optional[_Union[Rack, _Mapping]] = ..., interface_rack_reservation: _Optional[_Union[RackReservation, _Mapping]] = ..., interface_rack_role: _Optional[_Union[RackRole, _Mapping]] = ..., interface_rack_type: _Optional[_Union[RackType, _Mapping]] = ..., interface_rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., interface_region: _Optional[_Union[Region, _Mapping]] = ..., interface_role: _Optional[_Union[Role, _Mapping]] = ..., interface_route_target: _Optional[_Union[RouteTarget, _Mapping]] = ..., interface_service: _Optional[_Union[Service, _Mapping]] = ..., interface_site: _Optional[_Union[Site, _Mapping]] = ..., interface_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., interface_tag: _Optional[_Union[Tag, _Mapping]] = ..., interface_tenant: _Optional[_Union[Tenant, _Mapping]] = ..., interface_tenant_group: _Optional[_Union[TenantGroup, _Mapping]] = ..., interface_tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., interface_tunnel_group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., interface_tunnel_termination: _Optional[_Union[TunnelTermination, _Mapping]] = ..., interface_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., interface_vlan_group: _Optional[_Union[VLANGroup, _Mapping]] = ..., interface_vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., interface_vlan_translation_rule: _Optional[_Union[VLANTranslationRule, _Mapping]] = ..., interface_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., interface_vrf: _Optional[_Union[VRF, _Mapping]] = ..., interface_virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., interface_virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., interface_virtual_circuit_termination: _Optional[_Union[VirtualCircuitTermination, _Mapping]] = ..., interface_virtual_circuit_type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., interface_virtual_device_context: _Optional[_Union[VirtualDeviceContext, _Mapping]] = ..., interface_virtual_disk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., interface_virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., interface_wireless_lan: _Optional[_Union[WirelessLAN, _Mapping]] = ..., interface_wireless_lan_group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., interface_wireless_link: _Optional[_Union[WirelessLink, _Mapping]] = ..., priority: _Optional[int] = ...) -> None: ...

class FrontPort(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "color", "rear_port", "rear_port_position", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    REAR_PORT_POSITION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    color: str
    rear_port: RearPort
    rear_port_position: int
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., color: _Optional[str] = ..., rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., rear_port_position: _Optional[int] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class GenericObject(_message.Message):
    __slots__ = ("object_asn", "object_asn_range", "object_aggregate", "object_cable", "object_cable_path", "object_cable_termination", "object_circuit", "object_circuit_group", "object_circuit_group_assignment", "object_circuit_termination", "object_circuit_type", "object_cluster", "object_cluster_group", "object_cluster_type", "object_console_port", "object_console_server_port", "object_contact", "object_contact_assignment", "object_contact_group", "object_contact_role", "object_device", "object_device_bay", "object_device_role", "object_device_type", "object_fhrp_group", "object_fhrp_group_assignment", "object_front_port", "object_ike_policy", "object_ike_proposal", "object_ip_address", "object_ip_range", "object_ip_sec_policy", "object_ip_sec_profile", "object_ip_sec_proposal", "object_interface", "object_inventory_item", "object_inventory_item_role", "object_l2vpn", "object_l2vpn_termination", "object_location", "object_mac_address", "object_manufacturer", "object_module", "object_module_bay", "object_module_type", "object_platform", "object_power_feed", "object_power_outlet", "object_power_panel", "object_power_port", "object_prefix", "object_provider", "object_provider_account", "object_provider_network", "object_rir", "object_rack", "object_rack_reservation", "object_rack_role", "object_rack_type", "object_rear_port", "object_region", "object_role", "object_route_target", "object_service", "object_site", "object_site_group", "object_tag", "object_tenant", "object_tenant_group", "object_tunnel", "object_tunnel_group", "object_tunnel_termination", "object_vlan", "object_vlan_group", "object_vlan_translation_policy", "object_vlan_translation_rule", "object_vm_interface", "object_vrf", "object_virtual_chassis", "object_virtual_circuit", "object_virtual_circuit_termination", "object_virtual_circuit_type", "object_virtual_device_context", "object_virtual_disk", "object_virtual_machine", "object_wireless_lan", "object_wireless_lan_group", "object_wireless_link")
    OBJECT_ASN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ASN_RANGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CABLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CABLE_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONTACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_BAY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FHRP_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IKE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_SEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_SEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IP_SEC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INVENTORY_ITEM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INVENTORY_ITEM_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_L2VPN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_L2VPN_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MODULE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RIR_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_REGION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ROUTE_TARGET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SERVICE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SITE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TAG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TENANT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TENANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TUNNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TUNNEL_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VLAN_TRANSLATION_RULE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VRF_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_DEVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WIRELESS_LAN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WIRELESS_LAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    object_asn: ASN
    object_asn_range: ASNRange
    object_aggregate: Aggregate
    object_cable: Cable
    object_cable_path: CablePath
    object_cable_termination: CableTermination
    object_circuit: Circuit
    object_circuit_group: CircuitGroup
    object_circuit_group_assignment: CircuitGroupAssignment
    object_circuit_termination: CircuitTermination
    object_circuit_type: CircuitType
    object_cluster: Cluster
    object_cluster_group: ClusterGroup
    object_cluster_type: ClusterType
    object_console_port: ConsolePort
    object_console_server_port: ConsoleServerPort
    object_contact: Contact
    object_contact_assignment: ContactAssignment
    object_contact_group: ContactGroup
    object_contact_role: ContactRole
    object_device: Device
    object_device_bay: DeviceBay
    object_device_role: DeviceRole
    object_device_type: DeviceType
    object_fhrp_group: FHRPGroup
    object_fhrp_group_assignment: FHRPGroupAssignment
    object_front_port: FrontPort
    object_ike_policy: IKEPolicy
    object_ike_proposal: IKEProposal
    object_ip_address: IPAddress
    object_ip_range: IPRange
    object_ip_sec_policy: IPSecPolicy
    object_ip_sec_profile: IPSecProfile
    object_ip_sec_proposal: IPSecProposal
    object_interface: Interface
    object_inventory_item: InventoryItem
    object_inventory_item_role: InventoryItemRole
    object_l2vpn: L2VPN
    object_l2vpn_termination: L2VPNTermination
    object_location: Location
    object_mac_address: MACAddress
    object_manufacturer: Manufacturer
    object_module: Module
    object_module_bay: ModuleBay
    object_module_type: ModuleType
    object_platform: Platform
    object_power_feed: PowerFeed
    object_power_outlet: PowerOutlet
    object_power_panel: PowerPanel
    object_power_port: PowerPort
    object_prefix: Prefix
    object_provider: Provider
    object_provider_account: ProviderAccount
    object_provider_network: ProviderNetwork
    object_rir: RIR
    object_rack: Rack
    object_rack_reservation: RackReservation
    object_rack_role: RackRole
    object_rack_type: RackType
    object_rear_port: RearPort
    object_region: Region
    object_role: Role
    object_route_target: RouteTarget
    object_service: Service
    object_site: Site
    object_site_group: SiteGroup
    object_tag: Tag
    object_tenant: Tenant
    object_tenant_group: TenantGroup
    object_tunnel: Tunnel
    object_tunnel_group: TunnelGroup
    object_tunnel_termination: TunnelTermination
    object_vlan: VLAN
    object_vlan_group: VLANGroup
    object_vlan_translation_policy: VLANTranslationPolicy
    object_vlan_translation_rule: VLANTranslationRule
    object_vm_interface: VMInterface
    object_vrf: VRF
    object_virtual_chassis: VirtualChassis
    object_virtual_circuit: VirtualCircuit
    object_virtual_circuit_termination: VirtualCircuitTermination
    object_virtual_circuit_type: VirtualCircuitType
    object_virtual_device_context: VirtualDeviceContext
    object_virtual_disk: VirtualDisk
    object_virtual_machine: VirtualMachine
    object_wireless_lan: WirelessLAN
    object_wireless_lan_group: WirelessLANGroup
    object_wireless_link: WirelessLink
    def __init__(self, object_asn: _Optional[_Union[ASN, _Mapping]] = ..., object_asn_range: _Optional[_Union[ASNRange, _Mapping]] = ..., object_aggregate: _Optional[_Union[Aggregate, _Mapping]] = ..., object_cable: _Optional[_Union[Cable, _Mapping]] = ..., object_cable_path: _Optional[_Union[CablePath, _Mapping]] = ..., object_cable_termination: _Optional[_Union[CableTermination, _Mapping]] = ..., object_circuit: _Optional[_Union[Circuit, _Mapping]] = ..., object_circuit_group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., object_circuit_group_assignment: _Optional[_Union[CircuitGroupAssignment, _Mapping]] = ..., object_circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., object_circuit_type: _Optional[_Union[CircuitType, _Mapping]] = ..., object_cluster: _Optional[_Union[Cluster, _Mapping]] = ..., object_cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., object_cluster_type: _Optional[_Union[ClusterType, _Mapping]] = ..., object_console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., object_console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., object_contact: _Optional[_Union[Contact, _Mapping]] = ..., object_contact_assignment: _Optional[_Union[ContactAssignment, _Mapping]] = ..., object_contact_group: _Optional[_Union[ContactGroup, _Mapping]] = ..., object_contact_role: _Optional[_Union[ContactRole, _Mapping]] = ..., object_device: _Optional[_Union[Device, _Mapping]] = ..., object_device_bay: _Optional[_Union[DeviceBay, _Mapping]] = ..., object_device_role: _Optional[_Union[DeviceRole, _Mapping]] = ..., object_device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., object_fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., object_fhrp_group_assignment: _Optional[_Union[FHRPGroupAssignment, _Mapping]] = ..., object_front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., object_ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., object_ike_proposal: _Optional[_Union[IKEProposal, _Mapping]] = ..., object_ip_address: _Optional[_Union[IPAddress, _Mapping]] = ..., object_ip_range: _Optional[_Union[IPRange, _Mapping]] = ..., object_ip_sec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., object_ip_sec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., object_ip_sec_proposal: _Optional[_Union[IPSecProposal, _Mapping]] = ..., object_interface: _Optional[_Union[Interface, _Mapping]] = ..., object_inventory_item: _Optional[_Union[InventoryItem, _Mapping]] = ..., object_inventory_item_role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., object_l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., object_l2vpn_termination: _Optional[_Union[L2VPNTermination, _Mapping]] = ..., object_location: _Optional[_Union[Location, _Mapping]] = ..., object_mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., object_manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., object_module: _Optional[_Union[Module, _Mapping]] = ..., object_module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., object_module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., object_platform: _Optional[_Union[Platform, _Mapping]] = ..., object_power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., object_power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., object_power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., object_power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., object_prefix: _Optional[_Union[Prefix, _Mapping]] = ..., object_provider: _Optional[_Union[Provider, _Mapping]] = ..., object_provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., object_provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., object_rir: _Optional[_Union[RIR, _Mapping]] = ..., object_rack: _Optional[_Union[Rack, _Mapping]] = ..., object_rack_reservation: _Optional[_Union[RackReservation, _Mapping]] = ..., object_rack_role: _Optional[_Union[RackRole, _Mapping]] = ..., object_rack_type: _Optional[_Union[RackType, _Mapping]] = ..., object_rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., object_region: _Optional[_Union[Region, _Mapping]] = ..., object_role: _Optional[_Union[Role, _Mapping]] = ..., object_route_target: _Optional[_Union[RouteTarget, _Mapping]] = ..., object_service: _Optional[_Union[Service, _Mapping]] = ..., object_site: _Optional[_Union[Site, _Mapping]] = ..., object_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., object_tag: _Optional[_Union[Tag, _Mapping]] = ..., object_tenant: _Optional[_Union[Tenant, _Mapping]] = ..., object_tenant_group: _Optional[_Union[TenantGroup, _Mapping]] = ..., object_tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., object_tunnel_group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., object_tunnel_termination: _Optional[_Union[TunnelTermination, _Mapping]] = ..., object_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., object_vlan_group: _Optional[_Union[VLANGroup, _Mapping]] = ..., object_vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., object_vlan_translation_rule: _Optional[_Union[VLANTranslationRule, _Mapping]] = ..., object_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., object_vrf: _Optional[_Union[VRF, _Mapping]] = ..., object_virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., object_virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., object_virtual_circuit_termination: _Optional[_Union[VirtualCircuitTermination, _Mapping]] = ..., object_virtual_circuit_type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., object_virtual_device_context: _Optional[_Union[VirtualDeviceContext, _Mapping]] = ..., object_virtual_disk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., object_virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., object_wireless_lan: _Optional[_Union[WirelessLAN, _Mapping]] = ..., object_wireless_lan_group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., object_wireless_link: _Optional[_Union[WirelessLink, _Mapping]] = ...) -> None: ...

class IKEPolicy(_message.Message):
    __slots__ = ("name", "description", "version", "mode", "preshared_key", "comments", "tags", "custom_fields", "proposals")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PRESHARED_KEY_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    version: int
    mode: str
    preshared_key: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    proposals: _containers.RepeatedCompositeFieldContainer[IKEProposal]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[int] = ..., mode: _Optional[str] = ..., preshared_key: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., proposals: _Optional[_Iterable[_Union[IKEProposal, _Mapping]]] = ...) -> None: ...

class IKEProposal(_message.Message):
    __slots__ = ("name", "description", "authentication_method", "encryption_algorithm", "authentication_algorithm", "group", "sa_lifetime", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SA_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    authentication_method: str
    encryption_algorithm: str
    authentication_algorithm: str
    group: int
    sa_lifetime: int
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., authentication_method: _Optional[str] = ..., encryption_algorithm: _Optional[str] = ..., authentication_algorithm: _Optional[str] = ..., group: _Optional[int] = ..., sa_lifetime: _Optional[int] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class IPAddress(_message.Message):
    __slots__ = ("address", "vrf", "tenant", "status", "role", "assigned_object_fhrp_group", "assigned_object_interface", "assigned_object_vm_interface", "nat_inside", "dns_name", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    NAT_INSIDE_FIELD_NUMBER: _ClassVar[int]
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    address: str
    vrf: VRF
    tenant: Tenant
    status: str
    role: str
    assigned_object_fhrp_group: FHRPGroup
    assigned_object_interface: Interface
    assigned_object_vm_interface: VMInterface
    nat_inside: IPAddress
    dns_name: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, address: _Optional[str] = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., status: _Optional[str] = ..., role: _Optional[str] = ..., assigned_object_fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., assigned_object_interface: _Optional[_Union[Interface, _Mapping]] = ..., assigned_object_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., nat_inside: _Optional[_Union[IPAddress, _Mapping]] = ..., dns_name: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class IPRange(_message.Message):
    __slots__ = ("start_address", "end_address", "vrf", "tenant", "status", "role", "description", "comments", "tags", "mark_utilized", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    START_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    END_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MARK_UTILIZED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    start_address: str
    end_address: str
    vrf: VRF
    tenant: Tenant
    status: str
    role: Role
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    mark_utilized: bool
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, start_address: _Optional[str] = ..., end_address: _Optional[str] = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., status: _Optional[str] = ..., role: _Optional[_Union[Role, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., mark_utilized: bool = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class IPSecPolicy(_message.Message):
    __slots__ = ("name", "description", "pfs_group", "comments", "tags", "custom_fields", "proposals")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PFS_GROUP_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    pfs_group: int
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    proposals: _containers.RepeatedCompositeFieldContainer[IPSecProposal]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., pfs_group: _Optional[int] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., proposals: _Optional[_Iterable[_Union[IPSecProposal, _Mapping]]] = ...) -> None: ...

class IPSecProfile(_message.Message):
    __slots__ = ("name", "description", "mode", "ike_policy", "ipsec_policy", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    IPSEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    mode: str
    ike_policy: IKEPolicy
    ipsec_policy: IPSecPolicy
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., mode: _Optional[str] = ..., ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., ipsec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class IPSecProposal(_message.Message):
    __slots__ = ("name", "description", "encryption_algorithm", "authentication_algorithm", "sa_lifetime_seconds", "sa_lifetime_data", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    SA_LIFETIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SA_LIFETIME_DATA_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    encryption_algorithm: str
    authentication_algorithm: str
    sa_lifetime_seconds: int
    sa_lifetime_data: int
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., encryption_algorithm: _Optional[str] = ..., authentication_algorithm: _Optional[str] = ..., sa_lifetime_seconds: _Optional[int] = ..., sa_lifetime_data: _Optional[int] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Interface(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "enabled", "parent", "bridge", "lag", "mtu", "primary_mac_address", "speed", "duplex", "wwn", "mgmt_only", "description", "mode", "rf_role", "rf_channel", "poe_mode", "poe_type", "rf_channel_frequency", "rf_channel_width", "tx_power", "untagged_vlan", "qinq_svlan", "vlan_translation_policy", "mark_connected", "vrf", "tags", "custom_fields", "vdcs", "tagged_vlans", "wireless_lans")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_FIELD_NUMBER: _ClassVar[int]
    LAG_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    DUPLEX_FIELD_NUMBER: _ClassVar[int]
    WWN_FIELD_NUMBER: _ClassVar[int]
    MGMT_ONLY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RF_ROLE_FIELD_NUMBER: _ClassVar[int]
    RF_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    POE_MODE_FIELD_NUMBER: _ClassVar[int]
    POE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RF_CHANNEL_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RF_CHANNEL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    TX_POWER_FIELD_NUMBER: _ClassVar[int]
    UNTAGGED_VLAN_FIELD_NUMBER: _ClassVar[int]
    QINQ_SVLAN_FIELD_NUMBER: _ClassVar[int]
    VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    VDCS_FIELD_NUMBER: _ClassVar[int]
    TAGGED_VLANS_FIELD_NUMBER: _ClassVar[int]
    WIRELESS_LANS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    enabled: bool
    parent: Interface
    bridge: Interface
    lag: Interface
    mtu: int
    primary_mac_address: MACAddress
    speed: int
    duplex: str
    wwn: str
    mgmt_only: bool
    description: str
    mode: str
    rf_role: str
    rf_channel: str
    poe_mode: str
    poe_type: str
    rf_channel_frequency: float
    rf_channel_width: float
    tx_power: int
    untagged_vlan: VLAN
    qinq_svlan: VLAN
    vlan_translation_policy: VLANTranslationPolicy
    mark_connected: bool
    vrf: VRF
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    vdcs: _containers.RepeatedCompositeFieldContainer[VirtualDeviceContext]
    tagged_vlans: _containers.RepeatedCompositeFieldContainer[VLAN]
    wireless_lans: _containers.RepeatedCompositeFieldContainer[WirelessLAN]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., enabled: bool = ..., parent: _Optional[_Union[Interface, _Mapping]] = ..., bridge: _Optional[_Union[Interface, _Mapping]] = ..., lag: _Optional[_Union[Interface, _Mapping]] = ..., mtu: _Optional[int] = ..., primary_mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., speed: _Optional[int] = ..., duplex: _Optional[str] = ..., wwn: _Optional[str] = ..., mgmt_only: bool = ..., description: _Optional[str] = ..., mode: _Optional[str] = ..., rf_role: _Optional[str] = ..., rf_channel: _Optional[str] = ..., poe_mode: _Optional[str] = ..., poe_type: _Optional[str] = ..., rf_channel_frequency: _Optional[float] = ..., rf_channel_width: _Optional[float] = ..., tx_power: _Optional[int] = ..., untagged_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., qinq_svlan: _Optional[_Union[VLAN, _Mapping]] = ..., vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., mark_connected: bool = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., vdcs: _Optional[_Iterable[_Union[VirtualDeviceContext, _Mapping]]] = ..., tagged_vlans: _Optional[_Iterable[_Union[VLAN, _Mapping]]] = ..., wireless_lans: _Optional[_Iterable[_Union[WirelessLAN, _Mapping]]] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ("device", "parent", "name", "label", "status", "role", "manufacturer", "part_id", "serial", "asset_tag", "discovered", "description", "component_console_port", "component_console_server_port", "component_front_port", "component_interface", "component_power_outlet", "component_power_port", "component_rear_port", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    PART_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_TAG_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    parent: InventoryItem
    name: str
    label: str
    status: str
    role: InventoryItemRole
    manufacturer: Manufacturer
    part_id: str
    serial: str
    asset_tag: str
    discovered: bool
    description: str
    component_console_port: ConsolePort
    component_console_server_port: ConsoleServerPort
    component_front_port: FrontPort
    component_interface: Interface
    component_power_outlet: PowerOutlet
    component_power_port: PowerPort
    component_rear_port: RearPort
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., parent: _Optional[_Union[InventoryItem, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[str] = ..., role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., part_id: _Optional[str] = ..., serial: _Optional[str] = ..., asset_tag: _Optional[str] = ..., discovered: bool = ..., description: _Optional[str] = ..., component_console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., component_console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., component_front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., component_interface: _Optional[_Union[Interface, _Mapping]] = ..., component_power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., component_power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., component_rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class InventoryItemRole(_message.Message):
    __slots__ = ("name", "slug", "color", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    color: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., color: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class L2VPN(_message.Message):
    __slots__ = ("identifier", "name", "slug", "type", "description", "comments", "tenant", "tags", "custom_fields", "import_targets", "export_targets")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TARGETS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TARGETS_FIELD_NUMBER: _ClassVar[int]
    identifier: int
    name: str
    slug: str
    type: str
    description: str
    comments: str
    tenant: Tenant
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    import_targets: _containers.RepeatedCompositeFieldContainer[RouteTarget]
    export_targets: _containers.RepeatedCompositeFieldContainer[RouteTarget]
    def __init__(self, identifier: _Optional[int] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., import_targets: _Optional[_Iterable[_Union[RouteTarget, _Mapping]]] = ..., export_targets: _Optional[_Iterable[_Union[RouteTarget, _Mapping]]] = ...) -> None: ...

class L2VPNTermination(_message.Message):
    __slots__ = ("l2vpn", "assigned_object_interface", "assigned_object_vlan", "assigned_object_vm_interface", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    L2VPN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_VLAN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    l2vpn: L2VPN
    assigned_object_interface: Interface
    assigned_object_vlan: VLAN
    assigned_object_vm_interface: VMInterface
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., assigned_object_interface: _Optional[_Union[Interface, _Mapping]] = ..., assigned_object_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., assigned_object_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("name", "slug", "site", "parent", "status", "tenant", "facility", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    site: Site
    parent: Location
    status: str
    tenant: Tenant
    facility: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., site: _Optional[_Union[Site, _Mapping]] = ..., parent: _Optional[_Union[Location, _Mapping]] = ..., status: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., facility: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class MACAddress(_message.Message):
    __slots__ = ("mac_address", "assigned_object_interface", "assigned_object_vm_interface", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_OBJECT_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    mac_address: str
    assigned_object_interface: Interface
    assigned_object_vm_interface: VMInterface
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, mac_address: _Optional[str] = ..., assigned_object_interface: _Optional[_Union[Interface, _Mapping]] = ..., assigned_object_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Manufacturer(_message.Message):
    __slots__ = ("name", "slug", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Module(_message.Message):
    __slots__ = ("device", "module_bay", "module_type", "status", "serial", "asset_tag", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_TAG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module_bay: ModuleBay
    module_type: ModuleType
    status: str
    serial: str
    asset_tag: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., status: _Optional[str] = ..., serial: _Optional[str] = ..., asset_tag: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ModuleBay(_message.Message):
    __slots__ = ("device", "module", "name", "installed_module", "label", "position", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_MODULE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    installed_module: Module
    label: str
    position: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., installed_module: _Optional[_Union[Module, _Mapping]] = ..., label: _Optional[str] = ..., position: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ModuleType(_message.Message):
    __slots__ = ("manufacturer", "model", "part_number", "airflow", "weight", "weight_unit", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    manufacturer: Manufacturer
    model: str
    part_number: str
    airflow: str
    weight: float
    weight_unit: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., model: _Optional[str] = ..., part_number: _Optional[str] = ..., airflow: _Optional[str] = ..., weight: _Optional[float] = ..., weight_unit: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Platform(_message.Message):
    __slots__ = ("name", "slug", "manufacturer", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    manufacturer: Manufacturer
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class PowerFeed(_message.Message):
    __slots__ = ("power_panel", "rack", "name", "status", "type", "supply", "phase", "voltage", "amperage", "max_utilization", "mark_connected", "description", "tenant", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    RACK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPLY_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    AMPERAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    power_panel: PowerPanel
    rack: Rack
    name: str
    status: str
    type: str
    supply: str
    phase: str
    voltage: int
    amperage: int
    max_utilization: int
    mark_connected: bool
    description: str
    tenant: Tenant
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., rack: _Optional[_Union[Rack, _Mapping]] = ..., name: _Optional[str] = ..., status: _Optional[str] = ..., type: _Optional[str] = ..., supply: _Optional[str] = ..., phase: _Optional[str] = ..., voltage: _Optional[int] = ..., amperage: _Optional[int] = ..., max_utilization: _Optional[int] = ..., mark_connected: bool = ..., description: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class PowerOutlet(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "color", "power_port", "feed_leg", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    FEED_LEG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    color: str
    power_port: PowerPort
    feed_leg: str
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., color: _Optional[str] = ..., power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., feed_leg: _Optional[str] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class PowerPanel(_message.Message):
    __slots__ = ("site", "location", "name", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    SITE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    site: Site
    location: Location
    name: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class PowerPort(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "maximum_draw", "allocated_draw", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_DRAW_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_DRAW_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    maximum_draw: int
    allocated_draw: int
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., maximum_draw: _Optional[int] = ..., allocated_draw: _Optional[int] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Prefix(_message.Message):
    __slots__ = ("prefix", "vrf", "scope_location", "scope_region", "scope_site", "scope_site_group", "tenant", "vlan", "status", "role", "is_pool", "mark_utilized", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    SCOPE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_REGION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    IS_POOL_FIELD_NUMBER: _ClassVar[int]
    MARK_UTILIZED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    vrf: VRF
    scope_location: Location
    scope_region: Region
    scope_site: Site
    scope_site_group: SiteGroup
    tenant: Tenant
    vlan: VLAN
    status: str
    role: Role
    is_pool: bool
    mark_utilized: bool
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, prefix: _Optional[str] = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., scope_location: _Optional[_Union[Location, _Mapping]] = ..., scope_region: _Optional[_Union[Region, _Mapping]] = ..., scope_site: _Optional[_Union[Site, _Mapping]] = ..., scope_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., vlan: _Optional[_Union[VLAN, _Mapping]] = ..., status: _Optional[str] = ..., role: _Optional[_Union[Role, _Mapping]] = ..., is_pool: bool = ..., mark_utilized: bool = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Provider(_message.Message):
    __slots__ = ("name", "slug", "description", "comments", "tags", "custom_fields", "accounts", "asns")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ASNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    accounts: _containers.RepeatedCompositeFieldContainer[ProviderAccount]
    asns: _containers.RepeatedCompositeFieldContainer[ASN]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., accounts: _Optional[_Iterable[_Union[ProviderAccount, _Mapping]]] = ..., asns: _Optional[_Iterable[_Union[ASN, _Mapping]]] = ...) -> None: ...

class ProviderAccount(_message.Message):
    __slots__ = ("provider", "name", "account", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    provider: Provider
    name: str
    account: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, provider: _Optional[_Union[Provider, _Mapping]] = ..., name: _Optional[str] = ..., account: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class ProviderNetwork(_message.Message):
    __slots__ = ("provider", "name", "service_id", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    provider: Provider
    name: str
    service_id: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, provider: _Optional[_Union[Provider, _Mapping]] = ..., name: _Optional[str] = ..., service_id: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class RIR(_message.Message):
    __slots__ = ("name", "slug", "is_private", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    is_private: bool
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., is_private: bool = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Rack(_message.Message):
    __slots__ = ("name", "facility_id", "site", "location", "tenant", "status", "role", "serial", "asset_tag", "rack_type", "form_factor", "width", "u_height", "starting_unit", "weight", "max_weight", "weight_unit", "desc_units", "outer_width", "outer_depth", "outer_unit", "mounting_depth", "airflow", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ASSET_TAG_FIELD_NUMBER: _ClassVar[int]
    RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    U_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    STARTING_UNIT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESC_UNITS_FIELD_NUMBER: _ClassVar[int]
    OUTER_WIDTH_FIELD_NUMBER: _ClassVar[int]
    OUTER_DEPTH_FIELD_NUMBER: _ClassVar[int]
    OUTER_UNIT_FIELD_NUMBER: _ClassVar[int]
    MOUNTING_DEPTH_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    facility_id: str
    site: Site
    location: Location
    tenant: Tenant
    status: str
    role: RackRole
    serial: str
    asset_tag: str
    rack_type: RackType
    form_factor: str
    width: int
    u_height: int
    starting_unit: int
    weight: float
    max_weight: int
    weight_unit: str
    desc_units: bool
    outer_width: int
    outer_depth: int
    outer_unit: str
    mounting_depth: int
    airflow: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., facility_id: _Optional[str] = ..., site: _Optional[_Union[Site, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., status: _Optional[str] = ..., role: _Optional[_Union[RackRole, _Mapping]] = ..., serial: _Optional[str] = ..., asset_tag: _Optional[str] = ..., rack_type: _Optional[_Union[RackType, _Mapping]] = ..., form_factor: _Optional[str] = ..., width: _Optional[int] = ..., u_height: _Optional[int] = ..., starting_unit: _Optional[int] = ..., weight: _Optional[float] = ..., max_weight: _Optional[int] = ..., weight_unit: _Optional[str] = ..., desc_units: bool = ..., outer_width: _Optional[int] = ..., outer_depth: _Optional[int] = ..., outer_unit: _Optional[str] = ..., mounting_depth: _Optional[int] = ..., airflow: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class RackReservation(_message.Message):
    __slots__ = ("rack", "units", "tenant", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    RACK_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    rack: Rack
    units: _containers.RepeatedScalarFieldContainer[int]
    tenant: Tenant
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, rack: _Optional[_Union[Rack, _Mapping]] = ..., units: _Optional[_Iterable[int]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class RackRole(_message.Message):
    __slots__ = ("name", "slug", "color", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    color: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., color: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class RackType(_message.Message):
    __slots__ = ("manufacturer", "model", "slug", "description", "form_factor", "width", "u_height", "starting_unit", "desc_units", "outer_width", "outer_depth", "outer_unit", "weight", "max_weight", "weight_unit", "mounting_depth", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    U_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    STARTING_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESC_UNITS_FIELD_NUMBER: _ClassVar[int]
    OUTER_WIDTH_FIELD_NUMBER: _ClassVar[int]
    OUTER_DEPTH_FIELD_NUMBER: _ClassVar[int]
    OUTER_UNIT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_UNIT_FIELD_NUMBER: _ClassVar[int]
    MOUNTING_DEPTH_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    manufacturer: Manufacturer
    model: str
    slug: str
    description: str
    form_factor: str
    width: int
    u_height: int
    starting_unit: int
    desc_units: bool
    outer_width: int
    outer_depth: int
    outer_unit: str
    weight: float
    max_weight: int
    weight_unit: str
    mounting_depth: int
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., model: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., form_factor: _Optional[str] = ..., width: _Optional[int] = ..., u_height: _Optional[int] = ..., starting_unit: _Optional[int] = ..., desc_units: bool = ..., outer_width: _Optional[int] = ..., outer_depth: _Optional[int] = ..., outer_unit: _Optional[str] = ..., weight: _Optional[float] = ..., max_weight: _Optional[int] = ..., weight_unit: _Optional[str] = ..., mounting_depth: _Optional[int] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class RearPort(_message.Message):
    __slots__ = ("device", "module", "name", "label", "type", "color", "positions", "description", "mark_connected", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    device: Device
    module: Module
    name: str
    label: str
    type: str
    color: str
    positions: int
    description: str
    mark_connected: bool
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., color: _Optional[str] = ..., positions: _Optional[int] = ..., description: _Optional[str] = ..., mark_connected: bool = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ("name", "slug", "parent", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    parent: Region
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., parent: _Optional[_Union[Region, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("name", "slug", "weight", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    weight: int
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., weight: _Optional[int] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class RouteTarget(_message.Message):
    __slots__ = ("name", "tenant", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    tenant: Tenant
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("device", "virtual_machine", "name", "protocol", "ports", "description", "comments", "tags", "custom_fields", "ipaddresses")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    IPADDRESSES_FIELD_NUMBER: _ClassVar[int]
    device: Device
    virtual_machine: VirtualMachine
    name: str
    protocol: str
    ports: _containers.RepeatedScalarFieldContainer[int]
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    ipaddresses: _containers.RepeatedCompositeFieldContainer[IPAddress]
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., name: _Optional[str] = ..., protocol: _Optional[str] = ..., ports: _Optional[_Iterable[int]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., ipaddresses: _Optional[_Iterable[_Union[IPAddress, _Mapping]]] = ...) -> None: ...

class Site(_message.Message):
    __slots__ = ("name", "slug", "status", "region", "group", "tenant", "facility", "time_zone", "description", "physical_address", "shipping_address", "latitude", "longitude", "comments", "tags", "custom_fields", "asns")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ASNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    status: str
    region: Region
    group: SiteGroup
    tenant: Tenant
    facility: str
    time_zone: str
    description: str
    physical_address: str
    shipping_address: str
    latitude: float
    longitude: float
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    asns: _containers.RepeatedCompositeFieldContainer[ASN]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., status: _Optional[str] = ..., region: _Optional[_Union[Region, _Mapping]] = ..., group: _Optional[_Union[SiteGroup, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., facility: _Optional[str] = ..., time_zone: _Optional[str] = ..., description: _Optional[str] = ..., physical_address: _Optional[str] = ..., shipping_address: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., asns: _Optional[_Iterable[_Union[ASN, _Mapping]]] = ...) -> None: ...

class SiteGroup(_message.Message):
    __slots__ = ("name", "slug", "parent", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    parent: SiteGroup
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., parent: _Optional[_Union[SiteGroup, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("name", "slug", "color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    color: str
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class Tenant(_message.Message):
    __slots__ = ("name", "slug", "group", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    group: TenantGroup
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., group: _Optional[_Union[TenantGroup, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class TenantGroup(_message.Message):
    __slots__ = ("name", "slug", "parent", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    parent: TenantGroup
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., parent: _Optional[_Union[TenantGroup, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class Tunnel(_message.Message):
    __slots__ = ("name", "status", "group", "encapsulation", "ipsec_profile", "tenant", "tunnel_id", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ENCAPSULATION_FIELD_NUMBER: _ClassVar[int]
    IPSEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: str
    group: TunnelGroup
    encapsulation: str
    ipsec_profile: IPSecProfile
    tenant: Tenant
    tunnel_id: int
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., status: _Optional[str] = ..., group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., encapsulation: _Optional[str] = ..., ipsec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., tunnel_id: _Optional[int] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class TunnelGroup(_message.Message):
    __slots__ = ("name", "slug", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class TunnelTermination(_message.Message):
    __slots__ = ("tunnel", "role", "termination_asn", "termination_asn_range", "termination_aggregate", "termination_cable", "termination_cable_path", "termination_cable_termination", "termination_circuit", "termination_circuit_group", "termination_circuit_group_assignment", "termination_circuit_termination", "termination_circuit_type", "termination_cluster", "termination_cluster_group", "termination_cluster_type", "termination_console_port", "termination_console_server_port", "termination_contact", "termination_contact_assignment", "termination_contact_group", "termination_contact_role", "termination_device", "termination_device_bay", "termination_device_role", "termination_device_type", "termination_fhrp_group", "termination_fhrp_group_assignment", "termination_front_port", "termination_ike_policy", "termination_ike_proposal", "termination_ip_address", "termination_ip_range", "termination_ip_sec_policy", "termination_ip_sec_profile", "termination_ip_sec_proposal", "termination_interface", "termination_inventory_item", "termination_inventory_item_role", "termination_l2vpn", "termination_l2vpn_termination", "termination_location", "termination_mac_address", "termination_manufacturer", "termination_module", "termination_module_bay", "termination_module_type", "termination_platform", "termination_power_feed", "termination_power_outlet", "termination_power_panel", "termination_power_port", "termination_prefix", "termination_provider", "termination_provider_account", "termination_provider_network", "termination_rir", "termination_rack", "termination_rack_reservation", "termination_rack_role", "termination_rack_type", "termination_rear_port", "termination_region", "termination_role", "termination_route_target", "termination_service", "termination_site", "termination_site_group", "termination_tag", "termination_tenant", "termination_tenant_group", "termination_tunnel", "termination_tunnel_group", "termination_tunnel_termination", "termination_vlan", "termination_vlan_group", "termination_vlan_translation_policy", "termination_vlan_translation_rule", "termination_vm_interface", "termination_vrf", "termination_virtual_chassis", "termination_virtual_circuit", "termination_virtual_circuit_termination", "termination_virtual_circuit_type", "termination_virtual_device_context", "termination_virtual_disk", "termination_virtual_machine", "termination_wireless_lan", "termination_wireless_lan_group", "termination_wireless_link", "outside_ip", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    TUNNEL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ASN_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ASN_RANGE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CABLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CABLE_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CIRCUIT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CIRCUIT_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONSOLE_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONSOLE_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONTACT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONTACT_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_CONTACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_DEVICE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_DEVICE_BAY_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_DEVICE_ROLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_FHRP_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_FHRP_GROUP_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_FRONT_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IKE_POLICY_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IKE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IP_SEC_POLICY_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IP_SEC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_IP_SEC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_INVENTORY_ITEM_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_INVENTORY_ITEM_ROLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_L2VPN_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_L2VPN_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_MODULE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_MODULE_BAY_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_FEED_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_OUTLET_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_PANEL_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POWER_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_PREFIX_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_RIR_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_RACK_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_RACK_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_RACK_ROLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_RACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_REAR_PORT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_REGION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ROLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ROUTE_TARGET_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_SITE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_TAG_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_TENANT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_TENANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_TUNNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_TUNNEL_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VLAN_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VLAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VLAN_TRANSLATION_RULE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VRF_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_CHASSIS_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_CIRCUIT_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_DEVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_WIRELESS_LAN_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_WIRELESS_LAN_GROUP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_WIRELESS_LINK_FIELD_NUMBER: _ClassVar[int]
    OUTSIDE_IP_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    tunnel: Tunnel
    role: str
    termination_asn: ASN
    termination_asn_range: ASNRange
    termination_aggregate: Aggregate
    termination_cable: Cable
    termination_cable_path: CablePath
    termination_cable_termination: CableTermination
    termination_circuit: Circuit
    termination_circuit_group: CircuitGroup
    termination_circuit_group_assignment: CircuitGroupAssignment
    termination_circuit_termination: CircuitTermination
    termination_circuit_type: CircuitType
    termination_cluster: Cluster
    termination_cluster_group: ClusterGroup
    termination_cluster_type: ClusterType
    termination_console_port: ConsolePort
    termination_console_server_port: ConsoleServerPort
    termination_contact: Contact
    termination_contact_assignment: ContactAssignment
    termination_contact_group: ContactGroup
    termination_contact_role: ContactRole
    termination_device: Device
    termination_device_bay: DeviceBay
    termination_device_role: DeviceRole
    termination_device_type: DeviceType
    termination_fhrp_group: FHRPGroup
    termination_fhrp_group_assignment: FHRPGroupAssignment
    termination_front_port: FrontPort
    termination_ike_policy: IKEPolicy
    termination_ike_proposal: IKEProposal
    termination_ip_address: IPAddress
    termination_ip_range: IPRange
    termination_ip_sec_policy: IPSecPolicy
    termination_ip_sec_profile: IPSecProfile
    termination_ip_sec_proposal: IPSecProposal
    termination_interface: Interface
    termination_inventory_item: InventoryItem
    termination_inventory_item_role: InventoryItemRole
    termination_l2vpn: L2VPN
    termination_l2vpn_termination: L2VPNTermination
    termination_location: Location
    termination_mac_address: MACAddress
    termination_manufacturer: Manufacturer
    termination_module: Module
    termination_module_bay: ModuleBay
    termination_module_type: ModuleType
    termination_platform: Platform
    termination_power_feed: PowerFeed
    termination_power_outlet: PowerOutlet
    termination_power_panel: PowerPanel
    termination_power_port: PowerPort
    termination_prefix: Prefix
    termination_provider: Provider
    termination_provider_account: ProviderAccount
    termination_provider_network: ProviderNetwork
    termination_rir: RIR
    termination_rack: Rack
    termination_rack_reservation: RackReservation
    termination_rack_role: RackRole
    termination_rack_type: RackType
    termination_rear_port: RearPort
    termination_region: Region
    termination_role: Role
    termination_route_target: RouteTarget
    termination_service: Service
    termination_site: Site
    termination_site_group: SiteGroup
    termination_tag: Tag
    termination_tenant: Tenant
    termination_tenant_group: TenantGroup
    termination_tunnel: Tunnel
    termination_tunnel_group: TunnelGroup
    termination_tunnel_termination: TunnelTermination
    termination_vlan: VLAN
    termination_vlan_group: VLANGroup
    termination_vlan_translation_policy: VLANTranslationPolicy
    termination_vlan_translation_rule: VLANTranslationRule
    termination_vm_interface: VMInterface
    termination_vrf: VRF
    termination_virtual_chassis: VirtualChassis
    termination_virtual_circuit: VirtualCircuit
    termination_virtual_circuit_termination: VirtualCircuitTermination
    termination_virtual_circuit_type: VirtualCircuitType
    termination_virtual_device_context: VirtualDeviceContext
    termination_virtual_disk: VirtualDisk
    termination_virtual_machine: VirtualMachine
    termination_wireless_lan: WirelessLAN
    termination_wireless_lan_group: WirelessLANGroup
    termination_wireless_link: WirelessLink
    outside_ip: IPAddress
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., role: _Optional[str] = ..., termination_asn: _Optional[_Union[ASN, _Mapping]] = ..., termination_asn_range: _Optional[_Union[ASNRange, _Mapping]] = ..., termination_aggregate: _Optional[_Union[Aggregate, _Mapping]] = ..., termination_cable: _Optional[_Union[Cable, _Mapping]] = ..., termination_cable_path: _Optional[_Union[CablePath, _Mapping]] = ..., termination_cable_termination: _Optional[_Union[CableTermination, _Mapping]] = ..., termination_circuit: _Optional[_Union[Circuit, _Mapping]] = ..., termination_circuit_group: _Optional[_Union[CircuitGroup, _Mapping]] = ..., termination_circuit_group_assignment: _Optional[_Union[CircuitGroupAssignment, _Mapping]] = ..., termination_circuit_termination: _Optional[_Union[CircuitTermination, _Mapping]] = ..., termination_circuit_type: _Optional[_Union[CircuitType, _Mapping]] = ..., termination_cluster: _Optional[_Union[Cluster, _Mapping]] = ..., termination_cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., termination_cluster_type: _Optional[_Union[ClusterType, _Mapping]] = ..., termination_console_port: _Optional[_Union[ConsolePort, _Mapping]] = ..., termination_console_server_port: _Optional[_Union[ConsoleServerPort, _Mapping]] = ..., termination_contact: _Optional[_Union[Contact, _Mapping]] = ..., termination_contact_assignment: _Optional[_Union[ContactAssignment, _Mapping]] = ..., termination_contact_group: _Optional[_Union[ContactGroup, _Mapping]] = ..., termination_contact_role: _Optional[_Union[ContactRole, _Mapping]] = ..., termination_device: _Optional[_Union[Device, _Mapping]] = ..., termination_device_bay: _Optional[_Union[DeviceBay, _Mapping]] = ..., termination_device_role: _Optional[_Union[DeviceRole, _Mapping]] = ..., termination_device_type: _Optional[_Union[DeviceType, _Mapping]] = ..., termination_fhrp_group: _Optional[_Union[FHRPGroup, _Mapping]] = ..., termination_fhrp_group_assignment: _Optional[_Union[FHRPGroupAssignment, _Mapping]] = ..., termination_front_port: _Optional[_Union[FrontPort, _Mapping]] = ..., termination_ike_policy: _Optional[_Union[IKEPolicy, _Mapping]] = ..., termination_ike_proposal: _Optional[_Union[IKEProposal, _Mapping]] = ..., termination_ip_address: _Optional[_Union[IPAddress, _Mapping]] = ..., termination_ip_range: _Optional[_Union[IPRange, _Mapping]] = ..., termination_ip_sec_policy: _Optional[_Union[IPSecPolicy, _Mapping]] = ..., termination_ip_sec_profile: _Optional[_Union[IPSecProfile, _Mapping]] = ..., termination_ip_sec_proposal: _Optional[_Union[IPSecProposal, _Mapping]] = ..., termination_interface: _Optional[_Union[Interface, _Mapping]] = ..., termination_inventory_item: _Optional[_Union[InventoryItem, _Mapping]] = ..., termination_inventory_item_role: _Optional[_Union[InventoryItemRole, _Mapping]] = ..., termination_l2vpn: _Optional[_Union[L2VPN, _Mapping]] = ..., termination_l2vpn_termination: _Optional[_Union[L2VPNTermination, _Mapping]] = ..., termination_location: _Optional[_Union[Location, _Mapping]] = ..., termination_mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., termination_manufacturer: _Optional[_Union[Manufacturer, _Mapping]] = ..., termination_module: _Optional[_Union[Module, _Mapping]] = ..., termination_module_bay: _Optional[_Union[ModuleBay, _Mapping]] = ..., termination_module_type: _Optional[_Union[ModuleType, _Mapping]] = ..., termination_platform: _Optional[_Union[Platform, _Mapping]] = ..., termination_power_feed: _Optional[_Union[PowerFeed, _Mapping]] = ..., termination_power_outlet: _Optional[_Union[PowerOutlet, _Mapping]] = ..., termination_power_panel: _Optional[_Union[PowerPanel, _Mapping]] = ..., termination_power_port: _Optional[_Union[PowerPort, _Mapping]] = ..., termination_prefix: _Optional[_Union[Prefix, _Mapping]] = ..., termination_provider: _Optional[_Union[Provider, _Mapping]] = ..., termination_provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., termination_provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., termination_rir: _Optional[_Union[RIR, _Mapping]] = ..., termination_rack: _Optional[_Union[Rack, _Mapping]] = ..., termination_rack_reservation: _Optional[_Union[RackReservation, _Mapping]] = ..., termination_rack_role: _Optional[_Union[RackRole, _Mapping]] = ..., termination_rack_type: _Optional[_Union[RackType, _Mapping]] = ..., termination_rear_port: _Optional[_Union[RearPort, _Mapping]] = ..., termination_region: _Optional[_Union[Region, _Mapping]] = ..., termination_role: _Optional[_Union[Role, _Mapping]] = ..., termination_route_target: _Optional[_Union[RouteTarget, _Mapping]] = ..., termination_service: _Optional[_Union[Service, _Mapping]] = ..., termination_site: _Optional[_Union[Site, _Mapping]] = ..., termination_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., termination_tag: _Optional[_Union[Tag, _Mapping]] = ..., termination_tenant: _Optional[_Union[Tenant, _Mapping]] = ..., termination_tenant_group: _Optional[_Union[TenantGroup, _Mapping]] = ..., termination_tunnel: _Optional[_Union[Tunnel, _Mapping]] = ..., termination_tunnel_group: _Optional[_Union[TunnelGroup, _Mapping]] = ..., termination_tunnel_termination: _Optional[_Union[TunnelTermination, _Mapping]] = ..., termination_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., termination_vlan_group: _Optional[_Union[VLANGroup, _Mapping]] = ..., termination_vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., termination_vlan_translation_rule: _Optional[_Union[VLANTranslationRule, _Mapping]] = ..., termination_vm_interface: _Optional[_Union[VMInterface, _Mapping]] = ..., termination_vrf: _Optional[_Union[VRF, _Mapping]] = ..., termination_virtual_chassis: _Optional[_Union[VirtualChassis, _Mapping]] = ..., termination_virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., termination_virtual_circuit_termination: _Optional[_Union[VirtualCircuitTermination, _Mapping]] = ..., termination_virtual_circuit_type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., termination_virtual_device_context: _Optional[_Union[VirtualDeviceContext, _Mapping]] = ..., termination_virtual_disk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., termination_virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., termination_wireless_lan: _Optional[_Union[WirelessLAN, _Mapping]] = ..., termination_wireless_lan_group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., termination_wireless_link: _Optional[_Union[WirelessLink, _Mapping]] = ..., outside_ip: _Optional[_Union[IPAddress, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VLAN(_message.Message):
    __slots__ = ("site", "group", "vid", "name", "tenant", "status", "role", "description", "qinq_role", "qinq_svlan", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    SITE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QINQ_ROLE_FIELD_NUMBER: _ClassVar[int]
    QINQ_SVLAN_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    site: Site
    group: VLANGroup
    vid: int
    name: str
    tenant: Tenant
    status: str
    role: Role
    description: str
    qinq_role: str
    qinq_svlan: VLAN
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ..., group: _Optional[_Union[VLANGroup, _Mapping]] = ..., vid: _Optional[int] = ..., name: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., status: _Optional[str] = ..., role: _Optional[_Union[Role, _Mapping]] = ..., description: _Optional[str] = ..., qinq_role: _Optional[str] = ..., qinq_svlan: _Optional[_Union[VLAN, _Mapping]] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VLANGroup(_message.Message):
    __slots__ = ("name", "slug", "scope_cluster", "scope_cluster_group", "scope_location", "scope_rack", "scope_region", "scope_site", "scope_site_group", "vid_ranges", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    SCOPE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_CLUSTER_GROUP_FIELD_NUMBER: _ClassVar[int]
    SCOPE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_RACK_FIELD_NUMBER: _ClassVar[int]
    SCOPE_REGION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    VID_RANGES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    scope_cluster: Cluster
    scope_cluster_group: ClusterGroup
    scope_location: Location
    scope_rack: Rack
    scope_region: Region
    scope_site: Site
    scope_site_group: SiteGroup
    vid_ranges: _containers.RepeatedScalarFieldContainer[int]
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., scope_cluster: _Optional[_Union[Cluster, _Mapping]] = ..., scope_cluster_group: _Optional[_Union[ClusterGroup, _Mapping]] = ..., scope_location: _Optional[_Union[Location, _Mapping]] = ..., scope_rack: _Optional[_Union[Rack, _Mapping]] = ..., scope_region: _Optional[_Union[Region, _Mapping]] = ..., scope_site: _Optional[_Union[Site, _Mapping]] = ..., scope_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., vid_ranges: _Optional[_Iterable[int]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VLANTranslationPolicy(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class VLANTranslationRule(_message.Message):
    __slots__ = ("policy", "local_vid", "remote_vid", "description")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_VID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_VID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    policy: VLANTranslationPolicy
    local_vid: int
    remote_vid: int
    description: str
    def __init__(self, policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., local_vid: _Optional[int] = ..., remote_vid: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class VMInterface(_message.Message):
    __slots__ = ("virtual_machine", "name", "enabled", "parent", "bridge", "mtu", "primary_mac_address", "description", "mode", "untagged_vlan", "qinq_svlan", "vlan_translation_policy", "vrf", "tags", "custom_fields", "tagged_vlans")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UNTAGGED_VLAN_FIELD_NUMBER: _ClassVar[int]
    QINQ_SVLAN_FIELD_NUMBER: _ClassVar[int]
    VLAN_TRANSLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    TAGGED_VLANS_FIELD_NUMBER: _ClassVar[int]
    virtual_machine: VirtualMachine
    name: str
    enabled: bool
    parent: VMInterface
    bridge: VMInterface
    mtu: int
    primary_mac_address: MACAddress
    description: str
    mode: str
    untagged_vlan: VLAN
    qinq_svlan: VLAN
    vlan_translation_policy: VLANTranslationPolicy
    vrf: VRF
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    tagged_vlans: _containers.RepeatedCompositeFieldContainer[VLAN]
    def __init__(self, virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., name: _Optional[str] = ..., enabled: bool = ..., parent: _Optional[_Union[VMInterface, _Mapping]] = ..., bridge: _Optional[_Union[VMInterface, _Mapping]] = ..., mtu: _Optional[int] = ..., primary_mac_address: _Optional[_Union[MACAddress, _Mapping]] = ..., description: _Optional[str] = ..., mode: _Optional[str] = ..., untagged_vlan: _Optional[_Union[VLAN, _Mapping]] = ..., qinq_svlan: _Optional[_Union[VLAN, _Mapping]] = ..., vlan_translation_policy: _Optional[_Union[VLANTranslationPolicy, _Mapping]] = ..., vrf: _Optional[_Union[VRF, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., tagged_vlans: _Optional[_Iterable[_Union[VLAN, _Mapping]]] = ...) -> None: ...

class VRF(_message.Message):
    __slots__ = ("name", "rd", "tenant", "enforce_unique", "description", "comments", "tags", "custom_fields", "import_targets", "export_targets")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RD_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TARGETS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TARGETS_FIELD_NUMBER: _ClassVar[int]
    name: str
    rd: str
    tenant: Tenant
    enforce_unique: bool
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    import_targets: _containers.RepeatedCompositeFieldContainer[RouteTarget]
    export_targets: _containers.RepeatedCompositeFieldContainer[RouteTarget]
    def __init__(self, name: _Optional[str] = ..., rd: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., enforce_unique: bool = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ..., import_targets: _Optional[_Iterable[_Union[RouteTarget, _Mapping]]] = ..., export_targets: _Optional[_Iterable[_Union[RouteTarget, _Mapping]]] = ...) -> None: ...

class VirtualChassis(_message.Message):
    __slots__ = ("name", "domain", "master", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MASTER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain: str
    master: Device
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., domain: _Optional[str] = ..., master: _Optional[_Union[Device, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VirtualCircuit(_message.Message):
    __slots__ = ("cid", "provider_network", "provider_account", "type", "status", "tenant", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    CID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    cid: str
    provider_network: ProviderNetwork
    provider_account: ProviderAccount
    type: VirtualCircuitType
    status: str
    tenant: Tenant
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, cid: _Optional[str] = ..., provider_network: _Optional[_Union[ProviderNetwork, _Mapping]] = ..., provider_account: _Optional[_Union[ProviderAccount, _Mapping]] = ..., type: _Optional[_Union[VirtualCircuitType, _Mapping]] = ..., status: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VirtualCircuitTermination(_message.Message):
    __slots__ = ("virtual_circuit", "role", "interface", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    VIRTUAL_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    virtual_circuit: VirtualCircuit
    role: str
    interface: Interface
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, virtual_circuit: _Optional[_Union[VirtualCircuit, _Mapping]] = ..., role: _Optional[str] = ..., interface: _Optional[_Union[Interface, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VirtualCircuitType(_message.Message):
    __slots__ = ("name", "slug", "color", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    color: str
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., color: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VirtualDeviceContext(_message.Message):
    __slots__ = ("name", "device", "identifier", "tenant", "primary_ip4", "primary_ip6", "status", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IP4_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IP6_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    device: Device
    identifier: int
    tenant: Tenant
    primary_ip4: IPAddress
    primary_ip6: IPAddress
    status: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., device: _Optional[_Union[Device, _Mapping]] = ..., identifier: _Optional[int] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., primary_ip4: _Optional[_Union[IPAddress, _Mapping]] = ..., primary_ip6: _Optional[_Union[IPAddress, _Mapping]] = ..., status: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VirtualDisk(_message.Message):
    __slots__ = ("virtual_machine", "name", "description", "size", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    virtual_machine: VirtualMachine
    name: str
    description: str
    size: int
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., size: _Optional[int] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class VirtualMachine(_message.Message):
    __slots__ = ("name", "status", "site", "cluster", "device", "serial", "role", "tenant", "platform", "primary_ip4", "primary_ip6", "vcpus", "memory", "disk", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IP4_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IP6_FIELD_NUMBER: _ClassVar[int]
    VCPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: str
    site: Site
    cluster: Cluster
    device: Device
    serial: str
    role: DeviceRole
    tenant: Tenant
    platform: Platform
    primary_ip4: IPAddress
    primary_ip6: IPAddress
    vcpus: float
    memory: int
    disk: int
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., status: _Optional[str] = ..., site: _Optional[_Union[Site, _Mapping]] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., device: _Optional[_Union[Device, _Mapping]] = ..., serial: _Optional[str] = ..., role: _Optional[_Union[DeviceRole, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., platform: _Optional[_Union[Platform, _Mapping]] = ..., primary_ip4: _Optional[_Union[IPAddress, _Mapping]] = ..., primary_ip6: _Optional[_Union[IPAddress, _Mapping]] = ..., vcpus: _Optional[float] = ..., memory: _Optional[int] = ..., disk: _Optional[int] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class WirelessLAN(_message.Message):
    __slots__ = ("ssid", "description", "group", "status", "vlan", "scope_location", "scope_region", "scope_site", "scope_site_group", "tenant", "auth_type", "auth_cipher", "auth_psk", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    SSID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VLAN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_REGION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SITE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_CIPHER_FIELD_NUMBER: _ClassVar[int]
    AUTH_PSK_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    description: str
    group: WirelessLANGroup
    status: str
    vlan: VLAN
    scope_location: Location
    scope_region: Region
    scope_site: Site
    scope_site_group: SiteGroup
    tenant: Tenant
    auth_type: str
    auth_cipher: str
    auth_psk: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, ssid: _Optional[str] = ..., description: _Optional[str] = ..., group: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., status: _Optional[str] = ..., vlan: _Optional[_Union[VLAN, _Mapping]] = ..., scope_location: _Optional[_Union[Location, _Mapping]] = ..., scope_region: _Optional[_Union[Region, _Mapping]] = ..., scope_site: _Optional[_Union[Site, _Mapping]] = ..., scope_site_group: _Optional[_Union[SiteGroup, _Mapping]] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., auth_type: _Optional[str] = ..., auth_cipher: _Optional[str] = ..., auth_psk: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class WirelessLANGroup(_message.Message):
    __slots__ = ("name", "slug", "parent", "description", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    parent: WirelessLANGroup
    description: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., parent: _Optional[_Union[WirelessLANGroup, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...

class WirelessLink(_message.Message):
    __slots__ = ("interface_a", "interface_b", "ssid", "status", "tenant", "auth_type", "auth_cipher", "auth_psk", "distance", "distance_unit", "description", "comments", "tags", "custom_fields")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomFieldValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue, _Mapping]] = ...) -> None: ...
    INTERFACE_A_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_B_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_CIPHER_FIELD_NUMBER: _ClassVar[int]
    AUTH_PSK_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    interface_a: Interface
    interface_b: Interface
    ssid: str
    status: str
    tenant: Tenant
    auth_type: str
    auth_cipher: str
    auth_psk: str
    distance: float
    distance_unit: str
    description: str
    comments: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    custom_fields: _containers.MessageMap[str, CustomFieldValue]
    def __init__(self, interface_a: _Optional[_Union[Interface, _Mapping]] = ..., interface_b: _Optional[_Union[Interface, _Mapping]] = ..., ssid: _Optional[str] = ..., status: _Optional[str] = ..., tenant: _Optional[_Union[Tenant, _Mapping]] = ..., auth_type: _Optional[str] = ..., auth_cipher: _Optional[str] = ..., auth_psk: _Optional[str] = ..., distance: _Optional[float] = ..., distance_unit: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., custom_fields: _Optional[_Mapping[str, CustomFieldValue]] = ...) -> None: ...
