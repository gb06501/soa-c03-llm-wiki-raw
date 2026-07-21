---
type: AWS Service
title: EC2 performance
description: Diagnoses EC2 health and the lowest limiting compute, memory, storage, network, or placement layer.
tags: [soa-c03, domain-1, ec2, performance, health]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.2", "1.2.1", "1.3.1", "1.3.2", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Core model

An instance type defines CPU, memory, network, and EBS capability. Workload performance is constrained by the lowest limiting layer.

```text
high CPU + high latency -> compute pressure possible
low CPU + high latency -> inspect memory, storage, network, and dependencies
```

# Health signals and actions

| Signal | Meaning | First direction |
| --- | --- | --- |
| System status failure | AWS host/infrastructure path | Recover, stop/start, or replace as appropriate |
| Instance status failure | Guest OS, startup, or guest network | Reboot, inspect OS/console, repair or replace |
| Scheduled event | Planned maintenance or retirement | Act before deadline |

Reboot restarts the guest. Stop/start can move an EBS-backed instance to a new host. Auto Scaling replacement restores fleet service.

# Persistence

- EBS is persistent, AZ-scoped block storage.
- Instance store is physically attached and ephemeral.
- Instance-store data is lost on stop, termination, or host loss.
- Stop/start can change an auto-assigned public IPv4; use an Elastic IP or DNS abstraction when stability is required.

# Network and placement

Inspect bandwidth, packet rate, flows, ENI capability, and enhanced-networking support. Low byte throughput does not rule out latency, packet, routing, DNS, or security-path failure.

| Placement group | Fit | Trade-off |
| --- | --- | --- |
| Cluster | Tightly coupled low-latency workload in one AZ | Correlated capacity/failure risk |
| Spread | Few critical instances on distinct hardware | Limited scale |
| Partition | Large distributed fleet using hardware partitions | Application must place replicas correctly |

# Optimization

- Resize for sustained compute, memory, network, or EBS need.
- Scale horizontally for variable stateless demand.
- Choose an instance family matching the proven bottleneck.
- Validate AMI architecture, ENA/EFA support, licensing, and AZ capacity.
- Update launch templates and replace or refresh fleets for repeatability.

# Exam traps

- CPU is not the only instance limit.
- A larger EBS volume cannot exceed the EC2 EBS ceiling.
- Cluster placement is not multi-AZ availability.
- Savings Plans lower eligible compute price; they do not resize resources.
- Downsizing without guest memory metrics is guesswork.

# Related concepts

- [CloudWatch Agent](cloudwatch-agent.md)
- [EBS performance](ebs-performance.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)
- [Evidence-to-remediation loop](../concepts/evidence-to-remediation-loop.md)

# Sources

- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
