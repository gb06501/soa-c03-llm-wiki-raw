---
type: Decision Guide
title: CloudWatch dashboard design
description: Selects dashboard widgets, scope, and sharing behavior from an operator's evidence needs.
tags: [soa-c03, domain-1, cloudwatch, dashboards, selection]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.1.1", "1.1.3", "1.1.4"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
status: verified
---

# Decision table

| Need | Widget or design |
| --- | --- |
| Trend, comparison, or current numeric value | Metric widget |
| Current alarm state with alarm context | Alarm widget |
| Search or aggregate log records | Logs Insights query widget |
| Runbook link or operator instruction | Text widget |
| Several accounts or Regions in one view | Cross-account or cross-Region dashboard configuration |
| Different operational time context | Dashboard-wide or widget-specific time range |

Choose the exact namespace, metric, dimensions, statistic, Region, time range, query, and alarm reference. Build the view around the operator question rather than collecting unrelated charts.

# Rejection rules

- A dashboard does not create telemetry.
- A dashboard does not replace an alarm.
- A text widget documents an action; it does not execute it.
- A correct metric with the wrong statistic, dimension, Region, or time range can mislead.
- Sharing can expose operational detail and must be deliberate.

# Evidence and verification

Open the dashboard as the intended viewer, confirm every widget resolves in the expected account and Region, compare widgets with their source metric, log query, or alarm, and verify sharing access.

# Related concepts

- [CloudWatch dashboards](../services/cloudwatch-dashboards.md)
- [Telemetry selection](telemetry-selection.md)
- [CloudWatch alarms](../services/cloudwatch-alarms.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)
