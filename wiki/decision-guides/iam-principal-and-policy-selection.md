---
type: Decision Guide
title: IAM principal and policy selection
description: Chooses the correct identity, temporary-credential path, and policy location for workforce, workload, service, and cross-account access.
tags: ["soa-c03", "domain-4", "iam", "least-privilege"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
status: verified
---

# Decision table

| Need | Principal or policy choice |
| --- | --- |
| Workforce across many accounts | IAM Identity Center user/group assignment and permission set |
| Application on EC2, Lambda, ECS, or EKS | workload role with temporary credentials |
| One account accesses another | target-account role and explicit trust |
| AWS service acts for a workload | service role plus narrowly scoped `iam:PassRole` |
| Resource supports cross-account grants | resource policy naming the intended principal |
| Cap delegated identity administration | permissions boundary |
| Cap an assumed session | session policy |
| Cap member-account permissions broadly | SCP |
| Context-aware control | policy condition or principal/resource tags |
| Emergency privileged path | protected, monitored break-glass role |

# Rejection rules

- Avoid long-lived access keys when a role or federation path exists.
- A group cannot be assumed and cannot contain roles.
- Trust permits assumption; it does not grant workload actions.
- A boundary or SCP limits permission; it does not grant it.
- A resource policy is not supported uniformly across services.
- ABAC requires governed tag keys, values, and mutation permissions.

# Verification

Observe the actual session ARN, execute required actions, confirm nearby resources/actions remain denied, validate policy findings, and review last-accessed evidence after an appropriate observation window.

# Related pages

- [IAM access control](../services/iam-access-control.md)
- [IAM](../services/iam.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
