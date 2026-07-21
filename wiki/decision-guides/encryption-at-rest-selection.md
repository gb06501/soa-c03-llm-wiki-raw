---
type: Decision Guide
title: Encryption at rest selection
description: Chooses key ownership and service encryption patterns while preserving migration, backup, restore, and operational access.
tags: ["soa-c03", "domain-4", "kms", "encryption-at-rest"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Default service protection with minimal key operations | service-owned or service-managed key |
| Direct key policy, audit, lifecycle, or separation control | customer managed KMS key |
| Cross-account encrypted resource workflow | customer managed key with both-account authorization |
| Multi-Region cryptographic identity is explicitly required | evaluate multi-Region KMS keys and service behavior |
| Existing unencrypted resource cannot change in place | create/copy/restore, verify, cut over |
| Service must use key only through its integration | key-policy conditions such as `kms:ViaService` |
| Bind ciphertext use to non-secret context | encryption-context condition |

# Service boundary table

| Service family | Key operational question |
| --- | --- |
| S3 | object copy, replication, bucket policy, and default encryption |
| EBS | volume/snapshot copy and instance permission |
| RDS/Aurora | creation-time choice and encrypted snapshot restore |
| DynamoDB | table key and service access |
| EFS/FSx | creation-time key and client path |
| Backup | vault/recovery-point key and restore principal |
| SNS/SQS/Logs | producer, consumer, and service access to the key |

# Rejection rules

- A customer managed key is not automatically “more secure” without correct policy and operations.
- Rotation does not re-encrypt all historical data.
- Alias changes do not alter the key ID stored with existing ciphertext.
- An IAM allow alone may not satisfy the key policy.
- Do not delete a key to fix an access problem.

# Verification

Encrypt, decrypt, backup, copy or replicate where required, restore, and exercise the workload through the intended identity and Region before retiring the old path.

# Related pages

- [KMS](../services/kms.md)
- [KMS encryption at rest](../services/kms-encryption-at-rest.md)

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
