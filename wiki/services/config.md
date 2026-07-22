---
type: AWS Service
title: Config
service_id: config
description: Records resource configuration and evaluates state against compliance rules and conformance packs.
tags: ["soa-c03", "domain-4", "config", "compliance"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.2.1", "1.2.3", "4.1.5", "4.2.1", "4.2.5"]
domain_ids: ["1", "4"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

Config records supported resource configuration over time and evaluates rules against current or changed state. A recorder, delivery channel, configuration item, rule, evaluation, and remediation are separate objects.

# Key objects

| Object | Purpose |
| --- | --- |
| Configuration recorder | Selects supported resource types and captures change |
| Configuration item | Point-in-time resource state and relationships |
| Rule | Evaluates a condition on change or schedule |
| Conformance pack | Deploys a governed set of rules and remediation metadata |
| Aggregator | Centralizes multi-account and multi-Region results |
| Remediation | Invokes an SSM Automation document manually or automatically |

# Decision boundaries

Config is detective unless a separate preventive gate blocks creation. Automatic remediation must handle stale evaluations, concurrency, retries, permissions, and resource ownership.

# Evidence and diagnosis

Verify recorder status, delivery, resource coverage, rule trigger, evaluation timestamp, annotation, aggregator scope, and remediation execution history.

# Safe operations

Deploy organization rules consistently, exclude only with documented ownership, start remediation manually, bound automation, and verify both compliance and workload health.

# Related decisions

- [Compliance monitoring selection](../decision-guides/compliance-monitoring-selection.md)
- [Compliance remediation failure](../playbooks/compliance-remediation-failure.md)

# Finding-to-remediation path

A Config finding can trigger governed remediation, but evaluation scope, remediation mapping, execution role, parameters, retries, and resulting resource state must be verified separately.

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.2.3](../../raw/skills/1.2.3-create-and-run-systems-manager-automation-runbooks.md)
- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)

