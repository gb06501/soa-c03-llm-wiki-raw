---
type: Concept
title: Load balancing and health checks
description: Explains load-balancer selection, target health, and Route 53 health-driven DNS behavior.
tags: [soa-c03, domain-2, load-balancing, health-checks, route53]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["2.2.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
status: verified
---

# Core model

| Health layer | Controls |
| --- | --- |
| EC2 status check | Instance or platform health |
| ELB target health | Whether a target receives load-balancer traffic |
| Route 53 health | Which DNS answer is returned |

# Load-balancer selection

| Requirement | Choice |
| --- | --- |
| HTTP/HTTPS content routing | ALB |
| TCP/UDP/TLS, static IP, or extreme performance | NLB |
| Insert virtual network appliances | GWLB |
| Recognize an existing legacy design | CLB |

Listener, rule, target group, target type, protocol, port, enabled AZ, and health-check settings form one traffic path.

# Target health

Check protocol, port, path, matcher, interval, timeout, thresholds, startup, security groups, NACLs, enabled AZs, listener rules, and the application's dependencies.

A target can pass a narrow health path while real requests fail. A listener can also route users to a different target group than the one being inspected.

# Route 53 health

Endpoint checks, calculated checks, CloudWatch-alarm checks, and alias `EvaluateTargetHealth` support different evidence paths. Public health checkers cannot directly test a private endpoint; a CloudWatch-alarm pattern can represent private health.

# Evidence

Use target state/reason, healthy and unhealthy host counts, response time, HTTP/TCP errors, Flow Logs, Route 53 health status, alarm state, record association, and TTL/cache behavior.

# Exam traps

- Route 53 health does not change ELB target membership.
- Cross-zone balancing does not create capacity in an empty AZ.
- DNS failover is affected by TTL and resolver cache.
- A secondary endpoint must also be healthy and correctly configured.

# Related concepts

- [Load balancer and health-check selection](../decision-guides/load-balancer-health-check-selection.md)
- [Unhealthy target and DNS failover](../playbooks/unhealthy-target-and-dns-failover.md)

# Sources

- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
