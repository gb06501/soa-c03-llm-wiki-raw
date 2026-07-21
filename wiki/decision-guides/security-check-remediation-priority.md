---
type: Decision Guide
title: Security check remediation priority
description: Ranks Trusted Advisor security checks by exposure, privilege, data impact, freshness, and safe remediation readiness.
tags: ["soa-c03", "domain-4", "trusted-advisor", "risk-priority"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
status: verified
---

# Decision table

| Priority clue | Effect |
| --- | --- |
| Internet exposure or public data path | raise urgency |
| Root, administrative, or credential compromise risk | raise urgency sharply |
| Sensitive or regulated data | raise business impact |
| Active exploitation or correlated finding | raise urgency sharply |
| Broad account/Region scope | raise impact |
| Stale, deleted, or excluded resource | validate before action |
| High change blast radius | require stronger staging and rollback |
| Exact reversible fix with clear owner | increases safe execution readiness |

# Remediation selection

| Finding | First safe direction |
| --- | --- |
| Open security group | confirm workload path, narrow port/source, test access |
| Public S3 | identify intended public use, block unintended path, test clients |
| Root/MFA/access keys | secure alternate admin path, enable controls, rotate/revoke safely |
| Missing CloudTrail | establish durable central trail and protect logs |
| Certificate expiry | validate renewal/deployment path and rotate with overlap |
| Encryption or snapshot | plan key/data migration and verify restore |

# Rejection rules

- Do not prioritize only by advisory color.
- Do not remediate a stale check without current resource evidence.
- Exclusion is risk acceptance, not a fix.
- Do not automate an action without bounded scope, idempotence, rollback, and verification.

# Verification

Refresh the check, confirm the resource posture changed, prove workload health, inspect CloudTrail/change evidence, and document any residual or accepted risk.

# Related pages

- [Trusted Advisor security checks](../services/trusted-advisor-security.md)
- [Security finding remediation](../playbooks/security-finding-remediation.md)

# Sources

- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
