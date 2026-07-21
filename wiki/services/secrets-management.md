---
type: Concept
title: Secrets management
description: Separates secret lifecycle, runtime delivery, KMS authorization, rotation, and workload identity.
tags: ["soa-c03", "domain-4", "secrets", "credentials"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---
# Core model

A secret is sensitive configuration with an owner, consumer, version, rotation policy, retrieval path, audit trail, and revocation plan.

# Storage boundary

Use Secrets Manager for secret-specific versions, staging labels, resource policies, and managed rotation workflows. Use Systems Manager Parameter Store for hierarchical configuration and SecureString values when managed rotation is not required. KMS protects secret material but is not a secret database.

# Delivery boundary

Runtime retrieval through a workload role reduces static exposure and supports caching and version control. Deployment-time injection can expose values in environment, orchestration state, logs, or long-lived containers; understand the service behavior.

# Rotation invariant

The new credential, target system, application consumers, and staging labels must agree. Rotation success is not proven until a new connection succeeds and rollback remains possible.

# Related pages

- [Secrets Manager](secrets-manager.md)
- [Systems Manager Parameter Store](systems-manager-parameter-store.md)
- [Secrets storage selection](../decision-guides/secrets-storage-selection.md)

# Sources

- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
