---
type: Decision Guide
title: CloudWatch alarm design
description: Selects alarm type and evaluation behavior from signal shape, noise, and missing-data requirements.
tags: [soa-c03, domain-1, cloudwatch, alarms, selection]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.1.3"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Evaluate one metric or metric-math expression | Metric alarm |
| Detect deviation from an expected band | Anomaly-detection alarm |
| Combine states of existing alarms | Composite alarm |
| Require M breaches among N recent periods | Datapoints to alarm plus evaluation periods |
| Control how absent datapoints affect state | Missing-data treatment |
| Notify or invoke an action on state transition | Alarm action |
| Route the state-change event by content | EventBridge |

Choose namespace, metric, dimensions, statistic, period, threshold, comparison, evaluation periods, datapoints to alarm, and missing-data behavior as one coherent design. A correct threshold on the wrong statistic or dimension is still the wrong alarm.

# Rejection rules

- A dashboard displays data; it does not evaluate alarm state.
- A metric filter produces a metric; it does not alarm by itself.
- A composite alarm watches other alarm states, not raw metrics.
- Alarm state does not prove action or notification delivery.
- Avoid treating one brief datapoint as sustained failure when the requirement calls for persistence.

# Evidence and verification

Inspect the metric graph with the alarm settings overlaid, state-change history, evaluated datapoints, missing-data behavior, and action history. Then verify the downstream target separately.

# Related concepts

- [CloudWatch alarms](../services/cloudwatch-alarms.md)
- [Alarm and notification failure](../playbooks/alarm-and-notification-failure.md)
- [Event and notification routing](event-notification-routing.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
