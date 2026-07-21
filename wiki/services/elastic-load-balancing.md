---
type: AWS Service
title: Elastic Load Balancing
service_id: elastic-load-balancing
description: Terminates, passes through, or routes encrypted connections through managed load balancers.
tags: ["soa-c03", "domain-4", "elastic-load-balancing", "tls", domain-5, network-evidence]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["4.2.3", "5.1.3", "5.1.4", "5.2.3", "5.3.1", "5.3.2", "5.3.5"]
domain_ids: ["4", "5"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.1-troubleshoot-vpc-configurations.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---
# Core model

An Application Load Balancer commonly terminates HTTP/TLS and routes at Layer 7. A Network Load Balancer can terminate TLS or pass TCP through. Listener protocol, certificate, security policy, target protocol, and health checks are independent choices.

# Decision boundaries

Terminate when the load balancer must inspect and route application requests. Use pass-through when the target must own end-to-end TLS. Re-encryption creates a second independently validated TLS path.

# Evidence and diagnosis

Inspect DNS target, listener port/protocol, attached certificate and SANs, SNI selection, security policy, security groups, target group protocol/port, health, and backend certificate trust.

# Safe operations

Add and test the new certificate before removing the old one, preserve compatible policies for required clients, verify target health, and validate both handshake and application response.

# Related decisions

- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Domain 5: Balancing and request evidence

ALB provides Layer 7 host/path routing and integrates with Regional WAF. NLB provides Layer 4 TCP/UDP/TLS behavior. Gateway Load Balancer distributes transparent appliance traffic. Listener, rule, target group, health check, cross-zone behavior, security, and target application are separate layers.

Use access or connection logs to distinguish client/LB status from target status and processing time. Missing target status can mean the load balancer never received a response. Combine target health, component metrics, Flow Logs, and application logs.

Load-balancer hourly/capacity and cross-AZ paths are cost inputs, but consolidation must not create an unacceptable blast radius.

- [Content distribution selection](../decision-guides/content-distribution-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.1](../../raw/skills/5.3.1-troubleshoot-vpc-configurations.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
