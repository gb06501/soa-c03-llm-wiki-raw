---
type: Troubleshooting Playbook
title: Event-driven automation failure
description: Traces missing, duplicated, delayed, denied, throttled, or recursive automation from source to verified state.
tags: [soa-c03, domain-3, eventbridge, lambda, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Trigger

An expected automation does not run, repeats side effects, builds backlog, reaches a DLQ, or creates an invocation loop.

# Evidence path

1. Confirm the source emitted the expected real event shape.
2. Test event type, prefix/suffix, pattern fields, case, and enabled rule.
3. Inspect target ARN, resource policy or target role, source conditions, and KMS.
4. Confirm target invocation or event-source mapping and inspect input transformation.
5. Trace Lambda/workflow logs, execution role, timeout, concurrency, network, and downstream errors.
6. Inspect retries, maximum event age, queue visibility/redrive, DLQ policy/messages, and archive replay.
7. Check idempotency state, current-resource guard, event ordering, and recursive trigger path.

# Failure map

| Symptom | Direction |
| --- | --- |
| No match | producer configuration or filter/pattern |
| Match but no target | target ARN, role/resource policy, KMS |
| Target starts but no change | execution role, parameters, current state, dependency |
| SQS backlog grows | mapping, concurrency, visibility, poison message, downstream |
| Duplicate effect | at-least-once delivery and missing atomic idempotency |
| Old event overwrites new state | ordering/version guard absent |
| DLQ grows | persistent permission, input, throttle, or code failure |
| Invocation storm | recursive write/action, broad rule, uncontrolled retry |

# Safe action

Disable or narrow a damaging loop, preserve failed events, bound retries and concurrency, add an atomic idempotency/current-state guard, repair the exact permission or input, then replay only a controlled scope.

# Verification

Confirm source-to-target metrics, successful target evidence, intended resource/business state, stable backlog and concurrency, empty or deliberately retained DLQ, no recursion, and safe duplicate handling.

# Related concepts

- [Event-driven automation](/concepts/event-driven-automation.md)
- [Selection guide](/decision-guides/event-driven-automation-selection.md)

# Sources

- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
