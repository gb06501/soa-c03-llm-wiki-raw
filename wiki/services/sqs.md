---
type: AWS Service
title: SQS
service_id: sqs
description: Buffers events for polling consumers and controls backlog, visibility, retry, redrive, and failure isolation.
tags: [soa-c03, domain-3, sqs, events, buffering]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.5", "1.2.2", "2.2.2", "3.2.2"]
domain_ids: ["1", "2", "3"]
sources:
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Core model

```text
producer -> queue -> consumer receives batch -> process -> delete
                       failure -> visibility expires -> retry -> DLQ by redrive policy
```

# Selection

Use SQS when work must survive consumer outage, absorb a rate mismatch, or be processed by polling consumers. SNS pushes and fans out; SQS buffers. EventBridge routes events; an SQS target adds a durable consumer boundary.

# Lambda integration

Lambda event source mapping polls the queue. The execution role needs receive, delete, and queue-attribute permissions. Function processing time must fit the visibility design. Batch and partial-batch failure behavior determine which messages retry.

# Evidence and failure modes

Use queue depth and age, in-flight count, receive/delete behavior, mapping state, function concurrency and errors, visibility timeout, redrive count, and DLQ messages.

A poison message can repeat. A short visibility timeout can create overlapping processing. Increasing concurrency can overload downstream dependencies.

# Safety

Make consumers idempotent, set bounded redrive, retain failed messages, control concurrency, and replay only after correcting the cause.

# Related concepts

- [Event-driven automation](../concepts/event-driven-automation.md)
- [Event-driven selection](../decision-guides/event-driven-automation-selection.md)
- [Event-driven failure](../playbooks/event-driven-automation-failure.md)

# Reliability boundary

SQS decouples producer availability from consumer processing and exposes backlog as evidence. Visibility timeout, retry, dead-letter policy, duplicate delivery, idempotency, and downstream capacity determine whether buffering becomes recovery or merely delay.

# Sources

- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)

