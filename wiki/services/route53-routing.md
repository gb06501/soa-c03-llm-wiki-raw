---
type: AWS Feature
title: Route 53 routing
parent_services: [Route 53]
description: Selects DNS answers through routing policy, health eligibility, TTL, and authoritative or Resolver query evidence.
tags: ["soa-c03", "domain-5", "route-53", "dns-routing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md
status: verified
---

# Parent service

[Route 53](route-53.md)

# Routing policies

Simple, weighted, latency, failover, geolocation, geoproximity, multivalue, and IP-based routing solve different selection problems. Route 53 returns answers; it does not proxy requests or perform exact request balancing.

# Health and TTL

Endpoint, calculated, alarm-based, or alias target health can remove eligible answers. Public checkers cannot directly reach private endpoints. Failover time includes detection plus recursive/client cache TTL, and all-unhealthy behavior can fail open.

# Logging boundary

Public query logs record authoritative queries that reach a public hosted zone. Resolver query logs record VPC Resolver activity. CloudTrail records configuration changes, not DNS queries.

# Safe operations

Prepare a healthy endpoint, lower TTL before migration, introduce low weight or inactive role, observe DNS and application evidence, shift gradually, restore normal TTL, and retain rollback through the cache window.

# Related pages

- [DNS routing policy selection](../decision-guides/dns-routing-policy-selection.md)
- [DNS routing failure](../playbooks/dns-routing-failure.md)

# Sources

- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
