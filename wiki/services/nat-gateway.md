---
type: AWS Feature
title: NAT Gateway
parent_services: [VPC]
description: Provides managed IPv4 address translation for outbound private-subnet paths with explicit AZ, route, port, and cost behavior.
tags: ["soa-c03", "domain-5", "nat-gateway", "egress"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1", "5.1.4", "5.3.1", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

`private subnet default route -> NAT gateway in public subnet -> Elastic IP -> public-subnet route -> internet gateway`

Return traffic follows translation state. A NAT gateway does not accept unsolicited inbound internet connections and has no security group.

# Evidence and diagnosis

Check gateway state/AZ, private route association, more-specific routes, public subnet route, EIP, IGW, both subnet NACLs, source SG, port-allocation and connection metrics, bytes, and one-AZ comparison.

# Decision boundaries

One NAT per AZ improves failure isolation and avoids normal cross-AZ egress, but adds fixed cost. S3/DynamoDB gateway endpoints can remove supported traffic from NAT. Interface endpoints must be evaluated by service volume and per-AZ fixed cost.

# Safe operations

Keep the working AZ path, add same-AZ capacity or endpoint, test traffic and DNS, watch errors/bytes, then change routes and retire the old path.

# Related pages

- [Network cost optimization](../decision-guides/network-cost-optimization.md)
- [VPC connectivity failure](../playbooks/vpc-connectivity-failure.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
