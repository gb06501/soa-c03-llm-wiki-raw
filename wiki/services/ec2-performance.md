---
type: AWS Service
title: EC2
service_id: ec2
description: Runs virtual machine instances from versioned images with observable compute, storage, network, health, and deployment behavior.
tags: [soa-c03, domain-1, ec2, performance, health]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.2", "1.2.1", "1.3.1", "1.3.2", "1.3.6", "3.1.1", "3.1.3", "3.1.5", "1.1.1", "1.1.3", "2.1.1", "2.2.2", "2.3.1"]
domain_ids: ["1", "3", "2"]
sources:
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
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

# AMIs and deployment

An AMI combines Region-specific metadata, block-device mappings, and backing snapshots. Before launch, verify owner and permission, Region, architecture, boot/root compatibility, drivers, snapshot and KMS access, launch-template version, IAM profile, subnet capacity, and user-data behavior.

Image creation normally reboots for consistency. A no-reboot capture can be crash-consistent unless application writes are quiesced. Deregistration prevents new launches but does not terminate existing instances or automatically remove every snapshot.

During deployment, separate control-plane launch success from bootstrap, dependency, target-health, and application evidence. Instance refresh belongs to [EC2 Auto Scaling](ec2-auto-scaling.md).

# Health, capacity, storage, and network

System status failures point first to the AWS host path; instance status failures point first to guest startup, OS, or networking. Instance type bounds CPU, memory, network, and EBS capability. Guest memory and filesystem evidence requires an agent.

# Persistence and recovery

EBS persists independently of a running instance; instance store is disposable across stop, termination, or host loss. Reboot, stop/start, resize, Auto Scaling replacement, AMI recovery, and backup restore have different state and identity effects.

# Placement and scaling

Cluster placement optimizes close communication inside one AZ; spread and partition placement reduce different hardware-sharing risks. None replaces multi-AZ application design. A launch-template update affects new instances until replacement or refresh occurs.

# Sources

- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)

