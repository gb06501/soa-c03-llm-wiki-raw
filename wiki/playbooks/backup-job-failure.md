---
type: Troubleshooting Playbook
title: Backup job failure
description: Diagnoses absent, expired, failed, uncopyable, undeletable, or unrestorable recovery points.
tags: [soa-c03, domain-2, backup, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Trigger

A resource is not protected, a backup/copy job fails or expires, a recovery point cannot be deleted, or a restore cannot decrypt.

# Evidence path

1. Trace plan to rule to resource assignment to vault.
2. Verify ARN/tag/type selection, Region/account, support, and service opt-in.
3. Inspect schedule, start window, and job status/message.
4. Check service role, trust, resource state, and KMS permission.
5. For copy, inspect destination vault policy, key, account/Region support, and copy job.
6. For deletion, inspect retention, Vault Lock, and legal controls.
7. For restore, inspect role, key state, metadata, and dependencies.

# Failure map

| Symptom | Direction |
| --- | --- |
| Never backed up | Assignment, scope, Region, support/opt-in |
| Job never starts | Schedule, window, assignment, role |
| Job expires | Start window, capacity, service condition |
| Backup fails | Job message, role, state, KMS |
| Copy fails | Destination policy/key/support |
| Cannot delete | Vault Lock or retention |
| Restore cannot decrypt | Destination role and key |
| Restore works; app fails | Network, secrets, DNS, parameters, dependencies |

# Safe action

Correct selection or permission without weakening required retention. Do not delete the only usable recovery point; perform a controlled restore test after repair.

# Verification

Confirm a new successful job, expected recovery point and copy, correct retention, successful decrypting restore, application validation, and measured RTO.

# Sources

- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
