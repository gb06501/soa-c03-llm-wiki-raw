---
type: Troubleshooting Playbook
title: Network cost anomaly
description: Traces a network bill change from service and usage type to the exact traffic path and verifies a safe correction.
tags: ["soa-c03", "domain-5", "troubleshooting", "network-cost", "cost-anomaly"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.4"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md
status: verified
---

# Trigger

Network-related cost rises unexpectedly or a proposed topology change requires evidence that it will reduce total cost safely.

# Evidence path

1. Use Cost Explorer to locate service, account, Region, usage type, operation, and time.
2. Use CUR/Athena when detailed line items are required.
3. Separate fixed resources from per-byte processing and transfer.
4. Map source/destination/AZ/Region through every NAT, endpoint, TGW, firewall, LB, edge, or public-address hop.
5. Use Flow Logs and component metrics to quantify traffic.
6. Identify legitimate growth versus accidental hairpin, bypass, low cache hit, idle resource, or log volume.
7. Model alternatives including AZ count, fixed cost, availability, isolation, and security.
8. Test one workload/AZ and watch bytes, latency, errors, and redundancy.

# Failure map

| Cost clue | Direction |
| --- | --- |
| NAT bytes to S3/DynamoDB | gateway endpoint |
| Cross-AZ NAT processing | same-AZ NAT or justified central design |
| Many low-volume endpoints | fixed endpoint cost versus shared NAT |
| TGW/firewall bytes spike | route change, hairpin, new flow |
| CloudFront and origin both high | cache key/TTL/compression |
| Public IPv4 rise | allocation and ownership inventory |
| Log ingestion spike | new scope/verbosity/retention |
| Savings appear but errors rise | unsafe path/control removal |

# Safe action

Preserve HA, security, and audit requirements. Add the alternative path, shift a bounded flow, verify early traffic metrics and later billing, then retire the old component.

# Verification

Confirm service health, availability/failover, security controls, byte path, no displaced charge, and cost change after billing data settles.

# Rollback

Restore the prior route/resource while retaining the cost evidence and revisit the alternative model.

# Escalation

Provide usage type, topology, byte evidence, fixed/per-GB assumptions, service requirements, test result, and billing lag.

# Related pages

- [Network cost optimization](../concepts/network-cost-optimization.md)
- [Cost Explorer](../services/cost-explorer.md)

# Sources

- [Skill 5.1.4](../../raw/skills/5.1.4-optimize-the-cost-of-network-architectures.md)
