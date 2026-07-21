---
type: Decision Guide
title: AMI and container image selection
description: Chooses image identity, distribution, security, and lifecycle controls from release and runtime clues.
tags: [soa-c03, domain-3, images]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
status: verified
---

# Decision table

| Scenario clue | Required property | Select |
| --- | --- | --- |
| Reusable EC2 operating system and packages | bootable block volumes and EC2 metadata | AMI |
| Reusable application filesystem layers | container runtime artifact | ECR container image |
| Exact reproducible container release | immutable content identity | image digest |
| Readable tag must never be reused | protected label | ECR tag immutability |
| Same AMI usable from another account | source ownership retained | AMI share plus snapshot and KMS permission |
| Independent image in another Region/account | destination ownership and ID | AMI copy or Image Builder distribution |
| Private pull without internet | ECR API/registry and layer path | ECR endpoints plus S3 path or NAT |
| Multiple CPU platforms | platform-specific manifests | multi-architecture image index |

# Rejection rules

- Do not use one hard-coded AMI ID across Regions.
- Do not treat an ECR tag as immutable content identity.
- Do not assume scan findings enforce a deployment block.
- Do not expire an artifact still needed for rollback or scale-out.

# Verification

Confirm the selected object, identity, permission path, scope, and observable outcome. Preserve the prior safe state when the change can replace or retire resources.

# Related concepts

- [Image management](/services/image-management.md)
- [Image failure playbook](/playbooks/image-build-distribution-failure.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
