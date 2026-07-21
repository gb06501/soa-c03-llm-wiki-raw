---
type: AWS Service
title: GuardDuty
service_id: guardduty
description: Detects suspicious activity and threats from AWS telemetry without becoming the source log repository.
tags: ["soa-c03", "domain-4", "guardduty", "threat-detection"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

GuardDuty analyzes supported AWS telemetry and produces threat findings. The finding explains the suspected behavior, affected resource, severity, and evidence summary; the underlying source telemetry remains distinct.

# Decision boundaries

Use GuardDuty for threat detection, not configuration compliance, data classification, or software-vulnerability inventory. A high-severity finding requires context about exposure, criticality, privilege, and correlated activity.

# Evidence and diagnosis

Validate detector, protection plan, account and Region coverage, finding type, resource role, actor details, network or API evidence, timestamps, and whether the activity is expected.

# Safe operations

Use delegated administration, route findings centrally, preserve evidence, contain compromised identities or resources with bounded actions, rotate credentials when justified, and verify activity stops.

# Related decisions

- [Security findings](../concepts/security-findings.md)
- [Security finding triage](../decision-guides/security-finding-triage.md)

# Sources

- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
