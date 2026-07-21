---
type: AWS Service
title: EventBridge
description: Matches events on a bus and routes transformed payloads to authorized targets.
tags: [soa-c03, domain-1, eventbridge, automation]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.1.3", "1.1.5", "1.2.1", "1.2.2", "1.2.3"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
status: verified
---

# Core model

```text
source -> event bus -> rule pattern -> optional transform -> target
```

No pattern match means no target attempt. A pattern match does not prove target success.

# Bus and event identity

| Bus | Main source |
| --- | --- |
| Default | AWS services and account applications |
| Custom | Custom application events |
| Partner | Supported SaaS partners |

Important event fields include `source`, `detail-type`, `detail`, `resources`, `account`, `region`, `time`, and `id`. Match the actual nested event shape, not an assumed shape.

# Rule controls

- Event pattern or schedule.
- Enabled/disabled state.
- Target ARN and required role or resource policy.
- Input path and input transformer.
- Retry policy and maximum event age.
- DLQ for failed target delivery.
- Archive and replay for retained bus events.

An input transformer selects and reshapes existing event fields. Use Lambda or Step Functions when external lookup or complex logic is required.

# Cross-account path

```text
source rule -> destination bus -> destination bus policy -> destination rule -> target
```

# Failure evidence

```text
source emitted -> account/Region/bus -> rule enabled -> actual pattern match
-> target authorization -> retry/DLQ -> target logs or history
```

# Exam traps

- EventBridge is not a durable worker queue.
- A DLQ contains failed target deliveries, not unmatched events.
- Correct values at the wrong nesting level do not match.
- Archive replay can repeat actions; targets need idempotency.
- A remediation-generated event can retrigger the remediation.

# Related concepts

- [Safe automation](../concepts/safe-automation.md)
- [Systems Manager Automation](systems-manager-automation.md)
- [Event-driven remediation failure](../playbooks/event-driven-remediation-failure.md)
- [Remediation tool selection](../decision-guides/remediation-tool-selection.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)

