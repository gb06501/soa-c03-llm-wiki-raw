---
type: AWS Service
title: Security Agent
service_id: security-agent
description: Assists with application-security analysis and reports findings that still require human validation and controlled remediation.
tags: ["soa-c03", "domain-4", "security-agent", "application-security"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

Security Agent analyzes supported application context and proposes security findings or remediation guidance. Its output is evidence to validate, not an autonomous authorization to change production.

# Decision boundaries

Use agent-assisted analysis to accelerate investigation and explanation. Preserve source context, reproduce the issue, and apply the same ownership, review, least-privilege, and verification controls used for other security findings.

# Evidence and diagnosis

Record the analyzed resource or code version, finding rationale, affected path, confidence, suggested change, test evidence, and any unsupported assumptions.

# Safe operations

Protect proprietary inputs, limit repository and workload permissions, require review for changes, validate with deterministic tests or source-service evidence, and track false-positive or suppression decisions.

# Related decisions

- [Security findings](../concepts/security-findings.md)
- [Security finding triage](../decision-guides/security-finding-triage.md)

# Sources

- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
