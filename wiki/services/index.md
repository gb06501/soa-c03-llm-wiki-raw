# Services and features

Only pages in **Canonical services** use `type: AWS Service`. Display names follow the short-name registry in [`state/aws-service-registry.yaml`](../../state/aws-service-registry.yaml).

## Canonical services

### Observability and messaging

- [CloudWatch](cloudwatch-telemetry.md)
- [EventBridge](eventbridge.md)
- [SNS](sns-notifications.md)
- [SQS](sqs.md)

### Compute, containers, and serverless

- [EC2](ec2-performance.md)
- [EC2 Auto Scaling](ec2-auto-scaling.md)
- [ECS](ecs.md)
- [EKS](eks.md)
- [Lambda](lambda.md)
- [ECR](ecr.md)
- [Image Builder](image-builder.md)

### Infrastructure and operations

- [CloudFormation](cloudformation.md)
- [CDK](cdk.md)
- [Service Catalog](service-catalog.md)
- [Resource Access Manager](resource-access-manager.md)
- [Systems Manager](systems-manager.md)
- [Step Functions](step-functions.md)
- [DevOps Agent](devops-agent.md)

### Storage and databases

- [EBS](ebs-performance.md)
- [S3](s3-performance.md)
- [RDS](rds-performance.md)
- [Backup](aws-backup.md)

## AWS features

- [CloudWatch Agent](cloudwatch-agent.md) — parent: CloudWatch.
- [CloudWatch alarms](cloudwatch-alarms.md) — parent: CloudWatch.
- [CloudWatch dashboards](cloudwatch-dashboards.md) — parent: CloudWatch.
- [Systems Manager Automation](systems-manager-automation.md) — parent: Systems Manager.

## Cross-service concepts at stable paths

These paths are retained to avoid unnecessary link churn; their frontmatter now identifies them as concepts.

- [Shared storage](shared-storage.md)
- [Compute scaling](compute-scaling.md)
- [Caching](caching.md)
- [Managed database scaling](managed-database-scaling.md)
- [Load balancing and health checks](load-balancing-and-health-checks.md)
- [AMI and container image management](image-management.md)
- [CloudFormation and CDK lifecycle](cloudformation-and-cdk.md)

### Security, identity, and governance

- [IAM](iam.md)
- [IAM Identity Center](iam-identity-center.md)
- [STS](sts.md)
- [CloudTrail](cloudtrail.md)
- [Organizations](organizations.md)
- [Control Tower](control-tower.md)
- [Trusted Advisor](trusted-advisor.md)
- [Config](config.md)

### Data protection and security findings

- [Macie](macie.md)
- [KMS](kms.md)
- [Certificate Manager](certificate-manager.md)
- [Private CA](private-ca.md)
- [Secrets Manager](secrets-manager.md)
- [Security Hub CSPM](security-hub-cspm.md)
- [GuardDuty](guardduty.md)
- [Inspector](inspector.md)
- [Security Agent](security-agent.md)

### Network, edge, storage, and database services

- [CloudFront](cloudfront.md)
- [Route 53](route-53.md)
- [VPC](vpc.md)
- [Elastic Load Balancing](elastic-load-balancing.md)
- [DynamoDB](dynamodb.md)
- [Aurora](aurora.md)
- [EFS](efs.md)
- [FSx](fsx.md)

## Domain 4 AWS features

- [IAM Access Analyzer](iam-access-analyzer.md) — parent: IAM.
- [Systems Manager Parameter Store](systems-manager-parameter-store.md) — parent: Systems Manager.

## Domain 4 cross-service concepts at stable paths

- [IAM access control](iam-access-control.md)
- [Organizations and multi-account security](organizations-and-multi-account.md)
- [Config and continuous compliance](config-and-compliance.md)
- [Trusted Advisor security checks](trusted-advisor-security.md)
- [KMS encryption at rest](kms-encryption-at-rest.md)
- [Secrets management](secrets-management.md)
