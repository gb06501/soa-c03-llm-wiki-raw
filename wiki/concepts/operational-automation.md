---
type: Concept
title: Systems Manager operational automation
description: Selects and governs Systems Manager capabilities for fleet commands, desired state, patching, maintenance, sessions, and inventory.
tags: [soa-c03, domain-3, systems-manager, operations, automation]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.2.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
status: verified
---

# Core model

```text
supported machine + SSM Agent + node identity + Region/time + HTTPS/DNS path = managed node
```

This foundation is shared by Run Command, State Manager, Patch Manager, Session Manager, Fleet Manager, and Inventory.

# Capability map

| Need | Choice |
| --- | --- |
| Run one command across nodes | Run Command |
| Maintain recurring desired configuration | State Manager |
| Orchestrate AWS API/resource steps | Automation |
| Scan or install OS patches | Patch Manager |
| Schedule controlled operations | Maintenance Windows |
| Interactive access without inbound SSH/RDP | Session Manager |
| Browser-based administration | Fleet Manager |
| Collect fleet metadata | Inventory |
| Store hierarchical values | Parameter Store |

# Fleet safety

Pin the document version, preview dynamic targets, canary first, and set `MaxConcurrency` independently from `MaxErrors`. Rate control limits blast radius; it is not rollback. Inspect per-node output and verify the business result after an apparently successful command.

# Boundaries

Patch Scan reports; Install changes nodes. Maintenance-window cutoff prevents new task starts but does not necessarily terminate running work. Operator permission and node instance-profile permission are separate. `SecureString` also requires KMS decrypt and is not automatic secret rotation.

# Related concepts

- [Operational automation selection](/decision-guides/operational-automation-service-selection.md)
- [Automation execution failure](/playbooks/automation-execution-failure.md)
- [Systems Manager Automation](/services/systems-manager-automation.md)

# Sources

- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
