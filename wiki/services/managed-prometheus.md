---
type: AWS Service
title: Managed Service for Prometheus
service_id: managed-prometheus
description: Stores and queries Prometheus-compatible metrics for container and application monitoring.
tags: ["soa-c03", "domain-1", "prometheus", "metrics"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
status: verified
---

# Core model

`Prometheus-format metrics -> authorized collection -> workspace -> PromQL query -> dashboard or alert consumer`

Choose it when Prometheus metrics and PromQL are explicit requirements. It does not replace logs, traces, or AWS API audit history.

# Evidence and failure modes

Check collector scope, scrape target, labels, remote-write path, workspace identity, permissions, Region, query, and time range.

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
