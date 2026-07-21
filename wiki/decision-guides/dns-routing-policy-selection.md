---
type: Decision Guide
title: DNS routing policy selection
description: Chooses Route 53 policy, record properties, health model, TTL, and authoritative or Resolver logging.
tags: ["soa-c03", "domain-5", "dns", "route-53"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| One answer set without policy | simple |
| Approximate controlled DNS split | weighted |
| Lowest measured latency Region | latency |
| Active/passive DNS recovery | failover |
| User geographic location | geolocation with default |
| Shift geographic boundary | geoproximity bias |
| Return multiple healthy IPs | multivalue |
| Map resolver-source CIDR | IP-based |
| Combine endpoints/alarms | calculated or alarm-based health |
| Health of supported alias target | EvaluateTargetHealth |

# Rejection rules

- Weighted answers are not exact request percentages.
- Multivalue is not a load balancer.
- Latency is measured behavior, not fixed geography.
- Public health checkers cannot reach private-only endpoints.
- Failover includes health-detection and TTL/cache time.
- All unhealthy records can fail open.
- Public query logs and Resolver query logs capture different queries.
- CloudTrail records configuration, not DNS requests.

# Verification

Confirm matching zone/name/type, policy fields, eligibility and health, source geography/CIDR, answer/TTL from multiple paths, authoritative or Resolver logs, and application health after using the answer.

# Related pages

- [Route 53 routing](../services/route53-routing.md)
- [DNS routing failure](../playbooks/dns-routing-failure.md)

# Sources

- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
