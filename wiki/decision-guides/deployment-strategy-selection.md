---
type: Decision Guide
title: Deployment strategy selection
description: Selects all-at-once, rolling, immutable, blue/green, canary, or linear deployment from risk and capacity clues.
tags: [soa-c03, domain-3, deployment-strategy]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.5"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Downtime accepted; no spare capacity | fast whole-fleet change | all-at-once/in-place |
| Replace a few units at a time | bounded batches | rolling |
| Never modify old compute | new isolated fleet | immutable |
| Complete parallel environment and fast switch | traffic cutover and quick reversal | blue/green |
| Small initial traffic percentage | limited first exposure | canary |
| Fixed traffic increments over time | gradual scheduled exposure | linear |
| ASG replace nonmatching instances | health-governed instance turnover | instance refresh |
| Lambda stable endpoint with weighted versions | immutable function versions | alias routing |

# Rejection rules

- Do not assume rolling means zero downtime.
- Do not confuse blue/green environments with canary/linear traffic patterns.
- Do not select a strategy without checking surge quota and subnet IPs.
- Do not expect traffic rollback to reverse data mutations.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Deployment strategies](/concepts/deployment-strategies.md)
- [Deployment rollback](/playbooks/deployment-rollback.md)

# Sources

- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
