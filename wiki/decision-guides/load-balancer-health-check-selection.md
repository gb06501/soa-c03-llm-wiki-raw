---
type: Decision Guide
title: Load balancer and health-check selection
description: Selects the load balancer and health source from protocol, routing, reachability, and failover requirements.
tags: [soa-c03, domain-2, load-balancing, health-checks, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.2.1"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
status: verified
---

# Decision table

| Requirement | Choose |
| --- | --- |
| Route HTTP by host, path, header, or similar content | ALB |
| Balance TCP, UDP, or TLS with static IP needs | NLB |
| Insert and scale network appliances | GWLB |
| Remove an unhealthy backend from one load balancer | ELB target health |
| Choose a DNS endpoint by public reachability | Route 53 endpoint health check |
| Combine several health signals | Calculated Route 53 health check |
| Represent private or metric-derived health | CloudWatch alarm health check |
| Inherit supported alias-target health | Alias `EvaluateTargetHealth` |
| Replace an unhealthy EC2 fleet member | Auto Scaling health and replacement |

# Rejection rules

- Do not choose ALB solely for a static-IP requirement.
- Do not use GWLB for ordinary application targets.
- Do not infer target health from listener configuration.
- Do not expect a public Route 53 checker to reach a private endpoint.
- Do not assume a healthy target proves every dependency or user path.
- Do not expect DNS failover to bypass resolver caching immediately.

# Evidence and verification

Trace listener to rule to target group to target, then inspect target reason and network/application evidence. For DNS, verify record policy, attached health source, secondary health, returned answers, TTL, and application behavior.

# Related concepts

- [Load balancing and health checks](../services/load-balancing-and-health-checks.md)
- [Unhealthy target and DNS failover](../playbooks/unhealthy-target-and-dns-failover.md)

# Sources

- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
