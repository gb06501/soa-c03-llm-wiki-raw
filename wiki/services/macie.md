---
type: AWS Service
title: Macie
service_id: macie
description: Discovers and classifies sensitive data in S3 and produces actionable findings.
tags: ["soa-c03", "domain-4", "macie", "data-classification"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.1", "4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

Macie evaluates S3 data for sensitive-data patterns. Automated discovery continuously samples and builds account-level visibility; a classification job scans selected buckets and objects with an explicit scope.

# Detection objects

| Object | Use |
| --- | --- |
| Managed data identifier | AWS-maintained sensitive-data pattern |
| Custom data identifier | Organization-specific pattern and proximity rules |
| Allow list | Reduce known benign matches |
| Sensitive-data finding | Security signal and affected object |
| Discovery result | Detailed scan result stored in a protected destination |

# Decision boundaries

A data-classification label is a governance decision; a Macie finding is evidence. Macie does not by itself enforce access, encryption, retention, or deletion.

# Evidence and diagnosis

Check bucket and object scope, sampling or job definition, encryption access, unsupported objects, identifier selection, finding severity, and result repository permissions.

# Safe operations

Use delegated administration for multi-account coverage, protect discovery results, tune identifiers and allow lists with review, and route findings to an owned remediation workflow.

# Related decisions

- [Data protection control selection](../decision-guides/data-protection-control-selection.md)
- [Data classification gap](../playbooks/data-classification-gap.md)

# Sources

- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
