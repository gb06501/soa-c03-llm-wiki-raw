---
type: Concept
title: Deployment and operational automation
description: Unifies artifact identity, infrastructure ownership, rollout, event and fleet automation, evidence, and recovery across Domain 3.
tags: [soa-c03, domain-3, deployment, provisioning, automation]
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

# Core model

```text
versioned source -> immutable artifact -> reviewed infrastructure change -> controlled rollout
                 -> operational/event automation -> evidence -> verified state or recovery
```

# Decision layers

1. Pin the artifact: AMI ID, image digest, task definition, Lambda version, commit, or saved plan.
2. Assign one owner to each resource: CloudFormation/CDK, Terraform, or a deliberate human boundary.
3. Choose sharing versus deployment across accounts and Regions.
4. Preview replacement, data, permission, quota, subnet, and temporary-capacity impact.
5. Limit exposure through canary targets, batches, concurrency, and failure thresholds.
6. Separate trigger permission from execution permission.
7. Make retries idempotent and loop-safe.
8. Verify resource, application, dependency, and business outcomes.
9. Preserve rollback artifacts and reconcile drift.

# Failure-domain map

| Observation | Inspect |
| --- | --- |
| Artifact cannot launch or pull | identity, Region, architecture, permission, KMS, network |
| IaC operation fails | first failed resource, execution principal, replacement and state |
| Only some account/Region targets fail | target parameters, SCP/IAM/KMS, local quota/capacity |
| Rollout stalls | health, readiness, surge capacity, subnet IPs, mixed-version compatibility |
| Fleet automation misses nodes | SSM Agent, identity, Region, endpoints, target resolution |
| Event automation duplicates effects | delivery semantics, idempotency, retry, loop guard |

# Safety invariants

Do not retry permanent errors blindly, do not delete stateful evidence to force success, do not deploy a moving artifact reference, and do not equate orchestration success with application success.

# Related concepts

- [Deployment diagnostics](deployment-diagnostics.md)
- [Deployment strategies](deployment-strategies.md)
- [Operational automation](operational-automation.md)
- [Event-driven automation](event-driven-automation.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.4](../../raw/skills/3.1.4-provision-and-share-resources-across-regions-and-accounts.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
- [Skill 3.1.6](../../raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md)
- [Skill 3.2.1](../../raw/skills/3.2.1-automate-operational-processes-with-services.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
