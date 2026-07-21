---
type: Troubleshooting Playbook
title: VPC connectivity failure
description: Diagnoses exact VPC flows across routes, gateways, SGs, NACLs, NAT, endpoints, attachments, IP capacity, and applications.
tags: ["soa-c03", "domain-5", "troubleshooting", "vpc", "packet-path"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.1", "5.3.1"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.1-configure-a-vpc.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
status: verified
---

# Trigger

A VPC workload cannot reach or be reached by the intended address, service, network, or application.

# Evidence path

1. Record source/destination addresses, ports, protocol, account, Region, AZ, and time.
2. Resolve DNS and identify the actual address family and transformed source.
3. Inspect source subnet association and longest-prefix forward route.
4. Verify target/gateway/endpoint/attachment state.
5. Trace every intermediate and destination route plus exact return path.
6. Evaluate destination/source SGs and both-direction ordered NACL rules.
7. Check NAT public-subnet path, EIP, IGW, port metrics, or IPv6 gateway.
8. Inspect Flow Logs and Reachability Analyzer without overclaiming.
9. Check subnet available addresses and managed ENIs.
10. Test OS firewall, listener, TLS, and application.

# Failure map

| Symptom | Direction |
| --- | --- |
| Route blackhole | deleted/unavailable target or attachment |
| One subnet/AZ fails | different association, NAT/endpoint, NACL, or IP capacity |
| Flow REJECT | captured SG/NACL candidate |
| Flow ACCEPT, no app log | return path, OS/listener/proxy/application |
| Private egress fails | private NAT route plus NAT public route/EIP/IGW |
| New resources fail only | subnet IP exhaustion |
| Large transfers fail | MTU/MSS/asymmetric state |
| Endpoint AccessDenied | endpoint/IAM/resource/KMS policy |

# Safe action

Change the first proven blocking or wrong-path object. Add new rules/routes before removing old access, test one AZ and both directions, then expand.

# Verification

Repeat the identical five-tuple, observe expected Flow/application logs, confirm route and return path, and verify user/workload outcome in every required AZ/address family.

# Rollback

Restore prior route, association, SG/NACL, endpoint, or gateway configuration and return traffic to the last known-good path.

# Escalation

Provide exact flow, DNS answer, route chains, security rules, target state, Flow/analysis evidence, application evidence, and recent changes.

# Related pages

- [Packet-path diagnostics](../concepts/packet-path-diagnostics.md)
- [Network path evidence selection](../decision-guides/network-path-evidence-selection.md)

# Sources

- [Skill 5.1.1](../../raw/skills/5.1.1-configure-a-vpc.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
