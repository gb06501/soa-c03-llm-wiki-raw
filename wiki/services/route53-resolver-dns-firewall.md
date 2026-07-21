---
type: AWS Feature
title: Route 53 Resolver DNS Firewall
parent_services: [Route 53]
description: Filters VPC Resolver queries with prioritized allow, alert, and block rules and query evidence.
tags: ["soa-c03", "domain-5", "dns-firewall", "dns-security"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3", "5.2.1", "5.2.2", "5.3.2", "5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.2.1-configure-dns-and-route-53-resolver.md
  - /raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

`domain list -> firewall rule -> rule group -> VPC association -> Resolver queries`

Lower numeric priority evaluates first. ALERT permits the query and records evidence; BLOCK stops the answer; ALLOW creates an approved path.

# Evidence and diagnosis

Check exact VPC association, association and rule priorities, action, block response, domain-list pattern/update, managed-list selection, Resolver query logs, match/block metrics, client resolver path, and CloudTrail changes.

# Safe operations

Start a new list in ALERT, baseline legitimate queries, add narrow higher-priority exceptions, change to BLOCK, monitor failures and block volume, and retain rollback to ALERT.

# Related pages

- [Network protection selection](../decision-guides/network-protection-selection.md)
- [DNS resolution failure](../playbooks/dns-resolution-failure.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
