---
type: AWS Service
title: Athena
service_id: athena
description: Queries structured data stored in S3 with SQL for interactive and repeatable analysis.
tags: ["soa-c03", "domain-5", "athena", "log-analysis"]
timestamp: 2026-07-22T05:15:00Z
skill_ids: ["1.1.1", "1.3.1", "5.1.4", "5.3.2"]
domain_ids: ["1", "5"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---
# Core model

Athena is a query layer over data stored in S3. Results depend on the selected dataset, schema, partitions, file layout, and query; Athena does not collect, normalize, or guarantee completeness of the underlying data. Use it for historical logs, Cost and Usage Report data, and other structured S3 datasets.

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

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
