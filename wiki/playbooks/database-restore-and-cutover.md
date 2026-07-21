---
type: Troubleshooting Playbook
title: Database restore and cutover
description: Runs and diagnoses database restore, validation, application cutover, and recovery-time measurement.
tags: [soa-c03, domain-2, database, restore, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
status: verified
---

# Trigger

A database must be recovered, a restore option is unavailable, a restore fails, or the restored resource exists but the application is not recovered.

# Evidence path

1. Record the corruption/failure time and required RPO/RTO.
2. Select a recovery point before the bad event.
3. Verify source retention, snapshot/recovery point, Region/account, and KMS.
4. Supply destination subnet, security, parameter, capacity, and restore metadata.
5. Track restore job and resource readiness.
6. Validate data version and key records before traffic.
7. Rebuild required streams, mappings, scaling, HA, alarms, logs, and backups.
8. Update endpoint consumers: DNS, secrets, proxy, Lambda, ECS/EKS, or application config.
9. Measure the full timeline.

# Failure map

| Symptom | Direction |
| --- | --- |
| PITR unavailable | Backup/PITR enablement and retention |
| Snapshot absent | Region, account, sharing, copy |
| Cannot decrypt | Key state/policy/grant and role |
| RDS network restore fails | Subnet group, VPC, AZ capacity, security |
| Restored DB unused | Endpoint/DNS/secret/proxy/config |
| Aurora cluster unavailable | DB instance, endpoint, parameter/network |
| DynamoDB name conflict | Restore to a new name |
| Job completes; RTO missed | Validation, cutover, DNS, warm-up omitted |

# Safe action

Keep the old and restored resources isolated until data validation passes. Shift traffic deliberately with rollback available and preserve the recovery point.

# Verification

Confirm correct data point, successful reads/writes, expected capacity and latency, security, backups/alarms/logs, HA/replication, application traffic, actual data loss, and complete RTO.

# Sources

- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
