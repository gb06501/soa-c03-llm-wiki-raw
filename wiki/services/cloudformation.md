---
type: AWS Service
title: CloudFormation
service_id: cloudformation
description: Owns declarative stack resources, previews lifecycle changes, deploys across targets, and records resource-level failure evidence.
tags: [soa-c03, domain-3, cloudformation, iac]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["3.1.2", "3.1.3", "3.1.4", "3.1.5", "1.2.1", "2.3.4"]
domain_ids: ["3", "1", "2"]
sources:
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
status: verified
---

# Core model

```text
template + parameters -> change set -> stack operation -> physical resources -> events and drift
```

# Resource lifecycle

Logical IDs, resource types, properties, references, conditions, and outputs describe desired state. A property update can be in place, interrupting, or replacement. Review replacement of stateful resources and temporary quota/IP demand before execution.

`DeletionPolicy` controls resource removal with stack deletion or template removal. `UpdateReplacePolicy` controls the old physical resource after replacement. Termination protection and stack policies protect different actions.

# Permissions and evidence

The caller, `iam:PassRole`, execution role, target service policy, SCP, and KMS policy are separate gates. Start failures from the earliest failed logical resource and exact status reason; follow nested-stack summaries into child events.

# StackSets

A StackSet combines a template and parameters with target accounts or OUs, Regions, stack instances, and operation preferences. Maximum concurrency limits simultaneous targets. Failure tolerance decides when further rollout stops; it is not global rollback.

# Recovery

For `UPDATE_ROLLBACK_FAILED`, repair the blocking permission, dependency, or resource condition, then continue rollback. Skipping resources is a last resort because it can leave template and physical state inconsistent.

# Related concepts

- [CloudFormation and CDK lifecycle](cloudformation-and-cdk.md)
- [CloudFormation deployment failure](../playbooks/cloudformation-deployment-failure.md)
- [Cross-account provisioning](../concepts/cross-account-resource-provisioning.md)

# Corpus reconciliation: Domains 1 and 2

## Evidence and recovery readiness

Stack events provide infrastructure-change evidence. Templates recreate declared infrastructure for disaster recovery; they do not restore application data, runtime state, secrets, or undeclared dependencies.

# Sources

- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
