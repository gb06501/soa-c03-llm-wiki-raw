---
type: Concept
title: AMI and container image management
description: Builds, distributes, secures, verifies, and safely retires EC2 AMIs and ECR container images.
tags: [soa-c03, domain-3, ami, ecr, image-builder]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
status: verified
---

# Core model

```text
trusted base -> build and patch -> test and scan -> distribute -> deploy -> retain rollback -> retire
```

An AMI packages EC2 boot volumes and metadata. An ECR image packages container layers and a manifest. Both require a compatible runtime and an independently verified release reference.

# Object model

| Need | AMI path | Container path |
| --- | --- | --- |
| Build definition | Image Builder image recipe and components | Container recipe/build definition |
| Identity | Region-specific AMI ID | Repository plus immutable digest |
| Readable release label | AMI name/tags | ECR tag |
| Distribution | AMI copy/share and Image Builder distribution | ECR replication and repository policy |
| Runtime compatibility | architecture, boot mode, drivers, instance type | manifest platform and task/node architecture |

# Control boundaries

- AMI sharing grants use of the source image; copying creates a new destination image and snapshots.
- Encrypted cross-account AMI use also needs customer-managed KMS permission.
- A mutable ECR tag can move; a digest pins exact content.
- Registry authentication, repository authorization, KMS access, and the private network path are separate gates.
- Image scan findings do not block deployment unless a pipeline or policy enforces that decision.
- Lifecycle retirement must preserve every artifact still required for rollback or future scaling.

# Evidence

Use Image Builder phase/component logs, AMI copy state, launch reason, ECR authentication and pull errors, scan findings, replication state, and runtime architecture errors.

# Failure modes

Wrong Region or architecture, missing launch/snapshot/KMS permission, inconsistent no-reboot capture, Image Builder component failure, absent ECR API/DKR/S3 network path, lifecycle deletion, or a tag that moved unexpectedly.

# Related concepts

- [Image selection](/decision-guides/machine-container-image-selection.md)
- [Image build and distribution failure](/playbooks/image-build-distribution-failure.md)
- [Deployment strategies](/concepts/deployment-strategies.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
