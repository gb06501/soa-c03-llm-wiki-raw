---
type: Concept
title: Fault tolerance
description: Maps process, Availability Zone, and Region failures to prepared capacity, health, decoupling, and traffic controls.
tags: [soa-c03, domain-2, fault-tolerance, availability, resilience]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.2.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
status: verified
---

# Core model

```text
failure boundary -> redundant dependency and capacity -> health detection -> traffic or work movement -> verification
```

# Failure boundaries

| Failure | Design response |
| --- | --- |
| One process or instance | Multiple targets and health replacement |
| One Availability Zone | Resources and dependencies across AZs |
| One Region | Prepared second Region, protected data, and traffic control |

# Multi-AZ requirements

Multiple subnet selections are not enough. Healthy capacity, network paths, NAT or other egress, database failover, mount targets, and dependencies must survive the same boundary. Remaining capacity must carry expected traffic.

# Service patterns

- Auto Scaling and load balancing for replaceable compute.
- RDS Multi-AZ or Aurora replicas for database instance/AZ failure.
- DynamoDB service HA within a Region and global tables for multi-Region use.
- EFS Standard for Regional shared storage; EBS remains AZ-scoped.
- SQS to decouple producer and consumer failure and absorb backlog.
- Retry, DLQ, and circuit-breaker behavior for transient or repeated failure.
- ARC zonal shift, routing controls, and Region switch move traffic to prepared capacity.

# Evidence and validation

Inspect healthy capacity by AZ, replacement events, target health, database failover/replica state, queue age and DLQ growth, network dependencies, and Route 53 or ARC traffic state.

# Exam traps

- Multi-AZ is not backup or multi-Region DR.
- Aurora multi-AZ storage does not replace healthy DB instances.
- Cross-zone balancing does not create missing capacity.
- One NAT gateway can remain an AZ dependency.
- Retry without backoff can amplify failure.
- ARC does not create the alternate infrastructure.

# Related concepts

- [Fault-tolerance pattern selection](../decision-guides/fault-tolerance-pattern-selection.md)
- [Failure-boundary diagnosis](../playbooks/failure-boundary-diagnosis.md)
- [Disaster recovery](disaster-recovery.md)

# Sources

- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
