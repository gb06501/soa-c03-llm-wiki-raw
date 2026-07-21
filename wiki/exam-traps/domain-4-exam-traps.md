---
type: Exam Trap
title: Domain 4 exam traps
description: Corrects tempting security, identity, compliance, encryption, secrets, and finding-response misconceptions.
tags: ["soa-c03", "domain-4", "exam-traps"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.1.1", "4.1.2", "4.1.3", "4.1.4", "4.1.5", "4.2.1", "4.2.2", "4.2.3", "4.2.4", "4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.1.1-implement-iam-features.md
  - /raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md
  - /raw/skills/4.1.3-implement-secure-multi-account-strategies.md
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
  - /raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md
  - /raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md
  - /raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/4.2.4-securely-store-secrets-by-using-services.md
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---

# IAM and access

- Authentication proves identity; authorization evaluates the request.
- A role trust policy permits assumption but does not grant workload actions.
- `iam:PassRole` passes a role to a service; it does not assume the role.
- Permissions boundaries and SCPs limit permissions; neither grants an allow.
- Explicit deny wins across applicable policy types.
- Diagnose the assumed-role session ARN, not only the friendly role name.
- Resource and KMS policies can deny an IAM-allowed request.
- Last-accessed evidence shows observed use, not every future requirement.

# Multi-account governance

- The Organizations management account is not the normal workload account.
- An SCP allow list requires an allowed path at every inherited level.
- Central aggregation does not enable a service in missing accounts or Regions.
- Config detection is not prevention.
- A landing zone can drift and still requires operating ownership.
- Delegated administration does not erase member-account or regional scope.

# Trusted Advisor and compliance

- A check can be stale; verify the current resource before remediation.
- Excluding a check is risk acceptance, not remediation.
- A Config aggregator does not create recorders or rules.
- Automatic remediation is unsafe without exact selection, idempotence, rollback, and verification.
- A compliant state without coverage and freshness evidence is incomplete.

# Data classification

- A Macie finding is detection evidence, not a classification policy or enforcement control.
- Automated discovery sampling and a scoped classification job serve different needs.
- Tags can carry intended classification but do not prove object content.
- An allow list can hide true positives if it is too broad.
- Encryption does not define retention, residency, access, or deletion.

# Encryption at rest

- A customer managed KMS key adds control and operational responsibility; it is not automatically the right answer.
- An IAM allow may still fail the key policy.
- KMS key rotation does not re-encrypt all historical data.
- An alias is mutable; existing ciphertext remains bound to a key ID.
- Multi-Region keys do not make every service resource or ciphertext globally portable.
- Some resources require create-copy-restore migration to change encryption or key choice.
- Never schedule key deletion as a troubleshooting step.

# Encryption in transit

- DNS and TCP must succeed before TLS diagnosis.
- A valid certificate for the wrong hostname fails identity validation.
- Renewal does not prove attachment.
- CloudFront viewer TLS and origin TLS are independent.
- TLS termination and target re-encryption are separate choices.
- A successful handshake does not prove application authorization or health.
- Private certificates require distributing private trust.

# Secrets

- KMS is not a secret lifecycle store.
- Parameter Store SecureString does not provide managed rotation.
- A secret resource policy does not satisfy the KMS key policy.
- Environment injection can expose a secret and delay refresh.
- Rotation success requires the target system, staging labels, and consumers to agree.
- Repeated non-idempotent rotation can worsen partial state.

# Security findings

- Provider severity alone is not business risk.
- Security Hub CSPM aggregation does not replace source-service evidence.
- Workflow status is not source-level remediation.
- GuardDuty, Inspector, Config, and Macie answer different questions.
- Suppression needs owner, reason, scope, and expiry.
- Closing a finding without re-evaluation and workload verification is incomplete.

# Sources

- [Skill 4.1.1](../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.1.3](../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
- [Skill 4.1.5](../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
- [Skill 4.2.1](../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
- [Skill 4.2.2](../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 4.2.4](../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
