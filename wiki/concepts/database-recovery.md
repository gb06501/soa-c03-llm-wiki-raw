---
type: Concept
title: Database recovery
description: Connects RPO, RTO, restore point, resource recreation, cutover, and validation for RDS, Aurora, and DynamoDB.
tags: [soa-c03, domain-2, database, recovery, rto, rpo]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
status: verified
---

# Core model

```text
RPO selects acceptable recovery point
RTO measures restore + configuration + validation + cutover + warm-up
```

Snapshot restore and PITR normally create a new resource. Recovery is incomplete until applications use it and service controls are restored.

# Restore choices

| Need | Choice |
| --- | --- |
| Exact saved point | Snapshot or selected recovery point |
| Chosen time before corruption | PITR within retention |
| Central vault recovery | AWS Backup recovery point |
| Prove a backup is usable | Restore test |
| Near-zero outage objective | Prepared HA/replication design, not ordinary restore alone |

# Resource-specific behavior

- RDS/Aurora restore creates new endpoint and requires network, parameter, capacity, backup, and HA configuration review.
- Aurora restore creates a cluster and still needs healthy DB instance capacity.
- DynamoDB restore creates a new table and may require streams, mappings, IAM ARN, TTL, alarms, scaling, and replication to be rebuilt.
- Cross-account or Region recovery requires access, copy/share, KMS, and destination configuration.

# Validation

Verify the intended data point, key records, application reads/writes, capacity, security path, alarms/logs/backups, HA/replication, measured data loss, and complete recovery time.

# Exam traps

- RPO is allowable data loss; RTO is allowable downtime.
- Restore completion is not application recovery.
- Multi-AZ failover is not a restore method.
- Lower RPO and lower RTO require different controls.
- A new endpoint/name/ARN must be reflected in application dependencies.

# Related concepts

- [Database restore selection](../decision-guides/database-restore-selection.md)
- [Database restore and cutover](../playbooks/database-restore-and-cutover.md)
- [Disaster recovery](disaster-recovery.md)

# Sources

- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
