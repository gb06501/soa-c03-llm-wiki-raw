---
type: Concept
title: Managed database scaling
description: Explains RDS, Aurora, DynamoDB, connection, storage, and read-scaling mechanisms.
tags: [soa-c03, domain-2, database, scaling, rds, aurora, dynamodb]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["2.1.3"]
domain_ids: ["2"]
sources:
  - /raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md
status: verified
---

# Core model

```text
workload evidence -> limiting database dimension -> matching scaling control -> application routing -> verification
```

# Scaling dimensions

| Need | Mechanism |
| --- | --- |
| More RDS/Aurora reads | Read replicas or Aurora readers |
| More instance compute/memory | Larger DB instance class |
| More RDS storage space | Storage increase or storage autoscaling |
| Absorb connection bursts | Pooling or RDS Proxy |
| Variable Aurora capacity | Aurora Serverless v2 within ACU bounds |
| Unpredictable DynamoDB traffic | On-demand capacity |
| Predictable DynamoDB traffic | Provisioned capacity with auto scaling |
| Repeated DynamoDB reads | DAX |
| Hot DynamoDB partition | Better partition-key distribution |

# Important behavior

- Read replicas are asynchronous and must receive application reads.
- Multi-AZ standby is an availability mechanism, not normal read scaling.
- Aurora readers use reader endpoints; writes use the writer.
- Aurora Serverless v2 scales only within configured minimum and maximum.
- DynamoDB read, write, table, and GSI capacity can constrain independently.
- DynamoDB auto scaling reacts and can lag a sudden spike.

# Evidence

Use CPU, DB load/waits, connections, storage/IO, replica lag, Aurora capacity, consumed versus provisioned DynamoDB capacity, throttling, and table-versus-GSI evidence.

# Exam traps

- Adding a replica changes nothing if the application still reads the writer.
- RDS Proxy is neither cache nor database compute.
- More table capacity may not repair a hot partition.
- DAX improves repeated reads, not write throughput.
- Storage autoscaling does not automatically shrink storage.

# Related concepts

- [Database scaling selection](../decision-guides/database-scaling-selection.md)
- [Database scaling failure](../playbooks/database-scaling-failure.md)
- [RDS performance remediation](../decision-guides/database-remediation.md)

# Sources

- [Skill 2.1.3](../../raw/skills/2.1.3-configure-and-manage-scaling-in-managed-databases.md)
