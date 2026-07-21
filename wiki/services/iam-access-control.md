---
type: Concept
title: IAM access control
description: Connects workforce identity, workload roles, policy types, temporary sessions, and evidence-led least privilege.
tags: ["soa-c03", "domain-4", "iam", "access-control"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
status: verified
---
# Core model

Access design starts with principal lifecycle, then chooses the policy location and limiting boundaries. Human, workload, AWS service, and external-account principals have different credential and trust requirements.

# Principal map

| Need | Preferred direction |
| --- | --- |
| Workforce across accounts | IAM Identity Center federation and permission sets |
| AWS workload | Service role or task/function/instance role |
| Cross-account workload | Target role with explicit trust and scoped permissions |
| AWS service acting for workload | Service role plus controlled `iam:PassRole` |
| Emergency administration | Protected, monitored break-glass role |

# Policy map

Identity policy follows the principal. Resource policy is valuable for resources with supported policies and cross-account grants. Trust policy controls role assumption. Boundaries, session policies, and SCPs limit permissions; they do not grant them.

# Operational loop

Design least privilege, validate policy, deploy in limited scope, observe CloudTrail and last-accessed evidence, narrow permissions, and verify both intended success and expected denial.

# Related pages

- [IAM](iam.md)
- [IAM Identity Center](iam-identity-center.md)
- [STS](sts.md)
- [IAM Access Analyzer](iam-access-analyzer.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
