---
type: AWS Feature
title: CloudWatch Network Flow Monitor
parent_services: [CloudWatch]
description: Observes performance of actual supported TCP workload flows with flow volume, latency, loss, and contributor evidence.
tags: ["soa-c03", "domain-5", "cloudwatch", "flow-monitor"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

Network Flow Monitor observes supported real workload flows through required coverage or agents. It answers how actual TCP flows are behaving, not whether a configured idle path would work.

# Evidence and diagnosis

Inspect coverage state, source/destination flow, time/AZ/Region, flow volume, round-trip time, loss or retransmission-style indicators, top contributors, network health indicator, component metrics, and application evidence.

# Decision boundaries

Use VPC Flow Logs for five-tuple and ACCEPT/REJECT metadata. Use Network Flow Monitor for performance health of real flows. Healthy network evidence does not prove DNS, TLS, authorization, or application behavior.

# Safe operations

Deploy coverage through controlled permissions, baseline representative traffic, preserve the exact failing dimensions, change one route/capacity/target, and verify both flow health and user outcome.

# Related pages

- [Network monitor selection](../decision-guides/network-monitor-selection.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
