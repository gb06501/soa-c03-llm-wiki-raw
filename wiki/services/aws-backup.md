---
type: AWS Service
title: Backup
service_id: backup
description: Coordinates backup plans, assignments, vaults, copies, recovery points, and restore testing.
tags: [soa-c03, domain-2, aws-backup, backup]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["2.3.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Core model

```text
backup plan -> rule -> resource assignment -> job -> recovery point in vault
                                      -> optional copy -> destination vault
```

A plan without an assignment protects nothing. A vault stores recovery points; it does not schedule jobs.

# Important objects

- Backup plan and rule: schedule, windows, lifecycle, vault, copy, and continuous option where supported.
- Resource assignment: explicit ARNs, tags, type, role, account, and Region scope.
- Vault: access policy, encryption, retention, and optional Vault Lock.
- Jobs: backup, copy, restore, and restore testing.
- Recovery point: restorable resource-specific backup object.

# Protection choices

| Need | Choice |
| --- | --- |
| Recovery at scheduled points | Periodic backup |
| Fine-grained point-in-time recovery | Continuous backup/PITR where supported |
| Region/account isolation | Copy action to destination vault |
| Central policy and reporting | AWS Backup plans and Audit Manager |
| Prove usability and RTO | Restore testing |

Native mechanisms such as EBS snapshots, RDS automated backups, DynamoDB PITR, S3 versioning, and service-specific backups remain relevant.

# Permission and encryption path

Check service role/trust, resource support and opt-in, source and destination vault policies, KMS key state/policy/grant, and cross-account or Region permission.

# Evidence

Use job status/message, copy status, recovery-point inventory, retention/lock state, Audit Manager findings, restore-test result, and measured recovery time.

# Exam traps

- Lifecycle transition is not a vault copy.
- Multi-AZ is not backup.
- Successful source backup does not prove copy success.
- Vault Lock may intentionally prevent deletion.
- Backup success does not prove application consistency or restore time.

# Related concepts

- [Backup protection selection](../decision-guides/backup-protection-selection.md)
- [Backup job failure](../playbooks/backup-job-failure.md)
- [Database recovery](../concepts/database-recovery.md)

# Sources

- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
