---
type: Decision Guide
title: Private connectivity selection
description: Chooses endpoint, PrivateLink, peering, Transit Gateway, VPN, Direct Connect, Client VPN, or appliance connectivity.
tags: ["soa-c03", "domain-5", "private-connectivity", "hybrid"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.3.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| S3/DynamoDB privately from VPC | gateway endpoint |
| Supported AWS API via endpoint ENIs | interface endpoint |
| Expose one provider service | PrivateLink endpoint service |
| Few non-overlapping VPC pairs | VPC peering |
| Many VPC and hybrid networks | Transit Gateway |
| Encrypted on-prem path over internet | Site-to-Site VPN |
| Dedicated private hybrid capacity | Direct Connect |
| Individual remote users | Client VPN |
| Transparent virtual appliances | Gateway Load Balancer endpoint |

# Rejection rules

- PrivateLink does not provide full VPC routing.
- Peering is non-transitive and cannot borrow a peer IGW/NAT/VPN.
- Endpoint policy restricts use; it does not grant IAM permission.
- Gateway endpoints have route associations but no endpoint ENI/SG.
- Interface endpoints use ENIs/SG/private DNS and local VPC routing.
- A connected VPN or BGP session does not prove data or return routes.
- Hybrid connectivity does not automatically provide hybrid DNS.

# Verification

From the real source, prove DNS, object state, forward and return routes, association/propagation, SG/NACL/firewall, endpoint/resource/IAM/KMS policy, target health, every AZ, and application result.

# Related pages

- [Private connectivity](../services/private-connectivity.md)
- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
