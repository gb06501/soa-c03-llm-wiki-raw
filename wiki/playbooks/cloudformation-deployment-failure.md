---
type: Troubleshooting Playbook
title: CloudFormation deployment failure
description: Recovers failed CloudFormation or CDK changes from first resource evidence through stable rollback and validation.
tags: [soa-c03, domain-3, cloudformation, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
status: verified
---

# Trigger

A stack or CDK deployment fails, rolls back, replaces an unexpected resource, or cannot delete or update safely.

# Evidence path

1. Capture the template, parameters, CDK diff or change set.
2. Find the earliest failed logical resource and exact status reason.
3. Follow nested-stack failures into the child stack.
4. Identify caller, execution role, PassRole, resource-policy, or KMS gate.
5. Inspect replacement, deletion policies, quota, capacity, subnet IP, and Region-specific input.
6. If CDK failed before stack creation, inspect bootstrap and asset publication.

# Failure map

| Symptom | Direction |
| --- | --- |
| Unexpected replacement | changed property and change-set replacement flag |
| Stack action denied | caller, execution role, PassRole, capability, stack policy |
| Secret/key denied | execution role, secret policy, KMS |
| Export update blocked | active importer |
| CDK pre-stack failure | bootstrap role, asset bucket/ECR, network |
| Delete failed | protection, dependency, nonempty/stateful resource |
| Drift found | out-of-band supported-property change |

# Safe action

Preserve state, correct code or the proven permission/dependency, apply DeletionPolicy and UpdateReplacePolicy where needed, finish rollback, regenerate the preview, and deploy through the owning tool.

# Verification

Reach a stable stack status, confirm intended physical resources and retained data, validate the application and dependencies, rerun drift detection, and ensure the next preview is clean.

# Related concepts

- [CloudFormation and CDK](/services/cloudformation-and-cdk.md)
- [Deployment diagnostics](/concepts/deployment-diagnostics.md)

# Sources

- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
