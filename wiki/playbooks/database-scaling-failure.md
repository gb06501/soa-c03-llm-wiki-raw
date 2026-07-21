---
type: Troubleshooting Playbook
title: Database scaling failure
description: Diagnoses ineffective or blocked RDS, Aurora, and DynamoDB scaling.
tags: [soa-c03, domain-2, database, scaling, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
status: verified
---

# Trigger

Database latency, throttling, lag, connection pressure, or saturation remains after scaling was configured or attempted.

# Evidence path

1. Separate reads, writes, compute, memory, connections, storage, and key distribution.
2. For RDS/Aurora, inspect DB load, waits, CPU, storage, connections, and replica lag.
3. Verify the application uses the reader or replica endpoint.
4. Check instance, storage, reader, or Serverless minimum/maximum settings.
5. For DynamoDB, compare consumed/provisioned read and write capacity.
6. Inspect table and GSI throttling separately.
7. Test for hot partitions even when total utilization looks low.
8. Confirm DAX client/endpoint and consistency behavior when used.

# Failure map

| Symptom | Direction |
| --- | --- |
| Replica added; writer unchanged | Application routing or write-heavy load |
| Replica data old | Lag and asynchronous replication |
| Aurora readers unused | Writer endpoint still used |
| Serverless saturates | Maximum ACU or workload limit |
| DynamoDB throttles before scale-out | Reactive delay, maximum, sudden spike |
| Low overall use with throttles | Hot partition or index |
| DAX present; writes throttle | Write capacity or partition design |

# Safe action

Correct routing and configuration before adding capacity. Increase limits only after quota/cost review, keep safe baselines for sudden demand, and address hot-key or SQL causes directly.

# Verification

Confirm the intended endpoint receives traffic, lag is acceptable, latency/errors recover, capacity stays within bounds, no table/GSI or partition throttling remains, and cost matches the selected mode.

# Sources

- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
