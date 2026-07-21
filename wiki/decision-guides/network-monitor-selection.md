---
type: Decision Guide
title: Network monitor selection
description: Chooses synthetic probes, actual flow monitoring, public internet impact, scripted canaries, configuration analysis, logs, and component metrics.
tags: ["soa-c03", "domain-5", "network-monitoring", "cloudwatch"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Decision table

| Need | Select |
| --- | --- |
| Continuous configured AWS-to-on-prem path probes | Network Synthetic Monitor |
| Performance of actual supported TCP flows | Network Flow Monitor |
| Public internet user impact by geography/ASN | Internet Monitor |
| Scripted DNS/TLS/HTTP/application journey | CloudWatch Synthetics |
| Packet-free AWS configuration model | Reachability Analyzer |
| Observed five-tuple/action metadata | VPC Flow Logs |
| NAT capacity/port errors | NAT metrics |
| Tunnel redundancy and traffic | VPN metrics/logs |
| LB versus target errors | ELB metrics and logs |

# Rejection rules

- Synthetic probes do not require app traffic.
- Flow Monitor observes real flows and required coverage.
- Internet Monitor is not private VPN monitoring.
- Reachability Analyzer sends no packet.
- RTT increase alone does not prove AWS attribution.
- Healthy probe/network indicator does not prove DNS/TLS/application.
- Zero errors with zero traffic and missing data are not health.
- Regional aggregates can hide an AZ failure.

# Verification

Preserve exact dimensions, correlate monitor/metric with logs/configuration, reproduce from the relevant source, apply a narrow correction, and prove sustained network plus application-SLO recovery.

# Related pages

- [CloudWatch network monitoring](../services/cloudwatch-network-monitoring.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
