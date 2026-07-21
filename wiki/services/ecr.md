---
type: AWS Service
title: ECR
service_id: ecr
description: Stores, secures, scans, replicates, and retires container images by repository, tag, and digest.
tags: [soa-c03, domain-3, ecr, containers]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.1", "3.1.3", "3.1.5"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.1-create-and-manage-amis-and-container-images.md
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
  - /raw/skills/3.1.5-implement-deployment-strategies-and-services.md
status: verified
---

# Core model

```text
registry -> repository -> manifest -> layers
                         -> movable tag
                         -> immutable digest
```

# Configuration surfaces

Repository policy controls cross-account access. Tag immutability prevents accidental label reuse. Scanning produces vulnerability findings; it does not block deployment without enforcement. Lifecycle rules expire images by tag state, prefix or pattern, count, age, and priority. Replication copies eligible images to configured accounts or Regions.

# Pull permission and network path

```text
registry authentication
  + pull principal identity
  + repository policy
  + KMS permission
  + ECR API/DKR, DNS, and S3 layer path
  = successful pull
```

The ECS task execution role or compute/node role normally performs the pull; that is separate from the application task role.

# Deployment safety

Pin deployments to a digest when exact reproducibility matters. Keep every digest required for rollback and future scale-out. Verify replicated content at the destination rather than assuming the rule copied old or out-of-scope images.

# Evidence

Use authentication errors, repository and KMS denials, image/tag/digest lookup, lifecycle preview and history, replication status, pull timeout evidence, scan findings, and runtime architecture or entrypoint errors.

# Related concepts

- [Image selection](/decision-guides/machine-container-image-selection.md)
- [Deployment rollback](/playbooks/deployment-rollback.md)

# Sources

- [Skill 3.1.1](../../raw/skills/3.1.1-create-and-manage-amis-and-container-images.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
- [Skill 3.1.5](../../raw/skills/3.1.5-implement-deployment-strategies-and-services.md)
