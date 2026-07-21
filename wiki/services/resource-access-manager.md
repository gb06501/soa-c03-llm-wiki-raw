---
type: AWS Service
title: Resource Access Manager
service_id: resource-access-manager
description: Shares supported owner-account resources with authorized accounts, organizations, OUs, or other supported principals.
tags: [soa-c03, domain-3, ram, multi-account]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.4"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md
status: verified
---

# Core model

```text
owner -> resource share -> supported resource + principal + managed permission
      -> participant uses resource without receiving a copy
```

# Objects and behavior

A resource share associates resource ARNs, principals, and a managed permission. External principals may require an invitation. Organization sharing relies on Organizations integration and the correct target organization, OU, or account.

The owner keeps ownership and lifecycle control. The participant receives permitted use subject to its IAM, SCP, service rules, and the RAM permission. Sharing does not replicate a resource across Regions.

# Shared subnet boundary

The networking account owns the VPC, subnet, routes, NAT or endpoints, NACLs, and network architecture. A participant owns its supported workload resources and security configuration. Participant visibility does not prove the owner-side network path is usable.

# Evidence

Inspect resource-share status, resource association, principal, permission version, invitation, Organizations setting, Region, participant service error, and CloudTrail.

# Selection trap

Use StackSets when separate infrastructure must be created in each target. Use a resource policy for direct cross-account API access where that service supports it.

# Related concepts

- [Cross-account provisioning](../concepts/cross-account-resource-provisioning.md)
- [Provisioning selection](../decision-guides/resource-sharing-and-provisioning-selection.md)

# Sources

- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
