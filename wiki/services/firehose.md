---
type: AWS Service
title: Firehose
service_id: firehose
description: Buffers, optionally transforms, and delivers streaming records to supported storage and analysis destinations.
tags: ["soa-c03", "domain-5", "firehose", "log-delivery"]
timestamp: 2026-07-22T05:15:00Z
skill_ids: ["5.1.3", "5.3.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---
# Core model

Firehose accepts streaming records, buffers and optionally transforms or compresses them, then delivers them to a supported destination. It transports data; it does not analyze that data. Source integration, delivery configuration, IAM/KMS permission, transformation, and destination health are separate failure layers.

# Decision boundaries

Use Firehose when the source integration and delivery destination require managed streaming delivery. Use direct CloudWatch Logs or S3 delivery when that simpler path meets investigation and retention needs.

# Evidence and diagnosis

Inspect source logging configuration, delivery stream state, destination, role and resource policies, KMS key, transformation errors, backup/error prefix, delivery metrics, and destination object arrival.

# Safe operations

Test a known event, verify timestamps and fields at the destination, protect sensitive metadata, alarm on delivery failures, retain failed records, and change buffering or transformations without losing the original evidence.

# Related decisions

- [Network log selection](../decision-guides/network-log-selection.md)
- [Network protection gap](../playbooks/network-protection-gap.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
