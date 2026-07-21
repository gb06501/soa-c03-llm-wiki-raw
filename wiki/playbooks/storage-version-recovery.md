---
type: Troubleshooting Playbook
title: Storage-version recovery
description: Recovers S3 or FSx historical data and diagnoses missing versions, denied access, or failed replication.
tags: [soa-c03, domain-2, storage, versioning, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.3.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.3-implement-versioning-for-storage-services.md
status: verified
---

# Trigger

An object or file was overwritten/deleted, an old version is missing or inaccessible, protected data cannot be deleted, or a replica is absent.

# Evidence path

1. Identify S3 or the exact FSx family.
2. For S3, inspect bucket versioning state at the time of the write/delete.
3. List object versions and delete markers with version IDs.
4. Check `GetObjectVersion`, `DeleteObjectVersion`, bucket/SCP, KMS, and Object Lock.
5. Inspect lifecycle rules for noncurrent expiration.
6. For replication, inspect rule scope, both buckets' versioning, role/policy, KMS, and status.
7. For FSx, inspect family-specific snapshots, shadow copies, backups, schedule, capacity, and permission.

# Failure map

| Symptom | Direction |
| --- | --- |
| Object appears deleted; versions exist | Current delete marker |
| Old version absent | Versioning state or permanent version deletion |
| Old version denied | Version permission, policy/SCP, KMS |
| Cannot delete | Object Lock, legal hold, permission |
| Replica missing | Scope, versioning, role/policy, KMS, status |
| Old objects not replicated | Existing-data batch action required |
| Previous Versions empty | Shadow-copy schedule/capacity/permission |

# Safe action

Recover by copying or promoting the selected historical version without deleting other evidence. Preserve retention and verify the exact object or file before cleanup.

# Verification

Confirm the intended content is current and readable, protection remains enabled, replication or backup is healthy, permissions are correct, and no required historical version was removed.

# Sources

- [Skill 2.3.3](../../raw/skills/2.3.3-implement-versioning-for-storage-services.md)
