---
type: AWS Service
title: FSx
service_id: fsx
description: Provides managed file-system products with service-specific encryption and network access controls.
tags: ["soa-c03", "domain-4", "fsx", "encryption-at-rest"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
status: verified
---
# Core model

FSx products encrypt managed file-system storage and integrate with KMS according to the selected product and lifecycle. Client protocol, identity, directory, network, and backup controls remain separate.

# Decision boundaries

Choose the FSx product for workload protocol and operational requirements before choosing key ownership. A customer managed key adds policy and lifecycle control but also an availability dependency.

# Evidence and diagnosis

Check product, Region, file-system encryption key, key state and policy, subnet and security groups, directory or client identity, backup encryption, and restore behavior.

# Safe operations

Protect in-use keys, validate backups and restores, test client access after policy changes, and perform migrations through a rehearsed copy and cutover plan.

# Related decisions

- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [KMS access failure](../playbooks/kms-access-failure.md)

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
