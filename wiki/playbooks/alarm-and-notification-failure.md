---
type: Troubleshooting Playbook
title: Alarm and notification failure
description: Separates missing metric data, alarm evaluation errors, action configuration, and SNS delivery failures.
tags: [soa-c03, domain-1, troubleshooting, cloudwatch, sns]
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

# Trigger

An expected alarm did not change state, or the alarm changed state but no notification or remediation arrived.

# Stage 1: metric

1. Open the metric graph for the incident time.
2. Confirm account, Region, namespace, metric, dimensions, statistic, and period.
3. If data is absent, solve collection before alarm evaluation.

# Stage 2: evaluation

1. Inspect state reason and history.
2. Confirm threshold, comparison, `M` of `N`, and missing-data treatment.
3. For composites, inspect every child alarm and the Boolean rule.

# Stage 3: action

1. Confirm actions are enabled and the configured target is correct.
2. For direct SNS, verify topic ARN and source permission/topic policy.
3. For EventBridge, verify correct account, Region, bus, rule state, and actual event pattern.

# Stage 4: delivery

1. Confirm subscription status and filter policy.
2. Confirm SNS can use the KMS key.
3. Confirm the target resource policy or endpoint accepts delivery.
4. Inspect retry, DLQ, and endpoint evidence.

# Fast diagnosis

| Observation | Direction |
| --- | --- |
| `INSUFFICIENT_DATA` | Source data, dimensions, period, missing-data behavior |
| State never breaches | Statistic, threshold, comparison, `M/N` |
| State is `ALARM`, no message | Action, topic policy, confirmation, KMS, endpoint |
| Some subscribers receive | Filter, status, protocol-specific failure |

# Verification

Trigger a controlled test condition or test event. Confirm metric, state history, action attempt, and endpoint receipt as separate facts.

# Related concepts

- [CloudWatch alarms](../services/cloudwatch-alarms.md)
- [SNS notifications](../services/sns-notifications.md)
- [EventBridge](../services/eventbridge.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)

