---
type: Concept
title: Deployment strategies
description: Compares deployment blast radius, coexistence, traffic movement, health gates, capacity, and rollback.
tags: [soa-c03, domain-3, deployment, canary, blue-green]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.5"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
status: verified
---

# Core model

Every release chooses how much changes, whether old and new coexist, how traffic moves, which evidence proves health, and which immutable reference enables rollback.

# Strategy comparison

| Strategy | Dominant behavior | Main trade-off |
| --- | --- | --- |
| All-at-once / in-place | change the whole existing fleet | low extra cost, high blast radius |
| Rolling | replace batches | mixed versions and possible capacity dip |
| Immutable | build a new fleet | strong isolation, temporary duplicate capacity |
| Blue/green | switch between complete environments | fast switch, highest temporary footprint |
| Canary | send a small percentage first | limited initial blast, needs representative evidence |
| Linear | increase traffic by fixed steps | gradual exposure, longer rollout |

# Capacity and compatibility

Rolling, immutable, and blue/green may require old plus new quota, subnet IPs, compute, and target registrations. Coexisting versions require compatible APIs, sessions, configuration, and data schema.

# Health and rollback

Use version-specific infrastructure, target, application, dependency, and business evidence. Define alarms, missing-data treatment, bake time, and stop/rollback criteria before deployment. Keep the prior AMI, task definition and digest, Lambda version, or launch-template version until the rollback window closes.

Traffic rollback does not undo database writes or destructive schema changes.

# Related concepts

- [Strategy selection](../decision-guides/deployment-strategy-selection.md)
- [Deployment rollback](../playbooks/deployment-rollback.md)
- [Image management](../services/image-management.md)

# Sources

- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
