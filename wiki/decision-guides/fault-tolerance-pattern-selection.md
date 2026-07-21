---
type: Decision Guide
title: Fault-tolerance pattern selection
description: Selects redundancy, decoupling, and traffic controls from the required failure boundary.
tags: [soa-c03, domain-2, fault-tolerance, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.2.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
status: verified
---

# Decision table

| Requirement | Pattern |
| --- | --- |
| Survive one process or instance | Multiple healthy targets plus replacement |
| Survive one AZ | Multi-AZ compute and dependencies with enough remaining capacity |
| Survive one Region | Prepared second Region plus data and traffic recovery |
| Absorb producer/consumer timing differences | SQS queue |
| Isolate repeatedly failing messages | DLQ |
| Retry transient work | Bounded retry with backoff |
| Stop hammering a failed dependency | Circuit-breaker pattern |
| Shift supported traffic away from an impaired AZ | ARC zonal shift |
| Guard operator-controlled endpoint switching | ARC routing controls and safety rules |
| Orchestrate multi-Region recovery traffic | ARC Region switch |
| RDS automatic AZ failover | Multi-AZ |
| Normal database read scaling | Read replica, not Multi-AZ standby |

# Rejection rules

- Multiple configured AZs do not prove capacity is running in each.
- Cross-zone balancing does not repair an empty or failed AZ.
- A snapshot is recovery data, not live failover capacity.
- A read replica is not identical to a synchronous Multi-AZ standby.
- One Regional traffic control does not copy or validate data.
- A queue does not remove the need to scale or repair consumers.

# Evidence and verification

Test the intended boundary. Verify surviving capacity, every network and data dependency, health-driven removal, backlog recovery, application reconnection, and traffic-control state.

# Related concepts

- [Fault tolerance](../concepts/fault-tolerance.md)
- [Failure-boundary diagnosis](../playbooks/failure-boundary-diagnosis.md)

# Sources

- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
