---
type: AWS Service
title: DAX
service_id: dax
description: Caches repeated DynamoDB reads for DAX-aware clients while writes and strongly consistent reads still depend on DynamoDB.
tags: ["soa-c03", "domain-2", "dax", "dynamodb", "caching"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["2.1.2", "2.1.3", "2.3.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
status: verified
---

# Core model

`DAX-aware client -> DAX cluster -> cache hit or DynamoDB read -> DynamoDB remains system of record`

DAX improves repeated eventually consistent reads. Strongly consistent reads pass through, writes still consume DynamoDB capacity, and DAX is not backup.

# Evidence and failure modes

Check client library and endpoint, hit and miss behavior, item reuse, cluster nodes, errors, latency, DynamoDB consumed capacity, throttling, hot keys, and write traffic.

# Sources

- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
