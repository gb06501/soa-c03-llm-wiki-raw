---
type: AWS Feature
title: S3 Files
parent_services: ["S3"]
description: Exposes data retained in S3 through file-oriented access for applications that require file semantics.
tags: ["soa-c03", "domain-1", "s3", "files", "shared-storage"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.3.4"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
status: verified
---

# Core model

`S3 bucket data -> S3 file-system surface -> mount target and client -> file operations`

Choose it when data belongs in S3 and the application needs file access. Compare protocol, latency, throughput, filesystem semantics, identity, and availability with EFS and the correct FSx family.

# Evidence and failure modes

Check file-system and mount-target state, bucket and IAM access, subnet, security groups, DNS, client, mount evidence, CloudWatch health, and object/file behavior.

# Sources

- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
