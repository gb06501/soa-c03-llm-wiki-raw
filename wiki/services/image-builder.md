---
type: AWS Service
title: Image Builder
service_id: image-builder
description: Builds, tests, scans, distributes, and records reusable AMI and container image artifacts.
tags: [soa-c03, domain-3, image-builder, images]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
status: verified
---

# Core model

```text
pipeline -> recipe -> build components -> image -> test components -> distribution
                 \-> infrastructure configuration
                 \-> distribution configuration
```

# Objects and controls

| Object | Controls |
| --- | --- |
| Image or container recipe | base image, version, components, block or container settings |
| Component | ordered build or test steps |
| Infrastructure configuration | instance profile, instance type, subnet, security group, logs |
| Distribution configuration | Regions, accounts, naming, permissions, encryption |
| Pipeline | schedule or manual execution and dependency behavior |

A failed build or test should prevent distribution. The output identity and lineage must be recorded before downstream deployment.

# Evidence and failure boundaries

Start with pipeline execution, phase, and first failed component. Then inspect the temporary build/test instance, instance profile, package source, network path, disk, logs, output image, and per-destination distribution status.

Distribution failures commonly belong to target roles, account policy, KMS permission, Region support, or quota—not the build step.

# Safe lifecycle

Use a trusted base, patch and harden through versioned components, test and scan, distribute only after success, deploy by immutable identity, retain the previous artifact, and retire only after dependency review.

# Related concepts

- [Image-management lifecycle](image-management.md)
- [Image build and distribution failure](../playbooks/image-build-distribution-failure.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
