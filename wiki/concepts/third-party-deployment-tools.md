---
type: Concept
title: Terraform and Git deployment controls
description: Explains Terraform configuration, state, plan, locking, ownership, and reviewed Git release identity.
tags: [soa-c03, domain-3, terraform, git, state]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.6"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md
status: verified
---

# Core model

```text
configuration = desired resources
state = Terraform mapping and known attributes
AWS = real resources
plan = proposed reconciliation
```

A safe apply begins by verifying repository commit, backend, workspace, provider account, and Region.

# Terraform lifecycle

Initialize backend/providers/modules, format and validate, create a plan, review destructive and replacement actions, apply the reviewed plan, verify AWS and the application, then protect updated state.

# State controls

Remote state should be durable, encrypted, least-privilege, versioned or backed up, audited, and locked where supported. State can contain sensitive values. Never commit state or saved sensitive plans to Git.

An apply can partially succeed and has no universal rollback. Read the error, refresh evidence, and plan again before retrying. Force-unlock only after proving the original operation is gone.

# Ownership

One tool should own each resource or property. Use data sources, outputs, or imported identifiers to consume resources owned elsewhere. Import attaches an existing resource to state; the next plan still decides whether configuration matches.

# Git release boundary

A branch can move. A commit or controlled tag identifies the reviewed release. Resolve merge conflicts deliberately, rerun validation and plan, and rotate any committed secret before considering history cleanup.

# Related concepts

- [Deployment tool selection](../decision-guides/deployment-tool-selection.md)
- [Third-party deployment failure](../playbooks/third-party-deployment-failure.md)
- [CloudFormation lifecycle](../services/cloudformation-and-cdk.md)

# Sources

- [Skill 3.1.6](../../raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md)
