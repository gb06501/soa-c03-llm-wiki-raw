---
type: AWS Service
title: Secrets Manager
service_id: secrets-manager
description: Stores, versions, retrieves, and rotates application secrets under controlled access.
tags: ["soa-c03", "domain-4", "secrets-manager", "secrets"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.2", "4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---
# Core model

A secret contains encrypted versioned values. Staging labels such as `AWSCURRENT` and `AWSPREVIOUS` point to versions and provide a controlled cutover mechanism.

# Rotation lifecycle

1. `createSecret` creates the pending value.
2. `setSecret` installs it in the target system.
3. `testSecret` proves the new credential works.
4. `finishSecret` moves the current label.

Rotation must be idempotent because retries can repeat steps.

# Access path

Retrieval can depend on identity policy, secret resource policy, KMS key policy, VPC endpoint policy, Region and account, version label, and network reachability. Cross-account access requires coordinated secret and key authorization.

# Decision boundaries

Use Secrets Manager when managed rotation and secret-specific lifecycle are required. Use Parameter Store for hierarchical configuration and SecureString values when managed rotation is not required.

# Safe operations

Retrieve at runtime with a workload identity, cache for a bounded period, avoid logs and environment leakage, use private endpoints where needed, monitor retrieval and policy changes, and test rollback to the previous version.

# Related decisions

- [Secrets storage selection](../decision-guides/secrets-storage-selection.md)
- [Secret access and rotation failure](../playbooks/secret-access-and-rotation-failure.md)

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
