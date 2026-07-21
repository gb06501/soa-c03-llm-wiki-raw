---
type: Concept
title: Evidence-to-remediation loop
description: Diagnoses scope and cause before applying the smallest safe change and verifying recovery.
tags: [soa-c03, domain-1, diagnosis, remediation, verification]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.2.1", "1.2.2", "1.2.3", "1.3.1", "1.3.2", "1.3.5", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Core model

```text
symptom -> evidence -> correlation -> likely cause
-> smallest safe action -> verification -> notification
```

Do not start with the fix. First prove what failed, when it started, who or what is affected, what changed, and which layer or dependency is limiting the service.

# Diagnosis sequence

1. Define user-visible symptom and scope.
2. Establish a healthy baseline and incident time window.
3. Select evidence by question.
4. Correlate metrics, logs, changes, health events, and dependencies.
5. Identify the lowest limiting layer.
6. Reject actions that only treat the symptom.

# Change selection

- Prefer one targeted change so the result remains attributable.
- Check required permissions, blast radius, restart, failover, and maintenance effects.
- Preserve evidence before a restart or replacement when possible.
- Use automation only with narrow scope and an observable failure path.

# Verification

Successful API or workflow execution is not the end state. Verify:

- service latency and error rate;
- original saturation or health signal;
- resource state;
- downstream impact;
- required headroom;
- expected cost movement;
- absence of repeated triggering or rollback conditions.

# Exam traps

- Correlation does not always prove causation.
- More compute does not fix storage, locks, or downstream limits.
- Auto Scaling can overload a constrained database.
- A restart can hide evidence without repairing the cause.
- A successful runbook can target the wrong resource or use a weak assertion.

# Related concepts

- [Observability signal selection](observability-signal-selection.md)
- [Safe automation](safe-automation.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)
- [Remediation tool selection](../decision-guides/remediation-tool-selection.md)

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)

