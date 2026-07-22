---
type: AWS Service
title: X-Ray
service_id: x-ray
description: Traces requests across supported services so operators can locate latency, errors, and dependency boundaries.
tags: ["soa-c03", "domain-1", "x-ray", "tracing"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
status: verified
---

# Core model

`request -> trace -> segments/subsegments -> service map -> latency or error boundary`

Use tracing for request-path questions. Metrics quantify behavior, logs explain messages, and CloudTrail records API activity; none alone replaces a trace.

# Evidence and failure modes

Verify instrumentation, sampling, trace context propagation, permissions, service integration, account, Region, and time range before interpreting a missing path.

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
