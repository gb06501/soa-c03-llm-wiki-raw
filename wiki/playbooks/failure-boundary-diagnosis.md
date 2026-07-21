---
type: Troubleshooting Playbook
title: Failure-boundary diagnosis
description: Finds hidden single-instance, single-AZ, and single-Region dependencies in a supposedly fault-tolerant design.
tags: [soa-c03, domain-2, fault-tolerance, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.2.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
status: verified
---

# Trigger

A process, AZ, or Region impairment causes more service loss than the documented resilience design predicts.

# Evidence path

1. Name the failed boundary precisely.
2. Inventory compute, load balancing, database, storage, network, DNS, queue, encryption, and operational dependencies.
3. Count healthy usable capacity on each side of the boundary.
4. Verify traffic and return paths, including private outbound dependencies.
5. Inspect database failover, endpoint use, retry, and cached connections.
6. Inspect queue depth, age, receive count, consumer health, and DLQ.
7. Inspect Route 53 or ARC traffic state and alternate capacity.
8. Compare actual behavior with the tested recovery assumption.

# Failure map

| Symptom | Hidden dependency |
| --- | --- |
| Multi-AZ app fails with one AZ | Capacity, NAT, database, storage, or network remained single-AZ |
| No healthy targets in one AZ | No targets, disabled AZ, health-path failure |
| RDS fails over; app remains down | Endpoint/cache/retry/connection behavior |
| Aurora storage healthy; DB unavailable | No healthy promotable instance |
| Queue backlog grows | Consumers failed, slow, blocked, or cannot scale |
| ARC shift fails | Alternate capacity or routing setup not prepared |

# Safe action

Restore the missing dependency or capacity without directing more traffic into an unprepared location. Bound retries, preserve evidence, and use the documented traffic control.

# Verification

Repeat a controlled boundary test and verify service health, surviving capacity, data correctness, queue recovery, user traffic, alarms, and the absence of a new single point of failure.

# Sources

- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
