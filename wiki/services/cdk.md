---
type: AWS Service
title: CDK
service_id: cdk
description: Defines infrastructure with constructs, synthesizes CloudFormation, publishes assets, and deploys through stack lifecycle controls.
tags: [soa-c03, domain-3, cdk, iac]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.2", "3.1.3"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
status: verified
---

# Core model

```text
app -> stack -> constructs -> synth template -> publish assets -> CloudFormation deploy
```

# Commands and objects

| Command or object | Purpose |
| --- | --- |
| bootstrap | prepare target account/Region roles and asset stores |
| synth | generate CloudFormation template |
| diff | preview proposed deployed-template differences |
| deploy | publish assets and run CloudFormation |
| app / stack / construct | code hierarchy |
| file or image asset | staged S3 or ECR deployment input |

L1 constructs closely expose CloudFormation resources. L2 constructs add service-oriented defaults and methods. L3 constructs are opinionated patterns.

# Failure boundaries

A synth failure points to application code, context, dependency, or lookup. An asset publication failure points to bootstrap resources, credentials, role, network, S3, or ECR. A stack failure belongs in CloudFormation events.

Cached context can be stale, and account/Region lookups require the intended environment and credentials. An unresolved token cannot always be consumed as an ordinary synthesis-time string.

# Safety

Bootstrap every required target environment with deliberate trust. Review `diff`, inspect replacements, deploy, validate the application, and correct drift through code.

# Related concepts

- [CloudFormation](cloudformation.md)
- [Infrastructure provisioning selection](../decision-guides/infrastructure-provisioning-selection.md)

# Sources

- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
