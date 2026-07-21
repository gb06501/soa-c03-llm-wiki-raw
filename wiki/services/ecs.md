---
type: AWS Service
title: ECS
service_id: ecs
description: Runs versioned container tasks and controls service capacity, rolling deployment, health, and blue-green traffic transitions.
tags: [soa-c03, domain-3, ecs, containers, deployment]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.3", "3.1.5"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
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

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
