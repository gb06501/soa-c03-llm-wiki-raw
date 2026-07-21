---
type: Troubleshooting Playbook
title: Access denied
description: Diagnoses an exact authorization failure across identity, trust, resource, boundary, organization, endpoint, KMS, and service controls.
tags: ["soa-c03", "domain-4", "troubleshooting", "iam", "access-control"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
status: verified
---

# Trigger

An AWS API or workload request returns AccessDenied, UnauthorizedOperation, or an equivalent service authorization failure.

# Evidence path

1. Preserve the exact error, request ID, timestamp, account, Region, and client path.
2. Capture the actual principal or role-session ARN.
3. Record the exact API action, resource ARN, and relevant request context.
4. Locate the CloudTrail event and error details.
5. Find an applicable allow in identity or resource policy.
6. Trace explicit denies and permission ceilings: boundary, session policy, SCP, endpoint policy, and service controls.
7. For roles, separate AssumeRole trust from post-assumption permissions and `iam:PassRole`.
8. For encrypted resources, inspect the KMS key, policy, grants, state, Region, and encryption context.

# Failure map

| Symptom | Direction |
| --- | --- |
| AssumeRole denied | trust principal/conditions, caller allow, SCP |
| PassRole denied | caller permission on exact role and destination service |
| Cross-account denied | resource policy, actual session principal, both-account limits |
| IAM appears allowed but KMS fails | key policy/grant/context/state |
| Public path works, endpoint fails | endpoint DNS and endpoint policy |
| Old session behavior persists | active session and session-policy boundary |

# Safe action

Change the smallest statement, resource, principal, action, or condition proven to block the intended request. Avoid wildcard testing in production; use a limited test principal or Policy Simulator where appropriate.

# Verification

Repeat the exact request and confirm CloudTrail records the intended principal and success. Test a nearby prohibited action or resource to prove least privilege remains.

# Rollback

Restore the previous policy version or attachment if the change broadens unintended access, then revoke affected sessions or credentials where justified.

# Escalation

Escalate with the request tuple, event, evaluated policy layers, proposed minimal change, and required business action.

# Related pages

- [Access evaluation](../concepts/access-evaluation.md)
- [Access denial evidence selection](../decision-guides/access-denial-evidence-selection.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
