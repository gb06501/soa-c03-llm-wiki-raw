# Troubleshooting playbooks

## Domain 1: Monitoring and performance optimization

- [Missing telemetry](missing-telemetry.md) - Traces absent metrics or logs from source configuration through collection, authorization, transport, and destination identity.
- [Alarm and notification failure](alarm-and-notification-failure.md) - Separates missing metric data, alarm evaluation errors, action configuration, and SNS delivery failures.
- [Event-driven remediation failure](event-driven-remediation-failure.md) - Traces a failed remediation from event emission through matching, authorization, execution, and recovery verification.
- [Resource performance diagnosis](resource-performance-diagnosis.md) - Finds the lowest limiting compute, memory, storage, network, concurrency, database, or dependency layer.

## Domain 2: Reliability and business continuity

- [Scaling failure](scaling-failure.md) - Diagnoses absent, delayed, oscillating, or unusable scaling across compute environments.
- [Cache performance failure](cache-performance-failure.md) - Diagnoses low hit ratio, stale data, hot nodes, stampedes, and cache-backed overload.
- [Database scaling failure](database-scaling-failure.md) - Diagnoses ineffective or blocked RDS, Aurora, and DynamoDB scaling.
- [Unhealthy target and DNS failover](unhealthy-target-and-dns-failover.md) - Separates load-balancer target failure from Route 53 health and DNS failover problems.
- [Failure-boundary diagnosis](failure-boundary-diagnosis.md) - Finds hidden single-instance, single-AZ, and single-Region dependencies in a supposedly fault-tolerant design.
- [Backup job failure](backup-job-failure.md) - Diagnoses absent, expired, failed, uncopyable, undeletable, or unrestorable recovery points.
- [Database restore and cutover](database-restore-and-cutover.md) - Runs and diagnoses database restore, validation, application cutover, and recovery-time measurement.
- [Storage-version recovery](storage-version-recovery.md) - Recovers S3 or FSx historical data and diagnoses missing versions, denied access, or failed replication.
- [Disaster-recovery failover](disaster-recovery-failover.md) - Runs and diagnoses multi-Region recovery from declaration through validation, traffic shift, and failback.

## Domain 3: Deployment, provisioning, and automation

- [Image build and distribution failure](image-build-distribution-failure.md) - Diagnoses AMI creation, Image Builder, ECR push and pull, replication, and runtime compatibility failures.
- [CloudFormation deployment failure](cloudformation-deployment-failure.md) - Recovers failed CloudFormation or CDK changes from first resource evidence through stable rollback and validation.
- [Deployment failure](deployment-failure.md) - Diagnoses permission, quota, capacity, subnet, network, runtime, rollback, and deletion failures across deployment tools.
- [Cross-account provisioning failure](cross-account-provisioning-failure.md) - Diagnoses RAM and StackSet visibility, permission, target, Region, operation, and drift failures.
- [Deployment rollback](deployment-rollback.md) - Stops or reverses unsafe releases while preserving data compatibility, evidence, and known-good artifacts.
- [Third-party deployment failure](third-party-deployment-failure.md) - Diagnoses Terraform initialization, plan, lock, state, partial apply, drift, account, and Git release failures.
- [Systems Manager automation execution failure](automation-execution-failure.md) - Diagnoses managed-node, command, association, patch, window, session, output, and fleet-target failures.
- [Event-driven automation failure](event-driven-automation-failure.md) - Traces missing, duplicated, delayed, denied, throttled, or recursive automation from source to verified state.

## Domain 4: Security and compliance

- [Access denied](access-denied.md) - Diagnoses identity, trust, resource, boundary, organization, endpoint, KMS, and service-policy denials.
- [Cross-account access failure](cross-account-access-failure.md) - Diagnoses role, resource-policy, SCP, KMS, endpoint, and delegated-administration failures across accounts.
- [Compliance remediation failure](compliance-remediation-failure.md) - Diagnoses missing evaluations, stale aggregation, automation failures, and repeated drift.
- [Data classification gap](data-classification-gap.md) - Diagnoses unscanned, unclassified, misclassified, or unenforced data.
- [KMS access failure](kms-access-failure.md) - Diagnoses key-policy, grant, context, state, Region, and service-integration failures.
- [TLS connectivity failure](tls-connectivity-failure.md) - Diagnoses DNS, TCP, policy, certificate, trust, SNI, listener, origin, and application layers.
- [Secret access and rotation failure](secret-access-and-rotation-failure.md) - Diagnoses identity, policy, endpoint, version-label, target-system, and rotation-step failures.
- [Security finding remediation](security-finding-remediation.md) - Validates, prioritizes, contains, remediates, and closes source findings safely.

## Domain 5: Networking and content delivery

- [VPC connectivity failure](vpc-connectivity-failure.md) - Traces DNS, route, translation, security group, network ACL, load balancer, and application reachability.
- [DNS resolution failure](dns-resolution-failure.md) - Diagnoses hosted-zone, Resolver endpoint, forwarding-rule, association, and query-path failures.
- [DNS routing failure](dns-routing-failure.md) - Diagnoses record, health-check, routing-policy, propagation, and resolver-cache behavior.
- [Edge delivery failure](edge-delivery-failure.md) - Diagnoses client, DNS, edge, certificate, origin, and application failures.
- [CloudFront cache failure](cloudfront-cache-failure.md) - Diagnoses misses, stale objects, cache keys, directives, invalidations, and cached errors.
- [Hybrid and private connectivity failure](hybrid-private-connectivity-failure.md) - Diagnoses endpoints, peering, Transit Gateway, VPN, Direct Connect, and client access.
- [Network protection gap](network-protection-gap.md) - Finds missing associations, rule-order errors, bypass paths, and enforcement-mode gaps.
- [Network request tracing](network-request-tracing.md) - Correlates VPC, load-balancer, WAF, CloudFront, container, and application evidence.
- [Network cost anomaly](network-cost-anomaly.md) - Attributes network spend to traffic path and validates the smallest safe optimization.
- [Network performance diagnosis](network-performance-diagnosis.md) - Separates component saturation, flow behavior, synthetic path degradation, internet impact, and application latency.
