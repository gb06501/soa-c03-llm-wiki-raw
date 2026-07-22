---
type: AWS Service
title: DynamoDB
service_id: dynamodb
description: Provides managed NoSQL storage with service encryption and optional customer-managed KMS control.
tags: ["soa-c03", "domain-4", "dynamodb", "encryption-at-rest", domain-5, gateway-endpoint, network-cost]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["4.2.2", "5.1.2", "5.1.4", "1.2.1", "2.1.2", "2.1.3", "2.2.2", "2.3.1", "2.3.2", "2.3.4"]
domain_ids: ["4", "5", "1", "2"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.1-automate-snapshots-and-backups.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
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

# Domain 5: Gateway endpoint access

A DynamoDB gateway endpoint installs service prefix-list routes into associated route tables. It has no endpoint ENI or security group. Endpoint policy restricts use but does not grant identity or table permission.

Use the endpoint for supported private regional traffic and to avoid NAT processing. Verify route-table association, selected prefix-list route, DNS/Region, endpoint policy, IAM/table/KMS authorization, and application result.

- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [Network cost optimization](../decision-guides/network-cost-optimization.md)

# Corpus reconciliation: Domains 1 and 2

## Capacity, caching, and hot partitions

On-demand and provisioned modes address different demand predictability. Auto scaling is reactive and bounded. Low table utilization can coexist with throttling when a key or index is hot. DAX accelerates repeated eventually consistent reads; it does not add write capacity.

## Backup, restore, and global tables

Point-in-time, on-demand, and Backup recovery create a new table. Restore does not automatically recreate every stream, mapping, alarm, scaling, TTL, or application reference. Global tables provide multi-Region replicas and are not a substitute for backup.

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 2.1.2](../../raw/skills/2.1.2-implement-caching-for-dynamic-scalability.md)
- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.1](../../raw/skills/2.3.1-automate-snapshots-and-backups.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
