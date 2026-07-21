---
type: Concept
title: KMS encryption at rest
description: Connects key ownership and policy to service encryption, migration, backup, restore, and failure diagnosis.
tags: ["soa-c03", "domain-4", "kms", "encryption-at-rest"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
status: verified
---
# Core model

Encryption at rest is not only a checkbox. It binds data, ciphertext metadata, a KMS key, the service integration, authorized principals, Region, backup and restore paths, and key lifecycle.

# Decision model

Choose service-owned or managed keys for operational simplicity when policy permits. Choose a customer managed key for direct policy, separation, audit, lifecycle, or cross-account requirements.

# Service patterns

| Workload | Important boundary |
| --- | --- |
| S3 | Default encryption, bucket policy, object copy and replication |
| EBS | Volume/snapshot key and copy permissions |
| RDS/Aurora | Creation-time encryption and encrypted snapshot workflow |
| DynamoDB | Table key selection and service authorization |
| EFS/FSx | Creation-time key and client access layers |
| Backup | Vault and recovery-point encryption plus restore path |
| SNS/SQS/Logs | Publisher/consumer/service access to the key |

# Migration rule

When encryption or key choice cannot be changed in place, use a rehearsed create-copy-verify-cutover-retire sequence. Preserve rollback until data integrity and workload behavior are proven.

# Related pages

- [KMS](kms.md)
- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [KMS access failure](../playbooks/kms-access-failure.md)

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
