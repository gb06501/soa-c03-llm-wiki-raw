---
type: AWS Service
title: Compute Optimizer
service_id: compute-optimizer
description: Produces utilization-informed compute recommendations that require workload and risk validation before change.
tags: ["soa-c03", "domain-1", "compute-optimizer", "rightsizing"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
status: verified
---

# Core model

`historical utilization -> recommendation -> workload constraints -> controlled change -> performance and cost verification`

Treat recommendations as candidates. Peak demand, guest memory visibility, network and EBS ceilings, architecture, availability, and downstream capacity can reject a smaller target.

# Evidence and safety

Correlate recommendation scope with metrics, tags, owners, cost evidence, planned demand, rollback, and post-change latency, errors, saturation, and spend.

# Sources

- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
