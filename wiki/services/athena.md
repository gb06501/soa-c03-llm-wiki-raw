---
type: AWS Service
title: Athena
service_id: athena
description: Queries S3-resident network logs and cost line items with SQL for repeatable operational analysis.
tags: ["soa-c03", "domain-5", "athena", "log-analysis"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["5.1.4", "5.3.2", "1.1.1", "1.3.1"]
domain_ids: ["5", "1"]
sources:
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
status: verified
---
# Core model

Athena runs SQL against data in S3. It is an analysis surface for detailed Cost and Usage Report data, VPC Flow Logs, load-balancer logs, CloudFront logs, WAF logs, and other structured network evidence.

# Decision boundaries

Use CloudWatch Logs Insights for interactive queries over CloudWatch Logs. Use Athena for high-volume, retained S3 datasets and cross-period analysis. Partition and select columns intentionally to control scan cost.

# Evidence workflow

Define the correct schema and partitions, normalize UTC time, filter to the exact resource/request/flow, correlate identifiers across datasets, and compare the last observed good layer with the first bad layer.

# Safe operations

Protect result locations, encrypt logs and query output, restrict sensitive fields, lifecycle retained data intentionally, and validate queries on a narrow partition before large scans.

# Related decisions

- [Network log selection](../decision-guides/network-log-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Operational analysis

Athena applies SQL to structured evidence stored in S3, including historical logs and optimization exports. It is a query layer; collection, delivery, schema, partitioning, and source completeness remain separate.

# Sources

- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)

