---
type: AWS Feature
title: Site-to-Site VPN
parent_services: [VPC]
description: Connects a customer network to a virtual or transit gateway through two IPsec tunnels and dynamic or static routing.
tags: ["soa-c03", "domain-5", "vpn", "hybrid"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.1.4", "5.3.1", "5.3.4", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

`customer gateway device -> customer gateway resource -> VPN connection -> tunnel 1/tunnel 2 -> VGW or Transit Gateway -> VPC routes`

Tunnel UP does not prove BGP, prefixes, forward/return routes, security, MTU, or application success.

# Evidence and diagnosis

Separate underlay reachability, IKE phase 1, IPsec phase 2, BGP/static routes, learned/advertised prefixes, route preference, both directions, firewall/NACL, tunnel metrics/logs, and customer-device evidence.

# Safe operations

Keep the healthy tunnel active, repair one tunnel at a time, establish IKE/IPsec/BGP, validate exact prefixes and traffic, restore intended preference, and test failover plus MTU.

# Related pages

- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
