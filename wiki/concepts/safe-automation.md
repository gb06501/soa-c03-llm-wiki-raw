---
type: Concept
title: Safe automation
description: Constrains automated operational changes with least privilege, bounded execution, idempotency, and verification.
tags: [soa-c03, domain-1, automation, governance, safety]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.3", "1.2.1", "1.2.2", "1.2.3", "1.3.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
status: verified
---

# Control model

```text
detect -> route -> act -> verify -> notify
```

Each stage must have evidence, permissions, bounded failure behavior, and a clear desired state.

# Required controls

- Least-privilege execution role.
- Narrow resource IDs or tag scope.
- Idempotent actions and replay-safe targets.
- Retry limit, backoff, timeout, concurrency, and rate limits.
- Approval for high-blast-radius or destructive changes.
- Stop condition, rollback path, or controlled failure path.
- Execution logs and step-level outputs.
- Verification after the change.

# Loop analysis

An action can emit the same event that triggered it.

```text
event -> remediation -> matching change event -> remediation again
```

Prevent loops with narrow event patterns, state checks, idempotency, tags or markers, bounded retries, and a stop condition.

# Permission layers

Different workflows can require separate permissions for:

- the caller to start an action;
- `iam:PassRole`;
- the execution role to change the target;
- EventBridge to invoke the target;
- resource or KMS policies;
- a managed-node role for Run Command.

# Verification rule

```text
successful invocation != successful remediation
```

Check the resource and workload result, not only the function, rule, alarm action, or runbook status.

# Exam traps

- High concurrency widens damage.
- Retrying a non-idempotent action can repeat damage.
- Archive replay can repeat business effects.
- Broad Lambda permissions turn a small defect into a large incident.
- AI-assisted recommendations still require evidence, permission, and human validation.

# Related concepts

- [EventBridge](../services/eventbridge.md)
- [Systems Manager Automation](../services/systems-manager-automation.md)
- [Evidence-to-remediation loop](evidence-to-remediation-loop.md)
- [Event-driven remediation failure](../playbooks/event-driven-remediation-failure.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)

