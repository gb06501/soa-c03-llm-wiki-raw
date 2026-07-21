---
type: Decision Guide
title: Resource sharing and provisioning selection
description: Chooses RAM, StackSets, resource policies, or artifact copies across accounts and Regions.
tags: [soa-c03, domain-3, ram, stacksets]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.4"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Use one central supported resource | shared ownership | AWS RAM |
| Deploy the same baseline repeatedly | separate target stacks | CloudFormation StackSets |
| Grant cross-account access to one service object | resource API authorization | resource policy |
| Create independent regional image | destination artifact ownership | copy or Image Builder distribution |
| Organizations OU rollout | service-linked role integration | service-managed StackSets |
| Explicit accounts without Organizations integration | administrator/execution roles | self-managed StackSets |
| Limit fan-out risk | controlled target batches | operation concurrency and failure tolerance |
| New accounts in targeted OU | membership-driven deployment | StackSet auto-deployment |

# Rejection rules

- Do not use RAM to clone infrastructure.
- Do not use StackSets to share one live subnet.
- Do not assume RAM permission bypasses participant IAM or SCP.
- Do not assume StackSets replicate application data or artifacts.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Cross-account provisioning](../concepts/cross-account-resource-provisioning.md)
- [Provisioning failure](../playbooks/cross-account-provisioning-failure.md)

# Sources

- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
