---
type: AWS Service
title: Organizations
service_id: organizations
description: Groups AWS accounts into an organization and applies hierarchical policy guardrails.
tags: ["soa-c03", "domain-4", "organizations", "multi-account"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.3", "4.1.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
status: verified
---
# Core model

Organizations supplies an account hierarchy: organization root, organizational units, and member accounts. Policies inherit down the hierarchy. The management account remains a special trust boundary and should not host ordinary workloads.

# Service control policies

An SCP limits the maximum available permissions for member-account principals. It does not grant permission. Explicit denies apply through inheritance; an allow-list design requires the action to remain allowed at every relevant level.

# Governance objects

| Object | Use |
| --- | --- |
| OU | Group accounts with similar policy and lifecycle |
| SCP | Bound permissions available in member accounts |
| Trusted access | Allow an integrated service to act across the organization |
| Delegated administrator | Move service administration away from the management account |

# Evidence and diagnosis

Trace the target account through root and OU inheritance. Check policy type enablement, attachments, explicit denies, requested Region, principal class, and delegated-administrator registration.

# Safe operations

Test guardrails in a canary OU, protect break-glass access, avoid daily use of the management account, and deploy central evidence services across all required Regions.

# Related decisions

- [Multi-account guardrail selection](../decision-guides/multi-account-guardrail-selection.md)
- [Cross-account access failure](../playbooks/cross-account-access-failure.md)

# Sources

- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
