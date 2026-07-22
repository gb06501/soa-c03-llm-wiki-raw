---
type: AWS Service
title: EKS
service_id: eks
description: Runs Kubernetes workloads whose deployment health depends on pods, nodes, images, IAM, networking, and cluster capacity.
tags: [soa-c03, domain-3, eks, kubernetes, deployment, domain-5, network-logs]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["3.1.3", "5.3.2", "1.1.1", "1.1.2", "1.2.1", "1.3.1", "2.1.1", "2.3.2"]
domain_ids: ["3", "5", "1", "2"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
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

- [Deployment diagnostics](../concepts/deployment-diagnostics.md)
- [Deployment failure](../playbooks/deployment-failure.md)

# Network request evidence

Correlate ingress/controller logs, service and EndpointSlice state, pod current/previous logs and events, readiness/liveness, CoreDNS, VPC CNI/IP allocation, kube-proxy or data-plane evidence, node logs, enabled control-plane logs, and VPC/ELB evidence.

An application container can be healthy while an ingress, sidecar, network policy, DNS, CNI, target, or subnet-capacity layer fails.

- [Network log selection](../decision-guides/network-log-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Monitoring and scaling

Kubernetes evidence spans cluster, node, pod, container, resource requests, scheduler state, network addresses, and application behavior. Pod scaling and node scaling are separate; more pods require schedulable node capacity.

# Recovery dependency

A recovered backend is not in service until workload configuration, IAM, networking, and application discovery point EKS workloads to it.

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)

