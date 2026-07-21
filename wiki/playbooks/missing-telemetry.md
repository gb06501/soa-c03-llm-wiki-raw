---
type: Troubleshooting Playbook
title: Missing telemetry
description: Traces absent metrics or logs from source configuration through collection, authorization, transport, and destination identity.
tags: [soa-c03, domain-1, troubleshooting, telemetry]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.1", "1.1.2", "1.1.4", "1.2.1", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Trigger

An expected metric, log stream, container view, or dashboard widget is empty.

# Steps

1. Confirm the signal should exist. EC2 guest memory and filesystem require collection beyond native metrics.
2. Confirm account, Region, time range, namespace, metric name, dimensions, log group, and log stream.
3. Confirm the workload integration, agent, add-on, or collector is installed and running.
4. Confirm the active configuration includes the required metric or file path.
5. Read the collector's own log for parse, permission, identity, or transport errors.
6. Confirm instance/task/pod role permissions.
7. Confirm DNS, network path, endpoints, and destination Region.
8. Confirm recent datapoints or log events at the destination.
9. Confirm the dashboard/query uses the same identity and scope.

# Symptom map

| Symptom | Likely layer |
| --- | --- |
| Native EC2 metrics exist, memory missing | Agent/configuration required |
| Metrics and logs both missing | Role, network, Region, or stopped collector |
| Metrics exist, one log absent | File path/read access/timestamp parsing |
| Destination contains data, widget empty | Account, Region, dimensions, query, or time range |
| Wrong node identity | Reused dimensions or host identity |
| Container telemetry missing | Add-on/collector, service account/task role, deployment state |

# Verification

Generate or wait for a new signal. Confirm both source-side collection and a new destination datapoint/event with the correct dimensions and timestamp.

# Related concepts

- [CloudWatch Agent](../services/cloudwatch-agent.md)
- [CloudWatch telemetry](../services/cloudwatch-telemetry.md)
- [Observability signal selection](../concepts/observability-signal-selection.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)

