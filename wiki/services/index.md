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
