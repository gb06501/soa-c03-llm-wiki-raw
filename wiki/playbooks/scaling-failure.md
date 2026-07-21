---
type: Troubleshooting Playbook
title: Scaling failure
description: Diagnoses absent, delayed, oscillating, or unusable scaling across compute environments.
tags: [soa-c03, domain-2, scaling, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
status: verified
---

# Trigger

Demand rises but usable capacity does not, capacity oscillates, or newly launched capacity never becomes healthy.

# Evidence path

1. Identify the capacity surface: EC2 instances, ECS tasks, EKS pods/nodes, or Lambda concurrency.
2. Inspect demand, policy metric, alarm, policy, and recent scaling activity.
3. Compare desired capacity with minimum and maximum.
4. If desired changed, inspect launch or scheduling failures.
5. Check launch-template/workload version, IAM, quota, AZ capacity, and subnet IPs.
6. Trace health checks, startup, warmup, grace period, and replacement.
7. Inspect downstream load before forcing additional capacity.

# Failure map

| Symptom | Direction |
| --- | --- |
| No scale-out decision | Metric, alarm, policy, maximum, warmup/cooldown |
| Desired rises; no EC2 instance | AMI/type, quota/capacity, IAM, subnet IP |
| Repeated replacement | Health path, startup, grace period, user data |
| ECS tasks pending | Cluster capacity, placement, resources, IPs |
| EKS pods pending | Requests, node capacity, quotas, IPs |
| Lambda throttles | Reserved/account concurrency and downstream limit |
| Oscillation | Metric choice, target sensitivity, warmup/cooldown |

# Safe action

Correct the proven gate, preserve required minimum capacity, increase limits only with quota and dependency review, and change one policy variable at a time.

# Verification

Confirm desired and running capacity converge, new capacity becomes healthy, backlog/latency/errors recover, no replacement loop remains, scale-in is stable, and downstream metrics stay within limits.

# Sources

- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
