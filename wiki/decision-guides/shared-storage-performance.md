---
type: Decision Guide
title: Shared storage performance
description: Selects shared-storage family and performance controls from protocol, client, parallelism, throughput, and resilience requirements.
tags: [soa-c03, domain-1, efs, fsx, shared-storage, performance]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.3.3", "1.3.4"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
status: verified
---

# Decision table

| Requirement | Choice or control |
| --- | --- |
| Shared Linux NFS | EFS |
| Native Windows SMB with Active Directory | FSx for Windows File Server |
| HPC or ML parallel filesystem | FSx for Lustre |
| Enterprise NFS, SMB, or iSCSI features | FSx for NetApp ONTAP |
| Existing S3 data with file access | S3 Files |
| Hybrid local file, block, or tape interface | Storage Gateway |
| Most latency-sensitive EFS workloads | General Purpose performance mode |
| Very high EFS parallelism with latency trade-off | Max I/O performance mode |
| Throughput that follows activity | Elastic throughput |
| Throughput independent of stored size | Provisioned throughput |
| Size-linked baseline and credits | Bursting throughput |

Select the correct storage family and protocol before tuning performance mode, throughput mode, deployment, or lifecycle.

# Rejection rules

- EFS is NFS-focused; it is not native Windows SMB storage.
- An FSx family name is not enough; select the filesystem that matches the protocol and workload.
- EFS performance mode and throughput mode are different choices.
- Lifecycle changes storage class; it does not repair active-data throughput.
- Storage Gateway is a hybrid-access service, not a universal replacement for AWS filesystems.
- S3 object API and mounted filesystem semantics are different.

# Evidence and verification

Verify protocol and client compatibility, mount target or endpoint path, DNS and security, filesystem metrics, throughput mode, credits or limits, workload parallelism, latency, and resilience requirement.

# Related concepts

- [Shared storage](../services/shared-storage.md)
- [Storage service selection](storage-service-selection.md)
- [S3 transfer optimization](s3-transfer-optimization.md)

# Sources

- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
