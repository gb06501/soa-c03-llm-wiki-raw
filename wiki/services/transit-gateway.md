---
type: AWS Service
title: Transit Gateway
service_id: transit-gateway
description: Connects many VPC and hybrid attachments through associated and propagated routing domains.
tags: ["soa-c03", "domain-5", "transit-gateway", "routing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.2", "5.1.4", "5.3.1", "5.3.4", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---
# Core model

`VPC route -> attachment -> ingress-associated TGW route table -> destination route -> attachment -> destination VPC route`

Association selects the route table used when traffic enters through an attachment. Propagation installs attachment destinations into selected tables. They are different operations.

# Key objects

| Object | Purpose |
| --- | --- |
| Attachment | Connects a VPC, VPN, or supported gateway |
| VPC attachment subnet | Provides TGW data-plane presence in selected AZs |
| TGW route table | Selects egress attachment by destination |
| Association | Chooses ingress lookup table |
| Propagation | Adds attachment prefixes to a table |
| Blackhole route | Explicitly discards a destination |

# Decision boundaries

Use Transit Gateway for many-network routing and segmentation. Use peering for a small number of direct non-transitive pairs. Use PrivateLink when consumers need one service rather than routed adjacency.

# Evidence and diagnosis

Prove both VPC route tables, attachment state/subnets, ingress association, propagation or static route, reverse TGW table, reverse VPC route, security controls, appliance mode, and AZ symmetry.

# Safe operations

Capture all tables, add one narrow route or propagation, test both directions and AZs, preserve segmentation, inspect Flow Logs/metrics, then remove bypass routes.

# Related decisions

- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [Hybrid and private connectivity failure](../playbooks/hybrid-private-connectivity-failure.md)

# Sources

- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
