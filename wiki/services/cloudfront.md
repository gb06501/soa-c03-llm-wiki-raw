---
type: AWS Service
title: CloudFront
service_id: cloudfront
description: Delivers content through edge distributions with independent viewer and origin TLS policies.
tags: ["soa-c03", "domain-4", "cloudfront", "tls", domain-5, edge, caching]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["4.2.3", "5.1.3", "5.1.4", "5.2.3", "5.3.2", "5.3.3", "5.3.5", "1.3.3", "2.1.2"]
domain_ids: ["4", "5", "1", "2"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
status: verified
---
# Core model

A CloudFront request crosses two TLS relationships: viewer to edge and edge to origin. Each side has its own protocol policy, hostname, certificate, and trust requirements.

# Decision boundaries

The viewer certificate must cover the alternate domain name and be available in the Region required by CloudFront. Origin TLS must validate the origin hostname and chain. Redirect-to-HTTPS and HTTPS-only policies have different client behavior.

# Evidence and diagnosis

Separate DNS, viewer TLS, distribution behavior, origin routing, origin TLS, and application response. Inspect the requested hostname, certificate SANs, security policy, origin protocol policy, SNI, status code, and distribution configuration.

# Safe operations

Deploy certificate and policy changes with overlap, test default and alternate names, validate both viewer and origin paths, and keep rollback available while the distribution propagates.

# Related decisions

- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Domain 5: Edge delivery and caching

A request selects the first matching behavior, forms a cache key, applies viewer policy and WAF, then serves a fresh edge object or contacts the selected origin. Cache policy, origin request policy, and response headers policy have distinct roles.

Use S3 REST origin plus OAC for private buckets; bucket and KMS permissions are separate. Viewer and origin TLS are separate. Origin groups provide failover, not weighted balancing, and direct origin access can bypass edge protection.

Diagnose with hostname/path, behavior, X-Cache, Age, result/status, policy/TTL, WAF and edge logs, origin access/health/TLS, and CloudTrail changes.

- [Content distribution selection](../decision-guides/content-distribution-selection.md)
- [CloudFront cache policy selection](../decision-guides/cloudfront-cache-policy-selection.md)
- [Edge delivery failure](../playbooks/edge-delivery-failure.md)

# Corpus reconciliation: Domains 1 and 2

## Cache boundary

CloudFront caches edge responses according to behavior, key, TTL, origin directives, and invalidation. It reduces repeated origin work and remote latency; it is not S3 Transfer Acceleration, an application-data cache, or a DynamoDB read cache.

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.3](../../raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
