---
type: AWS Service
title: Cost Explorer
service_id: cost-explorer
description: Finds cost trends and network usage patterns by service, account, Region, usage type, operation, and ownership dimensions.
tags: ["soa-c03", "domain-5", "cost-explorer", "network-cost"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["5.1.4", "1.3.1"]
domain_ids: ["5", "1"]
sources:
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
status: verified
---
# Core model

Cost Explorer identifies which billed service and usage type changed. It does not by itself explain the packet path that produced the charge.

# Investigation model

1. Select the anomaly time window and baseline.
2. Group by service, account, Region, usage type, operation, and tags.
3. Separate fixed hourly resources from data processing or transfer.
4. Map the billed line to NAT, endpoints, TGW, firewall, load balancer, edge, or public-address paths.
5. Correlate Flow Logs and service metrics for traffic cause.
6. Verify savings after billing data catches up.

# Decision boundaries

Use Cost Explorer for trends and grouped cost exploration. Use Cost and Usage Report for detailed line items and Athena for repeatable queries. Use Flow Logs and CloudWatch to explain traffic.

# Safe operations

Model availability and security requirements before removing a charged path, test one workload/AZ, watch latency/errors/bytes, and delete old resources only after cost and service health are proven.

# Related decisions

- [Network cost optimization](../decision-guides/network-cost-optimization.md)
- [Network cost anomaly](../playbooks/network-cost-anomaly.md)

# Compute optimization evidence

Use Cost Explorer to confirm spend shape and resource-family trends after performance evidence identifies safe candidates. Cost alone does not prove a resource can be downsized without peak, memory, network, storage, availability, or downstream analysis.

# Sources

- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)

