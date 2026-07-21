---
type: Troubleshooting Playbook
title: Event-driven remediation failure
description: Traces a failed remediation from event emission through matching, authorization, execution, and recovery verification.
tags: [soa-c03, domain-1, troubleshooting, eventbridge, automation]
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

# Trigger

An alarm or AWS event should initiate an automated action, but no useful remediation occurs.

# Trace

1. Prove the source emitted the expected alarm state event or AWS event.
2. Confirm source account, Region, and event bus.
3. Test the rule against a captured event with the real nesting and values.
4. Confirm the rule is enabled.
5. Confirm target ARN, input path, and transformer output.
6. Confirm EventBridge target role or target resource policy.
7. Inspect retries, maximum event age, and DLQ.
8. Inspect Lambda, Step Functions, Automation, or target execution history.
9. For Automation, inspect document version, parameters, targets, `PassRole`, execution role, and failed step.
10. Verify the resource and workload reached desired state.

# Failure patterns

| Evidence | Direction |
| --- | --- |
| No rule match | Wrong bus/Region/account, disabled rule, pattern mismatch |
| Match but target denied | Target role, resource policy, KMS, cross-account trust |
| Wrong input | Input path or transformer field path |
| Runbook waits | Approval or resource wait condition |
| Action succeeds, issue remains | Wrong cause, target, parameter, or verification metric |
| Repeated action | Looping event or non-idempotent replay/retry |

# Safety before retry

- Confirm action is idempotent.
- Narrow the target.
- Bound concurrency and retries.
- Stop loop conditions.
- Preserve failed-event and execution evidence.

# Verification

Confirm the target execution and the original service-health signal. A successful invocation without recovery is still a failed remediation.

# Related concepts

- [EventBridge](../services/eventbridge.md)
- [Systems Manager Automation](../services/systems-manager-automation.md)
- [Safe automation](../concepts/safe-automation.md)

# Sources

- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)

