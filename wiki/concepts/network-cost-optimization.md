---
type: Concept
title: Network cost optimization
description: Maps billed usage to concrete traffic hops and removes only paths that preserve availability, security, and performance.
tags: ["soa-c03", "domain-5", "network-cost", "optimization"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
status: verified
---

# Core model

`network cost = fixed resources + processed bytes + boundary transfer + priced requests/connections`

The useful question is: which proven hop can be removed, shortened, cached, or replaced?

# Charged-path model

| Driver | Evidence and common correction |
| --- | --- |
| NAT processing | NAT metrics/usage plus Flow Logs; use supported gateway endpoints or same-AZ paths |
| Interface endpoints | endpoint hours/AZ and bytes; compare service volume with NAT |
| Cross-AZ | ENI/AZ and byte evidence; align producer, middlebox, and consumer |
| TGW/firewall/PrivateLink | attachment/endpoint/processed bytes; preserve segmentation and inspection |
| Cross-Region/internet | usage type and geography; cache or relocate where requirements allow |
| Public IPv4 | allocation inventory and owners; use private/edge/LB patterns |
| Logs | ingestion/storage/query volume; filter and lifecycle without losing required evidence |

# Optimization loop

Use Cost Explorer for trend, CUR/Athena for line items, Flow Logs for traffic, and service metrics for component behavior. Baseline cost and health, test one workload/AZ, verify bytes and latency early, then confirm billing after data lag.

# Safety invariant

A cheaper architecture that removes resilience, required inspection, private isolation, or audit evidence is not an optimization.

# Related pages

- [Cost Explorer](../services/cost-explorer.md)
- [Network cost optimization guide](../decision-guides/network-cost-optimization.md)
- [Network cost anomaly](../playbooks/network-cost-anomaly.md)

# Sources

- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
