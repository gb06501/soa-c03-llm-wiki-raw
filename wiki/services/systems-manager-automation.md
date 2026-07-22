---
type: AWS Feature
title: Systems Manager Automation
parent_services: [Systems Manager]
description: Runs governed, parameterized infrastructure workflows with step-level evidence and safety controls.
tags: [soa-c03, domain-1, systems-manager, automation, runbook]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.3", "1.2.1", "1.2.2", "1.2.3", "3.2.1", "3.2.2"]
domain_ids: ["1", "3"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Core model

```text
trigger/operator -> runbook -> ordered steps -> AWS resources -> outputs/status
```

A runbook is a definition. An Automation execution is one run of a selected version with parameters, targets, and an execution role.

# Important objects

- AWS-managed or custom runbook.
- Immutable document version and configured default version.
- Runtime parameters, ordered steps, inputs, outputs, and actions.
- Execution role and selected targets.
- Concurrency and error threshold.
- Execution ID with step-level status and output.

Important actions include calling AWS APIs, running commands on managed nodes, executing scripts, invoking Lambda, branching, waiting, asserting state, and invoking another runbook.

# Permission chain

```text
caller can start Automation
caller/service can pass execution role
execution role can perform each runbook action
```

Also inspect trust policies, KMS/resource policies, cross-account trust, and the managed-node role for Run Command steps.

# Safety controls

- Narrow targets by resource IDs or tags.
- Limit concurrency and stop after an error threshold.
- Require approval for risky actions.
- Bound timeout and retries.
- Make steps idempotent.
- Verify state before and after change.
- Test a new version on one resource first.

# Failure evidence

```text
execution ID -> document version -> failed or waiting step
-> inputs/outputs -> role/API error -> target resource state
```

# Exam traps

- The latest document version may not be the default version.
- Caller permission does not grant execution-role permission or `iam:PassRole`.
- `aws:runCommand` requires a managed node; AWS API actions may not.
- An approval step can make a healthy execution appear stuck.
- Successful steps do not prove final workload recovery.

# Related concepts

- [Safe automation](../concepts/safe-automation.md)
- [Evidence-to-remediation loop](../concepts/evidence-to-remediation-loop.md)
- [EventBridge](eventbridge.md)
- [Event-driven remediation failure](../playbooks/event-driven-remediation-failure.md)

# Operational and event integration

Automation orchestrates AWS actions and can invoke Run Command. Use it for governed infrastructure runbooks rather than a general application workflow. Execution role permission, document version, parameters, approvals, branches, waits, step output, and target resource/KMS policies determine behavior.

When invoked by EventBridge or another source, separately verify event match, invocation authorization, Automation execution, resource action, and desired-state verification. Add idempotency and a loop guard before automatic remediation.

# Runbook safety model

`trigger -> runbook version -> assume role -> bounded steps -> branch/retry/timeout -> output -> independent verification`

Automation success means the steps completed; it does not prove application recovery. Prefer narrow targets, idempotent actions, explicit failure branches, and postcondition checks.

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)

