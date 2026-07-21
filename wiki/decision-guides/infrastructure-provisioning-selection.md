---
type: Decision Guide
title: Infrastructure provisioning selection
description: Selects CloudFormation, CDK, Service Catalog, and lifecycle controls from infrastructure requirements.
tags: [soa-c03, domain-3, cloudformation, cdk]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Declarative native resource lifecycle | template to managed stack | CloudFormation |
| Higher-level code constructs | synthesize to CloudFormation | AWS CDK |
| Approved self-service products | central portfolio and constrained launch | Service Catalog |
| Preview risky update | add/modify/remove/replace view | change set or CDK diff |
| Protect resource on stack deletion | deletion lifecycle | DeletionPolicy |
| Protect old resource on replacement | replacement lifecycle | UpdateReplacePolicy |
| Adopt supported existing object | managed identity without recreation | resource import |
| Detect supported manual changes | desired versus actual comparison | drift detection |

# Rejection rules

- Do not use mappings for live dynamic service data.
- Do not use NoEcho as encryption.
- Do not confuse nested stacks with StackSets.
- Do not assume change preview proves application success.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [CloudFormation and CDK](/services/cloudformation-and-cdk.md)
- [CloudFormation failure](/playbooks/cloudformation-deployment-failure.md)

# Sources

- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
