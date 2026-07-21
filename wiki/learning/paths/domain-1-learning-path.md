---
type: Learning Path
title: Domain 1 learning path
description: Orders Domain 1 study from signal selection through safe remediation and resource optimization.
tags: [soa-c03, domain-1, learning-path]
timestamp: 2026-07-21T00:00:00+02:00
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

# Stage 1: Ask the right observability question

Read:

1. [Observability signal selection](../../concepts/observability-signal-selection.md)
2. [CloudWatch telemetry](../../services/cloudwatch-telemetry.md)
3. [CloudWatch Agent](../../services/cloudwatch-agent.md)
4. [Missing telemetry](../../playbooks/missing-telemetry.md)

Ready when you can choose metrics, logs, CloudTrail, traces, Health, or deployment evidence and prove the collection path.

# Stage 2: Convert signals into useful operations

Read:

1. [CloudWatch alarms](../../services/cloudwatch-alarms.md)
2. [CloudWatch dashboards](../../services/cloudwatch-dashboards.md)
3. [SNS notifications](../../services/sns-notifications.md)
4. [Alarm and notification failure](../../playbooks/alarm-and-notification-failure.md)

Ready when you can configure `M` of `N`, missing-data behavior, a safe dashboard scope, and a verified notification path.

# Stage 3: Diagnose before acting

Read:

1. [Evidence-to-remediation loop](../../concepts/evidence-to-remediation-loop.md)
2. [Remediation tool selection](../../decision-guides/remediation-tool-selection.md)
3. [Safe automation](../../concepts/safe-automation.md)

Ready when you reject an attractive action that does not match the proven cause.

# Stage 4: Build event-driven remediation

Read:

1. [EventBridge](../../services/eventbridge.md)
2. [Systems Manager Automation](../../services/systems-manager-automation.md)
3. [Event-driven remediation failure](../../playbooks/event-driven-remediation-failure.md)

Ready when you can trace source, bus, match, target authorization, execution, retry/DLQ, and desired-state verification.

# Stage 5: Optimize the limiting layer

Read:

1. [Resource performance diagnosis](../../playbooks/resource-performance-diagnosis.md)
2. [EC2 performance](../../services/ec2-performance.md)
3. [EBS performance](../../services/ebs-performance.md)
4. [RDS performance](../../services/rds-performance.md)
5. [S3 performance](../../services/s3-performance.md)
6. [Shared storage](../../services/shared-storage.md)
7. [Storage service selection](../../decision-guides/storage-service-selection.md)

Ready when you can identify compute, memory, storage, network, concurrency, database, or dependency pressure and select the smallest targeted change.

# Stage 6: Challenge misconceptions

Read [Domain 1 exam traps](../../exam-traps/domain-1-exam-traps.md), then explain why every tempting conclusion fails.

# Suggested practice

- Diagnose a missing EC2 memory metric.
- Explain an `ALARM` state with no email.
- Trace a rule that matches but cannot invoke a runbook.
- Separate an EBS volume ceiling from an EC2 EBS ceiling.
- Explain low EC2 CPU with high application latency.
- Select EFS, FSx, S3 Files, S3, or Storage Gateway from protocol clues.
- Separate RDS connection, I/O, CPU, lock, and query bottlenecks.

# Sources

- [Domain 1 Task 1.1 source](../../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Domain 1 Task 1.2 source](../../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Domain 1 Task 1.3 source](../../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
