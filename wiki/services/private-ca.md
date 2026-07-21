---
type: AWS Service
title: Private CA
service_id: private-ca
description: Operates private certificate authorities for internal PKI and private TLS trust.
tags: ["soa-c03", "domain-4", "private-ca", "pki"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---
# Core model

Private CA creates a private trust hierarchy. The root or subordinate CA issues certificates whose trust depends on distributing the correct private root to clients.

# Decision boundaries

Use private certificates for internal identities that do not need public-browser trust. Choose root versus subordinate placement based on blast radius, offline-root requirements, delegation, and lifecycle ownership.

# Evidence and diagnosis

Verify CA state, chain, template, subject and SANs, issuance permissions, revocation configuration, client trust store, and certificate deployment.

# Safe operations

Separate CA administration from certificate consumption, constrain issuance templates and principals, publish revocation information, protect root trust, and rehearse CA and certificate rotation.

# Related decisions

- [Encryption in transit](../concepts/encryption-in-transit.md)
- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
