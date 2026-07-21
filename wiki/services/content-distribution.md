---
type: Concept
title: Content and service distribution
description: Chooses DNS selection, HTTP edge caching, TCP/UDP global acceleration, or Regional load balancing by connection and content behavior.
tags: ["soa-c03", "domain-5", "content-distribution", "edge"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
status: verified
---

# Core distinction

| Requirement | Select |
| --- | --- |
| Cache and secure HTTP/HTTPS at edge | CloudFront |
| Stable global IPs and non-cacheable TCP/UDP acceleration | Global Accelerator |
| Return policy-based DNS answers | Route 53 |
| Balance connections/requests within a Region | Elastic Load Balancing |

# Delivery layers

CloudFront selects the first matching behavior, builds a cache key, applies viewer policy, optionally contacts an origin, and can protect private S3 through OAC. Global Accelerator selects a listener, Regional endpoint group/traffic dial, and weighted healthy endpoint.

# Evidence

Use DNS answers/TTL, CloudFront behavior and result fields, cache/origin logs, OAC/bucket/KMS policy, viewer/origin TLS, accelerator listener/dial/weight/health, ELB target evidence, and CloudTrail changes.

# Safe rollout

Introduce a tested distribution or low-dial endpoint group, validate identity, privacy, health, and origin behavior, shift traffic gradually, close direct-origin bypass, and preserve rollback.

# Related pages

- [CloudFront](cloudfront.md)
- [Global Accelerator](global-accelerator.md)
- [Content distribution selection](../decision-guides/content-distribution-selection.md)

# Sources

- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
