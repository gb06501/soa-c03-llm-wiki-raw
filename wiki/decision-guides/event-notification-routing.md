---
type: Decision Guide
title: Event and notification routing
description: Selects EventBridge, SNS, SQS, or an alarm action from routing, fan-out, buffering, and delivery requirements.
tags: [soa-c03, domain-1, eventbridge, sns, sqs, selection]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.1.3", "1.1.5", "1.2.1", "1.2.2"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Notify or invoke a configured target when an alarm changes state | CloudWatch alarm action |
| Broadcast one message to several subscriptions | SNS |
| Match and route events by content | EventBridge |
| Buffer work for a consumer | SQS |
| Reshape selected event fields before delivery | EventBridge input transformer |
| Preserve failed target deliveries for investigation | Supported DLQ configuration |
| Retain selected bus events for later replay | EventBridge archive and replay |

These services can form a chain. Select each component for its own responsibility: evaluation, routing, buffering, work, or notification.

# Rejection rules

- SNS fan-out is not a stateful workflow.
- EventBridge is not a durable worker queue.
- A DLQ contains failed delivery attempts, not unmatched events.
- A successful alarm transition does not prove SNS delivery.
- An input transformer cannot perform an external lookup or complex workflow.
- Replay and remediation can repeat actions; targets must tolerate repetition.

# Evidence and verification

Trace source emission, account and Region, bus or topic, rule pattern or subscription filter, target authorization, retries and DLQ, and target-side logs. Verify the intended recipient or resource outcome.

# Related concepts

- [SNS notifications](../services/sns-notifications.md)
- [EventBridge](../services/eventbridge.md)
- [Alarm and notification failure](../playbooks/alarm-and-notification-failure.md)
- [Event-driven remediation failure](../playbooks/event-driven-remediation-failure.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
