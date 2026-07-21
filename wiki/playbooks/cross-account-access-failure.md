---
type: Troubleshooting Playbook
title: Cross-account access failure
description: Diagnoses role assumption, resource-policy, SCP, KMS, endpoint, and delegated-administration failures across accounts.
tags: ["soa-c03", "domain-4", "troubleshooting", "cross-account", "iam"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
status: verified
---

# Trigger

A principal in one AWS account cannot assume a role, access a shared resource, or use an organization-level delegated service in another account.

# Evidence path

1. Record source and target account, actual principal ARN, target role/resource, action, Region, and path.
2. For role access, inspect the target trust policy and source permission to call AssumeRole.
3. Inspect ExternalId, MFA, source ARN/account, session-tag, and organization conditions.
4. Trace SCP inheritance in both relevant accounts.
5. For resource-policy access, inspect the named principal and exact resource ARN.
6. For encrypted data, prove both-account KMS authorization and key Region/state.
7. For private access, inspect VPC endpoint policy and DNS.
8. For delegated administration, verify trusted access, delegated-admin registration, member status, and Region.

# Failure map

| Symptom | Direction |
| --- | --- |
| AssumeRole denied immediately | trust/caller permission/condition/SCP |
| Role assumed, workload action denied | role permission/resource policy/KMS |
| One member account missing | organization membership or service enrollment |
| One Region fails | regional enablement, key, endpoint, or resource identity |
| Shared resource visible but unusable | participant permissions and service-specific access |
| Management account works, delegate fails | trusted access and delegated-admin registration |

# Safe action

Repair the exact half of the cross-account contract that is missing. Do not duplicate broad administrator roles or move workloads into the management account to bypass governance.

# Verification

Use a fresh role session from the intended source, perform the required action in the target, verify CloudTrail in both contexts, and test a disallowed account or resource.

# Rollback

Restore the prior trust/resource policy or assignment and revoke sessions if a change exposed unintended principals.

# Escalation

Include both account IDs, organization/OU path, principal and resource ARNs, CloudTrail events, policy layers, and intended ownership.

# Related pages

- [Organizations](../services/organizations.md)
- [STS](../services/sts.md)

# Sources

- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
