---
type: Decision Guide
title: Deployment failure evidence selection
description: Selects the first decisive evidence source for deployment, permission, capacity, network, and runtime failures.
tags: [soa-c03, domain-3, diagnostics]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.3"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Stack rolled back | initiating resource failure | earliest FAILED stack event |
| Parent nested stack failed | child resource cause | child stack events |
| AccessDenied | failed identity and API | status reason plus CloudTrail |
| PassRole denied | caller-to-role gate | caller policy, exact role, trust |
| Quota exceeded | account/Region usage limit | Service Quotas and current usage |
| Insufficient capacity | AZ/type availability | service capacity evidence |
| Resource created but unhealthy | data-plane startup and dependency | service events, logs, health and network evidence |
| UPDATE_ROLLBACK_FAILED | rollback blocker | failed rollback resource and reason |

# Rejection rules

- Do not start with the final rollback event.
- Do not treat quota and AZ capacity as the same problem.
- Do not retry a permanent validation or authorization failure.
- Do not remove stateful resources merely to make rollback finish.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Deployment diagnostics](/concepts/deployment-diagnostics.md)
- [Deployment failure](/playbooks/deployment-failure.md)

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
