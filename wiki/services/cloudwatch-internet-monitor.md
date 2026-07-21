---
type: AWS Feature
title: CloudWatch Internet Monitor
parent_services: [CloudWatch]
description: Measures public internet availability and performance impact by geography, ASN, traffic footprint, and monitored resource.
tags: ["soa-c03", "domain-5", "cloudwatch", "internet-monitor"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

Internet Monitor maps observed public-internet traffic to availability/performance measurements and health events by location and network provider.

# Evidence and diagnosis

Inspect affected geography, ASN, traffic percentage, monitored resource/Region, availability and performance score, health-event timing, suggested optimization, and correlated CloudFront/Global Accelerator/ELB/application logs.

# Decision boundaries

Use Internet Monitor for user-impact patterns on public internet paths. It does not diagnose private VPN health, and one ISP/city event does not prove a universal origin outage.

# Safe operations

Baseline normal traffic footprint, alarm on meaningful affected percentage, retain healthy Regions/paths, shift through Route 53, CloudFront, or Global Accelerator only with application evidence, and verify user SLO recovery.

# Related pages

- [Network monitor selection](../decision-guides/network-monitor-selection.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
