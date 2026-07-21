---
type: AWS Feature
title: VPC IPAM
parent_services: [VPC]
description: Plans, allocates, tracks, and audits non-overlapping address pools and utilization across network scopes.
tags: ["soa-c03", "domain-5", "ipam", "addressing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
status: verified
---

# Core model

IPAM manages address intent and evidence: scopes contain pools, pools allocate CIDRs, and allocations map to VPCs or other resources. It does not route packets.

# Decision boundaries

Use IPAM to standardize address plans, prevent overlap, delegate allocations, monitor utilization, and find unused or noncompliant space. Adding a secondary VPC CIDR does not resize an existing subnet.

# Evidence and diagnosis

Inspect scope and pool hierarchy, locale/Region, allocation rule, requested netmask, existing overlap, compliance status, resource discovery, and subnet available-address evidence.

# Safe operations

Reserve growth and deployment surge, allocate through governed pools, test cross-account/Region discovery, and migrate workloads into newly sized subnets rather than attempting in-place subnet growth.

# Related pages

- [VPC addressing and routing selection](../decision-guides/vpc-addressing-routing-selection.md)
- [VPC connectivity failure](../playbooks/vpc-connectivity-failure.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
