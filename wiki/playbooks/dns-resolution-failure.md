---
type: Troubleshooting Playbook
title: DNS resolution failure
description: Diagnoses namespace, hosted-zone association, Resolver direction, forwarding rules, endpoint network paths, caches, and upstream DNS.
tags: ["soa-c03", "domain-5", "troubleshooting", "dns", "resolver"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.1-configure-dns-and-route-53-resolver.md
status: verified
---

# Trigger

A name returns NXDOMAIN, SERVFAIL, timeout, a wrong public/private answer, or works from one resolver/VPC/network but not another.

# Evidence path

1. Query the exact name/type from the failing source and record resolver, rcode, answer, TTL, and chain.
2. Determine public versus private authoritative namespace and most-specific matching zone.
3. Inspect private-zone VPC association, split-horizon shadowing, and overlapping zones.
4. Check VPC DNS support/hostnames and client resolver configuration.
5. For inbound, verify external conditional forwarding to endpoint IPs.
6. For outbound, verify endpoint state, forwarding rule, most-specific match, share, and VPC association.
7. Check endpoint SG, UDP/TCP 53, subnet routes, NACL/firewall, and upstream DNS.
8. Inspect Resolver query logs, on-prem logs, Flow Logs, and CloudTrail changes.
9. Account for positive/negative caches and TTL.
10. Test reachability of the returned address separately.

# Failure map

| Symptom | Direction |
| --- | --- |
| Private name works in one VPC | zone/rule association or resolver path |
| Public name NXDOMAIN privately | private-zone shadowing |
| On-prem cannot resolve AWS | inbound endpoint and conditional forwarder |
| AWS cannot resolve on-prem | outbound endpoint, rule/association, upstream |
| UDP works, large answer fails | TCP 53 path |
| Rule shared, unused | VPC association missing |
| Correct answer, app fails | network/TLS/application after DNS |

# Safe action

Add and test the new zone/rule/endpoint path before removing the old one; lower planned public TTL early and retain rollback through cache windows.

# Verification

Test every VPC/on-prem resolver, UDP/TCP where needed, expected public/private answers and TTL, query logs, and application reachability.

# Rollback

Restore the prior zone association, rule, endpoint, delegation, or record and wait for relevant caches.

# Escalation

Provide query transcript, zone/rule specificity, endpoint/network evidence, upstream result, logs, and cache timing.

# Related pages

- [Route 53 Resolver](../services/route53-resolver.md)
- [DNS resolution selection](../decision-guides/dns-resolution-selection.md)

# Sources

- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
