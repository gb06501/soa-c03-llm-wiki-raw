---
type: Decision Guide
title: CloudFront cache policy selection
description: Chooses cache-key, TTL, forwarding, invalidation, error-caching, and privacy behavior from viewer and origin evidence.
tags: ["soa-c03", "domain-5", "cloudfront", "cache"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md
status: verified
---

# Decision table

| Requirement or clue | Select |
| --- | --- |
| Origin response varies by a value | include it in cache key or disable caching |
| Origin needs value but response does not vary | origin request policy only |
| Too many misses from unique values | remove unnecessary high-cardinality key values |
| Stale normal static release | versioned object names |
| Emergency removal/correction | targeted invalidation after root fix |
| Origin requires revalidation | respect `no-cache` and validator behavior |
| Must not store response | `no-store` plus compatible minimum TTL |
| Error persists after origin recovery | reduce error TTL or invalidate affected key |
| Personalized response | complete tenant/user key or no caching |
| Cold new POP miss | observe before changing policy |

# Rejection rules

- First matching behavior determines policy.
- Forwarding and cache-key inclusion are not the same.
- Positive minimum TTL can override restrictive origin directives.
- Invalidation does not fix policy or origin.
- High hit ratio is harmful if users share wrong content.
- A miss with 502/504 is often origin connectivity/TLS/latency.

# Verification

Test every response variant and identity boundary, inspect X-Cache/Age/result and origin logs, compare hit ratio and origin load, confirm stale/error removal, and verify no cross-user leakage.

# Related pages

- [CloudFront caching](../services/cloudfront-caching.md)
- [CloudFront cache failure](../playbooks/cloudfront-cache-failure.md)

# Sources

- [Skill 5.3.3](../../raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md)
