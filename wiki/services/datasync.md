---
type: AWS Service
title: DataSync
service_id: datasync
description: Runs managed storage-transfer tasks with explicit source, destination, options, scheduling, and execution evidence.
tags: ["soa-c03", "domain-1", "datasync", "storage-transfer"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.3"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
status: verified
---

# Core model

`source location -> agent when required -> task options -> destination -> execution and verification`

Use DataSync for managed on-premises-to-AWS or AWS-storage movement. Multipart client uploads and Transfer Acceleration solve different S3 transfer paths.

# Evidence and failure modes

Check location reachability, agent health, permissions, task options, include/exclude rules, destination capacity, execution status, errors, and transferred-object verification.

# Sources

- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
