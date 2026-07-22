---
type: AWS Feature
title: RDS Proxy
parent_services: ["RDS"]
description: Pools supported database connections so bursts consume fewer backend sessions without adding database compute or caching queries.
tags: ["soa-c03", "domain-1", "domain-2", "rds", "proxy", "connections"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.5", "2.1.3", "2.3.2"]
domain_ids: ["1", "2"]
sources:
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
status: verified
---

# Core model

`application connections -> proxy pool -> supported RDS or Aurora target`

Use it for connection churn or bursts. It is not a read replica, cache, storage scaler, or substitute for SQL and wait analysis.

# Recovery boundary

After database restore, register or select the recovered target and verify credentials, networking, endpoint use, connection health, transactions, and application behavior.

# Sources

- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
