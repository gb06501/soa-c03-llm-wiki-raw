---
type: Concept
title: Cross-account and multi-Region provisioning
description: Separates shared-resource use from repeated infrastructure deployment across accounts and Regions.
tags: [soa-c03, domain-3, ram, stacksets, multi-account]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.4"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md
status: verified
---

# Core model

```text
one supported live resource used by many accounts -> AWS RAM
same infrastructure created in many account/Region targets -> CloudFormation StackSets
```

RAM keeps ownership with the resource owner. StackSets creates separate underlying stacks through stack instances.

# Object boundaries

| Mechanism | Key objects | Ownership result |
| --- | --- | --- |
| AWS RAM | resource share, resource, principal, managed permission, invitation | owner retains lifecycle |
| StackSets | StackSet, target, Region, stack instance, operation preferences | target stack owns deployed resources |
| Resource policy | resource and allowed cross-account principal | API access, not cloning |
| Artifact copy | destination AMI/image and permissions | independent destination artifact |

# StackSet safety

Choose service-managed permissions for Organizations/OUs and self-managed permissions for explicit administration/execution-role paths. Test a canary account/Region, then control Region order, maximum concurrency, and failure tolerance.

# Cross-account gates

Organizations/SCP, administrator permission, execution role and trust, service IAM, resource policy, KMS policy, and Region-specific artifacts must all allow the action. No sharing method overrides an explicit deny.

# Common traps

RAM does not copy or replicate resources. One stack instance means one account plus one Region. Failure tolerance stops expansion after a threshold; it does not roll back every successful target. Retained stacks leave StackSet management.

# Related concepts

- [Sharing and provisioning selection](/decision-guides/resource-sharing-and-provisioning-selection.md)
- [Cross-account provisioning failure](/playbooks/cross-account-provisioning-failure.md)

# Sources

- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
