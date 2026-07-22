---
type: AWS Service
title: ECS
service_id: ecs
description: Runs versioned container tasks and controls service capacity, rolling deployment, health, and blue-green traffic transitions.
tags: [soa-c03, domain-3, ecs, containers, deployment, domain-5, network-logs]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["3.1.3", "3.1.5", "5.3.2", "1.1.1", "1.1.2", "1.2.1", "1.3.1", "2.1.1", "2.3.2"]
domain_ids: ["3", "5", "1", "2"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
status: verified
---

# Core model

```text
service + task-definition revision + desired count
  -> start new tasks -> readiness and target health -> drain old tasks
```

# Deployment controls

`minimumHealthyPercent` limits how low healthy running tasks may fall. `maximumPercent` limits temporary old-plus-new tasks. Circuit breaker, rollback, alarms, target health, grace period, and capacity provider behavior determine progress and recovery.

A deployment may need additional CPU, memory, ENIs, subnet IPs, target registrations, or container-instance/Fargate capacity.

# Evidence

Use ECS service events, deployment state, task stopped reasons, container logs, task definition and image digest, task execution role, secrets/KMS access, cluster capacity, network path, and target-health reasons.

# Failure boundaries

Tasks that never start point to capacity, IPs, image, role, secret, or task-definition configuration. Tasks that start then stop point to container/runtime evidence. Running but unhealthy tasks point to port mapping, health path, security groups, readiness, or dependency access.

# Rollback

Keep the prior task-definition revision and ECR digest. Drain connections deliberately, preserve mixed-version compatibility, and verify steady state and business results after rollback.

# Related concepts

- [ECR](ecr.md)
- [Deployment strategies](../concepts/deployment-strategies.md)
- [Deployment rollback](../playbooks/deployment-rollback.md)

# Domain 5: Network request evidence

Trace an ECS request through load-balancer logs and target status, task ENI Flow Logs, service/task events, configured stdout/stderr log driver, FireLens/router evidence, health checks, agent logs for EC2 launch type, DNS, and dependencies.

A task-role AccessDenied and a network timeout require different evidence. A healthy container process does not prove the target, sidecar, security group, route, or dependency path.

- [Network log selection](../decision-guides/network-log-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Corpus reconciliation: Domains 1 and 2

## Monitoring and scaling

Container evidence spans cluster, service, task, container, host capacity, placement, and application behavior. Increasing desired tasks does not help when no cluster capacity or subnet address is available. Service scaling and capacity-provider or EC2 scaling are separate layers.

## Recovery dependency

Restored databases or changed endpoints require task-definition or application configuration updates before ECS workloads use the recovered dependency.

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
