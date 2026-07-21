---
type: Troubleshooting Playbook
title: Hybrid and private connectivity failure
description: Diagnoses VPN, Direct Connect, Client VPN, endpoints, peering, Transit Gateway, hybrid DNS, MTU, and return paths.
tags: ["soa-c03", "domain-5", "troubleshooting", "hybrid", "private-connectivity"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.3.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
status: verified
---

# Trigger

A private, cross-VPC, remote-user, or hybrid path is down, one-way, denied, intermittently slow, or reachable only through an unintended public/NAT path.

# Evidence path

1. Record real source network, destination/name, protocol/port, time, and expected model.
2. Resolve DNS from the failing network.
3. Separate physical/underlay, tunnel/VIF/endpoint/attachment, BGP/static route, and data path.
4. Inspect both VPN tunnels or Direct Connect connection/VIF/BGP and exact prefixes.
5. Trace VPC routes, TGW association/propagation, peer routes, and return path.
6. Inspect endpoint state, ENIs/SG/private DNS/policy and provider NLB targets.
7. For Client VPN, prove authentication, authorization, route, association, security, and DNS.
8. Correlate tunnel/VIF/endpoint metrics/logs, Flow Logs, Resolver, customer device, and application.
9. Test MTU/MSS when small packets work but large transfers fail.
10. Correlate recent address, PSK, BGP, route, policy, DNS, or certificate change.

# Failure map

| Symptom | Direction |
| --- | --- |
| Tunnel DOWN | underlay, public IP, PSK, IKE/IPsec proposal |
| Tunnel UP, no traffic | BGP/static prefixes, routes, security, return path |
| One tunnel down | degraded redundancy and tunnel-specific config |
| Client connected, resource denied | authorization/route/association/SG |
| Endpoint timeout | private DNS, ENI SG, route, provider health |
| Endpoint AccessDenied | endpoint/IAM/resource/KMS policy |
| A-B and B-C work, A-C fails | expected peering non-transitivity |
| TGW one-way | reverse VPC/TGW associated-table route |
| Large transfer stalls | MTU/MSS/fragmentation/asymmetry |

# Safe action

Keep the healthy redundant path active. Repair one tunnel, route, association, propagation, endpoint, or policy at a time; verify both directions before restoring preference or retiring fallback.

# Verification

Confirm both tunnels/paths as required, exact prefixes, DNS, real client traffic, logs/metrics, application result, failover, and MTU behavior.

# Rollback

Restore prior route preference, TGW table, endpoint DNS/policy, or client configuration while preserving the proven healthy path.

# Escalation

Provide AWS and customer-side state/logs, prefixes, route chains, DNS answers, MTU evidence, affected scope, and rollback status.

# Related pages

- [Hybrid and private connectivity](../services/hybrid-private-connectivity.md)
- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
