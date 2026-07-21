---
type: Decision Guide
title: RDS performance remediation
description: Selects RDS remediation from resource metrics, database load, waits, SQL, storage, and connection evidence.
tags: [soa-c03, domain-1, rds, database, remediation]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.2.1", "1.3.1", "1.3.5"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
status: verified
---

# Decision table

| Dominant evidence | Direction |
| --- | --- |
| CPU pressure with expensive SQL | Tune SQL or indexes; resize only when compute remains the constraint |
| Database load dominated by I/O waits | Investigate access pattern and storage performance |
| Lock waits | Correct transaction or contention behavior |
| Low free storage | Increase allocation or configure safe storage autoscaling |
| Storage IOPS or throughput ceiling | Adjust storage type, IOPS, or throughput |
| Connection bursts or excessive connection overhead | Pool and reuse; use RDS Proxy where supported |
| Read-heavy workload requiring read capacity | Add an appropriate read-scaling mechanism |
| OS-level process or memory question | Enhanced Monitoring |
| DB load, waits, SQL, user, or host question | Performance Insights or CloudWatch Database Insights |
| Parameter change | Apply the correct parameter group and account for dynamic or reboot-required behavior |

# Rejection rules

- High database latency does not require high average CPU.
- A larger instance does not remove lock contention or inefficient SQL automatically.
- RDS Proxy does not cache query results or add database CPU.
- Multi-AZ is primarily an availability choice, not the primary read-scaling mechanism.
- Storage autoscaling grows storage; it does not automatically shrink it.
- Adding application capacity can intensify database pressure.

# Evidence and verification

Baseline application latency and errors, CloudWatch metrics, Enhanced Monitoring where needed, database load, waits, SQL, connections, and storage. Make one targeted change, then verify workload recovery and cost.

# Related concepts

- [RDS performance](../services/rds-performance.md)
- [Evidence-to-remediation loop](../concepts/evidence-to-remediation-loop.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
