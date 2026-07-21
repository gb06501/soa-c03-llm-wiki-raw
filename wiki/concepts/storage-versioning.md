---
type: Concept
title: Storage versioning and recovery
description: Explains S3 versions, Object Lock, replication, lifecycle, and FSx-specific historical recovery controls.
tags: [soa-c03, domain-2, storage, versioning, s3, fsx]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.3-implement-versioning-for-storage-services.md
status: verified
---

# Core model

```text
new write or delete -> current version changes -> older protected version may remain -> explicit recovery
```

# S3 version behavior

| State | New write | Older versions |
| --- | --- | --- |
| Unversioned | Replaces object | No protected history |
| Enabled | Gets a unique version ID | Preserved |
| Suspended | Uses null-version behavior | Existing non-null versions remain |

Deleting without a version ID normally creates a delete marker. Deleting a specific version can be permanent.

# Protection controls

- Versioning: object history in the bucket.
- Lifecycle: transition or expire current and noncurrent versions.
- Object Lock/legal hold: prevent protected version deletion.
- Replication: copy eligible versions to another bucket/Region/account.
- AWS Backup: centralized recovery points and restore workflow.
- FSx: family-specific snapshots, backups, replication, or Windows shadow copies.

# Evidence

Inspect versioning state, version IDs, delete markers, Object Lock, replication status, permissions/KMS, lifecycle, snapshot/shadow-copy inventory, backup jobs, and capacity.

# Exam traps

- Suspending versioning does not delete existing versions.
- Object Lock is not another copy.
- Replication needs versioning on both buckets and may not include old objects automatically.
- Windows shadow copies are not an independent full-filesystem backup.
- FSx families do not share one universal versioning switch.

# Related concepts

- [Versioning, backup, and Object Lock selection](../decision-guides/versioning-backup-object-lock-selection.md)
- [Storage-version recovery](../playbooks/storage-version-recovery.md)

# Sources

- [Skill 2.3.3](../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)
