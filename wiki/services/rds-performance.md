---
type: AWS Service
title: RDS
service_id: rds
description: Runs managed relational databases with observable compute, connection, storage, query, scaling, and recovery behavior.
tags: [soa-c03, domain-1, rds, database, performance]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.2.1", "1.3.1", "1.3.5", "2.1.3", "2.2.2", "2.3.1", "2.3.2", "2.3.4"]
domain_ids: ["1", "2"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Monitoring layers

| Question | Tool |
| --- | --- |
| CPU, memory, connections, storage, I/O, network, replica lag | CloudWatch metrics |
| OS process, memory, CPU, disk, and load detail | Enhanced Monitoring |
| DB load, waits, SQL, user, and host | Performance Insights or CloudWatch Database Insights |
| Engine error, slow-query, audit, or general logs | RDS logs or CloudWatch Logs export |
| Who changed configuration | CloudTrail |

High database latency does not require high CPU. Start at the application symptom and find the limiting layer.

# Load and wait interpretation

```text
DB load above available vCPU -> database work queues somewhere
```

| Dominant evidence | Direction |
| --- | --- |
| CPU wait | Compute or expensive SQL |
| I/O wait | Storage or query access pattern |
| Lock wait | Transaction contention |
| High connections with low useful work | Pooling, Proxy, or application connection behavior |
| One SQL dominates load | Query/index remediation by the responsible team |

# Targeted remediation

- Compute pressure: change instance class, optimize workload, or add read capacity where reads dominate.
- Storage pressure: increase storage or tune type, IOPS, and throughput.
- Connection bursts: pool and reuse connections; use RDS Proxy where supported.
- Configuration: change the correct parameter group and account for dynamic or reboot-required behavior.
- Replica lag: inspect replica capacity, source write rate, long queries, and engine limits.

RDS Proxy pools connections. It does not cache query results, add DB CPU, fix slow SQL, act as a read replica, or improve storage.

# Safe change path

```text
baseline -> limiting layer -> one targeted change -> impact review
-> apply now or maintenance window -> verify DB load, latency, errors, and cost
```

# Exam traps

- Multi-AZ improves availability; it is not the primary read-scaling mechanism.
- A read replica scales reads asynchronously and can lag.
- Storage autoscaling grows storage; it does not automatically shrink it.
- A larger DB instance does not automatically remove lock contention.
- Enhanced Monitoring and Database Insights observe different layers.

# Related concepts

- [Evidence-to-remediation loop](../concepts/evidence-to-remediation-loop.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)
- [Remediation tool selection](../decision-guides/remediation-tool-selection.md)

# Monitoring layers

CloudWatch shows service-level resource behavior; Enhanced Monitoring shows operating-system detail; database insights show load, waits, SQL, users, and hosts; logs show engine events. Start at the constrained layer.

# Scaling and proxy boundary

Instance class changes compute and memory. Read replicas offload reads and can lag. Storage autoscaling grows space within bounds. RDS Proxy pools connections; it does not add database compute or cache query results.

# Backup, restore, and availability

Multi-AZ is availability, not backup or read scaling. Snapshot and point-in-time restore create a new database identity that requires network, parameter, security, endpoint, monitoring, and application cutover validation.

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)

