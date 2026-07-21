---
type: AWS Service
title: Security Hub CSPM
service_id: security-hub-cspm
description: Aggregates standardized security findings and evaluates security controls across accounts and Regions.
tags: ["soa-c03", "domain-4", "security-hub", "findings"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

Security Hub CSPM evaluates enabled standards and controls and aggregates findings from integrated security products. A finding is a record with product, resource, severity, workflow state, record state, timestamps, and remediation context.

# Decision boundaries

The hub normalizes and routes evidence; it does not replace the source service or automatically prove remediation. Severity is one prioritization input, not a complete risk decision.

# Multi-account model

Use a delegated administrator, define member and Region coverage, centralize findings, and preserve account/Region ownership for remediation. Aggregation must not hide a disabled source or missing regional enablement.

# Evidence and diagnosis

Inspect product fields, resource ARN, first and last observed times, severity, workflow status, record state, compliance status, source-service evidence, and automation history.

# Safe operations

Deduplicate related findings, enrich with asset and data criticality, route through EventBridge, contain before destructive changes, update workflow state only after verification, and document suppression.

# Related decisions

- [Security finding triage](../decision-guides/security-finding-triage.md)
- [Security finding remediation](../playbooks/security-finding-remediation.md)

# Sources

- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
