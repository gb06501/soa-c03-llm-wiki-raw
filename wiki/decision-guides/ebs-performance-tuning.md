---
type: Decision Guide
title: EBS performance tuning
description: Selects an EBS change by separating IOPS, throughput, latency, queue, initialization, and EC2 limits.
tags: [soa-c03, domain-1, ebs, storage, performance]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.3.2", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Decision table

| Evidence or requirement | Direction |
| --- | --- |
| Small random transactional I/O | IOPS-oriented volume and settings |
| Large sequential transfer | Throughput-oriented volume and settings |
| Provisioned performance is below demand | Increase the proven IOPS or throughput control |
| Volume appears capable but instance path is capped | Change EC2 type or EBS capability |
| Queue and latency rise together | Confirm saturation, request shape, and all path limits |
| New or restored blocks show first-read delay | Initialize or read blocks when predictable performance is required |
| Filesystem reports full but EBS metrics look normal | Repair or expand the filesystem/storage allocation layer |
| Workload needs persistent block storage | EBS |
| Data is disposable scratch and local speed is decisive | Instance store |

Choose the volume type first, then provisioned size, IOPS, throughput, attachment, EC2 capability, and filesystem behavior as one path.

# Rejection rules

- EBS metrics do not show filesystem free space.
- Increasing IOPS does not fix a throughput, EC2, filesystem, or application bottleneck.
- An HDD-oriented volume is not the default answer for small random transactional I/O.
- Volume capability and EC2 capability must both support the target.
- Snapshot completion does not guarantee every block has already delivered predictable first-read latency.

# Evidence and verification

Inspect latency, queue, operations, bytes, burst or provisioned controls, EC2 EBS capability, filesystem state, and workload request shape. Change one constraint and verify latency, queue, throughput, errors, and cost.

# Related concepts

- [EBS performance](../services/ebs-performance.md)
- [EC2 performance](../services/ec2-performance.md)
- [Compute optimization](compute-optimization.md)

# Sources

- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
