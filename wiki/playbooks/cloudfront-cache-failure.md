---
type: Troubleshooting Playbook
title: CloudFront cache failure
description: Diagnoses behavior, cache key, TTL, directives, misses, stale or shared content, cached errors, and origin failures.
tags: ["soa-c03", "domain-5", "troubleshooting", "cloudfront", "cache"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md
status: verified
---

# Trigger

CloudFront repeatedly misses, serves stale/wrong/private content, retains an error, or a supposed cache issue is actually an origin failure.

# Evidence path

1. Record host/path/query/headers/cookies, status, X-Cache, Age, POP, time, and request ID.
2. Identify the first matching behavior and attached cache/origin-request policies.
3. Build the exact cache key and compare every response-varying value.
4. Inspect minimum/default/maximum TTL and origin Cache-Control/Expires.
5. Check invalidations, deployments, object version, compression variants, and cold POP behavior.
6. Determine whether the error was cached; compare repeated edge logs with origin logs.
7. For 502/504, inspect origin DNS, TLS, listener, SG/firewall, latency, health, and logs.
8. For wrong-user content, contain the affected cache path immediately and inspect identity/tenant variation.

# Failure map

| Symptom | Direction |
| --- | --- |
| Repeated miss | high-cardinality key, TTL zero/short, uncacheable response |
| Wrong shared content | missing response-varying key value |
| Stale object | effective TTL, version/path, incomplete invalidation |
| Error persists after origin fix | error cache TTL/key |
| Miss plus 502 | origin TLS/DNS/listener |
| Miss plus 504 | origin reachability/latency |
| No origin log on hit | expected edge cache |
| One path uses wrong policy | behavior order |

# Safe action

Clone the policy, attach to a narrow test behavior, validate variants and privacy, fix origin/policy before invalidation, then expand with rollback retained.

# Verification

Prove expected hit/miss and Age, correct content for every identity/variant, reduced origin load without error increase, resolved cached errors, and healthy origin when contacted.

# Rollback

Restore the prior behavior/policy and disable caching on a sensitive path if isolation cannot be proven.

# Escalation

Provide request variants, behavior/policies, effective TTL, edge/origin correlation, privacy impact, and rollback state.

# Related pages

- [CloudFront caching](../services/cloudfront-caching.md)
- [CloudFront cache policy selection](../decision-guides/cloudfront-cache-policy-selection.md)

# Sources

- [Skill 5.3.3](../../raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md)
