---
type: AWS Feature
title: CloudWatch Network Synthetic Monitor
parent_services: [CloudWatch]
description: Continuously probes configured AWS-to-on-premises network paths for round-trip time, packet loss, and network health.
tags: ["soa-c03", "domain-5", "cloudwatch", "synthetic-monitor"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

`monitor -> configured probes -> destination/protocol -> RTT, packet loss, network health indicator`

Synthetic probes do not require real application traffic.

# Evidence and diagnosis

Inspect probe source and destination, protocol/port, state, RTT and loss by dimension, traffic-independent baseline, network health indicator, route/tunnel component metrics, and actual application checks.

# Decision boundaries

Use Network Synthetic Monitor for configured hybrid path health even when applications are idle. Use Network Flow Monitor for real supported TCP flows and Internet Monitor for public internet user impact.

# Safe operations

Keep redundant paths active, baseline probes before change, alert on sustained degradation and redundancy loss, repair the narrow path, and verify with both probes and real requests.

# Related pages

- [Network monitor selection](../decision-guides/network-monitor-selection.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
