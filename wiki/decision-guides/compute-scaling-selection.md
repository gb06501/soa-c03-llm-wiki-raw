---
type: Decision Guide
title: Compute scaling selection
description: Selects a scaling policy and capacity surface from demand shape, metric behavior, and workload architecture.
tags: [soa-c03, domain-2, scaling, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Keep a utilization or request metric near a goal | Target tracking |
| Apply different changes for different breach sizes | Step scaling |
| Prepare for a known timetable | Scheduled scaling |
| Prepare for recurring forecastable demand | Predictive scaling |
| Change EC2 fleet capacity | EC2 Auto Scaling |
| Change ECS task count | ECS Service Auto Scaling |
| Change EKS workload replicas | Pod/workload scaling |
| Add EKS worker capacity | Node or cluster scaling |
| Bound Lambda execution capacity | Reserved/account concurrency controls |
| Reduce Lambda cold-start readiness delay | Provisioned concurrency |

Set minimum for required availability, maximum for safety and quota, and warmup or grace behavior for real startup time.

# Rejection rules

- A scaling policy does not repair an invalid launch template.
- Raising desired capacity does not bypass quota, subnet-IP, or EC2-capacity failures.
- Scheduled scaling is not reactive.
- Scaling tasks cannot help when the cluster has no placement capacity.
- More capacity is unsafe when a downstream system is already limited.

# Evidence and verification

Verify the chosen metric follows demand and responds to capacity, the policy changes desired capacity, new capacity becomes healthy, latency or backlog recovers, scale-in is stable, and dependencies remain healthy.

# Related concepts

- [Compute scaling](../services/compute-scaling.md)
- [Scaling failure](../playbooks/scaling-failure.md)

# Sources

- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
