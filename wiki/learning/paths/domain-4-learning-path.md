---
type: Learning Path
title: Domain 4 learning path
description: Orders Domain 4 study from authorization and account governance through data protection, secrets, findings, and verified remediation.
tags: ["soa-c03", "domain-4", "learning-path"]
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

# Stage 1: Build the authorization model

1. [IAM access control](../../services/iam-access-control.md)
2. [IAM](../../services/iam.md), [IAM Identity Center](../../services/iam-identity-center.md), and [STS](../../services/sts.md)
3. [Access evaluation](../../concepts/access-evaluation.md)
4. [IAM principal and policy selection](../../decision-guides/iam-principal-and-policy-selection.md)
5. [Access denied](../../playbooks/access-denied.md)

Goal: explain an authorization result from principal, action, resource, context, allows, explicit denies, and every limiting policy layer.

# Stage 2: Govern multiple accounts

1. [Organizations and multi-account security](../../services/organizations-and-multi-account.md)
2. [Organizations](../../services/organizations.md), [Control Tower](../../services/control-tower.md), and [IAM Identity Center](../../services/iam-identity-center.md)
3. [Multi-account security governance](../../concepts/multi-account-security-governance.md)
4. [Multi-account guardrail selection](../../decision-guides/multi-account-guardrail-selection.md)
5. [Cross-account access failure](../../playbooks/cross-account-access-failure.md)

Goal: separate grants, maximum-permission guardrails, detective controls, delegated administration, central evidence, and break-glass access.

# Stage 3: Establish continuous compliance

1. [Trusted Advisor security checks](../../services/trusted-advisor-security.md) and [Trusted Advisor](../../services/trusted-advisor.md)
2. [Config and continuous compliance](../../services/config-and-compliance.md) and [Config](../../services/config.md)
3. [Security check remediation priority](../../decision-guides/security-check-remediation-priority.md)
4. [Compliance monitoring selection](../../decision-guides/compliance-monitoring-selection.md)
5. [Compliance remediation failure](../../playbooks/compliance-remediation-failure.md)

Goal: distinguish advice, prevention, configuration recording, detection, aggregation, remediation, and verified compliance.

# Stage 4: Classify and protect data

1. [Data classification](../../concepts/data-classification.md) and [Macie](../../services/macie.md)
2. [Data protection control selection](../../decision-guides/data-protection-control-selection.md)
3. [KMS encryption at rest](../../services/kms-encryption-at-rest.md) and [KMS](../../services/kms.md)
4. [Encryption at rest selection](../../decision-guides/encryption-at-rest-selection.md)
5. [Data classification gap](../../playbooks/data-classification-gap.md) and [KMS access failure](../../playbooks/kms-access-failure.md)

Goal: map a classification requirement to discovery, access, key ownership, encryption, retention, monitoring, backup, and response.

# Stage 5: Protect connections and certificates

1. [Encryption in transit](../../concepts/encryption-in-transit.md)
2. [Certificate Manager](../../services/certificate-manager.md) and [Private CA](../../services/private-ca.md)
3. [Elastic Load Balancing](../../services/elastic-load-balancing.md), [CloudFront](../../services/cloudfront.md), and [VPC](../../services/vpc.md)
4. [TLS certificate selection](../../decision-guides/tls-certificate-selection.md)
5. [TLS connectivity failure](../../playbooks/tls-connectivity-failure.md)

Goal: trace DNS, routing, TCP, TLS policy, certificate identity, trust, termination, origin/target TLS, and application health as separate layers.

# Stage 6: Operate secret lifecycle

1. [Secrets management](../../services/secrets-management.md)
2. [Secrets Manager](../../services/secrets-manager.md) and [Systems Manager Parameter Store](../../services/systems-manager-parameter-store.md)
3. [Secrets storage selection](../../decision-guides/secrets-storage-selection.md)
4. [Secret access and rotation failure](../../playbooks/secret-access-and-rotation-failure.md)

Goal: choose storage and delivery by lifecycle, rotate idempotently, prove the target and consumer agree, and preserve rollback.

# Stage 7: Triage and remediate findings

1. [Security findings](../../concepts/security-findings.md)
2. [Security Hub CSPM](../../services/security-hub-cspm.md), [GuardDuty](../../services/guardduty.md), [Inspector](../../services/inspector.md), [Macie](../../services/macie.md), and [Security Agent](../../services/security-agent.md)
3. [Security finding triage](../../decision-guides/security-finding-triage.md)
4. [Security finding remediation](../../playbooks/security-finding-remediation.md)
5. [Domain 4 exam traps](../../exam-traps/domain-4-exam-traps.md)

Goal: preserve source evidence, prioritize by risk context, contain safely, remediate through the owning path, and close only after source and workload verification.

# Retrieval drills

For each skill, answer without notes:

1. What is the exact object or principal being controlled?
2. Which policy, key, certificate, finding, or configuration evidence is decisive?
3. Which tempting alternative solves a different problem?
4. What is the smallest reversible action?
5. Which security and workload checks prove success?

# Sources

- [Skill 4.1.1](../../../raw/skills/4.1.1-implement-iam-features.md)
- [Skill 4.1.2](../../../raw/skills/4.1.2-troubleshoot-and-audit-access-issues.md)
- [Skill 4.1.3](../../../raw/skills/4.1.3-implement-secure-multi-account-strategies.md)
- [Skill 4.1.4](../../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
- [Skill 4.1.5](../../../raw/skills/4.1.5-enforce-compliance-requirements-and-continuous-monitoring.md)
- [Skill 4.2.1](../../../raw/skills/4.2.1-implement-and-enforce-a-data-classification-scheme.md)
- [Skill 4.2.2](../../../raw/skills/4.2.2-implement-configure-and-troubleshoot-encryption-at-rest.md)
- [Skill 4.2.3](../../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 4.2.4](../../../raw/skills/4.2.4-securely-store-secrets-by-using-services.md)
- [Skill 4.2.5](../../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
