---
type: AWS Service
title: Certificate Manager
service_id: certificate-manager
description: Provisions and manages public or imported TLS certificates for supported AWS integrations.
tags: ["soa-c03", "domain-4", "acm", "tls"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---
# Core model

Certificate Manager manages certificate identity, subject names, validation, Region, renewal state, and deployment to supported integrated services.

# Certificate choices

| Choice | Best fit |
| --- | --- |
| Managed public certificate | Publicly trusted endpoint on a supported integration |
| Imported certificate | Existing external certificate or unsupported issuance workflow |
| Private certificate | Internal trust anchored in Private CA |

# Decision boundaries

A certificate must cover the requested hostname, include a valid chain, reside in the Region required by the integration, and be attached to the correct listener or distribution. Renewal does not prove deployment changed everywhere.

# Evidence and diagnosis

Check requested hostname, SAN coverage, validation records, status, expiration, chain order, key compatibility, listener attachment, SNI selection, and client trust.

# Safe operations

Automate DNS validation where controlled, monitor renewal and in-use status, overlap certificate rotation, and test both old and new client paths before retiring a certificate.

# Related decisions

- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
