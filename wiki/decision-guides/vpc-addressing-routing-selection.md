---
type: Decision Guide
title: VPC addressing and routing selection
description: Selects CIDR, subnet intent, IPv4/IPv6 gateway, route, security boundary, and availability pattern.
tags: ["soa-c03", "domain-5", "vpc", "routing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Govern non-overlapping address pools | VPC IPAM |
| Add VPC address space | supported secondary VPC CIDR and new subnets |
| Public IPv4 workload/LB path | IGW route plus public IPv4/EIP and security |
| Private IPv4 internet egress | public NAT gateway path |
| Public IPv6 inbound/outbound | `::/0` to internet gateway |
| IPv6 outbound initiation only | egress-only internet gateway |
| Resource-level stateful allow | security group |
| Subnet-level ordered allow/deny | NACL |
| Stable resource relationship | SG reference instead of changing CIDR |
| Multi-AZ private egress | same-AZ NAT per workload AZ when requirements justify cost |

# Rejection rules

- A subnet is public because of its route, not its name.
- A public address without IGW route is insufficient.
- NAT does not make a private subnet public or accept unsolicited inbound.
- Security groups cannot attach to NAT Gateway.
- IPv4 rules do not cover IPv6.
- Adding a VPC CIDR does not resize an existing subnet.
- An active route does not prove application health.

# Verification

Check exact subnet associations, longest-prefix forward and return routes, target state, addresses, SG/NACL behavior, Flow Logs, DNS, and application response in every required AZ.

# Related pages

- [VPC networking](../services/vpc-networking.md)
- [VPC connectivity failure](../playbooks/vpc-connectivity-failure.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
