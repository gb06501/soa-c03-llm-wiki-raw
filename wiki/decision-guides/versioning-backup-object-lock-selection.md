---
type: Decision Guide
title: Versioning, backup, and Object Lock selection
description: Selects versioning, immutable retention, replication, lifecycle, backup, or FSx recovery controls.
tags: [soa-c03, domain-2, storage, versioning, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.3-implement-versioning-for-storage-services.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Recover overwritten or deleted S3 object | S3 Versioning |
| Prevent permanent deletion during retention | Object Lock/legal hold and permissions |
| Move or expire old object versions | Lifecycle for noncurrent versions |
| Maintain another bucket/Region/account copy | Replication |
| Centralize recovery points and restore policy | AWS Backup |
| Replicate eligible pre-existing S3 objects | Batch Replication or migration action |
| Let a Windows user recover an old file | FSx for Windows shadow copies |
| Restore a supported FSx filesystem or volume | Family-specific snapshot or backup |
| Preserve historical S3 versions after stopping new version creation | Suspend versioning |

# Rejection rules

- Versioning is not an independent copy.
- Object Lock does not replicate data.
- Lifecycle expiration can permanently remove noncurrent versions.
- Replication does not automatically cover all old objects.
- Delete-marker removal does not restore a version that was permanently deleted.
- Windows shadow copies are not a full backup.
- Do not apply one FSx family's feature to every FSx filesystem.

# Evidence and verification

List versions and delete markers, retrieve the selected version, inspect retention and replication status, verify permissions and KMS, and test the family-specific FSx or backup recovery action.

# Related concepts

- [Storage versioning and recovery](../concepts/storage-versioning.md)
- [Storage-version recovery](../playbooks/storage-version-recovery.md)

# Sources

- [Skill 2.3.3](../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)
