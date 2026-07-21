---
type: Concept
title: Config and continuous compliance
description: Connects resource inventory, rules, conformance packs, aggregation, and bounded remediation.
tags: ["soa-c03", "domain-4", "config", "compliance"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
status: verified
---
# Core model

Continuous compliance is a loop:

`record state -> evaluate rule -> route result -> remediate safely -> re-evaluate -> report`

# Prevention versus detection

SCPs and supported Control Tower controls can prevent selected actions. Config records and detects deployed state. Systems Manager Automation or another owned workflow remediates. No one layer replaces the others.

# Coverage dimensions

Track account, Region, supported resource type, recorder scope, rule deployment, evaluation freshness, exception, remediation ownership, and verification. An aggregator centralizes results but does not create missing recorders or rules.

# Automation guardrails

Use explicit parameters, least-privilege roles, concurrency and error limits, idempotence, dry-run or manual approval, rollback, and workload-health verification.

# Related pages

- [Config](config.md)
- [Control Tower](control-tower.md)
- [Compliance monitoring selection](../decision-guides/compliance-monitoring-selection.md)
- [Compliance remediation failure](../playbooks/compliance-remediation-failure.md)

# Sources

- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
