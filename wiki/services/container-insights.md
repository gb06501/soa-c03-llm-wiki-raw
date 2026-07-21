---
type: AWS Feature
title: Container Insights
parent_services: ["CloudWatch"]
description: Collects and organizes container telemetry across cluster, node, service, task, pod, and container scopes.
tags: ["soa-c03", "domain-1", "cloudwatch", "container-insights"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.1", "1.1.2"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
status: verified
---

# Core model

`collector or add-on -> scoped container telemetry -> CloudWatch metrics and logs -> Container Insights views`

The correct scope matters: ECS service and task evidence differs from EKS node, pod, and container evidence.

# Evidence and failure modes

Check enablement, collector deployment, permissions, network path, namespace, cluster identity, account, Region, dimensions, log groups, and time range.

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
