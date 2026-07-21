---
type: AWS Service
title: Compute scaling
description: Explains scaling controls and evidence across EC2 Auto Scaling, ECS, EKS, and Lambda.
tags: [soa-c03, domain-2, scaling, compute]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
status: verified
---

# Core model

```text
demand -> policy and limits -> desired capacity -> launch or schedule -> health -> usable capacity
```

Scaling changes capacity. The launch template or workload definition determines what the new capacity is.

# Scaling surfaces

| Surface | Capacity unit | Important controls |
| --- | --- | --- |
| EC2 Auto Scaling | EC2 instance | launch template, min/desired/max, AZs, health, warmup |
| ECS Service Auto Scaling | task | desired task count, service metric, cluster capacity |
| EKS workload | pod | resource requests and workload scaling |
| EKS cluster | node | node capacity, quotas, subnet IPs |
| Lambda | concurrent execution | reserved/account concurrency and event-source behavior |

# Policy behavior

- Target tracking keeps an appropriate utilization or request metric near a target.
- Step scaling changes capacity by breach size.
- Scheduled scaling prepares for known time-based demand.
- Predictive capacity can prepare for recurring patterns.
- Warmup, cooldown, grace period, and lifecycle hooks affect when capacity becomes usable or replaceable.

# Evidence

Trace the policy metric and alarm, scaling activity, desired/min/max values, launch-template version, instance or task events, health state, quotas, subnet IPs, and downstream load.

# Failure modes

- Desired capacity rises but launch fails.
- New instances are replaced before startup completes.
- ECS tasks or EKS pods wait for underlying capacity.
- Maximum capacity blocks scale-out.
- Sensitive thresholds and missing warmup cause oscillation.
- Lambda throttles at a concurrency boundary.

# Exam traps

- EC2 health can pass while application health fails.
- Task scaling and cluster scaling are different.
- Pod scaling and node scaling are different.
- Provisioned and reserved Lambda concurrency solve different problems.
- More consumers can overload a database or dependency.

# Related concepts

- [Compute scaling selection](../decision-guides/compute-scaling-selection.md)
- [Scaling failure](../playbooks/scaling-failure.md)
- [Compute optimization](../decision-guides/compute-optimization.md)

# Sources

- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
