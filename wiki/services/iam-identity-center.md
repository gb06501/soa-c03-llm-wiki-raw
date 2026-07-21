---
type: AWS Service
title: IAM Identity Center
service_id: iam-identity-center
description: Provides workforce federation, permission sets, and centrally managed account assignments.
tags: ["soa-c03", "domain-4", "identity-center", "federation"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
status: verified
---
# Core model

IAM Identity Center connects a workforce identity source to AWS accounts and applications. A permission set is a centrally managed permission template; an assignment binds a user or group, permission set, and target account.

# Key objects

| Object | Meaning |
| --- | --- |
| Identity source | Built-in directory, Active Directory, or external identity provider |
| Permission set | Policy and session configuration provisioned into target accounts |
| Assignment | Principal plus permission set plus account |
| Provisioned role | Account-local IAM role created from a permission set |

# Decision boundaries

Use federation and groups for workforce access across accounts. Use workload roles for applications. A changed permission set must be provisioned to affected accounts; an assignment alone does not prove the generated role is current.

# Evidence and diagnosis

Check identity-source membership, account assignment, permission-set contents, provisioning status, session duration, and the role/session ARN observed in CloudTrail.

# Safe operations

Apply least privilege through permission sets, separate administrative tiers, require strong authentication, test assignments in a limited account, and retain an independently governed emergency path.

# Related decisions

- [IAM principal and policy selection](../decision-guides/iam-principal-and-policy-selection.md)
- [Multi-account guardrail selection](../decision-guides/multi-account-guardrail-selection.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
