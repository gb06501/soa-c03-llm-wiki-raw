---
type: Concept
title: Trusted Advisor security checks
description: Turns advisory security checks into evidence-led, reversible, and verified remediation.
tags: ["soa-c03", "domain-4", "trusted-advisor", "security-checks"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
status: verified
---
# Core model

Treat each advisory result as a potentially stale observation. Confirm current resource state, exposure, ownership, dependency, and the exact recommended control before changing production.

# Remediation pattern

| Finding family | Verify before action |
| --- | --- |
| Open security group | Listener, source range, workload and admin path |
| Public S3 access | Block settings, bucket/access-point policy, website requirement |
| Root or MFA posture | Credential inventory, emergency process, monitoring |
| Access keys | Last used, owner, replacement and revocation plan |
| CloudTrail | Trail scope, log destination, integrity and permissions |
| Certificate expiry | In-use attachments, renewal validation and deployment |
| Encryption or snapshot | Key, data lifecycle, backup/restore and workload impact |

# Automation boundary

Route and enrich automatically. Remediate automatically only when the target selection is exact, action is idempotent, blast radius is bounded, rollback exists, and both security and workload verification are built in.

# Related pages

- [Trusted Advisor](trusted-advisor.md)
- [Security check remediation priority](../decision-guides/security-check-remediation-priority.md)

# Sources

- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
