---
type: Concept
title: Data classification
description: Connects data sensitivity and business ownership to enforceable storage, access, encryption, retention, and monitoring controls.
tags: ["soa-c03", "domain-4", "data-classification", "governance"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.1"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
status: verified
---
# Core model

Classification turns data meaning into control requirements. A label without an owner, scope, and enforceable control matrix is only metadata.

# Classification dimensions

| Dimension | Example question |
| --- | --- |
| Sensitivity | What harm follows disclosure? |
| Regulation | Which legal or contractual rule applies? |
| Criticality | What happens if unavailable or corrupted? |
| Residency | Where may data be stored or processed? |
| Retention | How long must it remain and when must it be deleted? |
| Ownership | Who accepts risk and approves access? |

# Control matrix

For each class define allowed locations, principals, encryption/key ownership, TLS, public-access posture, logging, discovery cadence, backup, retention, deletion, and exception handling.

# Detection and enforcement

Macie detects sensitive patterns in S3. Tags and metadata carry intended classification. IAM, S3, KMS, Config, Control Tower, and SCPs enforce or evaluate controls. Findings route gaps to accountable remediation.

# Verification

Measure both coverage and effectiveness: in-scope resources discovered, unclassified data, control compliance, finding age, approved exceptions, and successful restore or decrypt tests.

# Related pages

- [Macie](../services/macie.md)
- [Data protection control selection](../decision-guides/data-protection-control-selection.md)
- [Data classification gap](../playbooks/data-classification-gap.md)

# Sources

- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
