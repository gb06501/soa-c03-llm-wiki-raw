---
type: Troubleshooting Playbook
title: Network performance diagnosis
description: Diagnoses synthetic path, real flow, public internet, component, and application performance with preserved dimensions and safe remediation.
tags: ["soa-c03", "domain-5", "troubleshooting", "network-monitoring", "performance"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Trigger

Network alarms show latency, loss, availability, errors, port pressure, tunnel degradation, or user impact without a proven responsible layer.

# Evidence path

1. Confirm metric, namespace, dimension, statistic, period, threshold, missing-data behavior, and traffic volume.
2. Scope by user, probe, flow, AZ, Region, tunnel, attachment, target, geography, or ASN.
3. Choose Network Synthetic Monitor, Flow Monitor, Internet Monitor, canary, component metric, or log by question.
4. Compare RTT/loss/health indicator with traffic and baseline.
5. Find the last healthy component and first abnormal component.
6. Handoff to NAT/VPN/TGW/ELB/firewall/GA metrics and Flow/access/tunnel/Resolver/application logs.
7. Inspect route, capacity, target, policy, and recent configuration changes.
8. Reproduce from the actual source and preserve healthy redundant paths.

# Failure map

| Symptom | Direction |
| --- | --- |
| Configured hybrid probe degrades | Network Synthetic Monitor plus tunnel/path |
| Real TCP flows degrade | Network Flow Monitor contributors |
| One ISP/city affected | Internet Monitor event/ASN |
| Scripted journey fails | canary step plus app logs |
| NAT ErrorPortAllocation | translation-port pressure |
| One VPN tunnel down | degraded redundancy and tunnel/device logs |
| ELB 5xx | split LB-generated from target-generated |
| Zero errors and zero traffic | not health proof |
| Regional graph healthy | inspect AZ/target dimensions |

# Safe action

Keep redundant healthy paths active, change one route/capacity/target/configuration, run probe/canary/real traffic, and observe recovery over sufficient periods.

# Verification

Confirm sustained metric recovery with correct traffic volume, logs/configuration evidence, application SLO, redundancy health, and no hidden AZ/geography regression.

# Rollback

Restore the prior path/target/capacity configuration if user impact worsens and retain the diagnostic baseline.

# Escalation

Provide exact dimensions, time series, traffic volume, monitor and component evidence, logs, recent changes, user impact, and rollback state.

# Related pages

- [CloudWatch network monitoring](../services/cloudwatch-network-monitoring.md)
- [Network monitor selection](../decision-guides/network-monitor-selection.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
