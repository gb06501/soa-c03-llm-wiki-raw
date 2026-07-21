---
type: AWS Service
title: EKS
service_id: eks
description: Runs Kubernetes workloads whose deployment health depends on pods, nodes, images, IAM, networking, and cluster capacity.
tags: [soa-c03, domain-3, eks, kubernetes, deployment]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.3"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
status: verified
---

# Core model

```text
workload definition -> pod scheduling -> node and network capacity -> image pull -> readiness -> service traffic
```

# Deployment evidence

Use pod status and events, replica and rollout state, node readiness, resource requests, cluster capacity, subnet IPs, ECR image/tag/digest, node or workload identity, secret/KMS access, container logs, and load-balancer health.

# Failure boundaries

Pending pods point to resource requests, node capacity, placement, quotas, or IP availability. Image-pull failures point to identity, repository/KMS permission, DNS, endpoints or NAT, and architecture. Running but unready pods point to probes, application startup, dependency access, or configuration.

A healthy control plane does not prove workload health. Adding pods does not help when nodes or subnet addresses are the limiting layer.

# Safe action

Correct the narrow scheduling, identity, image, network, or readiness gate. Preserve the prior workload specification and image digest, limit rollout exposure, and avoid increasing concurrency until downstream capacity is verified.

# Verification

Confirm desired replicas are scheduled and ready, the intended image digest is running, service and load-balancer paths are healthy, errors recover, and no repeated rollout or replacement loop remains.

# Related concepts

- [Deployment diagnostics](/concepts/deployment-diagnostics.md)
- [Deployment failure](/playbooks/deployment-failure.md)

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
