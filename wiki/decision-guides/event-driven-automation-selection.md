---
type: Decision Guide
title: Event-driven automation selection
description: Selects event routing, buffering, compute, workflows, retries, and failure controls from automation clues.
tags: [soa-c03, domain-3, eventbridge, lambda]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| S3 key event with prefix/suffix filter | direct object notification | S3 Event Notification |
| Rich event pattern or many targets | central event routing | EventBridge |
| Push one message to subscribers | fan-out | SNS |
| Buffer bursts and consumer outages | durable polling boundary | SQS |
| Short stateless reaction | bounded code execution | Lambda |
| Long or branching stateful process | explicit execution state | Step Functions |
| Governed infrastructure remediation | managed operational actions | Systems Manager Automation |
| Cross-signal operational investigation | correlation with guarded actions | AWS DevOps Agent |

# Rejection rules

- Do not confuse event-pattern match with target authorization.
- Do not assume DLQ messages replay themselves.
- Do not apply one Lambda retry model to every source.
- Do not automate a side effect without idempotency and loop analysis.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Event-driven automation](../concepts/event-driven-automation.md)
- [Event-driven failure](../playbooks/event-driven-automation-failure.md)

# Sources

- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
