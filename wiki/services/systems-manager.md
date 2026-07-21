---
type: AWS Service
title: Systems Manager
service_id: systems-manager
description: Operates managed nodes through documents, fleet targeting, configuration, patching, maintenance, sessions, inventory, and parameters.
tags: [soa-c03, domain-3, systems-manager, operations]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.2.1", "3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Core model

```text
supported machine + SSM Agent + node identity + Region/time + HTTPS/DNS path = managed node
```

# Capability map

| Need | Capability |
| --- | --- |
| one-time command | Run Command |
| recurring desired configuration | State Manager |
| multi-step AWS operation | Automation |
| scan or install operating-system patches | Patch Manager |
| scheduled controlled task | Maintenance Windows |
| interactive access without inbound administration ports | Session Manager |
| browser administration | Fleet Manager |
| collected fleet metadata | Inventory |
| hierarchical or encrypted parameter | Parameter Store |

# Fleet controls

Documents, versions, parameters, tag or resource-group targets, `MaxConcurrency`, `MaxErrors`, timeout, output, and notification determine execution. Preview targets and canary before broad changes. Rate control limits blast radius but does not roll back completed work.

# Managed-node evidence

Check agent installation and logs, process state, account/Region registration, instance profile or activation role, credentials, clock, DNS, HTTPS, Systems Manager messaging endpoints, endpoint policies, security controls, proxy, and firewall.

# Feature boundaries

Patch Scan reports; Install changes the node. Maintenance-window cutoff stops new task starts but does not necessarily cancel running tasks. Operator session permission differs from node permission. `SecureString` also needs KMS decrypt and is not automatic secret rotation.

# Related concepts

- [Operational automation](/concepts/operational-automation.md)
- [Systems Manager Automation](/services/systems-manager-automation.md)
- [Automation failure](/playbooks/automation-execution-failure.md)

# Sources

- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
