---
type: Concept
title: CloudWatch network monitoring
description: Selects synthetic path probes, actual flow performance, public internet impact, scripted canaries, component metrics, logs, and application evidence.
tags: ["soa-c03", "domain-5", "cloudwatch", "network-monitoring"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Monitor boundary

| Question | Select |
| --- | --- |
| Can a configured AWS-to-on-prem path work? | Network Synthetic Monitor |
| How are actual supported TCP flows behaving? | Network Flow Monitor |
| Which geography/ASN has public internet impact? | Internet Monitor |
| Can a DNS/TLS/HTTP/application journey succeed? | Synthetics canary |
| Does configuration permit the path? | Reachability Analyzer |
| What five-tuple was observed? | VPC Flow Logs |

# Evidence hierarchy

A monitor or metric detects and scopes a symptom. Logs show observed traffic or errors. Configuration explains route and policy. Application evidence proves the user result.

# Alarm design

Preserve dimensions such as AZ, tunnel, attachment, target, geography, ASN, probe, and flow. Alert on user impact, capacity error, and redundancy loss. Missing data or zero errors with zero traffic is not health.

# Related pages

- [CloudWatch](cloudwatch-telemetry.md)
- [Network monitor selection](../decision-guides/network-monitor-selection.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
