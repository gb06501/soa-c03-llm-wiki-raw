---
type: Decision Guide
title: Security finding triage
description: Prioritizes and routes findings using source evidence, exploitability, exposure, criticality, privilege, scope, age, and fix readiness.
tags: ["soa-c03", "domain-4", "security-findings", "triage"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---

# Decision table

| Finding context | Triage direction |
| --- | --- |
| Active suspicious behavior or compromised credential | immediate evidence preservation and containment |
| Exploitable vulnerability on an exposed critical workload | urgent controlled patch or isolation |
| Sensitive data publicly reachable | restrict exposure while preserving evidence |
| Configuration noncompliance with no exposure | assign owner and remediate by policy SLA |
| Duplicate aggregator and source findings | correlate under one case; preserve source records |
| Expected behavior with durable justification | documented suppression with scope and expiry |
| Stale resource or resolved source finding | verify source state before closure |

# Priority model

Combine provider severity with exploitability, network exposure, asset criticality, data sensitivity, privilege, affected scope, first/last observed time, and fix availability. Record uncertainty explicitly.

# Rejection rules

- Severity alone is not risk.
- Aggregation does not replace source-service investigation.
- Workflow status is not source-level remediation.
- Suppression without owner, reason, scope, and expiry creates hidden debt.
- A destructive “cleanup” can erase evidence or disrupt recovery.

# Verification

Re-query the source, confirm the affected resource and behavior, verify the fix or containment, test workload health, update workflow state, and retain investigation evidence.

# Related pages

- [Security findings](../concepts/security-findings.md)
- [Security Hub CSPM](../services/security-hub-cspm.md)

# Sources

- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
