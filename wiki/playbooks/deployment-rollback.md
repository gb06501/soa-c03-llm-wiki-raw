---
type: Troubleshooting Playbook
title: Deployment rollback
description: Stops or reverses unsafe releases while preserving data compatibility, evidence, and known-good artifacts.
tags: [soa-c03, domain-3, deployment, rollback]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.5"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
status: verified
---

# Trigger

A rolling, immutable, blue/green, canary, linear, ECS, ASG, or Lambda deployment stalls or harms service.

# Evidence path

1. Identify strategy, old/new versions, traffic percentage, batch, and rollback object.
2. Inspect version-specific infrastructure, target health, application, dependency, and business evidence.
3. Check readiness, warmup, deregistration, bake time, and alarm dimensions.
4. Verify surge compute, quota, subnet IPs, ENIs, and target capacity.
5. Check mixed-version API, session, configuration, and schema compatibility.
6. Confirm the known-good AMI, launch-template, task-definition digest, Lambda version, or blue environment still exists.

# Failure map

| Symptom | Direction |
| --- | --- |
| Rolling rollout freezes | health, percentage constraints, surge capacity/IPs |
| Canary appears healthy | insufficient traffic, bake time, or wrong aggregate metric |
| Blue/green switch fails | listener, target group, readiness, data compatibility |
| Compute rolls back; service does not | schema/data/config incompatibility |
| Old version still serves | traffic weight, listener/alias, long connections |
| Rollback artifact unavailable | lifecycle cleanup or mutable reference |

# Safe action

Stop further exposure. Route or restore compute to the pinned known-good version while preserving logs and the new environment for diagnosis. Do not attempt destructive schema reversal without a separate data recovery plan.

# Verification

Confirm traffic is on the intended version, errors/latency and business results recover, old connections drain safely, data remains compatible, capacity stabilizes, and the rollback artifact is retained until review.

# Related concepts

- [Deployment strategies](/concepts/deployment-strategies.md)
- [Strategy selection](/decision-guides/deployment-strategy-selection.md)

# Sources

- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
