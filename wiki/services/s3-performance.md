---
type: AWS Service
title: S3
service_id: s3
description: Provides object storage with transfer, request, lifecycle, versioning, and event-notification controls.
tags: [soa-c03, domain-1, s3, performance, lifecycle, domain-5, private-access, edge-origin]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["1.3.3", "1.3.4", "3.2.2", "5.1.2", "5.1.4", "5.2.3", "5.3.2"]
domain_ids: ["1", "3", "5"]
sources:
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
  - /raw/skills/3.2.2-implement-event-driven-automation.md
  - /raw/skills/5.1.2-configure-private-networking-connectivity.md
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---

# Problem separation

| Requirement | Choice |
| --- | --- |
| Reliable parallel large-object upload | Multipart upload |
| Faster path for a client far from the bucket Region | Transfer Acceleration, after testing |
| Managed bulk or recurring data movement | DataSync |
| Cached global reads | CloudFront |
| Partial or parallel object reads | Byte-range GET |
| Move aging objects to cheaper storage | Lifecycle transition |
| Remove old objects or abandoned parts | Lifecycle expiration/abort rule |

Lifecycle changes storage placement. It does not speed up network transfer. DataSync copies data; it does not cache reads.

# Multipart model

```text
initiate -> upload parts in parallel -> retry failed parts -> complete
```

Incomplete parts continue consuming storage until completed, aborted, or removed by Lifecycle.

# Request behavior

- Parallelize independent requests.
- Keep compute near the bucket when practical.
- Reuse client connections.
- Retry temporary failures with exponential backoff.
- Avoid synchronized retry storms after `503 Slow Down`.
- Monitor request errors, latency, and throughput.

# Storage-class decision

Choose from access frequency, retrieval speed, availability/resilience, retrieval charge, minimum duration, and object size. Intelligent-Tiering fits unknown or changing access. One Zone-IA trades multi-AZ resilience for cost. Archive classes must satisfy required retrieval time.

# Exam traps

- Transfer Acceleration is not content caching.
- CloudFront caches; DataSync copies.
- Cheapest storage can create retrieval or minimum-duration cost.
- Lifecycle runs asynchronously.
- S3 object storage is not a shared POSIX filesystem.

# Related concepts

- [Shared storage](shared-storage.md)
- [Storage service selection](../decision-guides/storage-service-selection.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)

# Domain 3: Event notifications

S3 Event Notification selects an event type and optional object-key prefix/suffix, then sends matching events to Lambda, SNS, SQS, or EventBridge. The destination must exist and authorize S3; encrypted destinations also require the correct KMS policy.

Delivery can be duplicated and out of order. Consumers must be idempotent. Avoid recursive writes by separating input/output prefixes or buckets and filtering only the input path.

# Domain 5: Private access and edge origin

An S3 gateway endpoint routes supported regional S3 traffic through associated route tables and prefix lists without endpoint ENIs or security groups. Endpoint, IAM, bucket, and KMS policies remain separate authorization layers.

For private CloudFront delivery, use the S3 REST origin with Origin Access Control, a distribution-scoped bucket policy, and KMS permission where required. Website origins are custom origins and cannot use OAC.

Flow Logs explain VPC-side endpoint/NAT paths; S3 and CloudFront access evidence explain object and edge behavior. Gateway endpoints can remove supported traffic from NAT processing.

- [Private connectivity selection](../decision-guides/private-connectivity-selection.md)
- [Content distribution selection](../decision-guides/content-distribution-selection.md)

# Sources

- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
- [Skill 3.2.2](../../raw/skills/3.2.2-implement-event-driven-automation.md)
- [Skill 5.1.2](../../raw/skills/5.1.2-configure-private-networking-connectivity.md)
- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
