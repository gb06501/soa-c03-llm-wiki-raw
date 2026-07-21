---
type: AWS Service
title: CloudWatch alarms
description: Evaluates metric conditions and emits state changes for notification or remediation.
tags: [soa-c03, domain-1, cloudwatch, alarms]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.3", "1.1.5", "1.2.1", "1.2.2"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
status: verified
---

# Core model

```text
metric -> evaluation -> state change -> direct action or EventBridge event
```

Alarm state and action delivery are separate stages.

# Alarm types

| Type | Evaluates |
| --- | --- |
| Metric alarm | One metric or metric-math expression |
| Anomaly alarm | A metric against an expected band |
| Composite alarm | Boolean state of other alarms |

A composite alarm reduces noise by combining existing alarm states. It does not read raw metrics.

# Evaluation properties

- Namespace, metric name, and dimensions identify the signal.
- Statistic and period define each evaluated bucket.
- Threshold and comparison define breach.
- Evaluation periods define `N` recent buckets.
- Datapoints to alarm define required `M` breaching buckets.
- Missing-data treatment must match meaning: no requests may be normal; no heartbeat may be failure.

States are `OK`, `ALARM`, and `INSUFFICIENT_DATA`.

# Action choice

| Requirement | Path |
| --- | --- |
| Simple notification | Alarm -> SNS |
| Filtered or multi-target reaction | Alarm state event -> EventBridge -> targets |
| Several conditions must agree | Child alarms -> composite alarm |
| Log pattern must alert | Metric filter -> metric -> alarm |

# Failure evidence

```text
metric graph -> alarm state reason -> alarm history -> action configuration
-> target policy/role -> delivery or execution history
```

# Exam traps

- `INSUFFICIENT_DATA` is not automatically workload failure.
- A correct `ALARM` state does not prove message delivery.
- A dashboard does not evaluate alarm state.
- A metric filter produces a metric; it does not alert by itself.
- Wrong dimensions commonly produce no data rather than a clear configuration error.

# Related concepts

- [SNS notifications](sns-notifications.md)
- [EventBridge](eventbridge.md)
- [Alarm and notification failure](../playbooks/alarm-and-notification-failure.md)
- [Safe automation](../concepts/safe-automation.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)

