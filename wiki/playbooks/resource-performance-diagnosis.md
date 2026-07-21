---
type: Troubleshooting Playbook
title: Resource performance diagnosis
description: Finds the lowest limiting compute, memory, storage, network, concurrency, database, or dependency layer.
tags: [soa-c03, domain-1, troubleshooting, performance, optimization]
timestamp: 2026-07-21T00:00:00+02:00
skill_ids: ["1.2.1", "1.3.1", "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md
  - /raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md
  - /raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md
  - /raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Trigger

Latency, errors, backlog, or cost is unacceptable, and the limiting layer is not yet proven.

# Baseline

1. Define the affected user flow, resources, time, accounts, Regions, and AZs.
2. Compare healthy versus affected, normal versus peak, and before versus after a change.
3. Read average and tail latency together when available.

# Layer checks

| Layer | Evidence |
| --- | --- |
| Compute | CPU, processing time, CPU credits, DB CPU waits |
| Memory | Agent/container memory, swapping, OOM/restarts, freeable memory |
| Storage | IOPS, throughput, latency, queue, burst, free capacity |
| Network | Throughput, packets, latency, loss, routes, instance ceiling |
| Concurrency | Lambda throttles, connections, task/worker backlog |
| Database | DB load, waits, top SQL, connections, replica lag |
| Dependency | Downstream latency/errors while local resources remain healthy |

# Decision rules

- Do not resize from CPU alone.
- High CPU with high latency suggests compute pressure; low CPU with high latency redirects to other layers.
- More application capacity can worsen a constrained database or dependency.
- Volume tuning cannot exceed the EC2 EBS ceiling.
- Storage Lifecycle is cost optimization, not active-performance remediation.
- A larger database class does not automatically remove locks or slow SQL.

# Change path

```text
observation window -> limiting layer -> smallest useful change
-> impact review -> controlled deployment -> before/after verification
```

# Verification

- User latency and errors improved.
- The proven bottleneck is no longer saturated.
- Required headroom remains.
- No downstream layer became the new bottleneck unexpectedly.
- Cost moved as intended.

# Related concepts

- [Evidence-to-remediation loop](../concepts/evidence-to-remediation-loop.md)
- [EC2 performance](../services/ec2-performance.md)
- [EBS performance](../services/ebs-performance.md)
- [RDS performance](../services/rds-performance.md)
- [Shared storage](../services/shared-storage.md)

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.2](../../raw/skills/1.3.2-analyze-and-optimize-ebs-performance.md)
- [Skill 1.3.3](../../raw/skills/1.3.3-implement-and-optimize-s3-performance-strategies.md)
- [Skill 1.3.4](../../raw/skills/1.3.4-evaluate-and-optimize-shared-storage-solutions.md)
- [Skill 1.3.5](../../raw/skills/1.3.5-monitor-and-optimize-amazon-rds.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
