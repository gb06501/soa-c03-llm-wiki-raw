---
type: AWS Feature
title: Route 53 Resolver
parent_services: [Route 53]
description: Resolves VPC DNS and connects private namespaces to external DNS through inbound/outbound endpoints and forwarding rules.
tags: ["soa-c03", "domain-5", "route-53", "resolver"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.1-configure-dns-and-route-53-resolver.md
status: verified
---

# Parent service

[Route 53](route-53.md)

# Core model

Inbound endpoints let external networks query AWS Resolver. Outbound endpoints send matching VPC queries to external DNS through forwarding rules. The most-specific domain rule wins.

# Key objects

VPC DNS attributes, private hosted-zone association, inbound/outbound endpoint ENIs, security groups, forwarding rules, RAM shares, VPC rule associations, upstream servers, and Resolver query logs.

# Decision boundaries

A share is not a VPC association. An outbound endpoint without a matching rule/association does nothing. An inbound endpoint still requires conditional forwarding from external DNS. Private zones can shadow public names without fallback.

# Evidence

Query from the failing resolver, inspect answer/rcode/TTL, endpoint state/IPs, UDP and TCP 53, route/SG/NACL/firewall, rule match and association, upstream logs, Resolver logs, and CloudTrail changes.

# Related pages

- [DNS resolution selection](../decision-guides/dns-resolution-selection.md)
- [DNS resolution failure](../playbooks/dns-resolution-failure.md)

# Sources

- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
