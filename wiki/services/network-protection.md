---
type: Concept
title: Network protection
description: Separates DNS, web-request, DDoS, and routed-packet protections and audits association, priority, action, logging, and bypass.
tags: ["soa-c03", "domain-5", "network-protection", "firewall"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
status: verified
---

# Layer model

| Traffic question | Control |
| --- | --- |
| Which DNS domains may resolve? | Route 53 Resolver DNS Firewall |
| Which HTTP/HTTPS requests may pass? | WAF |
| How is DDoS risk mitigated? | Shield |
| Which routed VPC flows may pass? | Network Firewall |
| Which ENI ports are allowed? | Security groups |
| Which subnet CIDRs are allowed/denied? | NACLs |

# Audit model

For every control ask: enabled, associated with the exact resource/VPC, actually on the traffic path, winning rule/action, default behavior, logs/metrics, exceptions, alternate bypass, IPv4/IPv6 and AZ/Region coverage.

# Enforcement lifecycle

Inventory and associate, enable evidence, start in ALERT/COUNT where supported, tune narrow exceptions, enforce BLOCK/DROP, monitor business and attack outcomes, test bypass paths, and retain rollback.

# Related pages

- [WAF](waf.md)
- [Shield](shield.md)
- [Network Firewall](network-firewall.md)
- [Network protection selection](../decision-guides/network-protection-selection.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
