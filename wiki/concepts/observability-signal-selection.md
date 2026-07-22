---
type: Concept
title: Observability signal selection
description: Chooses the evidence source from the operational question instead of from a preferred tool.
tags: [soa-c03, domain-1, observability, diagnosis]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.2.1", "1.3.5", "1.3.6", "1.1.5", "1.2.2", "1.2.3", "1.3.1", "1.3.2", "1.3.3", "1.3.4", "2.1.1", "2.1.2", "2.1.3", "2.2.1", "2.2.2", "2.3.1", "2.3.2", "2.3.3", "2.3.4"]
domain_ids: ["1", "2"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
  - /raw/skills/2.3.3-implement-versioning-for-storage-services.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
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

# Signal-class first

Choose the signal class before service-specific evidence. Then correlate scope, time, identity, recent change, dependency behavior, and a healthy baseline before remediation.

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.3](../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)

