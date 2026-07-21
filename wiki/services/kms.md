---
type: AWS Service
title: KMS
service_id: kms
description: Creates and controls cryptographic keys used by AWS services and applications for envelope encryption.
tags: ["soa-c03", "domain-4", "kms", "encryption"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.2", "4.2.1", "4.2.2", "4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---
# Core model

KMS protects data keys under a KMS key. Services commonly use envelope encryption: plaintext is encrypted with a data key, while the encrypted data key is stored with the ciphertext.

# Key control plane

| Object | Purpose |
| --- | --- |
| KMS key | Cryptographic identity with state, origin, and usage |
| Key policy | Primary authorization policy for the key |
| Grant | Delegated, often temporary permission for a principal or service |
| Alias | Mutable friendly reference to a key |
| Encryption context | Non-secret authenticated context that can constrain use |

# Decision boundaries

AWS owned, AWS managed, and customer managed keys provide different control. Symmetric encryption keys fit most AWS service integrations. Multi-Region keys support specific replication designs but do not make ordinary ciphertext globally portable by themselves.

# Access path

A caller can be allowed by IAM yet denied by the key policy, grant, SCP, endpoint policy, key state, Region, or encryption-context condition. Cross-account use requires authorization in both the key-owning and caller accounts.

# Safe operations

Use stable identifiers, narrow key policies, `kms:ViaService` and encryption context where appropriate, monitored rotation, staged disablement, and a waiting period before deletion. Test restore and decrypt paths.

# Related decisions

- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [KMS access failure](../playbooks/kms-access-failure.md)

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
