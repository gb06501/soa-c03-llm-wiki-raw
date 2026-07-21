---
type: Decision Guide
title: Database scaling selection
description: Selects RDS, Aurora, and DynamoDB scaling controls from the constrained database dimension.
tags: [soa-c03, domain-2, database, scaling, selection]
timestamp: 2026-07-21T13:00:00+02:00
skill_ids: ["2.1.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
status: verified
---

# Decision table

| Dominant requirement | Choose |
| --- | --- |
| RDS/Aurora read throughput | Read replica or Aurora reader plus application routing |
| RDS/Aurora compute or memory | Larger instance class after workload diagnosis |
| RDS storage capacity | Storage increase or autoscaling |
| Connection bursts | Pooling or RDS Proxy |
| Variable Aurora compute | Aurora Serverless v2 with safe ACU bounds |
| Unpredictable DynamoDB traffic | On-demand mode |
| Predictable DynamoDB traffic with control | Provisioned capacity and auto scaling |
| DynamoDB repeated reads | DAX |
| DynamoDB hot partition | Redesign key distribution |
| GSI-specific throttling | Scale or correct that GSI independently |

# Rejection rules

- Multi-AZ is not ordinary read scaling.
- A read replica does not scale writes.
- A replica is ineffective until the application uses its endpoint.
- RDS Proxy does not add query CPU or cache results.
- DynamoDB auto scaling is not instantaneous.
- Additional total DynamoDB capacity may not solve uneven key traffic.
- DAX does not increase write capacity.

# Evidence and verification

Confirm the constrained dimension before changing it. Afterward verify routing, replica lag, capacity bounds, throttling, hot-key distribution, connection behavior, latency, errors, and cost.

# Related concepts

- [Managed database scaling](../services/managed-database-scaling.md)
- [Database scaling failure](../playbooks/database-scaling-failure.md)

# Sources

- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
