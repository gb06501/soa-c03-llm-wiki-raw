---
type: Decision Guide
title: TLS certificate selection
description: Chooses public, imported, or private certificates and the correct termination pattern for AWS endpoints.
tags: ["soa-c03", "domain-4", "tls", "certificates"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Public trust on supported AWS integration | managed public Certificate Manager certificate |
| Existing external issuer or unsupported issuance path | imported certificate with owned renewal |
| Internal private trust | Private CA certificate and distributed root trust |
| Layer-7 routing at load balancer | ALB TLS termination |
| High-performance Layer-4 with managed certificate | NLB TLS termination |
| Target must own handshake | TCP pass-through |
| Edge delivery | CloudFront viewer certificate plus independent origin TLS |
| Enforce S3 HTTPS | bucket-policy deny on insecure transport |
| Database client encryption | TLS connection with correct CA trust and endpoint hostname |
| Shared file client encryption | EFS TLS mount path |

# Rejection rules

- A valid certificate for the wrong hostname still fails identity validation.
- Renewal does not prove the new certificate is attached everywhere.
- CloudFront viewer and origin TLS are separate.
- TLS success does not prove application authorization or health.
- Private certificates are not publicly trusted without distributing the private root.

# Verification

Resolve the endpoint, perform a handshake with the requested hostname and expected client policy, inspect the presented chain and expiry, test the application response, and repeat for every TLS hop.

# Related pages

- [Encryption in transit](../concepts/encryption-in-transit.md)
- [Certificate Manager](../services/certificate-manager.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
