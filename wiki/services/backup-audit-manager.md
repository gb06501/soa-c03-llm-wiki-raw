---
type: AWS Feature
title: Backup Audit Manager
parent_services: ["Backup"]
description: Evaluates and reports backup-control evidence separately from backup job execution and restore validation.
tags: ["soa-c03", "domain-2", "backup", "audit-manager"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["2.3.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Core model

`backup configuration and activity -> audit controls -> evaluation evidence -> report`

Audit evidence helps prove policy posture. It does not create recovery points or prove that a restore meets application RTO and RPO.

# Evidence and failure modes

Check framework and control scope, resource selection, evaluation time, report configuration, permissions, underlying backup state, and exceptions.

# Sources

- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
