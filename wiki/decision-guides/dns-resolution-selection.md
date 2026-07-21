---
type: Decision Guide
title: DNS resolution selection
description: Chooses hosted zones, record types, Resolver direction, forwarding rules, private namespace associations, and hybrid DNS paths.
tags: ["soa-c03", "domain-5", "dns", "resolver"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.1-configure-dns-and-route-53-resolver.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Public authoritative namespace | public hosted zone |
| VPC-private namespace | private hosted zone plus VPC association |
| Zone-apex AWS target | Route 53 alias |
| External DNS asks AWS private names | inbound Resolver endpoint plus external conditional forwarder |
| VPC asks external private names | outbound endpoint plus forwarding rule and VPC association |
| Share a Resolver rule | RAM share then explicit VPC association |
| Same name with public/private answers | deliberate split-horizon zones |
| Govern VPC domain queries | Resolver DNS Firewall |

# Rejection rules

- A CNAME cannot be used at zone apex; alias is Route 53-specific.
- A private zone can shadow public names and return NXDOMAIN without fallback.
- Inbound and outbound endpoint directions are not interchangeable.
- A shared rule is not automatically associated.
- Connected networks do not automatically share private DNS.
- Endpoint paths need both UDP and TCP 53 where required.
- DNS success does not prove target reachability.

# Verification

Query from every actual resolver path; record resolver, answer, rcode, TTL, and chain. Verify zone/rule specificity, endpoint state, SG/routes/firewall, upstream logs, Resolver logs, then test the returned target.

# Related pages

- [Route 53 Resolver](../services/route53-resolver.md)
- [DNS resolution failure](../playbooks/dns-resolution-failure.md)

# Sources

- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
