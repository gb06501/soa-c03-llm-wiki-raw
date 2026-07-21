---
type: Troubleshooting Playbook
title: Network protection gap
description: Finds missing association, bypass, wrong priority/action, logging gaps, and false positives across DNS Firewall, WAF, Shield, and Network Firewall.
tags: ["soa-c03", "domain-5", "troubleshooting", "network-protection", "audit"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
status: verified
---

# Trigger

A protection should block or detect traffic but does not, an expected log is missing, or a new enforcement rule disrupts legitimate traffic.

# Evidence path

1. Identify traffic layer: DNS, HTTP, DDoS, routed packet, ENI, or subnet.
2. Inventory exact resource/VPC association and enabled status.
3. Prove traffic actually traverses the protection.
4. Inspect numeric priority, first terminating rule, default action, and monitor versus enforce action.
5. Validate IPv4/IPv6, AZ, Region, alternate domain/origin, and resolver bypass.
6. Inspect full logs/metrics, delivery destination, permissions, retention, and samples.
7. Correlate CloudTrail changes with error or attack time.
8. Identify the exact false-positive request/query/flow before exception.

# Failure map

| Symptom | Direction |
| --- | --- |
| DNS still resolves | VPC association, priority/action, pattern, client resolver bypass |
| WAF bad request allowed | association/scope, COUNT, priority, default action |
| Legitimate request blocked | terminating rule, labels, managed-rule override |
| Shield Advanced gap | eligible resource not explicitly protected or response setup absent |
| Firewall never logs | route bypass, wrong endpoint/AZ, policy/rule-group absence |
| Stateful intermittent drops | asymmetric forward/return path |
| Policy exists, no effect | no association or traffic-path insertion |
| No logs | logging delivery or uncovered path |

# Safe action

Start new DNS/WAF/firewall logic in ALERT/COUNT where supported, create a narrow reviewed exception, enforce gradually, and never disable the whole control for one false positive.

# Verification

Generate known good and bad traffic, prove the winning rule/action and log, verify workload health, inspect alternate paths, and confirm every required VPC/resource/AZ is covered.

# Rollback

Return the exact rule to monitoring or restore its prior priority/action while keeping unaffected protections active.

# Escalation

Provide resource/path inventory, rule and action evidence, logs, bypass analysis, business owner, and exception scope/expiry.

# Related pages

- [Network protection](../services/network-protection.md)
- [Network protection selection](../decision-guides/network-protection-selection.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
