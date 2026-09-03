# Diode Python SDK - Entity Examples

Source: NetBox v4.7.0
Generated: 2026-09-02 20:52:39Z

## Prerequisites

- Python 3.10 or later
- Diode SDK for Python

## Installation

```bash
pip install netboxlabs-diode-sdk
```

## Configuration

Each example uses constants for configuration. You can modify these in the example code:

```python
TARGET = "grpc://localhost:8080/diode"
CLIENT_ID = "diode"
CLIENT_SECRET = "changeme"
```

## Quick Start

Each entity example is a standalone Python file. To run an example:

```bash
python examples/device.py
```

## Example Patterns

Each example module includes three pattern functions:

- **minimal**: Only required fields (using flat string references)
- **extended**: Required fields plus common optional fields
- **explicit**: Fully nested objects with all common fields

Switch between patterns by uncommenting the desired function call in `main()`.

## Available Entity Examples

### Circuits

- [Circuit](examples/circuit.py)
- [CircuitGroup](examples/circuit_group.py)
- [CircuitGroupAssignment](examples/circuit_group_assignment.py)
- [CircuitTermination](examples/circuit_termination.py)
- [CircuitType](examples/circuit_type.py)
- [Provider](examples/provider.py)
- [ProviderAccount](examples/provider_account.py)
- [ProviderNetwork](examples/provider_network.py)
- [VirtualCircuit](examples/virtual_circuit.py)
- [VirtualCircuitTermination](examples/virtual_circuit_termination.py)
- [VirtualCircuitType](examples/virtual_circuit_type.py)

### DCIM

- [Cable](examples/cable.py)
- [CablePath](examples/cable_path.py)
- [CableTermination](examples/cable_termination.py)
- [ConsolePort](examples/console_port.py)
- [ConsoleServerPort](examples/console_server_port.py)
- [Device](examples/device.py)
- [DeviceBay](examples/device_bay.py)
- [DeviceRole](examples/device_role.py)
- [DeviceType](examples/device_type.py)
- [FrontPort](examples/front_port.py)
- [Interface](examples/interface_example.py)
- [InventoryItem](examples/inventory_item.py)
- [InventoryItemRole](examples/inventory_item_role.py)
- [Location](examples/location.py)
- [Manufacturer](examples/manufacturer.py)
- [Module](examples/module.py)
- [ModuleBay](examples/module_bay.py)
- [ModuleType](examples/module_type.py)
- [ModuleTypeProfile](examples/module_type_profile.py)
- [Platform](examples/platform.py)
- [PowerFeed](examples/power_feed.py)
- [PowerOutlet](examples/power_outlet.py)
- [PowerPanel](examples/power_panel.py)
- [PowerPort](examples/power_port.py)
- [Rack](examples/rack.py)
- [RackReservation](examples/rack_reservation.py)
- [RackRole](examples/rack_role.py)
- [RackType](examples/rack_type.py)
- [RearPort](examples/rear_port.py)
- [Region](examples/region.py)
- [Site](examples/site.py)
- [SiteGroup](examples/site_group.py)
- [VirtualChassis](examples/virtual_chassis.py)
- [VirtualDeviceContext](examples/virtual_device_context.py)

### Extras

- [CustomField](examples/custom_field.py)
- [CustomFieldChoiceSet](examples/custom_field_choice_set.py)
- [CustomLink](examples/custom_link.py)
- [JournalEntry](examples/journal_entry.py)
- [Tag](examples/tag.py)

### IPAM

- [ASN](examples/asn.py)
- [ASNRange](examples/asn_range.py)
- [Aggregate](examples/aggregate.py)
- [FHRPGroup](examples/fhrp_group.py)
- [FHRPGroupAssignment](examples/fhrp_group_assignment.py)
- [IPAddress](examples/ip_address.py)
- [IPRange](examples/ip_range.py)
- [MACAddress](examples/mac_address.py)
- [Prefix](examples/prefix.py)
- [RIR](examples/rir.py)
- [Role](examples/role.py)
- [RouteTarget](examples/route_target.py)
- [Service](examples/service.py)
- [VLAN](examples/vlan.py)
- [VLANGroup](examples/vlan_group.py)
- [VLANTranslationPolicy](examples/vlan_translation_policy.py)
- [VLANTranslationRule](examples/vlan_translation_rule.py)
- [VRF](examples/vrf.py)

### Other

- [CableBundle](examples/cable_bundle.py)
- [CoolingFeed](examples/cooling_feed.py)
- [CoolingIntake](examples/cooling_intake.py)
- [CoolingOutflow](examples/cooling_outflow.py)
- [CoolingSource](examples/cooling_source.py)
- [DeviceConfig](examples/device_config.py)
- [ModuleBayType](examples/module_bay_type.py)
- [RackGroup](examples/rack_group.py)
- [ScriptModule](examples/script_module.py)
- [VirtualMachineType](examples/virtual_machine_type.py)

### Tenancy

- [Contact](examples/contact.py)
- [ContactAssignment](examples/contact_assignment.py)
- [ContactGroup](examples/contact_group.py)
- [ContactRole](examples/contact_role.py)
- [Owner](examples/owner.py)
- [OwnerGroup](examples/owner_group.py)
- [Tenant](examples/tenant.py)
- [TenantGroup](examples/tenant_group.py)

### VPN

- [IKEPolicy](examples/ike_policy.py)
- [IKEProposal](examples/ike_proposal.py)
- [IPSecPolicy](examples/ip_sec_policy.py)
- [IPSecProfile](examples/ip_sec_profile.py)
- [IPSecProposal](examples/ip_sec_proposal.py)
- [L2VPN](examples/l2vpn.py)
- [L2VPNTermination](examples/l2vpn_termination.py)
- [Tunnel](examples/tunnel.py)
- [TunnelGroup](examples/tunnel_group.py)
- [TunnelTermination](examples/tunnel_termination.py)

### Virtualization

- [Cluster](examples/cluster.py)
- [ClusterGroup](examples/cluster_group.py)
- [ClusterType](examples/cluster_type.py)
- [VMInterface](examples/vm_interface.py)
- [VirtualDisk](examples/virtual_disk.py)
- [VirtualMachine](examples/virtual_machine.py)

### Wireless

- [WirelessLAN](examples/wireless_lan.py)
- [WirelessLANGroup](examples/wireless_lan_group.py)
- [WirelessLink](examples/wireless_link.py)
