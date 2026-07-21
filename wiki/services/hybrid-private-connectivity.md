---
type: Concept
title: Hybrid and private connectivity
description: Diagnoses underlay, tunnel or circuit state, routing control plane, forward/return data path, security, DNS, MTU, and application layers.
tags: ["soa-c03", "domain-5", "hybrid", "private-connectivity"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
status: verified
---

# Layer model

1. DNS name and selected address.
2. Internet/private underlay.
3. VPN tunnel, VIF, endpoint, peering, or attachment state.
4. BGP/static/propagated control-plane routes.
5. Forward and return data-plane routes.
6. SG/NACL/firewall and endpoint/resource/IAM/KMS policy.
7. MTU, TLS, and application.

# Symptom boundaries

Tunnel UP does not prove BGP or traffic. BGP UP does not prove correct prefixes. Client VPN connected does not prove authorization or route. Endpoint timeout suggests DNS/network; AccessDenied suggests policy. Small packets working while large transfers stall suggests MTU/MSS.

# Evidence

Correlate AWS state/metrics/logs with customer router/firewall, Resolver, Flow Logs, Reachability Analyzer, CloudTrail/Config, and tests from the actual source network.

# Related pages

- [Direct Connect](direct-connect.md)
- [Site-to-Site VPN](site-to-site-vpn.md)
- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)

# Sources

- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
