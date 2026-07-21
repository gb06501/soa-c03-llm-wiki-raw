---
type: AWS Service
title: Lambda
service_id: lambda
description: Runs event-invoked code with immutable versions, aliases, concurrency controls, source-specific retries, and failure destinations.
tags: [soa-c03, domain-3, lambda, serverless, events]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.3", "3.1.5", "3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
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

- [Event-driven automation](/concepts/event-driven-automation.md)
- [Deployment strategy selection](/decision-guides/deployment-strategy-selection.md)
- [Event-driven failure](/playbooks/event-driven-automation-failure.md)

# Sources

- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
