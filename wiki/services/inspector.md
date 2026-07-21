---
type: AWS Service
title: Inspector
service_id: inspector
description: Continuously scans supported compute workloads and container images for software vulnerabilities and exposure.
tags: ["soa-c03", "domain-4", "inspector", "vulnerability"]
timestamp: 2026-07-21T22:00:00+02:00
skill_ids: ["4.2.5"]
domain_ids: ["4"]
sources:
  - /raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md
status: verified
---
# Core model

Inspector produces vulnerability findings for supported EC2 instances, container images, and functions. Findings connect a vulnerable package or code path to a workload, severity, exploitability context, and remediation information.

# Decision boundaries

Inspector is vulnerability management. It does not replace runtime threat detection, configuration compliance, or data discovery. Package severity alone does not define operational priority.

# Evidence and diagnosis

Check scan coverage, workload support, image digest or instance identity, package version, fixed version, network exposure, last observed time, suppression state, and deployment ownership.

# Safe operations

Prioritize exploitable and exposed workloads, patch through a versioned image or controlled deployment, verify service health, rescan the exact artifact, and avoid closing findings before the vulnerable version is gone.

# Related decisions

- [Security finding triage](../decision-guides/security-finding-triage.md)
- [Security finding remediation](../playbooks/security-finding-remediation.md)

# Sources

- [Skill 4.2.5](../../raw/skills/4.2.5-configure-reports-and-remediate-findings-from-services.md)
