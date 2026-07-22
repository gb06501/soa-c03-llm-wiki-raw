---
type: AWS Service
title: Managed Grafana
service_id: managed-grafana
description: Builds managed dashboards from multiple authorized observability data sources.
tags: ["soa-c03", "domain-1", "grafana", "dashboards"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
status: verified
---

# Core model

`workspace -> data-source authorization -> query -> panel -> dashboard`

Use it when a dashboard must combine multiple data sources. A visualization is not a collection pipeline or an alarm-delivery guarantee.

# Evidence and failure modes

Check workspace access, data-source identity, role permissions, query, variables, Region, time range, and underlying source freshness.

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
