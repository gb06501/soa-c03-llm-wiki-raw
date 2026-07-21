---
type: Troubleshooting Playbook
title: Cross-account provisioning failure
description: Diagnoses RAM and StackSet visibility, permission, target, Region, operation, and drift failures.
tags: [soa-c03, domain-3, ram, stacksets, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.4"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md
status: verified
---

# Trigger

A resource share is missing or unusable, or a StackSet operation fails in some accounts or Regions.

# Evidence path

1. Identify RAM sharing, StackSets deployment, resource policy, or artifact copy.
2. For RAM, inspect owner Region, resource support, principal, managed permission, invitation, and Organizations integration.
3. For StackSets, inspect permission model, administrator context, targets, Regions, operation preferences, and first failed stack instance.
4. Follow the failed instance into underlying CloudFormation events.
5. Check SCP, role trust, PassRole, service IAM, resource/KMS policy, quota, capacity, and Region-specific parameters.
6. Compare drift and retention state for exceptional targets.

# Failure map

| Symptom | Direction |
| --- | --- |
| RAM share invisible | Region, principal, invitation, Organizations setting |
| Resource visible but denied | RAM permission plus participant IAM/SCP/service policy |
| All self-managed targets fail | administrator/execution role trust and permissions |
| One account fails | SCP, quota, collision, local parameter |
| One Region fails | support, AMI/KMS/certificate/artifact, capacity |
| Operation stops early | failure tolerance and first failed instance |
| Retained stack no longer updates | expected loss of StackSet management |

# Safe action

Correct the specific principal, target, parameter, or role path. Retry a canary account/Region first, then expand with conservative concurrency; do not unshare or delete retained state blindly.

# Verification

Confirm participant use or successful stack instances in every intended account/Region, expected ownership, healthy underlying resources, correct drift state, and deliberate retain/delete behavior.

# Related concepts

- [Cross-account provisioning](/concepts/cross-account-resource-provisioning.md)
- [Selection guide](/decision-guides/resource-sharing-and-provisioning-selection.md)

# Sources

- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
