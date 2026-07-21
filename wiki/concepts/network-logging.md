---
type: Concept
title: Network logging
description: Correlates flow, load-balancer, WAF, edge, DNS, firewall, and workload logs to find the last layer that observed a request.
tags: ["soa-c03", "domain-5", "network-logging", "correlation"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---

# Request breadcrumb model

`client -> DNS -> edge/WAF -> load balancer -> ENI/flow -> proxy/container -> application/dependency`

A log proves that one layer observed something. A missing log can mean the traffic never arrived, logging or delivery failed, a cache served it earlier, or the path bypassed the layer.

# Log boundaries

| Log | Best question |
| --- | --- |
| VPC Flow Logs | Which ENI/five-tuple was accepted or rejected? |
| ELB access/connection logs | Did the listener select a target and what did each side return? |
| WAF logs | Which terminating rule/action decided the web request? |
| CloudFront logs | Was the response a hit, miss, edge error, or origin result? |
| Resolver logs | Which workload queried which name and what policy applied? |
| Network Firewall logs | Which flow/signature/action occurred? |
| Container/proxy logs | Did the workload, sidecar, or application observe and handle it? |

# Correlation method

Normalize UTC time, client and transformed IPs, ports, protocol, host/path, request/trace ID, resource, status, and processing time. Find last good and first bad. Use configuration and CloudTrail to explain the transition.

# Safety

Preserve evidence, protect sensitive fields, enable temporary verbosity narrowly, reproduce a known request, and confirm the fix across all required layers before reducing debug logging.

# Related pages

- [VPC Flow Logs](../services/vpc-flow-logs.md)
- [Network log selection](../decision-guides/network-log-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Sources

- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
