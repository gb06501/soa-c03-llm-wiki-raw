---
type: AWS Service
title: Step Functions
service_id: step-functions
description: Runs explicit stateful workflows with branching, waits, parallel work, retries, catches, and execution evidence.
tags: [soa-c03, domain-3, step-functions, workflow, events]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Core model

```text
state-machine definition -> execution -> states -> input/output/history
                         \-> execution role calls AWS services
```

# Selection

Use Step Functions for multiple steps, branching, parallel work, waits, callbacks, or per-step state and error handling. Use Lambda for a short stateless reaction and Systems Manager Automation for governed infrastructure runbooks.

# State and failure controls

Task, Choice, Wait, Parallel, Map, Pass, Succeed, and Fail states express flow. Retry matches errors and controls interval, attempts, and backoff. Catch routes exhausted errors to another state. Catch does not undo earlier side effects.

Standard workflows fit durable, auditable, potentially long-running execution. Express workflows fit high-rate, short-duration execution where those semantics are appropriate.

# Permissions and evidence

The execution role needs every target service action, while callers need permission to start or inspect execution. Resource and KMS policies remain separate. Use execution history, state input/output/error, configured logs and metrics, and target-service evidence.

# Safety

Make repeated tasks idempotent, design compensation explicitly, limit retries, preserve identifiers through state transitions, and verify the final business result.

# Related concepts

- [Event-driven automation](/concepts/event-driven-automation.md)
- [Event-driven selection](/decision-guides/event-driven-automation-selection.md)

# Sources

- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
