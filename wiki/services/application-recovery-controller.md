---
type: AWS Service
title: Application Recovery Controller
service_id: application-recovery-controller
description: Controls and assesses supported application recovery paths through readiness, routing, and zonal traffic mechanisms.
tags: ["soa-c03", "domain-2", "application-recovery-controller", "resilience"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["2.2.2", "2.3.4"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Core model

`prepared recovery design -> readiness evidence -> routing or zonal control -> traffic change -> application validation`

Zonal shift, zonal autoshift, routing control, and readiness concepts affect traffic or preparedness. They do not copy data, create missing capacity, or repair unhealthy application dependencies.

# Evidence and safety

Confirm supported resource, control state, safety rules, healthy destination capacity, data readiness, DNS or accelerator behavior, application validation, and failback plan.

# Sources

- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
