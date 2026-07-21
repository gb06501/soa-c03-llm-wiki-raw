---
type: AWS Service
title: PrivateLink
service_id: privatelink
description: Privately exposes one service through provider endpoint services and consumer interface endpoints without full network adjacency.
tags: ["soa-c03", "domain-5", "privatelink", "private-connectivity"]
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

`consumer interface endpoint -> PrivateLink -> provider endpoint service -> NLB -> healthy targets`

PrivateLink exposes one service, not an entire provider VPC. Provider and consumer CIDRs can overlap because the model does not create routed adjacency.

# Key objects

| Consumer | Provider |
| --- | --- |
| Interface endpoint and ENIs | Endpoint service |
| Endpoint subnets and security groups | Allowed principals and acceptance |
| Private DNS and endpoint policy | NLB listener and healthy targets |

# Decision boundaries

Use PrivateLink for one-way service consumption, overlapping CIDRs, and strong producer/consumer isolation. Use peering or Transit Gateway for general routed network connectivity.

# Evidence and diagnosis

Check service name and Region, endpoint state, provider acceptance, allowed principal, endpoint ENI/subnet/IP capacity, security group, private DNS, endpoint policy, NLB listener/targets, and application/TLS response.

# Safe operations

Create and test endpoint-specific DNS first, verify policy and every required AZ, enable normal private DNS, prove the public/NAT path is no longer used, then retire the legacy route.

# Related decisions

- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
