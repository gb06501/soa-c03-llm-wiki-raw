---
type: Troubleshooting Playbook
title: DNS routing failure
description: Diagnoses Route 53 policy eligibility, health, source geography/CIDR, TTL, fail-open behavior, and query-log delivery.
tags: ["soa-c03", "domain-5", "troubleshooting", "dns", "route-53"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md
status: verified
---

# Trigger

Route 53 returns an unexpected endpoint, fails to shift traffic, distributes differently than expected, or DNS query logs are missing.

# Evidence path

1. Confirm queried name/type and the authoritative hosted zone.
2. Inspect policy type and required record properties/set identifiers.
3. Determine source resolver geography/CIDR and eligible records.
4. Inspect health-check or alias target health and reachability.
5. Query from representative resolvers and record answers/TTLs over time.
6. Account for health detection, recursive/client caching, and all-unhealthy fail-open.
7. For logs, choose public authoritative versus VPC Resolver query logs.
8. Verify log configuration association, destination policy/KMS, generated test query, and delivery.
9. Correlate application health and CloudTrail record/health/log changes.

# Failure map

| Symptom | Direction |
| --- | --- |
| Weighted split unexpected | resolver caching/sample size/weights/eligibility |
| Geolocation no answer | missing default record |
| Failover slow | detection plus TTL/cache |
| Private endpoint marked unhealthy | public checker cannot reach it |
| Old endpoint persists | TTL/client/intermediate cache |
| All unhealthy still answered | fail-open behavior |
| No public log | wrong zone/config/destination or cache |
| No Resolver log | wrong VPC association/scope/destination |

# Safe action

Prepare a healthy endpoint, lower TTL before planned change, introduce low weight or inactive role, shift gradually with application evidence, and retain old capacity for rollback.

# Verification

Observe expected answers and health from multiple paths across cache windows, verify endpoint application health, and confirm the correct query-log stream and fields.

# Rollback

Restore weight/role/record and keep the previous endpoint until caches have converged.

# Escalation

Provide record sets, health evidence, source-resolver context, query samples, TTL timing, log configuration, and application results.

# Related pages

- [Route 53 routing](../services/route53-routing.md)
- [DNS routing policy selection](../decision-guides/dns-routing-policy-selection.md)

# Sources

- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
