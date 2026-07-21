---
type: Decision Guide
title: Remediation tool selection
description: Selects the smallest AWS mechanism that matches capacity, routing, workflow, notification, or infrastructure-remediation needs.
tags: [soa-c03, domain-1, remediation, selection]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.3", "1.1.5", "1.2.1", "1.2.2", "1.2.3", "1.3.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
status: verified
---

# Selection table

| Requirement | Choose | Reject when |
| --- | --- | --- |
| Add or remove capacity | Auto Scaling | Root cause is downstream, storage, or lock pressure |
| Small stateless custom action | Lambda | Workflow needs governed steps, approvals, or long-lived state |
| Governed infrastructure workflow | Systems Manager Automation | Need is only one command on managed nodes |
| One command across managed nodes | Run Command | Workflow needs multi-step AWS-resource logic |
| Route by event content | EventBridge | Need is durable worker buffering |
| Broadcast one message | SNS | Need is content-based orchestration or queueing |
| Buffer work for a consumer | SQS | Need is fan-out notification only |
| Multi-step stateful application workflow | Step Functions | Need is a simple infrastructure runbook |
| Notify operators | SNS | Notification itself must remediate the resource |

# Combined automation chain

```text
CloudWatch alarm or AWS event
-> EventBridge
-> Lambda, Automation, Auto Scaling, or Step Functions
-> metric/resource-state verification
-> SNS
```

# Governing questions

1. Is the cause proven?
2. Is the action stateless or stateful?
3. Does it operate on application logic, managed nodes, or AWS resources?
4. Does it need approval, versioning, or step-level evidence?
5. Can it repeat safely?
6. How is recovery verified?

# Exam traps

- EventBridge routes; it does not become the worker queue.
- SNS fans out; it does not preserve workflow state.
- Run Command is not the same as Systems Manager Automation.
- More capacity can amplify a database bottleneck.

# Related concepts

- [Safe automation](../concepts/safe-automation.md)
- [EventBridge](../services/eventbridge.md)
- [Systems Manager Automation](../services/systems-manager-automation.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)

