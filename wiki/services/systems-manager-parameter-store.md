---
type: AWS Feature
title: Systems Manager Parameter Store
parent_services: [Systems Manager]
description: Stores hierarchical configuration and encrypted SecureString values without a managed secret-rotation lifecycle.
tags: ["soa-c03", "domain-4", "systems-manager", "parameter-store"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.4"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
status: verified
---
# Parent service

[Systems Manager](systems-manager.md)

# Core model

Parameter Store holds versioned String, StringList, and SecureString parameters in a hierarchy. SecureString uses KMS; parameter authorization and key authorization are separate.

# Decision boundaries

Use Parameter Store when hierarchical configuration, version labels, and parameter policies meet the need. Use Secrets Manager when the workflow requires managed secret rotation and secret-specific staging labels.

# Evidence and diagnosis

Check parameter name and Region, version or label, type, caller policy, KMS key policy, endpoint policy, decryption flag, network path, and CloudTrail request.

# Safe operations

Retrieve at runtime through a workload role, keep sensitive values out of logs and templates, constrain path-based permissions, protect the KMS key, and build an explicit rotation workflow when required.

# Related decisions

- [Secrets storage selection](../decision-guides/secrets-storage-selection.md)
- [Secret access and rotation failure](../playbooks/secret-access-and-rotation-failure.md)

# Sources

- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
