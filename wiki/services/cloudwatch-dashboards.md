---
type: AWS Service
title: CloudWatch dashboards
description: Combines existing operational telemetry into scoped and shareable visual views.
tags: [soa-c03, domain-1, cloudwatch, dashboards]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.1", "1.1.3", "1.1.4"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
status: verified
---

# Core model

```text
existing telemetry -> widgets -> operational view
```

A dashboard displays data. It does not collect telemetry, evaluate conditions, or run a text-widget runbook.

# Widget selection

- Metric widget: graph or number.
- Alarm widget: existing alarm state and view.
- Log-query widget: Logs Insights result.
- Text widget: context and runbook links.
- Explorer-style widget: resource or tag-based view.
- Variables: reusable account, Region, or resource inputs.

Useful ordering is health, traffic, errors, latency, saturation, then logs and runbooks.

# Scope and sharing

Every widget has an account, Region, namespace, dimensions, statistic, period, and time range. Wrong scope can create an empty or misleading widget.

Cross-account observability uses a monitoring account, sink, source-account link, and permissions. Central viewing does not automatically copy telemetry centrally.

Review shared dashboards for exposed resource names, labels, operational patterns, and sensitive text-widget links.

# Failure evidence

| Symptom | First checks |
| --- | --- |
| Empty metric widget | Account, Region, dimensions, time range |
| Misleading value | Statistic, period, aggregation, metric math |
| Empty log widget | Query, log group, permissions, time range |
| Missing source account | Sink, link, permissions, monitoring account |
| Unexpected alarm widget | Underlying alarm configuration and state |

# Related concepts

- [CloudWatch telemetry](cloudwatch-telemetry.md)
- [CloudWatch alarms](cloudwatch-alarms.md)
- [Observability signal selection](../concepts/observability-signal-selection.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)

