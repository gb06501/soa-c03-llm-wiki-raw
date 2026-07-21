---
type: AWS Service
title: CloudTrail
service_id: cloudtrail
description: Records AWS control-plane and selected data-plane activity for audit and access diagnosis.
tags: ["soa-c03", "domain-4", "cloudtrail", "audit"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["4.1.2", "4.1.3", "4.1.4", "4.2.4", "1.1.1", "1.2.1", "2.1.1"]
domain_ids: ["4", "1", "2"]
sources:
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md
status: verified
---
# Core model

CloudTrail records who called which API, when, from where, against which resource, with what request parameters, and with what outcome. Event history is not a substitute for a durable multi-Region trail and does not include every data event by default.

# Evidence model

| Field | Diagnostic use |
| --- | --- |
| userIdentity / session context | Actual principal and assumed-role chain |
| eventName and eventSource | Exact action and service |
| requestParameters | Target resource and supplied configuration |
| sourceIPAddress / userAgent | Request origin and client |
| errorCode / errorMessage | Service-side denial or validation outcome |

# Decision boundaries

Enable the event classes required by the evidence objective. Management events cover control-plane operations; selected data events cover high-volume resource access such as S3 object operations.

# Safe operations

Centralize organization trails in a protected log archive, encrypt and validate logs, restrict mutation, monitor trail changes, and define retention that meets investigation and compliance needs.

# Related decisions

- [Access denial evidence selection](../decision-guides/access-denial-evidence-selection.md)
- [Multi-account security governance](../concepts/multi-account-security-governance.md)

# Corpus reconciliation: Domains 1 and 2

## Change evidence

Use CloudTrail when the question is who changed an AWS resource, which API request failed, or whether scaling configuration changed. It does not explain CPU, memory, query waits, or application errors without correlated service evidence.

# Sources

- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
- [Skill 1.1.1](../../raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md)
- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 2.1.1](../../raw/skills/2.1.1-configure-and-manage-scaling-mechanisms-in-compute-environments.md)
