---
type: AWS Service
title: DynamoDB
service_id: dynamodb
description: Provides managed NoSQL storage with service encryption and optional customer-managed KMS control.
tags: ["soa-c03", "domain-4", "dynamodb", "encryption-at-rest"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.2"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
status: verified
---
# Core model

DynamoDB encrypts table data at rest. Key choice changes control, policy, audit, and operational dependency, while table access and KMS key access remain distinct authorization paths.

# Decision boundaries

Use service-owned or managed encryption when default operational simplicity meets requirements. Use a customer managed key when key policy, separation, lifecycle, or cross-account controls require direct ownership. DAX has its own encryption and lifecycle considerations.

# Evidence and diagnosis

Check table Region, encryption status, key ARN and state, key policy/grants, caller and service principal, SCP, throttling or access error, and CloudTrail KMS evidence.

# Safe operations

Avoid disabling or scheduling deletion of an in-use key, test restore and replication workflows, monitor key changes, and stage key migration with a rollback plan.

# Related decisions

- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [KMS access failure](../playbooks/kms-access-failure.md)

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
