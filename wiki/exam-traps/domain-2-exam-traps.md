---
type: Exam Trap
title: Domain 2 exam traps
description: Consolidates misleading scaling, availability, backup, restore, versioning, and disaster-recovery alternatives.
tags: [soa-c03, domain-2, exam-traps, availability, recovery]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.1", "2.1.2", "2.1.3", "2.2.1", "2.2.2", "2.3.1", "2.3.2", "2.3.3", "2.3.4"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
  - /raw/skills/2.3.3-implement-versioning-for-storage-services.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Scaling and caching

- A scaling policy changes desired capacity; a launch template defines new instances.
- EC2 health can pass while application health fails.
- ECS task scaling and EC2 capacity scaling are different.
- EKS pod scaling and node scaling are different.
- Cache is normally not the source of truth.
- ElastiCache replicas and shards solve different limits.
- Strongly consistent DynamoDB reads bypass DAX.

# Database scaling

- Multi-AZ is availability, not normal read scaling.
- A read replica does nothing unless application reads use it.
- RDS Proxy handles connections, not query CPU or caching.
- DynamoDB auto scaling is reactive.
- Total capacity does not necessarily repair a hot partition.
- Table and GSI limits can fail independently.

# Health and fault tolerance

- Route 53 health changes DNS answers, not ELB target membership.
- Cross-zone balancing does not create capacity in an empty AZ.
- A public Route 53 checker cannot directly test a private endpoint.
- Multiple AZ subnet selections do not prove running capacity.
- Aurora multi-AZ storage does not replace healthy DB instances.
- ARC moves traffic only to prepared infrastructure.

# Backup and restore

- A backup plan without an assignment protects nothing.
- A vault stores recovery points; it does not schedule jobs.
- Backup success does not prove copy or restore success.
- RPO is allowable data loss; RTO is allowable downtime.
- Snapshot restore and PITR normally create a new resource.
- Restore completion is not application recovery.

# Versioning and disaster recovery

- S3 delete without version ID usually creates a delete marker.
- Suspending versioning preserves existing versions.
- Object Lock is not replication.
- Replication does not automatically include every old object.
- Multi-AZ is not multi-Region DR.
- Pilot light and warm standby are not the same.
- Traffic routing does not replicate data.
- Failback needs synchronization and a runbook.

# Related concepts

- [Scaling, resilience, and recovery](../concepts/scaling-resilience-and-recovery.md)
- [Domain 2 learning path](../learning/paths/domain-2-learning-path.md)

# Sources

- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.3](../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
