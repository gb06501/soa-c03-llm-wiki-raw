---
type: Decision Guide
title: Storage service selection
description: Chooses block, object, shared file, parallel file, or hybrid storage from semantics and performance requirements.
tags: [soa-c03, domain-1, storage, selection]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.3.2", "1.3.3", "1.3.4", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Decision sequence

1. Does the application require block, object, or mounted-file semantics?
2. Which protocol and operating system must clients use?
3. Is access single-host, shared, parallel, or hybrid?
4. Is data durable or disposable?
5. Which IOPS, throughput, latency, resilience, and lifecycle behavior is required?

# Selection table

| Requirement | Choice |
| --- | --- |
| Persistent EC2 block device | EBS |
| Disposable local scratch/cache | Instance store |
| Object API and object-scale storage | S3 |
| Shared Linux NFS | EFS |
| Windows SMB/AD | FSx for Windows File Server |
| HPC/ML parallel filesystem | FSx for Lustre |
| Enterprise NFS/SMB/iSCSI | FSx for NetApp ONTAP |
| S3-resident data with file access | S3 Files |
| Hybrid local file/block/tape interface | Storage Gateway |

# Performance refinement

- For EBS, distinguish IOPS, throughput, latency, queue, volume limit, and EC2 limit.
- For S3, separate transfer speed, request behavior, caching, data movement, and lifecycle.
- For EFS, choose performance mode separately from throughput mode.
- For FSx, choose the correct filesystem family before tuning deployment and throughput.

# Rejection rules

- Do not choose S3 when POSIX/NFS/SMB semantics are required.
- Do not choose EFS for native Windows SMB.
- Do not use instance store for irreplaceable data.
- Do not choose an HDD EBS type for small random transactional I/O.
- Do not use Lifecycle as a fix for active-data performance.

# Related concepts

- [EBS performance](../services/ebs-performance.md)
- [S3 performance](../services/s3-performance.md)
- [Shared storage](../services/shared-storage.md)
- [EC2 performance](../services/ec2-performance.md)

# Sources

- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
