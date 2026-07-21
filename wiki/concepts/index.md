# Cross-skill concepts

## Domain 1: Monitoring and performance optimization

- [Observability signal selection](observability-signal-selection.md) - Chooses the evidence source from the operational question instead of from a preferred tool.
- [Evidence-to-remediation loop](evidence-to-remediation-loop.md) - Diagnoses scope and cause before applying the smallest safe change and verifying recovery.
- [Safe automation](safe-automation.md) - Constrains automated operational changes with least privilege, bounded execution, idempotency, and verification.

## Domain 2: Reliability and business continuity

- [Fault tolerance](fault-tolerance.md) - Maps process, Availability Zone, and Region failures to prepared capacity, health, decoupling, and traffic controls.
- [Database recovery](database-recovery.md) - Connects RPO, RTO, restore point, resource recreation, cutover, and validation for RDS, Aurora, and DynamoDB.
- [Storage versioning and recovery](storage-versioning.md) - Explains S3 versions, Object Lock, replication, lifecycle, and FSx-specific historical recovery controls.
- [Disaster recovery](disaster-recovery.md) - Connects DR strategy, data method, infrastructure readiness, traffic movement, validation, and failback.
- [Scaling, resilience, and recovery](scaling-resilience-and-recovery.md) - Connects capacity response, fault containment, durable recovery, and traffic restoration across Domain 2.

## Domain 3: Deployment, provisioning, and automation

- [Deployment diagnostics](deployment-diagnostics.md) - Finds the earliest failing deployment layer, preserves state, and selects the smallest safe correction.
- [Cross-account and multi-Region provisioning](cross-account-resource-provisioning.md) - Separates shared-resource use from repeated infrastructure deployment across accounts and Regions.
- [Deployment strategies](deployment-strategies.md) - Compares deployment blast radius, coexistence, traffic movement, health gates, capacity, and rollback.
- [Terraform and Git deployment controls](third-party-deployment-tools.md) - Explains Terraform configuration, state, plan, locking, ownership, and reviewed Git release identity.
- [Systems Manager operational automation](operational-automation.md) - Selects and governs Systems Manager capabilities for fleet commands, desired state, patching, maintenance, sessions, and inventory.
- [Event-driven automation](event-driven-automation.md) - Connects event sources, filters, permissions, targets, retries, failure capture, idempotency, and loop prevention.
- [Deployment and operational automation](deployment-and-operational-automation.md) - Unifies artifact identity, infrastructure ownership, rollout, event and fleet automation, evidence, and recovery across Domain 3.

## Domain 4: Security and compliance

- [Access evaluation](access-evaluation.md) - Models authorization as one exact request evaluated against every applicable allow, deny, and limiting boundary.
- [Data classification](data-classification.md) - Connects data meaning and ownership to enforceable storage, access, encryption, retention, and monitoring controls.
- [Encryption in transit](encryption-in-transit.md) - Separates DNS, network, TLS policy, certificate identity, trust, and application delivery across each hop.
- [Security findings](security-findings.md) - Normalizes source evidence into risk-ranked investigation, containment, remediation, and verified closure.
- [Multi-account security governance](multi-account-security-governance.md) - Connects account boundaries, identity, guardrails, detection, evidence, and response across Domain 4.
