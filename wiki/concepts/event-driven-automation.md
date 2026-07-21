---
type: Concept
title: Event-driven automation
description: Connects event sources, filters, permissions, targets, retries, failure capture, idempotency, and loop prevention.
tags: [soa-c03, domain-3, eventbridge, lambda, automation]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Core model

```text
event source -> filter/router -> target permission -> automation -> retry/DLQ -> desired-state evidence
```

Correct routing is insufficient without target authorization and idempotent execution.

# Service boundaries

| Need | Choice |
| --- | --- |
| Direct filtered S3 object reaction | S3 Event Notification |
| Rich routing and many targets | EventBridge |
| Push fan-out | SNS |
| Durable pull buffer | SQS |
| Short stateless action | Lambda |
| Explicit stateful workflow | Step Functions |
| Governed infrastructure runbook | Systems Manager Automation |

# Delivery and safety

S3 and EventBridge can deliver at least once and out of order. Use an event or business identity, atomic current-state guard, bounded retry with backoff, maximum event age, DLQ or failure destination, and downstream concurrency limits.

Prevent recursive remediation by filtering input/output states, recording processed events, limiting attempts, and asking whether the fix emits the trigger again.

# Evidence ladder

Confirm source emission, filter match, target authorization, target start, workflow success, actual desired-state change, and retry/DLQ capture. A successful function or workflow is not proof of the business result.

# Related concepts

- [Event-driven selection](../decision-guides/event-driven-automation-selection.md)
- [Event-driven failure](../playbooks/event-driven-automation-failure.md)
- [EventBridge](../services/eventbridge.md)

# Sources

- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
