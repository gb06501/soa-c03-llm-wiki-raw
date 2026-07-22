---
type: AWS Service
title: EFS
service_id: efs
description: Provides managed shared NFS file systems with elastic capacity, mount targets, performance modes, and protection controls.
tags: ["soa-c03", "domain-4", "efs", "encryption"]
timestamp: 2026-07-22T05:15:00Z
skill_ids: ["1.3.4", "2.2.2", "2.3.4", "4.2.2", "4.2.3"]
domain_ids: ["1", "2", "4"]
sources:
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---
# Core model

EFS provides shared NFS file systems through mount targets that clients must reach. Availability and performance depend on mount-target placement, DNS, security groups, client and POSIX behavior, throughput mode, and workload parallelism. Encryption, backup, replication, and storage-class choices are separate protection and lifecycle controls.

# Decision boundaries

At-rest encryption and key selection are creation-time architectural choices. Use the TLS mount helper when the client path requires encryption in transit. TLS does not correct route, security-group, DNS, or NFS permission problems.

# Evidence and diagnosis

Check file-system encryption and key, mount-target AZ and security group, DNS resolution, NFS port reachability, mount-helper TLS options, IAM authorization, and POSIX identity.

# Safe operations

Select keys before creation, test mounts from each required subnet, use TLS consistently, monitor key lifecycle, and validate application I/O after remount or migration.

# Related decisions

- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Shared-storage selection and recovery

EFS supplies shared NFS storage. Mount targets, DNS, security groups, client behavior, throughput mode, I/O limit, and workload parallelism determine access and performance. Standard and One Zone choices carry different failure boundaries.

A second-Region requirement needs replication or backup copy plus infrastructure and client cutover; multi-AZ storage alone is not multi-Region DR.

# Sources

- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
