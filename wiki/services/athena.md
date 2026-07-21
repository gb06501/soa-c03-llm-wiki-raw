---
type: AWS Service
title: Athena
service_id: athena
description: Queries S3-resident network logs and cost line items with SQL for repeatable operational analysis.
tags: ["soa-c03", "domain-5", "athena", "log-analysis"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.4", "5.3.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---
# Core model

Athena runs SQL against data in S3. For Domain 5 it is an analysis surface for detailed Cost and Usage Report data, VPC Flow Logs, load-balancer logs, CloudFront logs, WAF logs, and other structured network evidence.

# Decision boundaries

Use CloudWatch Logs Insights for interactive queries over CloudWatch Logs. Use Athena for high-volume, retained S3 datasets and cross-period analysis. Partition and select columns intentionally to control scan cost.

# Evidence workflow

Define the correct schema and partitions, normalize UTC time, filter to the exact resource/request/flow, correlate identifiers across datasets, and compare the last observed good layer with the first bad layer.

# Safe operations

Protect result locations, encrypt logs and query output, restrict sensitive fields, lifecycle retained data intentionally, and validate queries on a narrow partition before large scans.

# Related decisions

- [Network log selection](../decision-guides/network-log-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Sources

- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
