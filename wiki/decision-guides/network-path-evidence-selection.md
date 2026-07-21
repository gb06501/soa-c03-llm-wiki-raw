---
type: Decision Guide
title: Network path evidence selection
description: Selects decisive routing, security, flow, configuration-model, component, and application evidence for a failed path.
tags: ["soa-c03", "domain-5", "packet-path", "evidence"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
status: verified
---

# Decision table

| Symptom | First evidence |
| --- | --- |
| Timeout to exact IP/port | forward/return longest-prefix routes, SG/NACL, Flow Logs |
| Route believed blocked | route associations and Reachability Analyzer |
| Flow REJECT | exact ENI, direction, SG/NACL candidates |
| Flow ACCEPT, no application log | OS firewall, listener, proxy, application |
| One AZ fails | subnet/route/NAT/endpoint/attachment/IP capacity by AZ |
| Private host lacks internet | private NAT route, NAT state, public NAT-subnet route, IGW |
| Endpoint AccessDenied | endpoint/IAM/resource/KMS policies |
| New resources cannot launch | subnet available addresses and ENI owners |
| Large transfers fail | MTU/MSS and stateful/asymmetric path |
| Worked before a change | CloudTrail/Config plus path diff |

# Rejection rules

- Reachability Analyzer sends no packets.
- ACCEPT does not prove response.
- REJECT does not identify the exact rule.
- Active route does not prove listener health.
- Forward route alone is incomplete.
- Aggregate metrics can hide an AZ-specific failure.

# Verification

Repeat the same five-tuple from the real source, prove the reverse path, observe expected logs, and confirm the application outcome rather than only the network model.

# Related pages

- [Packet-path diagnostics](../concepts/packet-path-diagnostics.md)
- [VPC connectivity failure](../playbooks/vpc-connectivity-failure.md)

# Sources

- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
