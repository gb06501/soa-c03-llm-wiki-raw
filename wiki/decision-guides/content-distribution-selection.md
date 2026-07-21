---
type: Decision Guide
title: Content distribution selection
description: Chooses CloudFront, Global Accelerator, Route 53, or Elastic Load Balancing from protocol, caching, IP, and health requirements.
tags: ["soa-c03", "domain-5", "edge", "content-distribution"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Cache HTTP/HTTPS content at edge | CloudFront |
| Edge WAF, signed viewer access, header policy | CloudFront |
| Non-cacheable TCP/UDP acceleration | Global Accelerator |
| Stable global anycast IPs | Global Accelerator |
| DNS policy/TTL based answer | Route 53 |
| Regional Layer 7 routing | ALB |
| Regional Layer 4/TLS/pass-through | NLB |
| Private S3 origin | CloudFront S3 REST origin plus OAC |
| HTTP origin failover on chosen statuses | CloudFront origin group |
| Shift a Global Accelerator Region | endpoint-group traffic dial |

# Rejection rules

- Global Accelerator does not cache.
- Route 53 does not proxy connections.
- First matching CloudFront behavior wins.
- Cache policy and origin request policy serve different purposes.
- OAC does not work with S3 website origins.
- Viewer and origin TLS are separate.
- An origin group fails over; it does not weight-balance.
- WAF at edge does not protect a directly exposed origin.

# Verification

Prove DNS/static IP, listener/behavior, cache/result or dial/weight, certificate and policy, origin/endpoint health, direct-origin restriction, logs/metrics, and application result.

# Related pages

- [Content and service distribution](../services/content-distribution.md)
- [Edge delivery failure](../playbooks/edge-delivery-failure.md)

# Sources

- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
