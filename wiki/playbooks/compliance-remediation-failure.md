---
type: Troubleshooting Playbook
title: Compliance remediation failure
description: Diagnoses missing evaluations, stale aggregation, permission errors, unsafe automation, and repeated compliance drift.
tags: ["soa-c03", "domain-4", "troubleshooting", "config", "compliance"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
status: verified
---

# Trigger

A Config rule does not evaluate correctly, a noncompliant resource is not remediated, or automatic remediation fails or causes unexpected impact.

# Evidence path

1. Confirm account, Region, resource type, and recorder coverage.
2. Check recorder and delivery-channel status.
3. Inspect the rule trigger, scope, parameters, latest evaluation, and annotation.
4. Distinguish source evaluation from aggregator freshness.
5. Inspect remediation configuration, execution role, parameters, concurrency, error limit, and SSM Automation execution.
6. Check CloudTrail for denied or invalid remediation API calls.
7. Confirm the resource still exists and the evaluation is not stale.
8. Verify a preventive control or owner process is not recreating the drift.

# Failure map

| Symptom | Direction |
| --- | --- |
| No evaluation | recorder/type/Region/trigger scope |
| Central view missing result | aggregator source and freshness |
| Remediation never starts | remediation association and eligibility |
| Access denied | automation role, PassRole, SCP, resource/KMS policy |
| Repeated failure | invalid parameter, unsupported state, dependency |
| Becomes compliant then drifts | source of configuration truth or deployment pipeline |
| Workload outage after fix | unsafe target selection or missing health gate |

# Safe action

Pause automatic remediation when scope or safety is uncertain. Correct recorder/rule coverage first, test remediation manually on one known resource, then enable bounded concurrency and verification.

# Verification

Create or use an approved test violation, observe evaluation, complete remediation, re-evaluate to compliant, and verify workload health and ownership metadata.

# Rollback

Disable the remediation association and restore the last known-good resource configuration through its owning deployment path.

# Escalation

Provide the configuration item, rule evaluation, automation execution, CloudTrail event, target resource owner, and rollback state.

# Related pages

- [Config](../services/config.md)
- [Compliance monitoring selection](../decision-guides/compliance-monitoring-selection.md)

# Sources

- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
