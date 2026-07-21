---
type: Concept
title: Deployment diagnostics
description: Finds the earliest failing deployment layer, preserves state, and selects the smallest safe correction.
tags: [soa-c03, domain-3, deployment, diagnostics, rollback]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.3"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
status: verified
---

# Core model

```text
tool/template -> orchestration -> service control plane -> resource startup/network -> application health
```

Diagnose the first layer that failed. Later rollback errors often describe consequences rather than the initiating cause.

# Evidence ladder

1. Deployment command and proposed diff.
2. Earliest failed CloudFormation logical resource and exact status reason.
3. Nested-stack events when the parent reports only a summary.
4. CloudTrail principal and denied API.
5. Service-specific state, quota, capacity, and Region support.
6. Runtime network, bootstrap, task, function, and application evidence.

# Classification

| Clue | Direction |
| --- | --- |
| Access denied / PassRole | caller, execution role, trust, SCP, resource policy, KMS |
| Invalid property or name exists | template/parameter or ownership collision |
| Limit exceeded | account/Region quota |
| Insufficient capacity | selected AZ/type capacity |
| Free addresses exhausted | subnet and surge ENI demand |
| Timeout or unhealthy | bootstrap, route, endpoint, dependency, health check |
| Delete or replacement blocked | protection, dependency, nonempty/stateful resource |

# Recovery invariants

Preserve state, stop blind retries, repair the proven blocker, preview replacement, finish rollback, then deploy a reviewed correction. For `UPDATE_ROLLBACK_FAILED`, repair the rollback blocker and continue rollback; skipping resources is a last resort that creates reconciliation work.

# Related concepts

- [Deployment evidence selection](/decision-guides/deployment-failure-evidence-selection.md)
- [Deployment failure playbook](/playbooks/deployment-failure.md)
- [CloudFormation lifecycle](/services/cloudformation-and-cdk.md)

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
