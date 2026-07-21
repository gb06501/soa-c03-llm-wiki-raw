---
type: Decision Guide
title: Database restore selection
description: Selects snapshot, point-in-time, vault, replica, or high-availability recovery from RPO, RTO, and cost.
tags: [soa-c03, domain-2, database, restore, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Return to an exact saved snapshot | Snapshot restore |
| Recover to a selected time before corruption | PITR |
| Restore from centralized protection | AWS Backup recovery point |
| Validate backup usability | Restore test |
| Minimize data loss beyond snapshot frequency | PITR or prepared replication |
| Minimize downtime beyond ordinary restore | HA or prepared replica/DR design |
| Restore copied RDS/Aurora data in another Region/account | Copied/shared snapshot or recovery point plus KMS |
| Restore DynamoDB from chosen backup | On-demand or AWS Backup restore |
| Restore DynamoDB to selected time | DynamoDB PITR |

# Rejection rules

- Do not choose a recovery time after the corrupting event.
- Do not count only the restore job when calculating RTO.
- Do not treat a read replica as a replacement for backup.
- Do not expect restore to overwrite the existing database in place.
- Do not omit endpoint, DNS, secret, proxy, or application cutover.
- Do not assume surrounding automation is recreated with table data.

# Evidence and verification

Confirm retention and restore-point availability, Region/account, KMS access, network settings, new resource identity, selected data point, application cutover, performance, HA, alarms, backups, RPO, and full RTO.

# Related concepts

- [Database recovery](../concepts/database-recovery.md)
- [Database restore and cutover](../playbooks/database-restore-and-cutover.md)

# Sources

- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
