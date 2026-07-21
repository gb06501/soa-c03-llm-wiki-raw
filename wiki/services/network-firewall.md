---
type: AWS Service
title: Network Firewall
service_id: network-firewall
description: Inspects routed VPC traffic with stateless and stateful rule groups, policies, per-AZ endpoints, and flow or alert logs.
tags: ["soa-c03", "domain-5", "network-firewall", "network-protection"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3", "5.1.4", "5.3.2", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---
# Core model

`rule groups -> firewall policy -> firewall -> per-AZ endpoint -> route-inserted traffic`

Creating a firewall does not place traffic in its path. Stateful inspection requires compatible forward and return flow through the same stateful path.

# Inspection layers

| Layer | Behavior |
| --- | --- |
| Stateless | Evaluates packets by priority and forwards, passes, or drops |
| Stateful | Tracks sessions and applies pass, drop, alert, reject, or signatures |
| Routing | Steers workload, firewall subnet, NAT/TGW, and return traffic |
| Logging | Records flow and alert evidence at configured destinations |

# Evidence and diagnosis

Map source route table, endpoint ID/AZ, firewall subnet route, next hop, and exact return route. Then inspect policy attachment, default actions, rule order, broad passes, rule-group capacity, logs, and bypass routes.

# Safe operations

Deploy endpoints in required AZs, insert one controlled path, start new rules in alert where possible, confirm symmetric routing and workload behavior, then enforce and expand.

# Related decisions

- [Network protection selection](../decision-guides/network-protection-selection.md)
- [Network protection gap](../playbooks/network-protection-gap.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
