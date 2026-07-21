# Decision guides

## Observability and alerting

- [Telemetry selection](telemetry-selection.md) - choose metrics, logs, audit, traces, Prometheus, dashboards, streaming, or agent collection.
- [CloudWatch alarm design](alarm-design.md) - choose alarm type, evaluation behavior, and missing-data treatment.
- [CloudWatch dashboard design](dashboard-design.md) - choose widgets, scope, time context, and sharing.
- [Event and notification routing](event-notification-routing.md) - choose alarm actions, SNS, EventBridge, or SQS.

## Remediation and performance

- [Remediation tool selection](remediation-tool-selection.md) - select scaling, Lambda, Automation, EventBridge, SNS, SQS, or Step Functions.
- [Compute optimization](compute-optimization.md) - choose scale, resize, family, placement, recovery, or storage-path remediation.
- [RDS performance remediation](database-remediation.md) - choose query, compute, storage, connection, or read-scaling remediation.
- [EBS performance tuning](ebs-performance-tuning.md) - distinguish IOPS, throughput, latency, queue, initialization, and EC2 limits.
- [S3 transfer optimization](s3-transfer-optimization.md) - choose multipart, byte ranges, acceleration, caching, movement, or lifecycle.

## Storage architecture

- [Storage service selection](storage-service-selection.md) - choose object, block, file, parallel, or hybrid storage.
- [Shared storage performance](shared-storage-performance.md) - choose EFS/FSx family and performance controls.

## Domain 2: Scaling and caching

- [Compute scaling selection](compute-scaling-selection.md)
- [Caching selection](caching-selection.md)
- [Database scaling selection](database-scaling-selection.md)

## Domain 2: Availability

- [Load balancer and health-check selection](load-balancer-health-check-selection.md)
- [Fault-tolerance pattern selection](fault-tolerance-pattern-selection.md)

## Domain 2: Recovery

- [Backup protection selection](backup-protection-selection.md)
- [Database restore selection](database-restore-selection.md)
- [Versioning, backup, and Object Lock selection](versioning-backup-object-lock-selection.md)
- [Disaster-recovery strategy selection](dr-strategy-selection.md)

## Domain 3: Artifacts and provisioning

- [AMI and container image selection](machine-container-image-selection.md)
- [Infrastructure provisioning selection](infrastructure-provisioning-selection.md)
- [Resource sharing and provisioning selection](resource-sharing-and-provisioning-selection.md)
- [Deployment tool selection](deployment-tool-selection.md)

## Domain 3: Deployment and automation

- [Deployment failure evidence selection](deployment-failure-evidence-selection.md)
- [Deployment strategy selection](deployment-strategy-selection.md)
- [Operational automation service selection](operational-automation-service-selection.md)
- [Event-driven automation selection](event-driven-automation-selection.md)
