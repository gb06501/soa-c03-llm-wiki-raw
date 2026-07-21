---
type: AWS Feature
title: Gateway Load Balancer
parent_services: [Elastic Load Balancing]
description: Distributes transparent network-appliance traffic through Gateway Load Balancer endpoints while preserving symmetric paths.
tags: ["soa-c03", "domain-5", "gateway-load-balancer", "appliances"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.1.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
status: verified
---

# Core model

`source route -> Gateway Load Balancer endpoint -> Gateway Load Balancer -> healthy virtual appliance -> return through compatible endpoint path`

The endpoint inserts an appliance service; it does not create full network adjacency.

# Evidence and diagnosis

Inspect endpoint and endpoint-service state, subnets/AZs, route targets, appliance target health, listener/protocol support, appliance routes and source/destination check, symmetric return path, and Flow Logs.

# Decision boundaries

Use Gateway Load Balancer for scalable transparent appliance fleets. Use Network Firewall when its managed inspection capabilities fit without third-party appliances.

# Safe operations

Deploy healthy appliances in required AZs, insert one path, prove symmetry and failover, monitor target and flow health, then expand and remove bypass routes.

# Related pages

- [Network protection selection](../decision-guides/network-protection-selection.md)
- [Network protection gap](../playbooks/network-protection-gap.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
