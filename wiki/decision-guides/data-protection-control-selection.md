---
type: Decision Guide
title: Data protection control selection
description: Maps classification requirements to discovery, access, encryption, retention, monitoring, and response controls.
tags: ["soa-c03", "domain-4", "data-classification", "data-protection"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.1"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
status: verified
---

# Decision table

| Requirement | Select |
| --- | --- |
| Discover sensitive patterns in S3 continuously | Macie automated discovery |
| Scan an exact bucket/object/time scope | Macie classification job |
| Detect organization-specific pattern | custom data identifier |
| Ignore reviewed benign pattern | narrowly scoped allow list |
| Carry intended classification | governed tag or metadata scheme |
| Restrict principals and resources | IAM and supported resource policies |
| Control encryption key and use | KMS customer managed key |
| Evaluate deployed configuration | Config rule or control |
| Prevent broad prohibited actions | SCP or preventive control |
| Route classification gaps | findings through Security Hub CSPM/EventBridge workflow |

# Rejection rules

- Discovery does not enforce access or encryption.
- Tags do not prove data content.
- Encryption does not define who may decrypt or how long data remains.
- Public-access prevention does not classify data.
- A finding closed in an aggregator is not source-level remediation.

# Verification

Seed approved test data, prove discovery and finding routing, inspect the applied control matrix, verify unauthorized access fails, and confirm retention, backup, decrypt, and deletion behavior as required.

# Related pages

- [Data classification](../concepts/data-classification.md)
- [Macie](../services/macie.md)

# Sources

- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
