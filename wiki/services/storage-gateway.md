---
type: AWS Service
title: Storage Gateway
service_id: storage-gateway
description: Provides hybrid file, volume, or tape access patterns backed by AWS storage.
tags: ["soa-c03", "domain-1", "storage-gateway", "hybrid-storage"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.4"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
status: verified
---

# Core model

`on-premises client -> gateway protocol surface -> local cache/buffer -> AWS-backed storage`

File, Volume, and Tape Gateway address different hybrid protocols. Storage Gateway is not a general substitute for EFS, FSx, S3 object access, or S3 Files inside AWS.

# Evidence and failure modes

Check gateway health, activation, network path, protocol, local cache or upload buffer, permissions, backing storage, and client evidence.

# Sources

- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
