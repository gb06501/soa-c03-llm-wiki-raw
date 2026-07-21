---
type: Decision Guide
title: Multi-account guardrail selection
description: Chooses account structure, identity, preventive limits, detective controls, and delegated security administration.
tags: ["soa-c03", "domain-4", "organizations", "multi-account"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Isolate workloads, environments, or ownership | separate accounts in purpose-based OUs |
| Central workforce access | IAM Identity Center permission sets and assignments |
| Bound member-account actions | SCP at the narrowest stable OU/account scope |
| Govern a managed landing zone | Control Tower |
| Detect configuration drift | Config and detective controls |
| Pre-provision supported validation | proactive controls |
| Central security-service operations | delegated administrator |
| Central activity evidence | organization CloudTrail to protected log archive |
| Approved resource sharing | Resource Access Manager |
| Standard account creation | Account Factory or governed vending workflow |

# Rejection rules

- Do not run ordinary workloads in the management account.
- An SCP is not an IAM permission grant.
- An allow-list SCP requires an allowed path through every inherited level.
- Central aggregation does not enable missing regional sources.
- A landing zone does not eliminate drift or operational ownership.

# Verification

Enroll a canary account, test allowed and denied actions, verify federation and break glass, confirm logs/findings from each required Region, and inspect delegated-administrator and control status.

# Related pages

- [Organizations and multi-account security](../services/organizations-and-multi-account.md)
- [Multi-account security governance](../concepts/multi-account-security-governance.md)

# Sources

- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
