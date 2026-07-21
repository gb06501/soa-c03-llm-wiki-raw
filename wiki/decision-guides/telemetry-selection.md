---
type: Decision Guide
title: Telemetry selection
description: Selects the evidence type, collection mechanism, and AWS observability service from an operational question.
tags: [soa-c03, domain-1, observability, telemetry, selection]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.1.1", "1.1.2"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
status: verified
---

# Decision table

| Operational need | Choose | Decisive clue |
| --- | --- | --- |
| Resource or application measurement over time | CloudWatch Metrics | Numeric series with namespace and dimensions |
| Application or system records | CloudWatch Logs | Timestamped events that must be searched or retained |
| Identify who changed an AWS resource | CloudTrail | Control-plane or enabled data-event audit |
| Follow a request across services | X-Ray or CloudWatch tracing views | End-to-end request path |
| ECS/EKS resource visibility | Container Insights | Cluster, node, pod, task, or container scope |
| PromQL and Prometheus data model | Amazon Managed Service for Prometheus | Prometheus ingestion and query semantics |
| Visualize several data sources | Amazon Managed Grafana | Visualization, not telemetry collection |
| Stream telemetry to another destination | Data Firehose | Delivery pipeline |
| Query historical logs already in S3 | Athena | SQL over S3 data |
| Guest memory, filesystem, process, or selected logs | CloudWatch agent | Data is not supplied by native EC2 metrics |

# Rejection rules

- Do not use CloudTrail as application logging.
- Do not expect CloudWatch Logs to identify every AWS API caller.
- Do not install the CloudWatch agent on Lambda.
- Do not choose Grafana when the missing requirement is collection.
- Do not treat an empty graph as proof that the workload emitted no data; verify Region, namespace, dimensions, permissions, and collection.

# Evidence and verification

Verify the collector or source is enabled, the destination Region is correct, the expected namespace or log group exists, dimensions or labels match, and a recent datapoint or event is visible.

# Related concepts

- [CloudWatch telemetry](../services/cloudwatch-telemetry.md)
- [CloudWatch Agent](../services/cloudwatch-agent.md)
- [Missing telemetry](../playbooks/missing-telemetry.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
