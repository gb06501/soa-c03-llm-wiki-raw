---
type: Concept
title: Multi-account security governance
description: Combines account boundaries, preventive guardrails, detective controls, centralized evidence, and delegated operations.
tags: ["soa-c03", "domain-4", "multi-account", "governance"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.2", "4.1.3", "4.1.4", "4.1.5", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Governance layers

| Layer | Primary question | Examples |
| --- | --- | --- |
| Account and OU design | Where is the blast-radius boundary? | Organizations, workload and security OUs |
| Identity | Who can enter and assume which role? | IAM Identity Center, roles, federation |
| Prevention | Which actions must never occur? | SCPs, Control Tower preventive controls |
| Detection | Which deployed state violates policy? | Config, Control Tower detective controls |
| Evidence | Can activity be investigated centrally? | CloudTrail, Config aggregation, findings |
| Response | Who owns containment and remediation? | Security Hub CSPM routing, automation |

# Decision layers

Use SCPs for broad maximum-permission guardrails, not workload grants. Use Config for state evaluation, not prevention. Use Control Tower for a managed landing-zone operating model. Use delegated administrators to separate service operations from the management account.

# Regional and account completeness

Most governance and detection services require deliberate enablement and aggregation by account and Region. “Enabled centrally” does not prove every workload Region is covered.

# Change safety

Test guardrails in a canary OU, retain an independently governed emergency path, protect the log archive, bound automation, and verify both security posture and workload behavior after change.

# Related pages

- [Organizations](../services/organizations.md)
- [Control Tower](../services/control-tower.md)
- [Multi-account guardrail selection](../decision-guides/multi-account-guardrail-selection.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
