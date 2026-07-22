---
type: AWS Service
title: Lambda
service_id: lambda
description: Runs event-invoked code with immutable versions, aliases, concurrency controls, source-specific retries, and failure destinations.
tags: [soa-c03, domain-3, lambda, serverless, events]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["3.1.3", "3.1.5", "3.2.2", "1.1.1", "1.1.3", "1.1.5", "1.2.1", "1.2.2", "1.2.3", "1.3.1", "2.1.1", "2.3.2"]
domain_ids: ["3", "1", "2"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
status: verified
---

# Core model

```text
mutable $LATEST -> published immutable version -> alias -> optional weighted second version
source -> invoke permission -> function -> execution role -> dependency and desired result
```

# Deployment controls

Clients invoke a stable alias while routing shifts between published versions. Canary or linear rollout needs version-specific errors, duration, throttles, concurrency, logs, traces, and business evidence. Resetting alias weight restores compute routing but does not undo data changes.

# Invocation models

| Model | Failure boundary |
| --- | --- |
| synchronous | caller receives response and owns retry |
| asynchronous | Lambda queue, retry, event age, DLQ or destination |
| event source mapping | poller, batches, checkpoints, visibility, redrive |

Source permission to invoke the function is separate from the execution role used by function code.

# Failure evidence

Check package/image format, handler/runtime/architecture, role trust and permission, KMS and secrets, timeout, memory/CPU, reserved/account concurrency, VPC subnet IPs, routes/endpoints/DNS, source rule or mapping, retry and failure destination.

# Safety

Make side effects idempotent, bound concurrency and retries, protect downstream services, retain the previous version, and verify the desired resource or business state rather than invocation success alone.

# Related concepts

- [Event-driven automation](../concepts/event-driven-automation.md)
- [Deployment strategy selection](../decision-guides/deployment-strategy-selection.md)
- [Event-driven failure](../playbooks/event-driven-automation-failure.md)

# Corpus reconciliation: Domains 1 and 2

## Monitoring, concurrency, and remediation

Duration, errors, throttles, concurrency, retries, and dependency latency identify different limits. Reserved concurrency allocates and caps capacity; provisioned concurrency reduces cold-start latency. More concurrency can overload a downstream database.

Lambda fits small custom reactions and event targets. Multi-step governed infrastructure actions fit Systems Manager Automation or Step Functions better.

## Recovery dependency

Database restore may require environment, secret, endpoint, event-source, and IAM updates before functions use the new resource.

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
