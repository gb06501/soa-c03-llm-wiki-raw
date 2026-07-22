---
type: AWS Service
title: DevOps Agent
service_id: devops-agent
description: Investigates correlated operational evidence and performs or recommends authorized, governed remediation.
tags: [soa-c03, domain-3, devops-agent, operations, automation]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["3.2.2", "1.2.1"]
domain_ids: ["3", "1"]
sources:
  - /raw/skills/3.2.2-implement-event-driven-automation.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
status: verified
---

# Core model

```text
telemetry and events -> investigation and correlation -> likely cause
                     -> recommendation or authorized action -> verification
```

# Selection

Use DevOps Agent when a scenario requires investigation across several operational signals and guided remediation. Use deterministic EventBridge rules, Lambda, Step Functions, or Systems Manager Automation when the trigger and workflow are already explicit.

# Controls

Verify connected evidence sources, resource/account/Region scope, IAM role, least-privilege actions, approval and guardrail requirements, and the permitted remediation boundary.

# Evidence and safety

Review the investigation evidence and recommendation before impactful action. Agent reasoning does not replace resource permission, deterministic alarms, rollback planning, operator accountability, or verification of the actual desired state.

# Failure boundaries

Missing evidence or scope prevents useful investigation. A valid recommendation can still fail because of IAM, SCP, resource, KMS, Region, or approval controls. Apparent execution success still requires resource and business verification.

# Related concepts

- [Event-driven automation](../concepts/event-driven-automation.md)
- [Event-driven selection](../decision-guides/event-driven-automation-selection.md)

# Assisted operations boundary

DevOps Agent can assist operational investigation and remediation, but source evidence, permissions, action scope, approval, and verification still govern safe changes. An assistant recommendation is not proof of root cause or recovery.

# Sources

- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)

