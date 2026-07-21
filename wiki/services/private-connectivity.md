---
type: Concept
title: Private connectivity
description: Chooses service-specific endpoints or routed network connectivity from exposure, topology, DNS, policy, scale, and cost requirements.
tags: ["soa-c03", "domain-5", "private-connectivity", "routing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
status: verified
---

# Core distinction

`endpoint/PrivateLink = private service access`

`peering/TGW/VPN/Direct Connect = network routing`

# Selection map

| Need | Direction |
| --- | --- |
| S3/DynamoDB from a VPC | gateway endpoint |
| Supported service API through ENIs | interface endpoint |
| One producer service to consumers | PrivateLink |
| Few direct VPC pairs | peering |
| Many VPC/hybrid networks | Transit Gateway |
| Encrypted internet hybrid path | Site-to-Site VPN |
| Dedicated private hybrid capacity | Direct Connect |
| Individual remote users | Client VPN |
| Transparent appliance service | Gateway Load Balancer endpoint |

# Path requirements

Private connectivity still depends on DNS, endpoint/attachment state, forward and return routes, SG/NACL/firewall, endpoint/resource/IAM/KMS policies, and target health.

# Related pages

- [PrivateLink](privatelink.md)
- [Transit Gateway](transit-gateway.md)
- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
