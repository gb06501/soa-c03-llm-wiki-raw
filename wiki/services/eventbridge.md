---
type: AWS Service
title: EventBridge
service_id: eventbridge
description: Matches events on buses and routes transformed payloads to authorized targets with retry and failure controls.
tags: [soa-c03, domain-1, eventbridge, automation]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.3", "1.1.5", "1.2.1", "1.2.2", "1.2.3", "3.2.2", "2.2.2", "2.3.1"]
domain_ids: ["1", "3", "2"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Core model

```text
source -> event bus -> rule pattern -> optional transform -> target
```

No pattern match means no target attempt. A pattern match does not prove target success.

# Bus and event identity

| Bus | Main source |
| --- | --- |
| Default | AWS services and account applications |
| Custom | Custom application events |
| Partner | Supported SaaS partners |

Important event fields include `source`, `detail-type`, `detail`, `resources`, `account`, `region`, `time`, and `id`. Match the actual nested event shape, not an assumed shape.

# Rule controls

- Event pattern or schedule.
- Enabled/disabled state.
- Target ARN and required role or resource policy.
- Input path and input transformer.
- Retry policy and maximum event age.
- DLQ for failed target delivery.
- Archive and replay for retained bus events.

An input transformer selects and reshapes existing event fields. Use Lambda or Step Functions when external lookup or complex logic is required.

# Cross-account path

```text
source rule -> destination bus -> destination bus policy -> destination rule -> target
```

# Failure evidence

```text
source emitted -> account/Region/bus -> rule enabled -> actual pattern match
-> target authorization -> retry/DLQ -> target logs or history
```

# Exam traps

- EventBridge is not a durable worker queue.
- A DLQ contains failed target deliveries, not unmatched events.
- Correct values at the wrong nesting level do not match.
- Archive replay can repeat actions; targets need idempotency.
- A remediation-generated event can retrigger the remediation.

# Related concepts

- [Safe automation](../concepts/safe-automation.md)
- [Systems Manager Automation](systems-manager-automation.md)
- [Event-driven remediation failure](../playbooks/event-driven-remediation-failure.md)
- [Remediation tool selection](../decision-guides/remediation-tool-selection.md)

# Delivery, replay, and loop safety

A rule pattern must match the real event envelope. A matching rule still needs a valid target ARN, target role or resource policy, and KMS access. Each target has independent retry, age, DLQ, and evidence.

Archive replay deliberately sends old events again; it does not reverse prior effects. Consumers need idempotency and current-state guards. Automatic remediation must filter its own result events or otherwise prevent recursive triggers.

# Routing and operational triggers

EventBridge matches event structure and routes to authorized targets. It does not replace a durable worker queue, target permissions, target retry design, or idempotent processing. Alarm changes, backup events, health events, and automation triggers retain their source-service evidence.

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)

