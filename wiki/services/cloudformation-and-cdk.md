---
type: Concept
title: CloudFormation and AWS CDK lifecycle
description: Explains declarative resource ownership, change preview, replacement protection, CDK synthesis, and governed products.
tags: [soa-c03, domain-3, cloudformation, cdk, iac]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.2"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
status: verified
---

# Core model

```text
template or CDK app -> synthesized template -> change set or diff -> stack operation -> physical resources
```

CloudFormation owns the declared resource lifecycle. CDK produces CloudFormation templates and stages assets; it does not replace CloudFormation update and rollback behavior.

# Important objects

| Object | Decision value |
| --- | --- |
| Parameter, mapping, condition | deployment input, static lookup, conditional creation/value |
| Logical ID and physical ID | template identity versus real AWS resource |
| Ref and GetAtt | main identifier versus named resource attribute |
| Change set | previews add, modify, remove, and replacement actions |
| DeletionPolicy | controls removal during stack deletion/template removal |
| UpdateReplacePolicy | controls the old resource after replacement |
| Stack policy / termination protection | constrain updates / stack deletion |
| CDK app, stack, construct, asset | code hierarchy and deployable artifacts |
| Service Catalog portfolio/product | approved self-service infrastructure |

# Safe lifecycle

Validate or synthesize, inspect the diff/change set, identify stateful replacements, preserve data, deploy, follow stack events, validate the application, and detect drift.

# Boundaries

- References normally create dependencies; use `DependsOn` only when no reference expresses the required ordering.
- `NoEcho` masks ordinary display; it is not encryption.
- IAM capability acknowledgement does not grant missing IAM permission.
- Drift detection reports supported differences but does not repair them.
- An imported resource is adopted, not recreated.
- CDK bootstrap prepares each target account/Region for roles and asset storage.

# Related concepts

- [Infrastructure provisioning selection](/decision-guides/infrastructure-provisioning-selection.md)
- [CloudFormation deployment failure](/playbooks/cloudformation-deployment-failure.md)
- [Deployment diagnostics](/concepts/deployment-diagnostics.md)

# Sources

- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
