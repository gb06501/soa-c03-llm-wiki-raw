---
type: AWS Service
title: SES
service_id: ses
description: Sends application-formatted email when an application or workflow controls message content and delivery.
tags: ["soa-c03", "domain-1", "ses", "email"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["1.1.5"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md
status: verified
---

# Core model

`application or workflow -> SES send request -> identity and policy checks -> mail delivery evidence`

Choose SNS for direct alarm fan-out and SES when application-controlled email content is required. SES is not a direct CloudWatch alarm action.

# Evidence and failure modes

Check sending identity, request permission, Region, message construction, suppression or delivery evidence, and application execution.

# Sources

- [Skill 1.1.5](../../raw/skills/1.1.5-configure-sns-notifications-and-alarm-integration.md)
