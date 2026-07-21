---
type: Decision Guide
title: Secrets storage selection
description: Chooses between Secrets Manager, Parameter Store, and direct KMS use based on lifecycle, rotation, hierarchy, policy, and delivery.
tags: ["soa-c03", "domain-4", "secrets", "parameter-store"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Managed secret rotation and staging labels | Secrets Manager |
| Secret resource policy or cross-account secret sharing | Secrets Manager plus KMS authorization |
| Hierarchical configuration with versions/labels | Systems Manager Parameter Store |
| Encrypted parameter without managed rotation | Parameter Store SecureString |
| Application cryptographic operation, not secret storage | KMS |
| Existing value should remain outside template state | supported dynamic reference and runtime retrieval design |
| Private service API path | VPC endpoint plus endpoint/service/key policies |
| Multi-Region secret availability | explicit replication and regional consumer design |

# Rejection rules

- KMS encrypts data but is not a secret lifecycle store.
- SecureString does not provide managed credential rotation.
- Environment injection can expose secrets and creates refresh limitations.
- A secret resource policy does not satisfy the KMS key policy.
- Rotation completion does not prove every consumer refreshed.

# Verification

Retrieve with the intended workload role and network, rotate to a new version, establish a new application connection, observe audit evidence, reject unauthorized retrieval, and rehearse rollback to the previous version.

# Related pages

- [Secrets management](../services/secrets-management.md)
- [Secrets Manager](../services/secrets-manager.md)

# Sources

- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
