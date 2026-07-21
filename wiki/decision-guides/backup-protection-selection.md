---
type: Decision Guide
title: Backup protection selection
description: Selects periodic, continuous, copied, locked, native, or centralized backup controls from recovery requirements.
tags: [soa-c03, domain-2, backup, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Recover only at scheduled points | Periodic snapshot or backup |
| Fine-grained point-in-time recovery | Continuous backup/PITR where supported |
| Protect against Region loss | Cross-Region copy |
| Isolate recovery points from the source account | Cross-account copy and destination policy |
| Enforce retention against deletion | Vault Lock or service-specific immutable protection |
| Centralize supported resource policies | AWS Backup |
| Prove recovery works within RTO | Restore testing |
| EC2 launchable machine recovery | AMI and underlying EBS snapshots |
| RDS/Aurora time-based restore | Automated backups/PITR |
| DynamoDB fine-grained restore point | PITR |
| Fast S3 object-version recovery | Versioning, with other protection as required |

# Rejection rules

- A plan without resource assignment is not protection.
- A vault alone does not create backups.
- A lifecycle transition does not create a second recovery copy.
- S3 versioning is not identical to an AWS Backup recovery point.
- A snapshot may not contain every surrounding application dependency.
- Do not infer restore success from backup-job success.

# Evidence and verification

Confirm plan, rule, assignment, job, recovery point, copy destination, retention, KMS access, and restore-test result. Measure restored application behavior, not only job completion.

# Related concepts

- [AWS Backup](../services/aws-backup.md)
- [Backup job failure](../playbooks/backup-job-failure.md)

# Sources

- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
