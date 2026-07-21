---
type: Concept
title: Shared storage
description: Selects EFS, an FSx family, S3 Files, S3, or Storage Gateway from protocol and workload needs.
tags: [soa-c03, domain-1, efs, fsx, s3-files, storage-gateway]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["1.3.3", "1.3.4"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
status: verified
---

# First decision

```text
Does the application need an object API or a mounted filesystem?
```

Then match protocol, operating system, performance pattern, resilience, and lifecycle.

# Service selection

| Requirement | Choice |
| --- | --- |
| Shared Linux NFS filesystem | EFS |
| Windows SMB with Active Directory | FSx for Windows File Server |
| HPC/ML parallel filesystem | FSx for Lustre |
| Enterprise NFS/SMB/iSCSI features | FSx for NetApp ONTAP |
| Existing S3 data exposed with file operations | S3 Files |
| Object API at object-storage scale | S3 |
| Hybrid local file, block, or tape access | Storage Gateway |

FSx for OpenZFS is outside the supplied SOA-C03 scope.

# EFS controls

- Clients mount through an AZ mount target and security path.
- General Purpose fits most latency-sensitive applications.
- Max I/O favors very high parallelism with a latency trade-off.
- Elastic throughput follows activity.
- Provisioned throughput is independent of stored size.
- Bursting throughput uses size-linked baseline and credits.
- Lifecycle can move cold files to lower-cost classes; it does not improve active-data throughput.

# Diagnosis

| Symptom | First direction |
| --- | --- |
| EFS mount failure | Mount target, DNS, security groups/NACLs, NFS client, IAM/access point |
| EFS slowdown | Throughput mode, I/O limit, burst credits, workload parallelism |
| Windows access failure | Correct FSx family, SMB, AD, DNS, security, permissions |
| S3 Files mount failure | File system/mount target, IAM, subnet, security, DNS |
| Gateway offline | Appliance, network, endpoint, cache/storage, credentials |

# Exam traps

- EFS is NFS-focused, not native Windows SMB.
- S3 object API is not a mounted shared filesystem.
- S3 Files keeps data in S3 while providing file access.
- EFS performance mode and throughput mode are different choices.
- One Zone trades resilience for lower cost.

# Related concepts

- [S3 performance](s3-performance.md)
- [Storage service selection](../decision-guides/storage-service-selection.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)

# Sources

- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)

