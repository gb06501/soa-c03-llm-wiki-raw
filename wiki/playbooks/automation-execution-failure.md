---
type: Troubleshooting Playbook
title: Systems Manager automation execution failure
description: Diagnoses managed-node, command, association, patch, window, session, output, and fleet-target failures.
tags: [soa-c03, domain-3, systems-manager, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.2.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
status: verified
---

# Trigger

A Systems Manager operation cannot find nodes, remains pending, fails on targets, misses its schedule, or reports success without the desired result.

# Evidence path

1. Confirm SSM Agent, node identity, account/Region, clock, IAM or activation role, DNS, and HTTPS endpoint path.
2. Resolve actual target IDs from tags or resource groups.
3. Inspect document name/version, platform, parameters, concurrency, error threshold, and per-node plugin output.
4. For patches, inspect baseline, patch group, scan/install mode, repository access, disk, locks, and reboot need.
5. For Maintenance Windows, inspect schedule, enabled state, duration, cutoff, targets, tasks, priority, and task role.
6. For sessions/output, inspect operator permission, session document, log destination, KMS, and node role.

# Failure map

| Symptom | Direction |
| --- | --- |
| Node absent/offline | agent, identity, Region, endpoints, DNS, proxy/firewall |
| Command pending | node message path or delivery window |
| One OS fails | document platform/plugin/command |
| Association drifts later | wrong tool or recurring execution failure |
| Patch noncompliant | baseline approval, last scan, install/reboot |
| Window task never starts | schedule, targets, task, cutoff, role |
| Session denied | operator StartSession and document permission |
| Success but no result | command exit semantics versus application state |

# Safe action

Narrow the target set, canary the correction, pin the document version, and set independent concurrency and error limits. Repair the managed-node foundation before changing individual automation features.

# Verification

Confirm nodes are online, every intended target completed, output and compliance are current, the application result is correct, no unintended targets changed, and logs/audit evidence were retained.

# Related concepts

- [Operational automation](/concepts/operational-automation.md)
- [Service selection](/decision-guides/operational-automation-service-selection.md)

# Sources

- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
