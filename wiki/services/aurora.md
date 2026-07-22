---
type: AWS Service
title: Aurora
service_id: aurora
description: Provides managed relational database clusters with reader scaling, snapshots, recovery, and security controls.
tags: ["soa-c03", "domain-4", "aurora", "data-protection"]
timestamp: 2026-07-22T05:15:00Z
skill_ids: ["1.2.1", "1.3.5", "2.1.3", "2.2.2", "2.3.1", "2.3.2", "2.3.4", "4.2.2", "4.2.3", "4.2.4"]
domain_ids: ["1", "2", "4"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---
# Core model

Aurora separates cluster storage, database instances, writer and reader endpoints, and clients. Reader capacity serves eligible reads only when applications use the reader endpoint, and multi-AZ storage does not replace healthy promotable instances. Performance, scaling, backup and recovery, networking, authentication, and encryption are distinct operational layers.

# Decision boundaries

Encryption at rest is chosen at cluster creation and affects snapshots and copies. TLS protects the client connection; it does not replace database authentication or storage encryption. Secret rotation must remain compatible with cluster users and applications.

# Evidence and diagnosis

Check cluster and snapshot encryption key, key Region and policy, endpoint hostname, CA trust, TLS parameter, security groups, database user state, secret version, and rotation execution.

# Safe operations

Test encrypted snapshot restore, preserve certificate trust during CA rotation, retrieve secrets at runtime, coordinate credential cutover, and verify read/write behavior after security changes.

# Related decisions

- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [Secret access and rotation failure](../playbooks/secret-access-and-rotation-failure.md)

# Scaling and availability

Readers scale eligible reads only when applications use the reader endpoint. Serverless v2 capacity stays inside configured bounds. Multi-AZ storage does not replace healthy promotable database instances.

# Restore and disaster recovery

Cluster restore also requires database instances and working endpoints. Cross-Region replica or Global Database readiness differs from backup restore in standing cost, promotion work, RPO, and RTO.

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
