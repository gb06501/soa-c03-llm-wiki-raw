---
type: AWS Service
title: Control Tower
service_id: control-tower
description: Operates a governed multi-account landing zone with controls, account vending, and drift visibility.
tags: ["soa-c03", "domain-4", "control-tower", "landing-zone"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.3", "4.1.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
status: verified
---
# Core model

Control Tower establishes and governs a landing zone using Organizations, IAM Identity Center, centralized logging, account baselines, and controls. Account Factory standardizes account provisioning.

# Control behavior

| Control class | Effect |
| --- | --- |
| Preventive | Blocks disallowed actions through policy guardrails |
| Detective | Evaluates deployed state and reports noncompliance |
| Proactive | Evaluates supported resources before provisioning |

Control status is not the same as remediation. Drift means managed resources or configurations no longer match the expected landing-zone baseline.

# Evidence and diagnosis

Inspect control applicability, OU registration, account enrollment, landing-zone version, drift state, Config recorder/rule health, and the underlying SCP or CloudFormation evidence.

# Safe operations

Update the landing zone through supported workflows, test new controls on a limited OU, preserve logging accounts, and remediate drift before assuming governance is effective.

# Related decisions

- [Multi-account security governance](../concepts/multi-account-security-governance.md)
- [Compliance monitoring selection](../decision-guides/compliance-monitoring-selection.md)

# Sources

- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
