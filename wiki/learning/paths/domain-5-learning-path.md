---
type: Learning Path
title: Domain 5 learning path
description: Orders Domain 5 study from packet paths and private connectivity through protection, DNS, edge delivery, logging, caching, hybrid diagnosis, and monitoring.
tags: ["soa-c03", "domain-5", "learning-path"]
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

# Stage 1: Build the packet-path model

1. [VPC networking](../../services/vpc-networking.md) and [VPC](../../services/vpc.md)
2. [VPC IPAM](../../services/vpc-ipam.md), [NAT Gateway](../../services/nat-gateway.md), and [VPC Flow Logs](../../services/vpc-flow-logs.md)
3. [VPC addressing and routing selection](../../decision-guides/vpc-addressing-routing-selection.md)
4. [Packet-path diagnostics](../../concepts/packet-path-diagnostics.md)
5. [VPC connectivity failure](../../playbooks/vpc-connectivity-failure.md)

Goal: trace the exact forward and return flow through longest-prefix routes, transformations, stateful and stateless controls, addresses, and application state.

# Stage 2: Choose private and hybrid connectivity

1. [Private connectivity](../../services/private-connectivity.md)
2. [PrivateLink](../../services/privatelink.md), [Transit Gateway](../../services/transit-gateway.md), and [Direct Connect](../../services/direct-connect.md)
3. [Site-to-Site VPN](../../services/site-to-site-vpn.md) and [Client VPN](../../services/client-vpn.md)
4. [Private connectivity selection](../../decision-guides/private-connectivity-selection.md)
5. [Hybrid and private connectivity failure](../../playbooks/hybrid-private-connectivity-failure.md)

Goal: distinguish service access from routed networks and prove DNS, object state, routes, policy, target health, redundancy, and the real source path.

# Stage 3: Audit network protection

1. [Network protection](../../services/network-protection.md)
2. [Route 53 Resolver DNS Firewall](../../services/route53-resolver-dns-firewall.md), [WAF](../../services/waf.md), [Shield](../../services/shield.md), and [Network Firewall](../../services/network-firewall.md)
3. [Network protection selection](../../decision-guides/network-protection-selection.md)
4. [Network protection gap](../../playbooks/network-protection-gap.md)

Goal: select the right traffic layer, prove association and path coverage, understand rule priority/action, roll out enforcement safely, and find bypasses.

# Stage 4: Optimize network cost

1. [Network cost optimization](../../concepts/network-cost-optimization.md)
2. [Cost Explorer](../../services/cost-explorer.md), [Athena](../../services/athena.md), and [VPC Flow Logs](../../services/vpc-flow-logs.md)
3. [Network cost optimization guide](../../decision-guides/network-cost-optimization.md)
4. [Network cost anomaly](../../playbooks/network-cost-anomaly.md)

Goal: connect billed usage to the exact charged path and verify savings without weakening availability, security, or evidence.

# Stage 5: Operate DNS and routing policy

1. [Route 53 Resolver](../../services/route53-resolver.md) and [DNS resolution selection](../../decision-guides/dns-resolution-selection.md)
2. [DNS resolution failure](../../playbooks/dns-resolution-failure.md)
3. [Route 53 routing](../../services/route53-routing.md) and [DNS routing policy selection](../../decision-guides/dns-routing-policy-selection.md)
4. [DNS routing failure](../../playbooks/dns-routing-failure.md)

Goal: separate recursive and authoritative DNS, endpoint direction, rule/zone specificity, policy eligibility, health, TTL, logging, and target reachability.

# Stage 6: Deliver content and services globally

1. [Content and service distribution](../../services/content-distribution.md)
2. [CloudFront](../../services/cloudfront.md), [Global Accelerator](../../services/global-accelerator.md), [Route 53](../../services/route-53.md), and [Elastic Load Balancing](../../services/elastic-load-balancing.md)
3. [Content distribution selection](../../decision-guides/content-distribution-selection.md)
4. [Edge delivery failure](../../playbooks/edge-delivery-failure.md)

Goal: choose DNS, edge caching, global TCP/UDP acceleration, or Regional balancing and diagnose behavior, TLS, access, origin, dial, weight, and health.

# Stage 7: Trace requests and repair caching

1. [Network logging](../../concepts/network-logging.md) and [VPC Flow Logs](../../services/vpc-flow-logs.md)
2. [Network log selection](../../decision-guides/network-log-selection.md)
3. [Network request tracing](../../playbooks/network-request-tracing.md)
4. [CloudFront caching](../../services/cloudfront-caching.md) and [CloudFront cache policy selection](../../decision-guides/cloudfront-cache-policy-selection.md)
5. [CloudFront cache failure](../../playbooks/cloudfront-cache-failure.md)

Goal: correlate the last good and first bad layer, then fix cache behavior without harming privacy or origin health.

# Stage 8: Monitor and verify network performance

1. [CloudWatch network monitoring](../../services/cloudwatch-network-monitoring.md)
2. [Network Synthetic Monitor](../../services/cloudwatch-network-synthetic-monitor.md), [Network Flow Monitor](../../services/cloudwatch-network-flow-monitor.md), [Internet Monitor](../../services/cloudwatch-internet-monitor.md), and [CloudWatch Synthetics](../../services/cloudwatch-synthetics.md)
3. [Network monitor selection](../../decision-guides/network-monitor-selection.md)
4. [Network performance diagnosis](../../playbooks/network-performance-diagnosis.md)
5. [Domain 5 exam traps](../../exam-traps/domain-5-exam-traps.md)

Goal: select the right monitor, preserve dimensions, correlate metrics with logs/configuration, and verify remediation through application outcomes.

# Retrieval drills

For every scenario, answer:

1. What exact source, destination/name, protocol, port, Region, AZ, and time are involved?
2. Is the requirement DNS selection, service access, routed connectivity, protection, caching, or observation?
3. Which object and evidence prove the first failing layer?
4. What is the smallest reversible change?
5. Which forward, return, security, cost, and application checks prove success?

# Sources

- [Skill 5.1.1](../../../raw/skills/5.1.1-configure-a-vpc.md)
- [Skill 5.1.2](../../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.3](../../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.1.4](../../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.2.1](../../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
- [Skill 5.2.2](../../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
- [Skill 5.2.3](../../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.1](../../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.2](../../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.3](../../../raw/skills/5.3.3-identify-and-remediate-cloudfront-caching-issues.md)
- [Skill 5.3.4](../../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
- [Skill 5.3.5](../../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
