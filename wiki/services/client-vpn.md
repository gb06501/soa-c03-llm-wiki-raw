---
type: AWS Feature
title: Client VPN
parent_services: [VPC]
description: Provides managed remote-user VPN access with separate authentication, authorization, routing, target association, and DNS gates.
tags: ["soa-c03", "domain-5", "client-vpn", "remote-access"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.3.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
status: verified
---

# Core model

`client -> endpoint authentication -> authorization rule -> endpoint route -> target-network association -> VPC security path -> destination`

A connected client tunnel proves only the first gate.

# Evidence and diagnosis

Check endpoint state, client configuration, certificate or identity provider, authorization rule CIDR/group, endpoint route, target-network association, security group, return route, client CIDR overlap, split/full tunnel behavior, DNS, and connection logs.

# Safe operations

Add the narrow authorization and route, test one user and destination, preserve existing sessions where possible, require reconnection when route behavior needs refresh, and verify both IP and private DNS.

# Related pages

- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
