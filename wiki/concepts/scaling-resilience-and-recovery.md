---
type: Concept
title: Scaling, resilience, and recovery
description: Connects capacity response, fault containment, durable recovery, and traffic restoration across Domain 2.
tags: [soa-c03, domain-2, scaling, resilience, recovery]
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

# Core model

```text
normal demand -> scale capacity or reduce repeated work
component failure -> replace, fail over, or decouple
data loss/corruption -> restore a selected recovery point
Region loss -> activate prepared strategy and shift traffic
```

These are different operational problems. Scaling is not availability, availability is not backup, and backup is not complete disaster recovery.

# Decision layers

| Question | Knowledge path |
| --- | --- |
| How does usable capacity follow demand? | [Compute scaling](../services/compute-scaling.md) |
| Can repeated work be avoided safely? | [Caching](../services/caching.md) |
| Which database dimension is constrained? | [Managed database scaling](../services/managed-database-scaling.md) |
| Which health signal removes or redirects traffic? | [Load balancing and health checks](../services/load-balancing-and-health-checks.md) |
| Which failure boundary must survive? | [Fault tolerance](fault-tolerance.md) |
| Which recovery point exists and is usable? | [AWS Backup](../services/aws-backup.md) |
| Which data point and cutover meet RPO/RTO? | [Database recovery](database-recovery.md) |
| Is historical data protected by version, lock, copy, or backup? | [Storage versioning](storage-versioning.md) |
| Which multi-Region readiness level is required? | [Disaster recovery](disaster-recovery.md) |

# Dependency ordering

1. Prove the current bottleneck or failure boundary.
2. Select a mechanism that acts on that boundary.
3. Preserve data authority and recovery evidence.
4. Confirm downstream and surviving capacity.
5. Validate the real application.
6. Measure recovery, not just infrastructure completion.

# Cross-skill traps

- Scaling can amplify a downstream failure.
- A cache can hide backend pressure until cache failure.
- Health checks route away only when healthy capacity exists.
- Multi-AZ does not replace backup or multi-Region DR.
- Recovery points do not recreate every application dependency.
- Traffic controls do not copy or validate data.

# Related concepts

- [Evidence-to-remediation loop](evidence-to-remediation-loop.md)
- [Safe automation](safe-automation.md)
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
