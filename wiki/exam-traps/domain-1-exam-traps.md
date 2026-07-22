---
type: Exam Trap
title: Domain 1 exam traps
description: Corrects recurring monitoring, automation, compute, storage, and database misconceptions.
tags: [soa-c03, domain-1, exam-traps]
timestamp: 2026-07-22T05:15:00Z
skill_ids: ["1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.1.5", "1.2.1", "1.2.2", "1.2.3", "1.3.1", "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Telemetry

| Tempting conclusion | Correct mental model |
| --- | --- |
| CloudTrail is application logging | CloudTrail records API activity; application errors belong in workload logs |
| EC2 exposes guest memory and free disk by default | Guest memory/filesystem needs agent or custom collection |
| Empty dashboard means zero activity | First verify scope, dimensions, time range, and collection |
| Managed Prometheus is the visualization layer | It stores/queries Prometheus metrics; Grafana visualizes |

# Alarms and notifications

| Tempting conclusion | Correct mental model |
| --- | --- |
| Dashboard evaluates alarms | Alarm service evaluates; dashboard displays |
| Metric filter alerts by itself | It creates a metric that an alarm can evaluate |
| `INSUFFICIENT_DATA` means outage | It means insufficient usable data under current settings |
| `ALARM` proves email delivery | Alarm evaluation and SNS delivery are separate |
| Email subscription exists, so it works | Confirmation may still be pending |

# Events and automation

| Tempting conclusion | Correct mental model |
| --- | --- |
| EventBridge is a worker queue | It matches and routes events; SQS buffers consumer work |
| DLQ stores unmatched events | It stores failed target deliveries |
| Input transformer performs lookup | It selects and reshapes event fields |
| Runbook definition proves execution | Inspect a specific execution and step evidence |
| Caller access covers the execution role | Start permission, `PassRole`, and role action permission are separate |
| Successful execution proves recovery | Verify target resource and workload health |

# Compute and storage

| Tempting conclusion | Correct mental model |
| --- | --- |
| Low average CPU proves overprovisioning | Peaks, memory, network, storage, and dependencies still matter |
| More instances fix latency | They can worsen a limited database or dependency |
| Savings Plans optimize performance | They change eligible price, not resource configuration |
| Bigger `gp3` is faster automatically | Configure IOPS and throughput independently |
| EBS tuning overrides instance limits | Actual performance is bounded by both volume and EC2 capability |
| More EBS capacity grows the filesystem | Partition/filesystem growth is separate |
| Instance store is durable | It is lost on stop, termination, or host loss |

# S3 and shared storage

| Tempting conclusion | Correct mental model |
| --- | --- |
| Lifecycle speeds upload | It transitions or expires stored objects |
| Transfer Acceleration is caching | It optimizes the client-to-S3 path; CloudFront caches |
| DataSync caches application reads | It performs managed data movement |
| Cheapest class is always cheapest | Retrieval and minimum-duration behavior matter |
| S3 is a mounted POSIX filesystem | S3 is object storage; use the correct file service or S3 Files |
| EFS is Windows SMB | EFS is NFS-focused; FSx Windows supplies SMB/AD integration |

# RDS

| Tempting conclusion | Correct mental model |
| --- | --- |
| High DB latency requires high CPU | I/O, locks, connections, SQL, or network can dominate |
| Multi-AZ scales reads | Multi-AZ primarily improves availability |
| RDS Proxy is a read replica or cache | It pools and reuses connections |
| Bigger DB class fixes locks | Lock contention needs transaction/query remediation |
| Storage autoscaling can shrink later | It grows storage; it does not automatically reduce it |

# Related concepts

- [Domain 1 learning path](../learning/paths/domain-1-learning-path.md)
- [Evidence-to-remediation loop](../concepts/evidence-to-remediation-loop.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)

# Sources

- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.4](../../raw/skills/1.1.4-create-and-manage-cloudwatch-dashboards.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
