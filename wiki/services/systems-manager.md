---
type: AWS Service
title: Systems Manager
service_id: systems-manager
description: Operates managed nodes through documents, fleet targeting, configuration, patching, maintenance, sessions, inventory, and parameters.
tags: [soa-c03, domain-3, systems-manager, operations]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["3.2.1", "3.2.2", "1.1.2", "1.1.3", "1.2.1", "1.2.2", "1.2.3"]
domain_ids: ["3", "1"]
sources:
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
  - /raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md
  - /raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
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

- [Operational automation](../concepts/operational-automation.md)
- [Systems Manager Automation](systems-manager-automation.md)
- [Automation failure](../playbooks/automation-execution-failure.md)

# Corpus reconciliation: Domains 1 and 2

## Telemetry deployment and governed remediation

Systems Manager can distribute or retrieve CloudWatch Agent configuration and supply governed operational actions. Managed-node actions and direct AWS API actions have different prerequisites. Target resolution, execution role, step output, timeout, rollback, and verification remain explicit.

# Sources

- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
- [Skill 1.1.2](../../raw/skills/1.1.2-configure-and-manage-the-cloudwatch-agent.md)
- [Skill 1.1.3](../../raw/skills/1.1.3-configure-and-troubleshoot-cloudwatch-alarms.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.2](../../raw/skills/1.2.2-route-enrich-and-deliver-events-with-eventbridge.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
