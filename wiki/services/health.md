---
type: AWS Service
title: Health
service_id: health
description: Reports AWS-side service events, planned maintenance, and resource impact for operational correlation.
tags: ["soa-c03", "domain-1", "health", "events"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.2.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
status: verified
---

# Core model

`AWS-side event -> affected service/resource scope -> event status -> operator correlation and action`

Use Health for AWS maintenance or service-impact evidence. It does not replace resource metrics, workload logs, deployment history, or request traces.

# Evidence and failure modes

Confirm account, Region or global scope, affected entity, event timing, status, and whether the workload symptom aligns with the event.

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
