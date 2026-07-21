---
type: AWS Feature
title: RDS Performance Insights
parent_services: ["RDS"]
description: Exposes database-load, wait, and SQL evidence through the RDS performance observability surface and API.
tags: ["soa-c03", "domain-1", "rds", "performance-insights"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.5"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
status: verified
---

# Core model

`database activity -> DB load and waits -> dimensions such as SQL, user, and host -> tuning evidence`

The source distinguishes the continuing API from the console experience moving to CloudWatch Database Insights. Preserve that boundary when interpreting older exam wording.

# Evidence and failure modes

Check enablement, retention or mode where applicable, time range, DB load, top waits, SQL, resource metrics, logs, and whether the workload is actually connection-, compute-, storage-, or query-bound.

# Sources

- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
