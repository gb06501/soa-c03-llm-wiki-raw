---
type: AWS Service
title: Application Auto Scaling
service_id: application-auto-scaling
description: Registers supported scalable targets and applies bounded scaling policies to service dimensions such as DynamoDB capacity.
tags: ["soa-c03", "domain-2", "application-auto-scaling", "scaling"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["2.1.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
status: verified
---

# Core model

`service dimension -> scalable target -> minimum/maximum -> policy -> CloudWatch evidence -> capacity change`

For DynamoDB provisioned capacity, configure table and index dimensions separately where required. Auto scaling is reactive and cannot repair a hot partition or an unsuitable key.

# Evidence and failure modes

Check registered target, resource identifier, min/max, policy, metric, managed alarms, current capacity, throttling, scaling activity, and uneven traffic.

# Sources

- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
