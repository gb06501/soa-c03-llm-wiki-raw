---
type: Concept
title: Security findings
description: Normalizes detection evidence into a risk-ranked workflow for investigation, containment, remediation, and verified closure.
tags: ["soa-c03", "domain-4", "security-findings", "triage"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

A finding is a claim about a resource at a time. It is neither proof of compromise nor proof that the issue still exists. Preserve the source-service identity and evidence.

# Source boundaries

| Source | Primary evidence |
| --- | --- |
| Security Hub CSPM | Aggregated findings and control evaluations |
| GuardDuty | Suspicious or malicious activity |
| Inspector | Software vulnerabilities and exposure context |
| Config | Resource-state compliance |
| Macie | Sensitive data in S3 |
| Security Agent | Agent-assisted application-security analysis |

# Risk priority

Combine provider severity with exploitability, exposure, asset criticality, data sensitivity, privilege, scope, age, and fix availability. A lower provider severity on a public privileged path can outrank a higher isolated finding.

# Workflow

1. Validate scope, freshness, and source evidence.
2. Correlate duplicate or related findings.
3. Assign an owner and urgency.
4. Contain with the smallest reversible action.
5. Remediate the root condition through controlled change.
6. Re-evaluate at the source and verify workload health.
7. Close, suppress, or accept risk with evidence and expiry.

# Related pages

- [Security Hub CSPM](../services/security-hub-cspm.md)
- [Security finding triage](../decision-guides/security-finding-triage.md)
- [Security finding remediation](../playbooks/security-finding-remediation.md)

# Sources

- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
