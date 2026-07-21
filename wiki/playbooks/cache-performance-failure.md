---
type: Troubleshooting Playbook
title: Cache performance failure
description: Diagnoses low hit ratio, stale data, hot nodes, stampedes, and cache-backed overload.
tags: [soa-c03, domain-2, caching, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.2"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
status: verified
---

# Trigger

Cache latency or misses rise, the origin remains overloaded, one node is hot, data is stale, or cache failure breaks the application.

# Evidence path

1. Identify CloudFront, ElastiCache, or DAX and the request type.
2. Confirm the application actually uses the intended endpoint or behavior.
3. Inspect hit/miss result, cache key, TTL, headers, cookies, and query strings.
4. Check memory, eviction, CPU, replicas, shards, lag, and hot-key distribution.
5. Correlate cache misses with source latency, errors, and throttling.
6. Test whether strong consistency or uncacheable requests bypass the cache.
7. Inspect fallback and rebuild behavior during expiry or outage.

# Failure map

| Symptom | Direction |
| --- | --- |
| CloudFront hit ratio low | Behavior, cache key, TTL, bypass inputs |
| Origin still overloaded | Uncacheable traffic, low reuse, short TTL |
| ElastiCache misses high | TTL, key construction, eviction, reuse |
| One node hot | Hot key, shard distribution, client routing |
| DAX no benefit | Client/endpoint, reuse, consistency mode |
| Writes throttle behind DAX | DynamoDB write capacity or partitioning |
| Cache outage breaks app | Missing fallback or weak HA |

# Safe action

Correct the key or routing first, then tune TTL or capacity. Add replicas for reads, shards for distribution, and stampede protection before broad expiry or invalidation.

# Verification

Confirm improved hit ratio and latency, reduced backend load, balanced nodes or shards, controlled expiry behavior, and successful application fallback during a cache interruption.

# Sources

- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
