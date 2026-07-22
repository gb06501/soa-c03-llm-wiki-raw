---
type: AWS Service
title: EC2 Auto Scaling
service_id: ec2-auto-scaling
description: Maintains EC2 group capacity and replaces instances through health-governed scaling and instance refresh.
tags: [soa-c03, domain-3, ec2, auto-scaling]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.3", "1.2.1", "1.3.1", "1.3.6", "2.1.1", "2.2.2", "3.1.5"]
domain_ids: ["1", "2", "3"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
status: verified
---

# Core model

```text
launch template + min/desired/max + policy -> instances -> health -> usable capacity
new desired configuration -> instance refresh -> controlled replacement
```

# Instance refresh controls

Use launch-template version, minimum and maximum healthy percentages, instance warmup, checkpoints, checkpoint delay, skip matching, alarms, bake time, and automatic rollback where configured.

Minimum healthy capacity protects availability. Maximum healthy capacity permits surge. Both interact with quota, AZ capacity, subnet IPs, health-check grace, and startup time.

# Failure evidence

If desired capacity changes but instances do not launch, inspect scaling activity, AMI and architecture, instance type, IAM profile, quota/capacity, and subnet IPs. If refresh stalls, inspect protected or standby instances, health failure, warmup, percentage constraints, and target registration.

# Rollback

Keep the known-good launch-template version and AMI. Rollback cannot succeed if the previous configuration is missing or the environment still blocks new launches.

# Related concepts

- [Compute scaling](compute-scaling.md)
- [Deployment strategies](../concepts/deployment-strategies.md)
- [Scaling failure](../playbooks/scaling-failure.md)

# Scaling policies and refresh

Target tracking maintains a metric target; step scaling maps breach ranges to adjustments; scheduled scaling follows known time; predictive scaling follows recurring forecasts. Minimum, desired, and maximum bound capacity.

A launch template defines new instances. Instance refresh replaces existing capacity in controlled batches. Grace period, warmup, health checks, lifecycle hooks, termination policy, subnet capacity, and downstream limits determine whether desired capacity becomes usable service.

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)

