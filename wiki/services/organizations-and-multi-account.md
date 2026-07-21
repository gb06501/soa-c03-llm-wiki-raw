---
type: Concept
title: Organizations and multi-account security
description: Explains how organization structure, landing-zone controls, federation, and central security services work together.
tags: ["soa-c03", "domain-4", "organizations", "multi-account"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
status: verified
---
# Core model

A secure multi-account design uses accounts as isolation boundaries and centralizes only what benefits from shared governance: identity, policies, logging, findings, backups, and approved resource sharing.

# Operating model

| Capability | Owner |
| --- | --- |
| Organization and OU structure | Governance team |
| Workforce assignments | Identity team |
| Preventive guardrails | Governance and security |
| Central logs and findings | Security operations |
| Workload permissions and remediation | Account workload owner |
| Break-glass path | Independently controlled security owner |

# Control hierarchy

Organizations provides hierarchy, SCPs, trusted access, and delegated administration. IAM Identity Center supplies workforce assignments. Control Tower operates a landing zone and controls. CloudTrail, Config, Security Hub CSPM, GuardDuty, Macie, and Backup require account/Region coverage.

# Related pages

- [Organizations](organizations.md)
- [Control Tower](control-tower.md)
- [IAM Identity Center](iam-identity-center.md)
- [Cross-account access failure](../playbooks/cross-account-access-failure.md)

# Sources

- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
