---
type: AWS Service
title: Trusted Advisor
service_id: trusted-advisor
description: Evaluates account resources against AWS checks and provides prioritized recommendations.
tags: ["soa-c03", "domain-4", "trusted-advisor", "security-checks"]
timestamp: 2026-07-22T09:00:00+02:00
skill_ids: ["4.1.4", "1.3.1"]
domain_ids: ["4", "1"]
sources:
  - /raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
status: verified
---
# Core model

A Trusted Advisor result combines a check definition, status, affected resource, recommendation, and freshness. Availability and refresh behavior depend on the check and support entitlement.

# Security workflow

1. Confirm the finding is current and the resource is still in scope.
2. Establish exposure, data sensitivity, privilege, and workload dependency.
3. Select the smallest reversible remediation.
4. Apply through controlled configuration or infrastructure as code.
5. Refresh or re-evaluate the check and verify workload health.

# Common check families

Network exposure, public storage, root and MFA posture, access keys, CloudTrail coverage, certificate expiry, snapshots, and encryption all require service-specific verification.

# Automation boundary

Use EventBridge or notifications to route findings. Use Lambda or Systems Manager Automation only when selection, scope, rollback, and post-change verification are explicit. Exclusion is documented risk acceptance, not remediation.

# Related decisions

- [Security check remediation priority](../decision-guides/security-check-remediation-priority.md)
- [Security finding remediation](../playbooks/security-finding-remediation.md)

# Optimization boundary

Trusted Advisor recommendations are candidates for evidence-backed review. Validate workload ownership, peak demand, redundancy, dependency limits, planned events, and post-change health before acting.

# Sources

- [Skill 4.1.4](../../raw/skills/4.1.4-remediate-trusted-advisor-security-checks.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)

