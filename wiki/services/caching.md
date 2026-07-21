---
type: Concept
title: Caching
description: Explains CloudFront, ElastiCache, and DAX cache boundaries, scaling controls, and evidence.
tags: [soa-c03, domain-2, caching, cloudfront, elasticache, dax]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["2.1.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
status: verified
---

# Core model

```text
request -> cache lookup -> hit returns cached value
                       -> miss reads source and may populate cache
```

A cache reduces repeated work. It is normally not the source of truth.

# Cache families

| Need | Choice |
| --- | --- |
| HTTP content near global users | CloudFront |
| Application data, sessions, counters, or general key/value use | ElastiCache |
| Repeated DynamoDB reads | DAX |

# Important controls

- CloudFront: behavior, cache policy, cache key, TTL, invalidation, versioned names.
- ElastiCache: engine, cluster/replication group, node, shard, replica, TTL, eviction.
- DAX: DAX-aware client, cluster endpoint, nodes, repeated eventually consistent reads.
- Replicas add cache read capacity and availability; shards add data/write distribution.
- Cache-aside, write-through, TTL, eviction, hot keys, and stampede control determine application behavior.

# Evidence

Inspect hit ratio, hits/misses, result type, memory, CPU, eviction, replication lag, shard distribution, origin/backend load, and DynamoDB throttling behind DAX.

# Failure modes

Low key reuse, excessive key cardinality, short TTL, eviction, one hot key, unavailable fallback, stampede, wrong endpoint/client, or requests that cannot use the cache.

# Exam traps

- CloudFront cache policy and origin request policy differ.
- Invalidation is immediate cleanup; versioned names fit repeated immutable releases.
- Memcached does not provide Redis-style replication/failover.
- Strongly consistent DynamoDB reads bypass DAX.
- DAX does not fix DynamoDB writes or RDS queries.
- Cache failure can suddenly expose the backend to full load.

# Related concepts

- [Caching selection](../decision-guides/caching-selection.md)
- [Cache performance failure](../playbooks/cache-performance-failure.md)

# Sources

- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
