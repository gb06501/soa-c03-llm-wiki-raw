---
type: Decision Guide
title: Network cost optimization
description: Selects a safe network-cost correction from billed service, usage type, topology, traffic volume, and operational requirements.
tags: ["soa-c03", "domain-5", "network-cost", "optimization"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
status: verified
---

# Decision table

| Cost evidence | Candidate correction |
| --- | --- |
| S3/DynamoDB bytes through NAT | gateway endpoint |
| High supported service traffic through NAT | compare interface endpoint by AZ/volume |
| Workload and NAT in different AZs | same-AZ path or justified architecture |
| Many low-volume endpoints | compare fixed endpoint cost with shared NAT |
| Few VPC pairs | compare peering with TGW |
| One producer service to many consumers | compare PrivateLink with routed adjacency |
| Low CloudFront hit ratio/high origin bytes | correct cache key/TTL/compression |
| Public IPv4 inventory | private/LB/edge access pattern |
| High log ingestion/storage | supported filtering, format, retention, lifecycle |
| Cross-Region hairpin | relocate/cache/reroute if residency and resilience allow |

# Rejection rules

- Interface endpoints are not always cheaper.
- Central NAT reduces count but can add cross-AZ cost and dependency.
- Removing one-NAT-per-AZ can weaken resilience.
- Global Accelerator does not cache.
- Savings Plans do not reduce network transfer charges.
- Do not remove security, HA, or required audit evidence for cost alone.

# Verification

Baseline cost and traffic, test one path, verify bytes/latency/errors and redundancy, wait for billing evidence, then remove the old resource and confirm no cost moved to another hop.

# Related pages

- [Network cost optimization concept](../concepts/network-cost-optimization.md)
- [Network cost anomaly](../playbooks/network-cost-anomaly.md)

# Sources

- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
