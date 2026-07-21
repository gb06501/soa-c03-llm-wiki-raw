---
type: Exam Trap
title: Domain 5 exam traps
description: Corrects tempting VPC, connectivity, protection, cost, DNS, edge, logging, cache, hybrid, and monitoring misconceptions.
tags: ["soa-c03", "domain-5", "exam-traps"]
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

# VPC addressing and packet paths

- A subnet is public because its route targets an internet gateway, not because of its name.
- Public IPv4 access needs both a public address and an IGW route.
- NAT Gateway provides outbound translation, not unsolicited inbound access.
- NAT Gateway has no security group.
- Egress-only internet gateway is for outbound-initiated IPv6, not IPv4 NAT.
- Longest-prefix route wins in each direction.
- Security groups are stateful and allow-only; NACLs are stateless, ordered, and allow/deny.
- NACL return and ephemeral traffic must be explicit.
- Adding a VPC CIDR does not resize an existing subnet.
- Active route and Flow Log ACCEPT do not prove application health.

# Private and hybrid connectivity

- Gateway endpoints use route-table associations and no ENI security group.
- Interface endpoints use ENIs, security groups, and private DNS.
- Endpoint policy restricts access but does not grant IAM permission.
- PrivateLink exposes one service, not a whole provider VPC.
- Peering is non-transitive and cannot borrow peer NAT, IGW, or VPN transit.
- Transit Gateway association selects ingress lookup; propagation installs destinations.
- Tunnel UP does not prove BGP, routes, or traffic.
- BGP UP does not prove correct prefixes or return routes.
- Direct Connect is not encrypted merely because it is private.
- Client VPN needs authentication, authorization, route, target association, security, and DNS.
- Small packets working while large transfers stall suggests MTU/MSS.

# Network protection

- DNS Firewall ALERT and WAF COUNT observe; they do not block.
- Lower numeric priority evaluates first for DNS Firewall and WAF.
- WAF filters HTTP/HTTPS, not arbitrary TCP/UDP.
- Shield does not replace WAF for application attacks.
- Network Firewall protects only traffic routed through it.
- Stateful firewall requires compatible symmetric forward/return paths.
- A policy with no association or path insertion protects nothing.
- Sampled WAF requests are not complete logs.

# Network cost

- S3/DynamoDB gateway endpoints can avoid NAT processing without endpoint-hour cost.
- Interface endpoints have per-AZ fixed cost and are not always cheaper.
- One NAT per AZ improves resilience and can avoid cross-AZ traffic but adds fixed cost.
- Central NAT can add cross-AZ transfer and one-AZ dependency.
- PrivateLink isolation can justify its cost.
- CloudFront reduces origin cost only when requests cache effectively.
- Global Accelerator does not cache.
- Savings Plans do not remove network transfer charges.
- Do not remove HA, security, or audit evidence only for cost.

# DNS and Route 53

- Public hosted zones provide answers, not reachability.
- Private zones can shadow public names and return NXDOMAIN without fallback.
- CNAME cannot be used at zone apex; Route 53 alias can.
- Inbound Resolver endpoints accept external-to-AWS queries; outbound endpoints forward AWS-to-external queries.
- A shared Resolver rule is not automatically associated.
- Weighted routing is not exact request percentage.
- Multivalue routing is not a load balancer.
- Public health checkers cannot directly reach private endpoints.
- Failover time includes health detection and TTL/cache.
- All unhealthy records can fail open.
- Public query logs, Resolver query logs, and CloudTrail record different events.

# Edge delivery and caching

- CloudFront caches HTTP/HTTPS; Global Accelerator routes TCP/UDP without caching.
- Route 53 returns DNS; it does not proxy connections.
- First matching CloudFront behavior wins.
- Cache policy defines the key; origin request policy can forward more without changing it.
- Missing response-varying values can share wrong/private content.
- Positive minimum TTL can cache despite restrictive origin directives.
- Invalidation removes copies but does not fix origin or policy.
- Versioned names are preferred for normal static releases.
- Viewer and origin TLS are separate.
- OAC requires S3 REST origin; website endpoints cannot use it.
- OAC bucket policy and KMS policy are separate.
- Origin group is failover, not weighted balancing.
- WAF at CloudFront does not protect a directly reachable origin.

# Logs and monitoring

- Flow Logs contain metadata, not payload.
- REJECT does not identify the exact SG/NACL rule.
- NODATA means no eligible traffic; SKIPDATA means incomplete evidence.
- ALB status and target status point to different layers.
- WAF terminating rule determines final action.
- A CloudFront cache hit normally creates no origin request log.
- Log absence can mean no arrival, disabled delivery, caching, or bypass.
- Reachability Analyzer sends no packets.
- Synthetic Monitor uses configured probes; Flow Monitor observes real supported TCP flows.
- Internet Monitor reports public user impact, not private VPN health.
- RTT increase alone does not prove AWS caused it.
- Zero errors with zero traffic and missing data are not health.
- Aggregate Regional metrics can hide one-AZ failure.

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
