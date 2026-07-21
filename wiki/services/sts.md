---
type: AWS Service
title: STS
service_id: sts
description: Issues temporary credentials for role sessions, federation, and cross-account access.
tags: ["soa-c03", "domain-4", "sts", "temporary-credentials"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.2", "4.1.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
status: verified
---
# Core model

STS exchanges an authenticated caller and an allowed role-assumption path for temporary credentials. The resulting session has its own ARN, duration, session name, tags, and optional session-policy ceiling.

# AssumeRole gates

1. The target role trust policy accepts the caller and required conditions.
2. The caller is permitted to call `sts:AssumeRole` when an identity allow is required.
3. Organization, boundary, and session-policy limits do not deny the path.
4. The resulting role permissions authorize the requested workload action.

# Evidence and diagnosis

Use the exact caller ARN, target role ARN, ExternalId or MFA condition, source account, session tags, and CloudTrail AssumeRole event. Diagnose the role session, not only the base role name.

# Safe operations

Use short, purposeful sessions, distinctive session names, constrained trust principals, ExternalId for third parties where applicable, and session tags for attribute-based controls.

# Related decisions

- [Cross-account access failure](../playbooks/cross-account-access-failure.md)
- [Access denial evidence selection](../decision-guides/access-denial-evidence-selection.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
