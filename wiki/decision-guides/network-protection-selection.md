---
type: Decision Guide
title: Network protection selection
description: Chooses the correct DNS, web, DDoS, routed-packet, ENI, or subnet protection layer.
tags: ["soa-c03", "domain-5", "network-protection", "security"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
status: verified
---

# Decision table

| Threat or control | Select |
| --- | --- |
| Domain-query allow/alert/block | Route 53 Resolver DNS Firewall |
| HTTP/HTTPS fields, rates, managed rules | WAF |
| DDoS baseline and advanced response | Shield |
| Routed VPC packet/session inspection | Network Firewall |
| Transparent third-party appliances | Gateway Load Balancer |
| ENI protocol/port/source allow | security group |
| Subnet CIDR allow/deny | NACL |

# Rejection rules

- DNS Firewall does not block direct IP traffic.
- WAF does not filter arbitrary TCP/UDP.
- WAF COUNT and DNS Firewall ALERT observe but do not block.
- Shield does not replace WAF for application attacks.
- Network Firewall protects only routed-through traffic.
- A policy without association or traffic-path insertion protects nothing.
- A broad early allow/pass can shadow later enforcement.

# Verification

Inventory all VPCs/resources and alternate IPv4/IPv6 paths, prove association/routing, identify the winning priority/action, validate logs/metrics, test a known request/flow, and confirm application health.

# Related pages

- [Network protection](../services/network-protection.md)
- [Network protection gap](../playbooks/network-protection-gap.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
