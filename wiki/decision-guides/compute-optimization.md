---
type: Decision Guide
title: Compute optimization
description: Selects compute remediation from health, utilization, architecture, and downstream-bottleneck evidence.
tags: [soa-c03, domain-1, ec2, compute, optimization]
timestamp: 2026-07-21T12:00:00+02:00
skill_ids: ["1.2.1", "1.3.1", "1.3.6"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
  - /raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md
  - /raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md
status: verified
---

# Decision table

| Evidence or requirement | Direction |
| --- | --- |
| Sustained compute, memory, network, or EBS ceiling | Select a family and size that removes the proven ceiling |
| Horizontal demand with independent workers | Scale out where the architecture supports it |
| Burstable instance constrained by credits | Change burst model, baseline, or instance choice |
| Unhealthy host or failed status check | Recover, stop/start, or replace according to the health evidence |
| Storage queue or latency dominates | Tune the EBS and EC2 storage path before adding CPU |
| Placement-sensitive low-latency workload | Select a justified placement-group strategy |
| Disposable high-performance scratch data | Instance store |
| Persistent block data | EBS |
| Container or Lambda constraint | Tune the service-specific capacity or concurrency control |

Baseline before changing capacity, correlate traffic with resource signals, and verify the downstream system can accept the new load.

# Rejection rules

- More instances can overload a limited database or dependency.
- Compute Optimizer recommends; it does not prove migration safety.
- Downsizing without memory or workload evidence is guesswork.
- Low average utilization does not exclude short peaks, latency, credit, or per-resource limits.
- Instance store is not for irreplaceable data.

# Evidence and verification

Compare before and after traffic, latency, errors, CPU, memory where collected, network, EBS, credits, status checks, downstream load, and cost. Verify required headroom remains.

# Related concepts

- [EC2 performance](../services/ec2-performance.md)
- [EBS performance tuning](ebs-performance-tuning.md)
- [Resource performance diagnosis](../playbooks/resource-performance-diagnosis.md)

# Sources

- [Skill 1.2.1](../../raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md)
- [Skill 1.3.1](../../raw/skills/1.3.1-optimize-compute-resources-and-remediate-performance-problems.md)
- [Skill 1.3.6](../../raw/skills/1.3.6-implement-monitor-and-optimize-ec2-instances-storage-and-networking.md)
