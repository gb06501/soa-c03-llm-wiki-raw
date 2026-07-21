---
type: Learning Path
title: Domain 3 learning path
description: Orders Domain 3 study from immutable artifacts and infrastructure ownership through safe deployment and automation.
tags: [soa-c03, domain-3, learning-path]
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

# Stage 1: Establish identity and ownership

1. [EC2](../../services/ec2-performance.md), [Image Builder](../../services/image-builder.md), and [ECR](../../services/ecr.md)
2. [CloudFormation](../../services/cloudformation.md), [CDK](../../services/cdk.md), and [Service Catalog](../../services/service-catalog.md)
3. [Terraform and Git controls](../../concepts/third-party-deployment-tools.md)

Goal: distinguish immutable release identity, resource ownership, and reviewed change preview.

# Stage 2: Provision across boundaries

1. [Resource Access Manager](../../services/resource-access-manager.md) and [CloudFormation](../../services/cloudformation.md)
2. [Cross-account and multi-Region provisioning](../../concepts/cross-account-resource-provisioning.md)
3. [Resource sharing and provisioning selection](../../decision-guides/resource-sharing-and-provisioning-selection.md)
4. [Cross-account provisioning failure](../../playbooks/cross-account-provisioning-failure.md)

Goal: choose sharing, repeated deployment, or artifact copying without confusing ownership.

# Stage 3: Release safely

1. [Deployment strategies](../../concepts/deployment-strategies.md)
2. [Deployment strategy selection](../../decision-guides/deployment-strategy-selection.md)
3. [Deployment rollback](../../playbooks/deployment-rollback.md)

Goal: reason about blast radius, mixed versions, temporary capacity, health gates, and data-compatible rollback.

# Stage 4: Diagnose from evidence

1. [Deployment diagnostics](../../concepts/deployment-diagnostics.md)
2. [Deployment evidence selection](../../decision-guides/deployment-failure-evidence-selection.md)
3. [Deployment failure](../../playbooks/deployment-failure.md)
4. [CloudFormation deployment failure](../../playbooks/cloudformation-deployment-failure.md)

Goal: find the first failed layer and correct the smallest safe cause.

# Stage 5: Automate operations

1. [Systems Manager](../../services/systems-manager.md) and [Systems Manager Automation](../../services/systems-manager-automation.md)
2. [Operational automation selection](../../decision-guides/operational-automation-service-selection.md)
3. [S3](../../services/s3-performance.md), [EventBridge](../../services/eventbridge.md), [SNS](../../services/sns-notifications.md), [SQS](../../services/sqs.md), and [Lambda](../../services/lambda.md)
4. [Step Functions](../../services/step-functions.md) and [DevOps Agent](../../services/devops-agent.md)
5. [Event-driven automation](../../concepts/event-driven-automation.md)
6. [Event-driven automation selection](../../decision-guides/event-driven-automation-selection.md)

Goal: select the right control surface, permission model, failure semantics, idempotency, and loop guard.

# Stage 6: Integrate and test

Read [the Domain 3 operating model](../../concepts/deployment-and-operational-automation.md), then review [Domain 3 exam traps](../../exam-traps/domain-3-exam-traps.md). For each scenario, state the artifact identity, owner, preview, exposure limit, evidence path, rollback object, and verification.

# Sources

- [Skill 3.1.1](../../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
- [Skill 3.1.2](../../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
- [Skill 3.1.3](../../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.4](../../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
- [Skill 3.1.5](../../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 3.1.6](../../../raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md)
- [Skill 3.2.1](../../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
- [Skill 3.2.2](../../../raw/skills/3.2.2-implement-event-driven-automation.md)
