---
type: Troubleshooting Playbook
title: Data classification gap
description: Diagnoses unscanned, unclassified, misclassified, or unenforced data and repairs the control matrix safely.
tags: ["soa-c03", "domain-4", "troubleshooting", "macie", "data-classification"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.1"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
status: verified
---

# Trigger

Sensitive data is missing from discovery, a Macie job has incomplete coverage, or the applied storage/access controls do not match the intended classification.

# Evidence path

1. Identify data owner, bucket/object scope, Region, expected class, and applicable control matrix.
2. Confirm Macie account, delegated-administrator, member, and Region enablement.
3. Inspect automated-discovery or classification-job scope, sampling, schedule, and completion.
4. Check S3 and KMS permissions for scanning and result storage.
5. Inspect managed/custom data identifiers and allow lists.
6. Validate object format, encryption, size, and other scan constraints from source evidence.
7. Compare findings and labels with actual access, public posture, encryption, retention, and backup controls.
8. Trace finding routing and remediation ownership.

# Failure map

| Symptom | Direction |
| --- | --- |
| Bucket absent | account/Region/member/inventory coverage |
| Job skips objects | scope, object support, encryption access |
| Expected pattern absent | identifier choice, proximity, sampling |
| Too many benign matches | custom identifier tuning or narrow allow list |
| Finding exists but no action | routing, owner, workflow, suppression |
| Label present but control absent | Config/policy enforcement gap |

# Safe action

Correct coverage and identifiers on a bounded sample, protect discovery results, then apply the required control through the owning S3/IAM/KMS/configuration path.

# Verification

Run an approved test object through discovery, confirm classification and routing, verify intended access succeeds, unauthorized access fails, and retention/encryption controls match the matrix.

# Rollback

Restore the previous identifier or policy configuration if tuning hides valid data or breaks approved access, while retaining findings for review.

# Escalation

Provide ownership, scope, job/discovery evidence, identifiers, false-positive/negative examples, and missing control.

# Related pages

- [Data classification](../concepts/data-classification.md)
- [Macie](../services/macie.md)

# Sources

- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
