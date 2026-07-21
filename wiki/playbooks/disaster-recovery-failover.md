---
type: Troubleshooting Playbook
title: Disaster-recovery failover
description: Runs and diagnoses multi-Region recovery from declaration through validation, traffic shift, and failback.
tags: [soa-c03, domain-2, disaster-recovery, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.4"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Trigger

A Region-level event requires recovery, a DR test begins, or the recovery environment fails deployment, promotion, validation, or traffic cutover.

# Evidence path

1. Declare scope, write authority, target RPO/RTO, and approved runbook version.
2. Inspect recovery-point age, copy status, or replication lag.
3. Verify infrastructure definitions, artifacts, IAM, quotas, IPs, keys, secrets, certificates, and dependencies.
4. Restore or promote data with split-brain protection.
5. Deploy or scale compute and consumers.
6. Validate data point, capacity, queues, security, monitoring, backup, and user functions.
7. Inspect Route 53, Global Accelerator, or ARC health and traffic state.
8. Shift traffic with rollback available.
9. Record the complete timeline and prepare failback synchronization.

# Failure map

| Symptom | Direction |
| --- | --- |
| Recovery stack will not deploy | IAM, quota, Region parameter, dependency/artifact |
| Data too old | Backup/copy schedule or replication lag |
| Replica cannot promote | State, lag, write authority, engine procedure |
| Cannot decrypt | Recovery key/policy/grant |
| Internal tests pass; users fail | Traffic, health, certificate, TTL/cache |
| Warm standby overloads | Scale-up, quota, insufficient baseline |
| Both Regions accept unsafe writes | Split-brain/traffic-control failure |
| Failback risks data loss | Reverse synchronization incomplete |

# Safe action

Do not shift production traffic until data authority and validation are clear. Preserve the last good recovery copy, use guarded controls, and stop if recovery would create conflicting writes.

# Verification

Confirm correct data, expected capacity, queues and consumers, security controls, alarms/logs/backups, real user traffic, achieved RPO/RTO, stable operation, and a tested failback path.

# Sources

- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
