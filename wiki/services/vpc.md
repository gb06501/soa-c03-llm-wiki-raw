---
type: AWS Service
title: VPC
service_id: vpc
description: Provides network boundaries, routes, endpoints, and private connectivity that constrain security-service data paths.
tags: ["soa-c03", "domain-4", "vpc", "private-connectivity", domain-5, networking, routing]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["4.1.2", "4.2.3", "4.2.4", "5.1.1", "5.1.2", "5.1.3", "5.1.4", "5.2.1", "5.2.2", "5.2.3", "5.3.1", "5.3.2", "5.3.3", "5.3.4", "5.3.5"]
domain_ids: ["4", "5"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
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
# Core model

A VPC data path depends on addressing, routes, security groups, network ACLs, name resolution, endpoint selection, and service policy. Authorization success does not prove network reachability, and network reachability does not grant authorization.

# Security integrations

| Mechanism | Use |
| --- | --- |
| Interface endpoint | Private access to supported service APIs |
| Gateway endpoint | Private route-based access for supported services |
| Endpoint policy | Additional authorization boundary on endpoint traffic |
| Security group | Stateful traffic control for interfaces and endpoints |
| Site-to-Site VPN | Encrypted network path between networks |

# Evidence and diagnosis

Resolve the service name, endpoint DNS mode, subnet/AZ placement, route, security-group direction, NACL, source address, proxy, endpoint policy, and service/KMS policy separately.

# Safe operations

Prefer least-privilege endpoint policies, explicit DNS ownership, redundant endpoint placement where required, and path tests from the actual workload identity and network.

# Related decisions

- [Access denial evidence selection](../decision-guides/access-denial-evidence-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Domain 5: Packet paths and connectivity

## Route and security model

A Domain 5 VPC path is resolved by the exact source/destination, longest-prefix route in each direction, target or attachment state, SG and ordered NACL behavior, transformed addresses, and application listener. IPv4 and IPv6 require independent routes and rules.

## Private and hybrid connectivity

Gateway/interface endpoints, PrivateLink, peering, Transit Gateway, VPN, Direct Connect, and Client VPN solve different scopes. Private connectivity still requires DNS, forward/return routes, security, policy, target health, and AZ coverage.

## Evidence and verification

Use route associations, Flow Logs, Reachability Analyzer, NAT/endpoint/TGW/VPN metrics, Resolver tests, CloudTrail/Config, and real application evidence. ACCEPT or a modeled path is not proof that the application responded.

## Related Domain 5 decisions

- [VPC addressing and routing selection](../decision-guides/vpc-addressing-routing-selection.md)
- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [VPC connectivity failure](../playbooks/vpc-connectivity-failure.md)

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
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
