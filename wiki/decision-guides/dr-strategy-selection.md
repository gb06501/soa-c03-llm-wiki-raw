---
type: Decision Guide
title: Disaster-recovery strategy selection
description: Selects backup and restore, pilot light, warm standby, or active-active from cost, RTO, RPO, and readiness.
tags: [soa-c03, domain-2, disaster-recovery, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.4"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Decision table

| Scenario clue | Choose |
| --- | --- |
| Lowest standing cost; hours to restore | Backup and restore |
| Core/data always running; application capacity starts later | Pilot light |
| Complete smaller environment already operational | Warm standby |
| Multiple Regions serve production before disaster | Multi-site active/active |
| Automatic AZ failover in one Region | High availability, not a DR strategy |
| DNS failover between prepared endpoints | Route 53 |
| Static anycast with endpoint traffic controls | Global Accelerator |
| Guarded operator-controlled regional recovery | ARC routing controls or Region switch |
| Supported temporary AZ traffic avoidance | ARC zonal shift |

Select the strategy separately from each data-protection mechanism and traffic-control mechanism.

# Rejection rules

- Do not call Multi-AZ multi-Region DR.
- Do not call a complete reduced environment pilot light.
- Do not assume traffic routing replicates data.
- Do not choose backup/restore for an RTO that excludes provisioning and restoration time.
- Do not choose active-active without conflict, isolation, and capacity design.
- Do not omit failback and reverse data synchronization.

# Evidence and verification

Verify recovery-point age or replication lag, deployability, quotas, keys/secrets/certificates, healthy capacity, data authority, traffic controls, full application tests, achieved RPO/RTO, and failback readiness.

# Related concepts

- [Disaster recovery](../concepts/disaster-recovery.md)
- [Disaster-recovery failover](../playbooks/disaster-recovery-failover.md)

# Sources

- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
