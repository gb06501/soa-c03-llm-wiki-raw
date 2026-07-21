---
type: Concept
title: Packet-path diagnostics
description: Models one exact flow through forward and return routes, stateful and stateless controls, transformations, middleboxes, and application state.
tags: ["soa-c03", "domain-5", "packet-path", "diagnostics"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
status: verified
---

# Core model

Record an exact flow:

`source IP:port -> destination IP:port + protocol + time`

Then trace:

`source ENI -> source route -> target/attachment -> destination route -> NACL -> SG -> listener -> return path`

# Invariants

- Longest-prefix route wins in each direction.
- A forward route without return route is incomplete.
- Security groups are stateful and allow-only.
- NACLs are stateless, ordered, and require return/ephemeral rules.
- NAT, load balancers, and proxies can change the address seen by later controls.
- Stateful appliances require compatible symmetric paths.
- IPv4 and IPv6 routes/rules are separate.
- An active route or ACCEPT log does not prove application health.

# Evidence ladder

Use route tables and associations, target/attachment state, SG/NACL rules, Reachability Analyzer, Flow Logs, component metrics, CloudTrail/Config changes, socket/TLS tests, and application logs.

# Safe remediation

Change the first proven blocking or misdirecting object, not every layer. Retest the same five-tuple in both directions and verify application recovery.

# Related pages

- [VPC](../services/vpc.md)
- [Network path evidence selection](../decision-guides/network-path-evidence-selection.md)
- [VPC connectivity failure](../playbooks/vpc-connectivity-failure.md)

# Sources

- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
