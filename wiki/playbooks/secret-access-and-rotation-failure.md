---
type: Troubleshooting Playbook
title: Secret access and rotation failure
description: Diagnoses workload identity, secret and key policy, endpoint, version-label, target-system, and rotation-step failures.
tags: ["soa-c03", "domain-4", "troubleshooting", "secrets-manager", "parameter-store"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---

# Trigger

A workload cannot retrieve a secret or parameter, receives the wrong version, or secret rotation fails or breaks application connectivity.

# Evidence path

1. Record workload role/session, secret or parameter ARN/name, Region, account, version/label, network path, and exact error.
2. Inspect CloudTrail retrieval and KMS events.
3. Evaluate identity policy, secret resource policy, KMS key policy, SCP, and endpoint policy.
4. Verify endpoint DNS, routes, security groups, and private API reachability.
5. For Secrets Manager, inspect versions and staging labels.
6. Inspect rotation Lambda permissions, network access, logs, and the create/set/test/finish step that failed.
7. Verify target-system credential state and application cache/injection behavior.
8. For Parameter Store, verify type, decryption request, version/label, and explicit rotation ownership.

# Failure map

| Symptom | Direction |
| --- | --- |
| Resource not found | Region/account/name/version |
| Access denied | identity/resource/KMS/endpoint policy |
| Timeout | VPC/DNS/endpoint/NAT or target database path |
| AWSCURRENT wrong | staging-label transition or partial rotation |
| New secret tests, app fails | consumer cache/injection/connection pool |
| Rotation repeats or corrupts state | non-idempotent rotation step |
| SecureString fails only with decrypt | KMS policy/key state |

# Safe action

Stop repeated rotation when target state is uncertain. Restore a known-good label or credential, correct the proven policy/network/step issue, and rerun one idempotent rotation with monitoring.

# Verification

Retrieve as the real workload, establish a fresh target-system connection with the current value, confirm unauthorized retrieval fails, inspect audit evidence, and verify previous-version rollback behavior.

# Rollback

Move the current label back to the last known-good version or restore the prior target credential through the owned procedure; invalidate the failed pending value.

# Escalation

Provide resource ARN, version labels, workload role, KMS key, endpoint path, failing rotation step, target state, and rollback option.

# Related pages

- [Secrets management](../services/secrets-management.md)
- [Secrets storage selection](../decision-guides/secrets-storage-selection.md)

# Sources

- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
