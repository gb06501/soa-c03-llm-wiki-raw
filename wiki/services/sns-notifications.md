---
type: AWS Service
title: SNS
service_id: sns
description: Fans out messages to authorized subscriptions with delivery, filtering, encryption, and failure evidence.
tags: [soa-c03, domain-1, sns, notifications]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.3", "1.1.5", "1.2.1", "1.2.2", "2.2.2", "2.3.1", "3.2.2"]
domain_ids: ["1", "2", "3"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Core model

```text
publisher -> topic -> subscriptions -> endpoints
```

Use SNS to broadcast or fan out a message. Use SQS to buffer work and EventBridge to route by event content.

# Delivery controls

- Topic policy controls allowed publishers and subscribers.
- Subscription protocol identifies the endpoint type.
- Email and HTTP-style subscriptions may require confirmation.
- Filter policy can intentionally discard nonmatching messages.
- Delivery policy controls supported retry behavior.
- A configured KMS key encrypts topic messages at rest.
- A subscription DLQ can retain supported failed deliveries.

# Permission questions

1. Can the publisher send to the topic?
2. Can SNS use the configured KMS key?
3. Can SNS deliver to the endpoint?

Cross-account delivery may involve publisher IAM, topic policy, key policy, and target resource policy.

# Failure evidence

```text
source/alarm history -> topic ARN -> topic policy and KMS key
-> subscription status and filter -> delivery evidence -> endpoint
```

# Exam traps

- Creating an email subscription does not confirm it.
- Alarm evaluation can succeed while SNS delivery fails.
- IAM allow can still be blocked by a topic, key, or target policy.
- A healthy filtered subscription can correctly receive nothing.
- SNS delivery does not prove a human read the message.

# Related concepts

- [CloudWatch alarms](cloudwatch-alarms.md)
- [EventBridge](eventbridge.md)
- [Alarm and notification failure](../playbooks/alarm-and-notification-failure.md)
- [Remediation tool selection](../decision-guides/remediation-tool-selection.md)

# Event automation

SNS is the push fan-out boundary. Use SQS when consumers need a durable polling buffer. Each subscription has independent delivery and filtering behavior, and source, topic, subscription, encryption, and consumer permissions remain separate.

Duplicate delivery and retry require idempotent subscribers. Fan-out success does not prove every subscriber completed its business action.

# Alarm, fan-out, and delivery boundary

CloudWatch may evaluate an alarm correctly while SNS delivery fails. Verify topic policy, KMS access, subscription confirmation, filter policy, retry evidence, and target policy. SNS fans out; SQS buffers; EventBridge matches and routes.

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)

