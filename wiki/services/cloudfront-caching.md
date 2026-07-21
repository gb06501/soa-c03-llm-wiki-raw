---
type: AWS Feature
title: CloudFront caching
parent_services: [CloudFront]
description: Controls behavior selection, cache key, TTL, forwarding, invalidation, error caching, origin contact, and privacy.
tags: ["soa-c03", "domain-5", "cloudfront", "caching"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md
status: verified
---

# Parent service

[CloudFront](cloudfront.md)

# Core pipeline

`viewer request -> first matching behavior -> cache key -> edge lookup -> hit or origin miss -> cacheability/TTL -> response`

# Key boundaries

Cache policy defines the cache key. Origin request policy can forward additional values without changing that key. Extra high-cardinality values cause misses; missing response-varying identity values can leak or share wrong content.

Minimum TTL can cache despite restrictive origin directives. `no-cache` means revalidate; `no-store` means do not store. Error responses can remain cached after origin recovery.

# Evidence

Use matched behavior, `X-Cache`, `Age`, result type, status, cache-hit metric, invalidations, policy/TTL, origin access logs, and viewer/origin request correlation.

# Safe operations

Clone a policy, test a narrow behavior, validate every response variant and privacy boundary, compare hit rate and origin load, then expand and invalidate only affected keys.

# Related pages

- [CloudFront cache policy selection](../decision-guides/cloudfront-cache-policy-selection.md)
- [CloudFront cache failure](../playbooks/cloudfront-cache-failure.md)

# Sources

- [Skill 5.3.3](../../raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md)
