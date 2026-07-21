---
type: AWS Service
title: Direct Connect
service_id: direct-connect
description: Provides dedicated private connectivity whose physical link, virtual interface, BGP, and routing layers are diagnosed independently.
tags: ["soa-c03", "domain-5", "direct-connect", "hybrid"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.1.4", "5.3.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
status: verified
---
# Core model

`connection -> virtual interface -> BGP session -> learned routes -> forward and return data path`

A physical connection can be up while the virtual interface, BGP session, accepted prefixes, or return route is wrong.

# Key objects

| Object | Purpose |
| --- | --- |
| Connection | Physical hosted or dedicated circuit |
| Virtual interface | Public, private, or transit logical service access |
| BGP peer | Exchanges prefixes with the customer router |
| Direct Connect gateway | Connects supported virtual interfaces to multiple gateways or Regions |
| Link aggregation group | Bundles supported connections |

# Decision boundaries

Use Direct Connect for predictable private capacity and stable hybrid traffic. Use Site-to-Site VPN for faster setup, encrypted internet transport, or backup. Direct Connect is not encrypted merely because it is private.

# Evidence and diagnosis

Check physical state and optics, VIF state, VLAN and peer addresses, ASN, BGP state, advertised/accepted prefixes, route filters, gateway association, VPC/TGW routes, return path, MTU, and customer-device evidence.

# Safe operations

Keep a redundant VPN or separate circuit active, change one path at a time, verify BGP and exact prefixes, test application traffic and failover, then remove the old preference.

# Related decisions

- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
