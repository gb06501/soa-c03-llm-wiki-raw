# Decision guides

## Domain 1: Monitoring and performance optimization

### Observability and alerting

- [Telemetry selection](telemetry-selection.md) - Selects the evidence type, collection mechanism, and AWS observability service from an operational question.
- [CloudWatch alarm design](alarm-design.md) - Selects alarm type and evaluation behavior from signal shape, noise, and missing-data requirements.
- [CloudWatch dashboard design](dashboard-design.md) - Selects dashboard widgets, scope, and sharing behavior from an operator's evidence needs.
- [Event and notification routing](event-notification-routing.md) - Selects EventBridge, SNS, SQS, or an alarm action from routing, fan-out, buffering, and delivery requirements.

### Remediation and performance

- [Remediation tool selection](remediation-tool-selection.md) - Selects the smallest AWS mechanism that matches capacity, routing, workflow, notification, or infrastructure-remediation needs.
- [Compute optimization](compute-optimization.md) - Selects compute remediation from health, utilization, architecture, and downstream-bottleneck evidence.
- [RDS performance remediation](database-remediation.md) - Selects RDS remediation from resource metrics, database load, waits, SQL, storage, and connection evidence.
- [EBS performance tuning](ebs-performance-tuning.md) - Selects an EBS change by separating IOPS, throughput, latency, queue, initialization, and EC2 limits.
- [S3 transfer optimization](s3-transfer-optimization.md) - Selects multipart, parallel reads, acceleration, caching, data movement, or lifecycle from the actual S3 constraint.

### Storage architecture

- [Storage service selection](storage-service-selection.md) - Chooses block, object, shared file, parallel file, or hybrid storage from semantics and performance requirements.
- [Shared storage performance](shared-storage-performance.md) - Selects shared-storage family and performance controls from protocol, client, parallelism, throughput, and resilience requirements.

## Domain 2: Reliability and business continuity

### Scaling and caching

- [Compute scaling selection](compute-scaling-selection.md) - Selects a scaling policy and capacity surface from demand shape, metric behavior, and workload architecture.
- [Caching selection](caching-selection.md) - Selects CloudFront, ElastiCache, or DAX and the correct scaling control from request semantics.
- [Database scaling selection](database-scaling-selection.md) - Selects RDS, Aurora, and DynamoDB scaling controls from the constrained database dimension.

### Availability

- [Load balancer and health-check selection](load-balancer-health-check-selection.md) - Selects the load balancer and health source from protocol, routing, reachability, and failover requirements.
- [Fault-tolerance pattern selection](fault-tolerance-pattern-selection.md) - Selects redundancy, decoupling, and traffic controls from the required failure boundary.

### Recovery

- [Backup protection selection](backup-protection-selection.md) - Selects periodic, continuous, copied, locked, native, or centralized backup controls from recovery requirements.
- [Database restore selection](database-restore-selection.md) - Selects snapshot, point-in-time, vault, replica, or high-availability recovery from RPO, RTO, and cost.
- [Versioning, backup, and Object Lock selection](versioning-backup-object-lock-selection.md) - Selects versioning, immutable retention, replication, lifecycle, backup, or FSx recovery controls.
- [Disaster-recovery strategy selection](dr-strategy-selection.md) - Selects backup and restore, pilot light, warm standby, or active-active from cost, RTO, RPO, and readiness.

## Domain 3: Deployment, provisioning, and automation

### Artifacts and provisioning

- [AMI and container image selection](machine-container-image-selection.md) - Chooses image identity, distribution, security, and lifecycle controls from release and runtime clues.
- [Infrastructure provisioning selection](infrastructure-provisioning-selection.md) - Selects CloudFormation, CDK, Service Catalog, and lifecycle controls from infrastructure requirements.
- [Resource sharing and provisioning selection](resource-sharing-and-provisioning-selection.md) - Chooses RAM, StackSets, resource policies, or artifact copies across accounts and Regions.
- [Deployment tool selection](deployment-tool-selection.md) - Chooses Terraform, CloudFormation/CDK, data references, imports, and Git release identities from ownership clues.

### Deployment and automation

- [Deployment failure evidence selection](deployment-failure-evidence-selection.md) - Selects the first decisive evidence source for deployment, permission, capacity, network, and runtime failures.
- [Deployment strategy selection](deployment-strategy-selection.md) - Selects all-at-once, rolling, immutable, blue/green, canary, or linear deployment from risk and capacity clues.
- [Operational automation service selection](operational-automation-service-selection.md) - Selects the correct Systems Manager capability for fleet operations and configuration.
- [Event-driven automation selection](event-driven-automation-selection.md) - Selects event routing, buffering, compute, workflows, retries, and failure controls from automation clues.

## Domain 4: Security and compliance

### Identity and governance

- [IAM principal and policy selection](iam-principal-and-policy-selection.md) - Chooses identities, temporary credentials, and policy locations for workforce, workload, service, and cross-account access.
- [Access denial evidence selection](access-denial-evidence-selection.md) - Selects decisive identity, trust, resource, boundary, KMS, and endpoint evidence.
- [Multi-account guardrail selection](multi-account-guardrail-selection.md) - Chooses account structure, federation, preventive limits, detective controls, and delegated administration.
- [Security check remediation priority](security-check-remediation-priority.md) - Ranks advisory checks by exposure, privilege, data impact, freshness, and remediation readiness.
- [Compliance monitoring selection](compliance-monitoring-selection.md) - Chooses preventive, detective, aggregation, and remediation controls.

### Data protection and findings

- [Data protection control selection](data-protection-control-selection.md) - Maps classification requirements to discovery, access, encryption, retention, and response.
- [Encryption at rest selection](encryption-at-rest-selection.md) - Chooses key ownership and service encryption patterns with safe migration and recovery.
- [TLS certificate selection](tls-certificate-selection.md) - Chooses public, imported, or private certificates and endpoint termination patterns.
- [Secrets storage selection](secrets-storage-selection.md) - Chooses Secrets Manager, Parameter Store, or direct KMS use by lifecycle and delivery requirements.
- [Security finding triage](security-finding-triage.md) - Prioritizes and routes source findings using risk and operational context.
