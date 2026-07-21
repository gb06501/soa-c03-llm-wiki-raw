---
type: AWS Service
title: WAF
service_id: waf
description: Filters supported HTTP and HTTPS requests using ordered web ACL rules, managed rule groups, rate controls, and request evidence.
tags: ["soa-c03", "domain-5", "waf", "web-security"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3", "5.2.3", "5.3.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---
# Core model

`web ACL -> numeric-priority rules -> terminating action or default action -> associated web resource`

WAF understands web requests. It is not a general TCP/UDP firewall.

# Rule behavior

| Action | Effect |
| --- | --- |
| ALLOW / BLOCK | Terminating decision |
| COUNT | Observe and continue |
| CAPTCHA / CHALLENGE | Require valid client token behavior |
| Managed rule group | Maintained rule set that can be overridden or scoped |

CloudFront and Regional web ACLs have different scopes.

# Evidence and diagnosis

Check exact association, scope, rule priority, terminating rule, default action, managed-rule override or exclusion, labels, rate aggregation, sampled requests, full logs, application access logs, and CloudTrail changes.

# Safe operations

Deploy a rule or managed group in COUNT, baseline legitimate traffic, create narrow exceptions, change to enforcement, monitor block/error trends, and retain rapid rollback to COUNT.

# Related decisions

- [Network protection selection](../decision-guides/network-protection-selection.md)
- [Network request tracing](../playbooks/network-request-tracing.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
