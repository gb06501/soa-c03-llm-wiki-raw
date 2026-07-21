---
type: Concept
title: VPC networking
description: Connects addressing, subnets, routing, IPv4/IPv6 gateways, security controls, evidence, availability, and cost.
tags: ["soa-c03", "domain-5", "vpc", "routing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
status: verified
---

# Core model

A VPC is Regional; a subnet belongs to one Availability Zone. CIDRs define address capacity, route tables choose next hops, security groups filter ENIs statefully, and NACLs filter subnet boundaries statelessly.

# Subnet intent

| Intent | Route clue |
| --- | --- |
| Public IPv4 | default route to internet gateway plus public address on resource/LB |
| Private IPv4 egress | default route to NAT gateway |
| Isolated | no public/NAT default path |
| Public IPv6 | `::/0` to internet gateway |
| Egress-only IPv6 | `::/0` to egress-only internet gateway |

# Design boundaries

Size for managed ENIs, deployment surge, load balancers, endpoints, appliances, and failure replacement. Use multiple subnets/AZs for HA. Use same-AZ NAT paths when resilience and traffic justify the cost.

# Evidence

Inspect exact subnet associations, longest-prefix routes, target state, ENIs and addresses, SG/NACL rules, NAT metrics, Flow Logs, Reachability Analyzer, DNS, application listener, and IP availability.

# Related pages

- [VPC](vpc.md)
- [VPC addressing and routing selection](../decision-guides/vpc-addressing-routing-selection.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
