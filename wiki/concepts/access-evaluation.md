---
type: Concept
title: Access evaluation
description: Models an authorization decision as the intersection of an exact request and every applicable allow or deny boundary.
tags: ["soa-c03", "domain-4", "access-control", "authorization"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
status: verified
---
# Core model

Evaluate one request tuple:

`principal + action + resource + context -> decision`

Do not debug “the user” or “the service” in general. Record the role-session ARN, exact API action, exact resource ARN, account, Region, network path, tags, MFA state, and other request conditions.

# Evaluation sequence

1. Confirm authentication and the actual session principal.
2. Find an applicable allow in identity or resource policy.
3. Apply explicit denies.
4. Apply permission ceilings: boundary, session policy, SCP, and service controls.
5. Evaluate trust for role assumption and `iam:PassRole` for service role attachment.
6. Apply resource, KMS, and VPC endpoint policies.
7. Confirm the service supports the resource and condition keys used.

# Evidence map

| Evidence | Proves |
| --- | --- |
| Error and request ID | Failed request and service |
| CloudTrail event | Principal, action, resource context, and outcome |
| Policy documents | Candidate allows, denies, and conditions |
| Access Analyzer | Policy findings and selected access paths |
| Last-accessed data | Observed use, not complete required access |

# Safety rule

The correct fix is the narrowest proven change that restores the intended request while preserving nearby denied paths.

# Related pages

- [IAM](../services/iam.md)
- [Access denial evidence selection](../decision-guides/access-denial-evidence-selection.md)
- [Access denied](../playbooks/access-denied.md)

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
