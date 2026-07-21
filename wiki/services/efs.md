---
type: AWS Service
title: EFS
service_id: efs
description: Provides managed shared file storage with KMS encryption at rest and optional TLS in transit.
tags: ["soa-c03", "domain-4", "efs", "encryption"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.2", "4.2.3"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
status: verified
---
# Core model

EFS separates file-system encryption at rest from client-to-mount-target encryption in transit. Mount-target networking and IAM/file permissions remain additional access layers.

# Decision boundaries

At-rest encryption and key selection are creation-time architectural choices. Use the TLS mount helper when the client path requires encryption in transit. TLS does not correct route, security-group, DNS, or NFS permission problems.

# Evidence and diagnosis

Check file-system encryption and key, mount-target AZ and security group, DNS resolution, NFS port reachability, mount-helper TLS options, IAM authorization, and POSIX identity.

# Safe operations

Select keys before creation, test mounts from each required subnet, use TLS consistently, monitor key lifecycle, and validate application I/O after remount or migration.

# Related decisions

- [Encryption at rest selection](../decision-guides/encryption-at-rest-selection.md)
- [TLS connectivity failure](../playbooks/tls-connectivity-failure.md)

# Sources

- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
