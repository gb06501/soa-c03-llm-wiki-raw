---
type: Decision Guide
title: Network log selection
description: Chooses the log source that can prove DNS, edge, WAF, load-balancer, flow, firewall, proxy, container, or application behavior.
tags: ["soa-c03", "domain-5", "network-logs", "evidence"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---

# Decision table

| Question | Select |
| --- | --- |
| Was an ENI five-tuple accepted/rejected? | VPC Flow Logs |
| Did ALB select a target and what returned? | ELB access log |
| Did TLS fail before HTTP? | ELB connection/TLS evidence |
| Which web rule made the final action? | WAF log |
| Hit, miss, edge error, or origin result? | CloudFront log plus viewer headers |
| Which VPC Resolver query occurred? | Resolver query log |
| Which routed rule/signature acted? | Network Firewall flow/alert log |
| Did task/pod/proxy/application receive it? | ECS/EKS/proxy/application logs |
| Who changed configuration? | CloudTrail |
| Large retained S3 dataset query | Athena |
| Interactive CloudWatch log query | Logs Insights |

# Rejection rules

- Flow Logs have no payload.
- Sampled WAF requests are not a complete audit.
- CloudFront hit normally creates no origin log.
- CloudTrail is not a packet/request log.
- Log absence has several explanations.
- Container and network logs do not replace one another.

# Verification

Generate a known request, confirm expected records at each traversed layer with aligned UTC time and identifiers, prove final status/timing, and retain the minimum sensitive evidence needed.

# Related pages

- [Network logging](../concepts/network-logging.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Sources

- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
