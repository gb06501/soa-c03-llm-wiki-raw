---
type: Troubleshooting Playbook
title: Unhealthy target and DNS failover
description: Separates load-balancer target failure from Route 53 health and DNS failover problems.
tags: [soa-c03, domain-2, load-balancing, route53, troubleshooting]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.2.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
status: verified
---

# Trigger

A target is unhealthy or unused, users reach the wrong endpoint, or Route 53 does not fail over as expected.

# Evidence path

1. Decide whether the failure is target membership, listener routing, application behavior, or DNS answer selection.
2. Trace listener, rule priority/action, target group, registered target, port, and enabled AZ.
3. Inspect target-health state and reason.
4. Test health-check path, matcher, application readiness, and dependencies.
5. Verify load-balancer-to-target SG and NACL request/return path.
6. For DNS, inspect record policy, health association, alias target-health setting, and secondary health.
7. Query DNS from relevant resolvers and account for TTL/cache.

# Failure map

| Symptom | Direction |
| --- | --- |
| All targets unhealthy | Shared path/port/matcher, network, application |
| One target unhealthy | Local app, registration, overload, network |
| Healthy but no traffic | Listener rule, action, AZ, cross-zone behavior |
| Stays initial | Registration, startup, health path, enabled AZ |
| Route 53 returns failed endpoint | Record/health association, state, TTL/cache |
| Private endpoint check fails | Public checker reachability; alarm pattern |
| Failover record unused | Primary association or unhealthy secondary |

# Safe action

Fix the narrow failing layer. Do not weaken a health check merely to make it green; ensure it represents the dependency level required for safe traffic.

# Verification

Confirm target health and real requests, expected listener routing, healthy capacity in required AZs, correct DNS answers from fresh queries, secondary readiness, and stable service after TTL expiry.

# Sources

- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
