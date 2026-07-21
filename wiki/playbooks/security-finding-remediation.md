---
type: Troubleshooting Playbook
title: Security finding remediation
description: Validates, prioritizes, contains, remediates, and closes findings without losing evidence or disrupting recovery.
tags: ["soa-c03", "domain-4", "troubleshooting", "security-findings", "remediation"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.4", "4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---

# Trigger

Trusted Advisor, Security Hub CSPM, GuardDuty, Inspector, Config, Macie, or Security Agent reports a security issue requiring investigation or remediation.

# Evidence path

1. Capture source service, finding ID, account, Region, resource ARN, first/last observed time, severity, and raw evidence.
2. Confirm the source is enabled and the finding is current.
3. Correlate related findings without discarding source records.
4. Assess exploitability, exposure, criticality, data, privilege, scope, age, and fix availability.
5. Identify resource owner, deployment source of truth, and business dependency.
6. Preserve relevant CloudTrail, configuration, network, workload, and artifact evidence.
7. Choose containment and remediation separately.
8. Re-query the source after the controlled change.

# Failure map

| Symptom | Direction |
| --- | --- |
| Finding only in hub | inspect source product and regional integration |
| High severity, weak context | enrich asset, exposure, privilege, exploitability |
| Closed then returns | root configuration or deployment pipeline not fixed |
| Remediation breaks workload | missing dependency, health gate, or rollback |
| Finding persists after patch | wrong artifact/resource, stale scan, incomplete rollout |
| Excess noise | correlation, identifier tuning, documented scoped suppression |

# Safe action

Contain with the smallest reversible control, then remediate through the owning configuration or deployment path. Bound automation by exact finding type, resource, state, approval, idempotence, rollback, and verification.

# Verification

Confirm the source finding resolves or changes as expected, the unsafe behavior is gone, required workload behavior remains healthy, and workflow state, owner, and evidence are updated.

# Rollback

Undo the remediation through the source of truth if business impact exceeds the accepted risk, retain containment where safe, and reopen the finding with explicit residual risk.

# Escalation

Provide source finding, evidence bundle, priority rationale, owner, containment, remediation diff, verification, and rollback state.

# Related pages

- [Security findings](../concepts/security-findings.md)
- [Security finding triage](../decision-guides/security-finding-triage.md)

# Sources

- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
