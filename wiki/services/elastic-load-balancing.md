---
type: AWS Service
title: Elastic Load Balancing
service_id: elastic-load-balancing
description: Terminates, passes through, or routes encrypted connections through managed load balancers.
tags: ["soa-c03", "domain-4", "elastic-load-balancing", "tls"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---
# Core model

An Application Load Balancer commonly terminates HTTP/TLS and routes at Layer 7. A Network Load Balancer can terminate TLS or pass TCP through. Listener protocol, certificate, security policy, target protocol, and health checks are independent choices.

# Decision boundaries

Terminate when the load balancer must inspect and route application requests. Use pass-through when the target must own end-to-end TLS. Re-encryption creates a second independently validated TLS path.

# Evidence and diagnosis

Inspect DNS target, listener port/protocol, attached certificate and SANs, SNI selection, security policy, security groups, target group protocol/port, health, and backend certificate trust.

# Safe operations

Add and test the new certificate before removing the old one, preserve compatible policies for required clients, verify target health, and validate both handshake and application response.

# Related decisions

- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
