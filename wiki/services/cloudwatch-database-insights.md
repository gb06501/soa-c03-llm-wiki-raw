---
type: AWS Feature
title: CloudWatch Database Insights
parent_services: ["CloudWatch", "RDS"]
description: Organizes database load, waits, SQL, users, and hosts for database-layer performance diagnosis.
tags: ["soa-c03", "domain-1", "cloudwatch", "database-insights", "rds"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.5"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
status: verified
---

# Core model

`database activity -> DB load -> waits -> SQL, user, and host dimensions -> bottleneck decision`

Use Database Insights for database-engine load questions. CloudWatch resource metrics, Enhanced Monitoring, database logs, and application traces answer different layers.

# Evidence and failure modes

Check database selection, mode and retention where applicable, time window, DB load, top waits, SQL, hosts, users, resource saturation, and correlated logs.

# Sources

- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
