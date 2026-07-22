---
type: AWS Service
title: Global Accelerator
service_id: global-accelerator
description: Routes TCP or UDP connections through static anycast IPs to healthy Regional endpoints without caching content.
tags: ["soa-c03", "domain-5", "global-accelerator", "edge"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["2.3.4", "5.1.4", "5.2.3", "5.3.5"]
domain_ids: ["2", "5"]
sources:
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---
# Core model

`client -> static anycast IP -> listener -> endpoint group -> healthy endpoint`

Global Accelerator proxies network connections over the AWS global network. It does not cache responses and does not select answers through DNS.

# Key objects

| Object | Purpose |
| --- | --- |
| Accelerator | Owns static anycast IPs and enablement |
| Listener | Accepts protocol and port ranges |
| Endpoint group | Represents one Region and traffic dial |
| Endpoint | ALB, NLB, EC2, or Elastic IP with weight and health |

# Decision boundaries

Use Global Accelerator for stable IPs, TCP/UDP acceleration, and rapid health-based Regional routing. Use CloudFront for HTTP edge caching and web policies. Use Route 53 when DNS policy selection is sufficient.

Traffic dial controls a Regional endpoint group; endpoint weight divides traffic inside that group.

# Evidence and diagnosis

Inspect accelerator state, listener protocol/ports, endpoint group Region/dial, endpoint weight and health reason, security path, load-balancer target health, flow metrics/logs, and CloudTrail changes.

# Safe operations

Add endpoints with a controlled dial, verify health and client protocols, shift traffic gradually, monitor flows and application outcomes, and retain the prior dial/weight for rollback.

# Related decisions

- [Content distribution selection](../decision-guides/content-distribution-selection.md)
- [Edge delivery failure](../playbooks/edge-delivery-failure.md)

# Disaster-recovery traffic boundary

Global Accelerator can move new traffic to healthy endpoints, but it does not copy data, provision recovery capacity, repair applications, or validate recovered dependencies.

# Sources

- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)

