---
type: Exam Trap
title: Domain 3 exam traps
description: Corrects tempting deployment, provisioning, infrastructure-as-code, fleet automation, and event-automation misconceptions.
tags: [soa-c03, domain-3, exam-traps]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.1", "3.1.2", "3.1.3", "3.1.4", "3.1.5", "3.1.6", "3.2.1", "3.2.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
  - /raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md
  - /raw/skills/3.2.1-automate-operational-processes-with-services.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
status: verified
---

# Images and infrastructure as code

- AMI IDs are Region-specific; sharing is not copying.
- ECR tags can move; digests identify exact content.
- A vulnerability finding does not block deployment without enforcement.
- DeletionPolicy and UpdateReplacePolicy protect different lifecycle paths.
- CDK synthesizes and deploys CloudFormation; CDK success stages do not bypass stack behavior.
- IAM capability acknowledgement does not grant permission.

# Deployment diagnosis

- The final rollback event is usually not the root cause.
- `UPDATE_ROLLBACK_FAILED` requires blocker repair before continuing rollback.
- Quota, AZ capacity, and subnet IP exhaustion are different constraints.
- Control-plane creation success does not prove runtime or application health.

# Multi-account and Region provisioning

- RAM shares one owned resource; StackSets deploys separate stacks.
- RAM permission does not bypass participant IAM, SCP, service, or KMS policy.
- StackSet failure tolerance is not global rollback.
- Region-specific artifacts and parameters do not become portable automatically.

# Deployment strategies

- Rolling can mix versions and can still cause downtime.
- Blue/green describes environments; canary and linear describe exposure.
- Immutable compute does not make shared data immutable.
- Traffic rollback does not reverse database mutations.

# Third-party deployment

- Terraform configuration, state, and AWS reality are separate.
- Apply can partially succeed; Terraform has no universal rollback.
- A workspace is not a Git branch or security boundary.
- Git ignore rules do not remove or rotate committed secrets.
- Two tools must not own the same resource/property.

# Operational automation

- A running EC2 instance is not necessarily an online managed node.
- Run Command is one-time; State Manager maintains configuration.
- MaxConcurrency and MaxErrors are independent, and neither is rollback.
- Patch Scan does not install; command success does not prove application success.

# Event-driven automation

- S3 and EventBridge delivery can duplicate or reorder events.
- A matching EventBridge rule does not prove target authorization.
- SNS fans out; SQS buffers for polling consumers.
- DLQs do not replay themselves.
- Every automatic remediation needs idempotency and loop analysis.

# Related concepts

- [Domain 3 operating model](/concepts/deployment-and-operational-automation.md)
- [Domain 3 learning path](/learning/paths/domain-3-learning-path.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 3.1.6](../../raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md)
- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
