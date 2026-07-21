---
type: Decision Guide
title: Access denial evidence selection
description: Selects decisive evidence for identity, trust, policy-boundary, resource-policy, KMS, and endpoint denials.
tags: ["soa-c03", "domain-4", "access-control", "diagnostics"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
status: verified
---

# Decision table

| Scenario clue | First decisive evidence | Then inspect |
| --- | --- | --- |
| Generic AccessDenied | CloudTrail principal, action, resource, context | identity/resource policies and explicit denies |
| AssumeRole denied | caller and target-role event | trust conditions, caller allow, SCP, MFA/ExternalId |
| PassRole denied | caller, role ARN, destination service | caller `iam:PassRole`, resource scope, passed-role trust |
| Cross-account resource denied | resource policy and actual session ARN | caller policy, SCP, condition and account |
| KMS-related denial | key ARN and KMS event | key policy, grant, context, ViaService, key state |
| Works publicly, fails through endpoint | endpoint used and policy | endpoint DNS, endpoint policy, service/resource policy |
| New policy has no effect | active role/session and policy version | propagation, cached credential, boundary/session ceiling |

# Rejection rules

- Do not add wildcard access before identifying the request tuple.
- Do not treat a trust policy as the role permission policy.
- Do not inspect only IAM when a resource or KMS policy participates.
- Do not assume the friendly role name is the observed session principal.
- Do not conclude “network” from an authorization error or “IAM” from a timeout.

# Verification

Repeat the exact request through the intended path, confirm CloudTrail shows the intended principal, and test a nearby action or resource that must remain denied.

# Related pages

- [Access evaluation](../concepts/access-evaluation.md)
- [Access denied](../playbooks/access-denied.md)

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
