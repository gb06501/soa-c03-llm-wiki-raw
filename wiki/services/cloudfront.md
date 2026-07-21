---
type: AWS Service
title: CloudFront
service_id: cloudfront
description: Delivers content through edge distributions with independent viewer and origin TLS policies.
tags: ["soa-c03", "domain-4", "cloudfront", "tls"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
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

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
