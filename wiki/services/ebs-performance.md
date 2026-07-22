---
type: AWS Service
title: EBS
service_id: ebs
description: Provides EC2 block storage with measurable IOPS, throughput, latency, queue, and initialization behavior.
tags: [soa-c03, domain-1, ebs, storage, performance]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.2.1", "1.3.1", "1.3.2", "1.3.6", "2.2.2", "2.3.1"]
domain_ids: ["1", "2"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Core model

```text
application I/O -> filesystem -> EBS volume -> EC2 EBS capability
actual performance = lowest limiting layer
```

IOPS is operation rate. Throughput is data rate. Latency is time per operation. Queue length is waiting work.

# Volume choice

| Workload | Likely type |
| --- | --- |
| General SSD | `gp3` |
| Critical consistent high IOPS | `io2` |
| Large sequential throughput | `st1` |
| Cold sequential data | `sc1` |

`gp3` decouples size, IOPS, and throughput. `gp2` performance is linked to size and burst behavior. HDD types do not fit small random transactional I/O and are not boot-volume choices.

# Diagnostic patterns

| Evidence | Direction |
| --- | --- |
| High queue, latency, and max IOPS | IOPS saturation likely |
| Sequential workload at throughput ceiling | Throughput saturation likely |
| Low `BurstBalance` with slowdown | Burst credits exhausted where applicable |
| Volume below limits but application slow | EC2 ceiling, filesystem, application, or dependency |
| Restored volume slow on first reads | Lazy block loading/initialization |

Filesystem free space is not native EBS telemetry; collect it from the OS or CloudWatch Agent.

# Safe change path

Elastic Volumes can modify supported type, size, IOPS, and throughput. Monitor modification state, then extend the partition/filesystem when capacity increases. Increasing the volume does not grow the filesystem automatically, and a volume cannot simply be shrunk in place.

# Exam traps

- Volume capability and EC2 EBS capability are separate limits.
- Larger `gp3` does not automatically raise IOPS or throughput.
- High queue alone is not proof of a bottleneck.
- Snapshot restore can have a first-read penalty.
- EBS volumes are AZ-scoped even though snapshots support recreation elsewhere.

# Related concepts

- [EC2 performance](ec2-performance.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)
- [Storage service selection](../decision-guides/storage-service-selection.md)

# Performance and scope

Effective storage performance is limited by the lower of volume capability, EC2 EBS capability, filesystem behavior, and application I/O pattern. Queue, latency, IOPS, throughput, burst state, and instance ceiling must be separated.

# Snapshot and recovery

An EBS volume is AZ-scoped. A snapshot is a recovery object, not a live standby. Restored blocks can require initialization before predictable performance, and increasing a volume does not automatically grow its filesystem.

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)

