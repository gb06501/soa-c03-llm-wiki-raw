---
type: Troubleshooting Playbook
title: TLS connectivity failure
description: Diagnoses DNS, route, TCP, protocol, certificate identity, trust-chain, SNI, listener, origin, and application failures.
tags: ["soa-c03", "domain-4", "troubleshooting", "tls", "connectivity"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---

# Trigger

A client reports timeout, connection reset, protocol mismatch, certificate warning, handshake failure, or HTTPS response failure.

# Evidence path

1. Record client location, requested hostname, port, timestamp, endpoint, and error.
2. Resolve DNS from the client path and confirm the intended endpoint.
3. Prove route and TCP reachability before changing certificates.
4. Capture the TLS handshake: protocol, cipher, SNI, presented leaf/chain, SANs, issuer, and validity.
5. Inspect Certificate Manager status, Region, renewal, and attachment.
6. For ELB or CloudFront, separate viewer/client TLS from target/origin TLS.
7. Check listener policy, target protocol, backend trust, redirects, S3 secure-transport policy, or database/file-system TLS settings.
8. After handshake success, inspect HTTP/application health separately.

# Failure map

| Symptom | Direction |
| --- | --- |
| Timeout | DNS, route, security group, NACL, endpoint |
| No shared protocol/cipher | client/server TLS policy |
| Hostname mismatch | SAN, requested name, wrong endpoint |
| Unknown issuer/incomplete chain | client trust store or deployment chain |
| One hostname fails | SNI/certificate attachment/SAN |
| CloudFront viewer succeeds, origin fails | origin hostname, chain, protocol policy |
| TLS succeeds, HTTP fails | listener routing, authentication, application |

# Safe action

Correct the earliest proven layer. Rotate certificates with overlap, add before removing, preserve compatible policies for required clients, and test the second TLS hop independently.

# Verification

Repeat DNS, TCP, handshake, hostname and chain validation, then application request from every required client path. Confirm monitoring sees the new certificate and no unintended plaintext path remains.

# Rollback

Reattach the prior certificate or policy and restore the prior listener/origin setting while keeping evidence of the failed change.

# Escalation

Provide DNS results, endpoint/listener configuration, handshake output, certificate ARN/status/SANs, client policy, origin evidence, and rollback state.

# Related pages

- [Encryption in transit](../concepts/encryption-in-transit.md)
- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
