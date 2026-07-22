---
type: AWS Service
title: ElastiCache
service_id: elasticache
description: Provides managed in-memory caches whose replicas, shards, TTLs, and eviction behavior solve different scaling limits.
tags: ["soa-c03", "domain-2", "elasticache", "caching"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["2.1.2", "2.1.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
status: verified
---

# Core model

`application -> cache key -> node or shard -> hit/miss -> source database on miss`

Replicas add read capacity and availability; shards add data and write distribution. TTL, key construction, reuse, memory pressure, eviction, and hot keys determine benefit.

# Selection boundaries

Use ElastiCache for application data or sessions. Use DAX for DynamoDB-aware repeated reads and CloudFront for edge HTTP content.

# Evidence and failure modes

Inspect hit ratio, misses, latency, CPU, memory, evictions, connections, replication, shard balance, failover, source load, and client endpoint use.

# Sources

- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
