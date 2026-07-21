---
type: Troubleshooting Playbook
title: Deployment failure
description: Diagnoses permission, quota, capacity, subnet, network, runtime, rollback, and deletion failures across deployment tools.
tags: [soa-c03, domain-3, deployment, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.3"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
status: verified
---

# Trigger

A deployment reports failure or success without producing a usable application state.

# Evidence path

1. Stop parallel changes and capture command, version, parameters, and preview.
2. Find the earliest failing orchestration or service event.
3. Classify configuration, IAM/KMS, quota, capacity, IP, network, runtime, or dependency.
4. Use the principal ARN and CloudTrail for authorization failures.
5. Use service state, subnet address count, quota, and Region/AZ evidence.
6. Trace startup, endpoint, artifact, secret, health, and application logs for created resources.

# Failure map

| Symptom | Direction |
| --- | --- |
| AccessDenied | caller, PassRole, execution role, SCP, resource/KMS policy |
| Quota exceeded | account/Region usage and quota |
| Insufficient capacity | AZ/type availability |
| Free addresses exhausted | subnet and rollout surge ENIs |
| Created but unhealthy | bootstrap, network, dependency, readiness |
| UPDATE_ROLLBACK_FAILED | specific rollback blocker |
| Delete failed | protection, attachment, retention, missing permission |

# Safe action

Fix the smallest proven cause in code or controlled configuration. Preserve data, preview replacement, continue blocked rollback only after repair, and use bounded retry only for throttling or temporary capacity.

# Verification

Confirm stable orchestration state, expected resource identity, healthy application traffic, dependency access, absence of unintended drift, and a usable rollback path.

# Related concepts

- [Deployment diagnostics](/concepts/deployment-diagnostics.md)
- [Evidence selection](/decision-guides/deployment-failure-evidence-selection.md)

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
