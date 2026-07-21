---
type: AWS Feature
title: IAM Access Analyzer
parent_services: [IAM]
description: Analyzes policies and access paths for external, internal, and unused access findings.
tags: ["soa-c03", "domain-4", "iam", "access-analyzer"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
status: verified
---
# Parent service

[IAM](iam.md)

# Core model

IAM Access Analyzer evaluates policies and observed access to identify unintended external, internal, or unused access. It can also validate policies, preview selected access changes, and generate policy candidates from CloudTrail activity.

# Decision boundaries

A finding is an access observation, not proof of compromise. Policy validation catches structural and security issues but does not simulate every request context. Generated policy is a starting point constrained by the activity window.

# Evidence and diagnosis

Inspect analyzer scope, finding type, principal, resource, condition, archive rule, last accessed evidence, policy version, and whether the access is intended and documented.

# Safe operations

Review before archiving, narrow the exact principal/action/resource/condition, preview supported policy changes, retest required access, and verify nearby denied paths.

# Related decisions

- [Access denial evidence selection](../decision-guides/access-denial-evidence-selection.md)
- [IAM principal and policy selection](../decision-guides/iam-principal-and-policy-selection.md)

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
