---
type: Concept
title: Observability signal selection
description: Chooses the evidence source from the operational question instead of from a preferred tool.
tags: [soa-c03, domain-1, observability, diagnosis]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.2.1", "1.3.5", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Decision rules

| Operational question | First evidence |
| --- | --- |
| How much, how often, how saturated? | Metrics |
| What exact error or message occurred? | Logs |
| Who changed configuration? | CloudTrail |
| Where is request latency introduced? | Traces |
| Did AWS report maintenance or service impact? | AWS Health |
| Did deployment or infrastructure state change? | Deployment history, CloudFormation events, CloudTrail |
| Did automated action run? | Automation/Lambda execution history and logs |

Service-specific layers refine the choice. For RDS, CloudWatch shows the resource, Enhanced Monitoring shows the OS, and Database Insights/Performance Insights shows DB load, waits, and SQL.

# Correlation model

```text
metric symptom -> matching log -> recent change -> health event
-> dependency evidence -> comparison with healthy baseline
```

Compare before and after a change, healthy and affected resources, average and percentile latency, traffic and errors, and one AZ/Region/account against others.

# Collection gap versus healthy zero

No data can mean:

- no activity;
- wrong account, Region, namespace, dimension, or time range;
- missing collector or integration;
- permission or network failure;
- an intentionally filtered signal.

Prove data collection before interpreting absence.

# Exam traps

- CloudTrail cannot explain CPU saturation.
- An empty dashboard widget is not proof that the resource was idle.
- A running agent is not proof that data reached CloudWatch.
- One metric is a clue, not automatic proof of root cause.

# Related concepts

- [CloudWatch telemetry](../services/cloudwatch-telemetry.md)
- [Evidence-to-remediation loop](evidence-to-remediation-loop.md)
- [Missing telemetry](../playbooks/missing-telemetry.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)

