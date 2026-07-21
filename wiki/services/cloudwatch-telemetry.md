---
type: AWS Service
title: CloudWatch
service_id: cloudwatch
description: Collects and relates metrics, logs, traces, alarms, dashboards, and operational evidence.
tags: [soa-c03, domain-1, cloudwatch, observability]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["1.1.1", "1.1.2", "1.2.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
status: verified
---

# Core model

```text
workload -> emits signal -> collector/service -> query, graph, alarm, or audit
```

CloudWatch Metrics answers quantitative resource and application questions. CloudWatch Logs stores timestamped messages. Neither replaces CloudTrail API audit history or distributed traces.

# Signal map

| Question | Evidence |
| --- | --- |
| Is CPU, latency, error rate, or capacity abnormal? | CloudWatch metrics |
| What error did the application or OS report? | CloudWatch or application logs |
| Who changed an AWS resource? | CloudTrail |
| Where is a request slow across services? | X-Ray or CloudWatch tracing views |
| Which pod, task, node, or container is pressured? | Container Insights |
| Which Prometheus series matches? | Amazon Managed Service for Prometheus |
| How can several data sources be visualized? | Amazon Managed Grafana |
| How can historical S3 logs be queried with SQL? | Athena |

# Important objects

- Metric identity: namespace, metric name, and dimensions.
- Metric evaluation: period and statistic.
- Log hierarchy: log group, log stream, log event.
- Metric filter: matching log event to metric.
- Subscription filter: matching log event to downstream destination.
- Logs Insights: interactive log query.
- CloudTrail trail: ongoing delivery of selected management or data events.

# Workload rules

- EC2 publishes native CPU, network, and status metrics.
- Guest memory, filesystem, and process telemetry requires an agent or custom collection.
- Lambda evidence includes invocations, errors, throttles, duration, and concurrency.
- ECS/EKS diagnosis needs workload and infrastructure scope: service/task or pod/node/container.

# Verification

1. Confirm the expected account and Region.
2. Confirm namespace, dimensions, log group, or trail scope.
3. Confirm recent datapoints or events exist.
4. Confirm the time range includes the symptom.
5. Correlate telemetry with recent changes and affected dependencies.

# Exam traps

- A missing dimension can look like missing telemetry.
- CloudTrail records API activity, not workload CPU or application errors.
- A dashboard displays existing telemetry; it does not collect it.
- Central visibility does not necessarily copy telemetry into one account.

# Related concepts

- [Observability signal selection](../concepts/observability-signal-selection.md)
- [CloudWatch Agent](cloudwatch-agent.md)
- [CloudWatch alarms](cloudwatch-alarms.md)
- [Missing telemetry](../playbooks/missing-telemetry.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)

