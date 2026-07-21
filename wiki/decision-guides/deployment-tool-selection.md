---
type: Decision Guide
title: Deployment tool selection
description: Chooses Terraform, CloudFormation/CDK, data references, imports, and Git release identities from ownership clues.
tags: [soa-c03, domain-3, terraform, git]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.6"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Existing Terraform-owned resource | configuration-state-AWS reconciliation | Terraform |
| AWS-native stack owned by template | managed stack lifecycle | CloudFormation or CDK |
| Read resource owned elsewhere | consume without ownership | data source or output |
| Adopt existing object into Terraform | attach address to physical ID | terraform import then plan |
| Preview third-party IaC action | create/update/delete/replacement evidence | terraform plan |
| Team-shared state | durability and coordination | protected remote backend with locking |
| Identify reviewed release exactly | immutable source identity | commit hash or controlled tag |
| Resolve IaC merge conflict | semantic infrastructure reconciliation | manual resolution then validate and plan |

# Rejection rules

- Do not let Terraform and CloudFormation own the same property.
- Do not treat a workspace as a Git branch or security boundary.
- Do not force-unlock until the original operation is proven absent.
- Do not commit state, secrets, or sensitive plan artifacts.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Third-party tools](/concepts/third-party-deployment-tools.md)
- [Third-party failure](/playbooks/third-party-deployment-failure.md)

# Sources

- [Skill 3.1.6](../../raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md)
