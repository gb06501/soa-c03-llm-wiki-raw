---
type: Decision Guide
title: Operational automation service selection
description: Selects the correct Systems Manager capability for fleet operations and configuration.
tags: [soa-c03, domain-3, systems-manager]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.2.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Execute a command now | one-time node action | Run Command |
| Continuously or periodically enforce configuration | desired-state association | State Manager |
| Orchestrate multiple AWS actions | stepwise operational workflow | Automation |
| Assess or install OS patches | baseline and compliance | Patch Manager |
| Run controlled tasks on a schedule | time window, targets, cutoff | Maintenance Windows |
| Interactive shell without inbound ports | IAM-mediated session | Session Manager |
| Browser administration | managed-node GUI | Fleet Manager |
| Search installed software/configuration | collected fleet metadata | Inventory |
| Hierarchical configuration or simple secured value | versioned parameter | Parameter Store |

# Rejection rules

- Do not use Run Command when recurring desired state is required.
- Do not treat MaxErrors as rollback.
- Do not treat Patch Scan as remediation.
- Do not treat Inventory as real-time performance telemetry.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Operational automation](/concepts/operational-automation.md)
- [Automation failure](/playbooks/automation-execution-failure.md)

# Sources

- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
