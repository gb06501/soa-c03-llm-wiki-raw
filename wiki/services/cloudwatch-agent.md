---
type: AWS Feature
title: CloudWatch Agent
parent_services: [CloudWatch]
description: Collects guest, process, filesystem, log, and supported trace telemetry from compute environments.
tags: [soa-c03, domain-1, cloudwatch-agent, telemetry]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["1.1.1", "1.1.2", "1.3.1", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# When to use

Use the CloudWatch Agent when native service metrics do not expose the required guest or application evidence.

```text
host/container data -> agent -> CloudWatch Metrics or Logs
```

Typical collected data includes memory, filesystem, swap, processes, selected custom metrics, and configured log files.

# Deployment model

| Target | Form |
| --- | --- |
| EC2 or supported on-premises server | Installed agent process |
| ECS | Collector in the container environment |
| EKS | Observability add-on or collector deployment |
| Lambda | No agent installation required |

A fleet can store the configuration in Parameter Store and distribute or fetch it through Systems Manager.

# Configuration path

1. Install or deploy the collector.
2. Attach the correct instance, task, or pod role.
3. Define metrics and log sources.
4. Set Region, namespace, log groups, streams, and retention.
5. Start or reload the configuration.
6. Verify agent state and agent logs.
7. Verify new metrics and log events in CloudWatch.

# Failure model

| Symptom | First checks |
| --- | --- |
| Agent stopped | Package/deployment, process or container state, configuration load |
| Only metrics missing | Metric section, namespace, dimensions, IAM, Region |
| Only logs missing | File path, file permission, timestamp parsing, destination |
| All data missing | Role, network/DNS/endpoints, Region, agent state |
| Duplicate or expensive telemetry | Duplicate collectors, dimensions, collection interval |

Running the agent proves only that a process exists. Data arrival proves the collection path works.

# Exam traps

- EC2 native metrics do not include guest memory or free filesystem space.
- The CloudWatch Agent and ECS container agent perform different jobs.
- Correct IAM with the wrong Region still produces an empty view.
- More dimensions can increase custom-metric cost.

# Related concepts

- [CloudWatch telemetry](cloudwatch-telemetry.md)
- [Missing telemetry](../playbooks/missing-telemetry.md)
- [EC2 performance](ec2-performance.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)

