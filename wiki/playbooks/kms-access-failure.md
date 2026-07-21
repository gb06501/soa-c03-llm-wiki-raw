---
type: Troubleshooting Playbook
title: KMS access failure
description: Diagnoses key-policy, grant, context, state, Region, service-integration, and cross-account encryption failures.
tags: ["soa-c03", "domain-4", "troubleshooting", "kms", "encryption"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
status: verified
---

# Trigger

Encrypt, decrypt, data-key, copy, restore, replication, publish, consume, or log delivery fails with a KMS-related authorization or key-state error.

# Evidence path

1. Record caller/session ARN, KMS key ARN, operation, service resource, account, Region, and exact error.
2. Confirm the key ID—not only alias—and current key state.
3. Inspect CloudTrail KMS and calling-service events.
4. Evaluate the key policy, IAM policy, grants, SCP, and endpoint policy.
5. Check encryption-context and `kms:ViaService` conditions.
6. Confirm the service principal and producer/consumer roles required by the integration.
7. For cross-account access, prove permission in both accounts.
8. For copy, restore, or replication, verify source/destination key and Region behavior.

# Failure map

| Symptom | Direction |
| --- | --- |
| IAM allows, KMS denies | key policy or grant |
| Works directly, fails via service | ViaService/context/service principal |
| Only old ciphertext fails | original key ID/state/Region |
| Cross-account copy fails | source decrypt and destination encrypt grants |
| Queue/topic/log delivery fails | service plus producer/consumer key access |
| Alias points correctly but decrypt fails | ciphertext references key ID, not current alias target |
| Key pending deletion/disabled | lifecycle state |

# Safe action

Correct the narrow key-policy statement, grant, context, or service integration. Cancel accidental deletion or re-enable only after ownership and risk review; never replace evidence with a broad wildcard principal.

# Verification

Exercise encrypt and decrypt or the full service workflow, test backup/restore/copy where required, inspect CloudTrail, and confirm an unauthorized principal remains denied.

# Rollback

Restore the prior key-policy version or service configuration and return traffic to the last proven key path. Preserve the old key until all data paths are verified.

# Escalation

Provide key ARN/state, caller and service principals, events, context, policies/grants, resource ARN, and migration or rollback status.

# Related pages

- [KMS](../services/kms.md)
- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
