---
type: Concept
title: Disaster recovery
description: Connects DR strategy, data method, infrastructure readiness, traffic movement, validation, and failback.
tags: [soa-c03, domain-2, disaster-recovery, resilience]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.4"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Core model

```text
detect and declare -> activate prepared environment -> recover/promote data
-> validate -> shift traffic -> monitor -> reconcile and fail back
```

# Strategy continuum

| Strategy | Environment before disaster | Cost tendency | Recovery tendency |
| --- | --- | --- | --- |
| Backup and restore | Backups; little runtime | Lowest | Longest |
| Pilot light | Core/data running | Low-medium | Faster |
| Warm standby | Complete reduced environment | Medium-high | Short |
| Multi-site active/active | Multiple sites serving | Highest | Shortest |

Strategy is not the data mechanism. Backups, replication, global tables, global databases, and service-specific copies support different workloads.

# Prepared dependencies

Infrastructure definitions, artifacts, quotas, IP capacity, keys, secrets, certificates, network paths, monitoring, backup, data authority, runbooks, and traffic controls must exist or be reproducible in the recovery Region.

# Traffic controls

Route 53 changes DNS answers; Global Accelerator controls static-anycast endpoint traffic; ARC provides guarded routing controls, Region switch, and supported zonal shift. None copies data.

# Validation and failback

Validate recovery point, capacity, security, queues, consumers, alarms, logs, and application behavior before traffic. Failback requires reverse synchronization and its own runbook.

# Exam traps

- Multi-AZ is HA, not multi-Region DR.
- Pilot light is not a full reduced application.
- Warm standby is fully functional at reduced capacity.
- Failover without validation can expose stale or corrupt data.
- RTO includes deployment, validation, traffic shift, and warm-up.

# Related concepts

- [DR strategy selection](../decision-guides/dr-strategy-selection.md)
- [Disaster-recovery failover](../playbooks/disaster-recovery-failover.md)
- [Database recovery](database-recovery.md)

# Sources

- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
