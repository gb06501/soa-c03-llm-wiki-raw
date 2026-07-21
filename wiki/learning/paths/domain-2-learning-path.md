---
type: Learning Path
title: Domain 2 learning path
description: Orders scaling, availability, backup, restore, versioning, and disaster recovery into an operational study sequence.
tags: [soa-c03, domain-2, learning-path, availability, recovery]
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

# Stage 1: Capacity follows demand

1. [Compute scaling](../../services/compute-scaling.md)
2. [Compute scaling selection](../../decision-guides/compute-scaling-selection.md)
3. [Scaling failure](../../playbooks/scaling-failure.md)
4. [Caching](../../services/caching.md)
5. [Caching selection](../../decision-guides/caching-selection.md)
6. [Cache performance failure](../../playbooks/cache-performance-failure.md)
7. [Managed database scaling](../../services/managed-database-scaling.md)
8. [Database scaling selection](../../decision-guides/database-scaling-selection.md)
9. [Database scaling failure](../../playbooks/database-scaling-failure.md)

# Stage 2: Health and failure boundaries

1. [Load balancing and health checks](../../services/load-balancing-and-health-checks.md)
2. [Load balancer and health-check selection](../../decision-guides/load-balancer-health-check-selection.md)
3. [Unhealthy target and DNS failover](../../playbooks/unhealthy-target-and-dns-failover.md)
4. [Fault tolerance](../../concepts/fault-tolerance.md)
5. [Fault-tolerance pattern selection](../../decision-guides/fault-tolerance-pattern-selection.md)
6. [Failure-boundary diagnosis](../../playbooks/failure-boundary-diagnosis.md)

# Stage 3: Protect and recover data

1. [AWS Backup](../../services/aws-backup.md)
2. [Backup protection selection](../../decision-guides/backup-protection-selection.md)
3. [Backup job failure](../../playbooks/backup-job-failure.md)
4. [Database recovery](../../concepts/database-recovery.md)
5. [Database restore selection](../../decision-guides/database-restore-selection.md)
6. [Database restore and cutover](../../playbooks/database-restore-and-cutover.md)
7. [Storage versioning](../../concepts/storage-versioning.md)
8. [Versioning, backup, and Object Lock selection](../../decision-guides/versioning-backup-object-lock-selection.md)
9. [Storage-version recovery](../../playbooks/storage-version-recovery.md)

# Stage 4: Recover the service

1. [Disaster recovery](../../concepts/disaster-recovery.md)
2. [DR strategy selection](../../decision-guides/dr-strategy-selection.md)
3. [Disaster-recovery failover](../../playbooks/disaster-recovery-failover.md)
4. [Scaling, resilience, and recovery](../../concepts/scaling-resilience-and-recovery.md)
5. [Domain 2 exam traps](../../exam-traps/domain-2-exam-traps.md)

# Readiness questions

- Can you separate scale, cache, failover, backup, restore, and DR?
- Can you choose a health source from the traffic layer?
- Can you calculate which mechanism primarily affects RPO versus RTO?
- Can you explain why the tempting alternative fails?
- Can you identify evidence proving application recovery rather than job completion?

# Sources

- [Skill 2.1.1](../../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.1.2](../../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
- [Skill 2.1.3](../../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.1](../../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
- [Skill 2.2.2](../../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.2](../../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.3](../../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)
- [Skill 2.3.4](../../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
