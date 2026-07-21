---
type: AWS Feature
title: VPC Flow Logs
parent_services: [VPC]
description: Records observed IP flow metadata at VPC, subnet, or ENI scope for path, security, and cost analysis.
tags: ["soa-c03", "domain-5", "flow-logs", "network-evidence"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1", "5.1.4", "5.3.1", "5.3.2", "5.3.4", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

Flow Logs record metadata such as interface, source/destination addresses and ports, protocol, packets, bytes, time, action, and log status. They do not capture payloads.

# Interpretation

| Value | Meaning |
| --- | --- |
| ACCEPT | Captured network controls accepted the flow |
| REJECT | A captured security control rejected it |
| NODATA | No eligible traffic in the interval |
| SKIPDATA | Incomplete evidence for the interval |

ACCEPT does not prove return traffic or application success. REJECT does not identify the exact SG or NACL rule.

# Evidence and diagnosis

Normalize UTC time, exact ENI, five-tuple, flow direction, packet addresses, TCP flags, packets/bytes, action, and log status. Absence can mean scope/filter/delivery error, caching, bypass, or no traffic.

# Safe operations

Enable the narrow scope and fields needed, generate a known test flow, verify delivery and retention, protect sensitive network metadata, and remove only temporary verbosity.

# Related pages

- [Network logging](../concepts/network-logging.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.4](../../raw/skills/5.3.4-identify-and-troubleshoot-hybrid-and-private-connectivity-issues.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
