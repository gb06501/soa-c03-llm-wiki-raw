---
type: Decision Guide
title: Compliance monitoring selection
description: Chooses preventive, detective, aggregation, and remediation controls for continuous compliance.
tags: ["soa-c03", "domain-4", "compliance", "config"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
status: verified
---

# Decision table

| Requirement | Select | Why |
| --- | --- | --- |
| Prohibit an account-level action broadly | SCP or supported preventive control | blocks before resource state changes |
| Validate a supported resource before creation | supported proactive control | pre-provision evaluation |
| Record configuration history | Config recorder and delivery | evidence over time |
| Evaluate deployed state | Config rule | change or scheduled compliance |
| Deploy a governed rule set | Conformance pack | consistent rules and remediation metadata |
| Central view across accounts/Regions | Config aggregator | read aggregation of existing coverage |
| Managed landing-zone governance | Control Tower | account enrollment and control operations |
| Correct a proven drift | SSM Automation or owned workflow | bounded remediation with execution evidence |

# Rejection rules

- An SCP does not grant access or inspect resource configuration.
- A Config rule is not preventive by itself.
- An aggregator does not enable recorders or rules.
- Automatic remediation is not safe merely because a rule is managed.
- “Compliant” is incomplete without account, Region, resource-type, and freshness coverage.

# Verification

Confirm the control is enabled in every intended account and Region, create a safe test violation, observe detection or prevention, execute remediation, re-evaluate, and verify workload health.

# Related pages

- [Config](../services/config.md)
- [Config and continuous compliance](../services/config-and-compliance.md)

# Sources

- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
