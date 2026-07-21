---
type: AWS Feature
title: VPC Reachability Analyzer
parent_services: [VPC]
description: Models supported AWS network configuration to identify a blocking or permitting path without sending packets.
tags: ["soa-c03", "domain-5", "reachability-analyzer", "diagnostics"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1", "5.3.1", "5.3.4", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

A path analysis evaluates supported configuration between a source and destination: routes, gateways, attachments, security groups, NACLs, and supported middleboxes.

# Decision boundaries

Use Reachability Analyzer to prove whether the AWS configuration model permits a path. It sends no packets and does not prove DNS, external networks, operating-system firewall, listener, TLS, authentication, or application health.

# Evidence and diagnosis

Select the exact source/destination resources and protocol/port, inspect the first blocking component or modeled path, then compare with actual Flow Logs, metrics, DNS, and application tests.

# Safe operations

Capture the analysis before change, make the smallest configuration correction, rerun the same path, and validate with a real request and return path.

# Related pages

- [Packet-path diagnostics](../concepts/packet-path-diagnostics.md)
- [Network path evidence selection](../decision-guides/network-path-evidence-selection.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
