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
