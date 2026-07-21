---
type: Concept
title: Encryption in transit
description: Separates endpoint identity, TLS policy, certificate lifecycle, trust, and application delivery across each network hop.
tags: ["soa-c03", "domain-4", "tls", "encryption-in-transit"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---
# Core model

A successful secure request requires all layers to agree:

`DNS -> route -> TCP -> TLS policy -> certificate identity -> trust chain -> application`

A load balancer or edge service can create two independent TLS hops. Protect and test each hop separately.

# TLS objects

| Object | Question |
| --- | --- |
| Hostname and SAN | Does the certificate cover the name the client requested? |
| Issuer and chain | Does the client trust the complete chain? |
| Validity and renewal | Is the certificate current and deployable? |
| Protocol and cipher policy | Do client and server overlap? |
| SNI and listener | Is the correct certificate selected? |
| Region and integration | Is the certificate available where the service requires it? |

# Termination choices

Terminate at an ALB or CloudFront when managed routing and policy are required. Re-encrypt to the origin when the second hop also requires TLS. Use pass-through when the target must own the end-to-end handshake.

# Enforcement

Use HTTPS-only listeners or redirect policies as appropriate, S3 `aws:SecureTransport` denies, database TLS settings, EFS TLS mounts, and private network paths where required.

# Related pages

- [Certificate Manager](../services/certificate-manager.md)
- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
