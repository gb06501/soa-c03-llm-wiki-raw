---
type: Decision Guide
title: Caching selection
description: Selects CloudFront, ElastiCache, or DAX and the correct scaling control from request semantics.
tags: [soa-c03, domain-2, caching, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Cache HTTP responses near viewers | CloudFront |
| Cache application sessions or rich data structures | ElastiCache with Valkey/Redis OSS |
| Simple distributed volatile key/value cache | ElastiCache for Memcached |
| Cache repeated eventually consistent DynamoDB reads | DAX |
| Add ElastiCache read capacity or availability | Replica |
| Add ElastiCache data/write distribution | Shard |
| Remove stale CloudFront content now | Invalidation |
| Avoid repeated invalidations for immutable releases | Versioned object names |
| Protect backend from simultaneous rebuild after expiry | Controlled refresh/locking pattern |
| Keep service available when cache fails | Application miss/fallback path |

# Rejection rules

- Do not use DAX for DynamoDB writes, RDS, or strongly consistent cached reads.
- Do not add replicas to solve a shard/write-distribution limit.
- Do not add shards when the actual problem is a hot key.
- Do not tune TTL before confirming the correct behavior and cache key.
- Do not treat cached data as the sole durable copy.

# Evidence and verification

Measure hit ratio, backend request reduction, latency, memory/eviction, shard/node balance, replication lag, and fallback behavior. Test expiry and cache failure without causing a backend stampede.

# Related concepts

- [Caching](../services/caching.md)
- [Cache performance failure](../playbooks/cache-performance-failure.md)
- [S3 transfer optimization](s3-transfer-optimization.md)

# Sources

- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
