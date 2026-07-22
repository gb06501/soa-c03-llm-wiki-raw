---
type: AWS Service
title: IAM
service_id: iam
description: Controls AWS identities and permissions through principals, policies, conditions, and explicit evaluation boundaries.
tags: ["soa-c03", "domain-4", "iam", "access-control"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["4.1.1", "4.1.2", "1.2.3", "2.3.1", "2.3.3"]
domain_ids: ["4", "1", "2"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/2.3.3-implement-versioning-for-storage-services.md
status: verified
---
# Core model

IAM answers four questions: who is the principal, which action is requested, which resource is addressed, and which request context applies. Authentication establishes identity; authorization evaluates every applicable policy layer.

# Key objects

| Object | Purpose |
| --- | --- |
| User | Long-lived human or workload identity; prefer federation or roles when possible |
| Group | Shared permissions for IAM users |
| Role | Assumable identity with temporary credentials |
| Identity policy | Grants permissions to a user, group, or role |
| Resource policy | Grants through the resource and can name cross-account principals |
| Permissions boundary | Maximum permissions available to an identity |
| Condition | Restricts a statement by context such as Region, network, tags, or MFA |

# Evaluation boundaries

An explicit deny wins. Otherwise a request needs an applicable allow and must remain inside every limiting layer: permissions boundary, session policy, service control policy, resource policy rules, and service-specific controls.

Trust policy and permissions policy solve different halves of role use: trust permits assumption; permissions authorize actions after assumption. `iam:PassRole` authorizes attaching a role to a service and does not assume it.

# Evidence and diagnosis

Capture the principal ARN, action, resource ARN, account and Region, request context, and exact error. Inspect identity, resource, trust, boundary, session, SCP, endpoint, and KMS policies before changing access. CloudTrail and last-accessed evidence constrain least-privilege changes.

# Safe operations

Prefer temporary credentials, narrow resources, conditions, MFA for privileged paths, tested explicit denies, and an auditable break-glass route. Validate a proposed policy and verify both the intended allow and nearby denied actions.

# Related decisions

- [IAM principal and policy selection](../decision-guides/iam-principal-and-policy-selection.md)
- [Access denied](../playbooks/access-denied.md)

# Operational permission boundaries

Automation, backup, replication, restore, and version recovery each require both caller permissions and service or target resource permissions. A healthy control-plane object does not prove its execution role can perform the data-plane action.

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.3](../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)

