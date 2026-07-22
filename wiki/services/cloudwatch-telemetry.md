---
type: AWS Service
title: CloudWatch
service_id: cloudwatch
description: Collects and relates metrics, logs, traces, alarms, dashboards, and operational evidence.
tags: [soa-c03, domain-1, cloudwatch, observability, domain-5, network-monitoring]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.1", "1.1.2", "1.2.1", "5.3.2", "5.3.5", "1.1.3", "1.1.4", "1.3.1", "1.3.2", "1.3.5", "1.3.6", "2.1.1", "2.1.3", "2.2.1"]
domain_ids: ["1", "5", "2"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
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

# Domain 5: Network monitoring

CloudWatch network evidence includes configured hybrid probes, actual supported flow performance, public internet health events, scripted canaries, component metrics, alarms, dashboards, and Logs Insights.

Choose the monitor by question: Network Synthetic Monitor for configured paths, Network Flow Monitor for real TCP flows, Internet Monitor for geography/ASN public impact, Synthetics for application journeys, and component metrics/logs for NAT, VPN, TGW, ELB, Route 53, firewall, and accelerator diagnosis.

Preserve AZ, tunnel, attachment, target, geography, ASN, probe, and flow dimensions. Metrics detect and scope symptoms; logs, configuration, and application evidence establish cause and recovery.

- [Network monitor selection](../decision-guides/network-monitor-selection.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Corpus reconciliation: Domains 1 and 2

## Metrics, logs, alarms, and views

Metrics quantify resource behavior; logs preserve messages; alarms evaluate time-series conditions; dashboards combine widgets and queries. Missing guest or container telemetry is a collection problem until agent, scope, permissions, and destination are proven.

## Evidence order

`symptom -> resource metric -> workload or database detail -> matching log -> recent change -> service health -> remediation evidence`

Alarm state does not prove action delivery. A dashboard is a view, not an alert. Scaling and health integrations consume CloudWatch evidence but retain their own configuration and failure boundaries.

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
