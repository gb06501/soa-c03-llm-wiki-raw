---
type: AWS Service
title: VPC
service_id: vpc
description: Provides network boundaries, routes, endpoints, and private connectivity that constrain security-service data paths.
tags: ["soa-c03", "domain-4", "vpc", "private-connectivity"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.2", "4.2.3", "4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
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

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
