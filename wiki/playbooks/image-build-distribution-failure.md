---
type: Troubleshooting Playbook
title: Image build and distribution failure
description: Diagnoses AMI creation, Image Builder, ECR push and pull, replication, and runtime compatibility failures.
tags: [soa-c03, domain-3, images, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.1"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
status: verified
---

# Trigger

An AMI or container image fails to build, distribute, launch, pull, scan, or remain available for rollback.

# Evidence path

1. Identify AMI, Image Builder, ECR, or runtime as the failing layer.
2. Check Region/account, immutable identity, architecture, and lifecycle state.
3. Read the first failed Image Builder component or AMI copy/launch reason.
4. Trace authentication, repository/snapshot policy, execution role, and KMS access.
5. For private pulls, verify DNS, ECR API/DKR, S3 layer path, endpoints or NAT.
6. Inspect runtime entrypoint, configuration, secret, and health evidence after a successful pull.

# Failure map

| Symptom | Direction |
| --- | --- |
| AMI not found | Region, ID, owner, deregistration |
| AMI launch denied | launch, snapshot, and KMS permission |
| Image Builder failed | first component, role, network, package source, disk |
| Container pull denied | registry auth, pull principal, repository/KMS policy |
| Pull timeout | DNS, endpoint/NAT, SG/NACL, S3 path |
| Exec-format error | image/runtime architecture |
| Rollback image missing | lifecycle policy or replication scope |

# Safe action

Repair the narrow failed gate, rebuild from the controlled recipe, publish a new immutable identity, and keep the known-good artifact. Do not overwrite evidence or reuse a mutable release tag.

# Verification

Launch or pull by exact identity in every required account/Region, pass tests and scans, observe healthy runtime behavior, confirm replication, and prove the retained rollback artifact remains usable.

# Related concepts

- [Image management](/services/image-management.md)
- [Image selection](/decision-guides/machine-container-image-selection.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
