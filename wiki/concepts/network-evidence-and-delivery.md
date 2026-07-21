---
type: Concept
title: Network evidence and delivery
description: Unifies packet path, DNS, edge delivery, protection, logs, metrics, cost, and application verification across Domain 5.
tags: ["soa-c03", "domain-5", "networking", "evidence"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1", "5.1.2", "5.1.3", "5.1.4", "5.2.1", "5.2.2", "5.2.3", "5.3.1", "5.3.2", "5.3.3", "5.3.4", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.2.1-configure-dns-and-route-53-resolver.md
  - /raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Evidence layers

| Layer | Decisive objects |
| --- | --- |
| Name selection | Resolver, zone, rule, record, TTL, returned address |
| Packet path | source ENI, longest-prefix routes, gateway/attachment, return route |
| Security | SG, NACL, endpoint/resource policy, firewall/WAF rule |
| Connectivity state | endpoint, peering, TGW, VPN, Direct Connect, target health |
| Edge delivery | CloudFront behavior/cache/origin or accelerator dial/endpoint |
| Observed traffic | Flow, ELB, WAF, CloudFront, Resolver, firewall, workload logs |
| Performance | probes, real-flow monitoring, internet events, component metrics |
| Outcome | TLS, application status, user journey, workload SLO |

# Diagnostic rule

Start with the exact source, destination/name, protocol, port, time, account, Region, and AZ. Find the last layer with good evidence and the first layer with missing or failing evidence. Prove the return path and application result.

# Decision layers

Choose service access versus network routing; DNS answer versus proxied connection; stateful versus stateless control; synthetic versus real-flow monitoring; cache versus non-cache acceleration; and fixed versus per-byte cost.

# Safe-change loop

Capture current associations, routes, policies, TTLs, and health. Add a narrow alternative, test forward and return behavior, expand gradually, observe logs/metrics/application, then retire the old path with rollback retained.

# Related pages

- [Packet-path diagnostics](packet-path-diagnostics.md)
- [Network logging](network-logging.md)
- [Domain 5 learning path](../learning/paths/domain-5-learning-path.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.3](../../raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
