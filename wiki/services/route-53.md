---
type: AWS Service
title: Route 53
service_id: route-53
description: Provides DNS routing and validation records used by secure endpoint and certificate workflows.
tags: ["soa-c03", "domain-4", "route-53", "dns", domain-5, resolver, dns-routing]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["4.2.3", "5.1.3", "5.2.1", "5.2.2", "5.2.3", "5.3.2", "5.3.5"]
domain_ids: ["4", "5"]
sources:
  - /raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.2.1-configure-dns-and-route-53-resolver.md
  - /raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---
# Core model

Route 53 maps names to endpoints and can host DNS validation records for managed certificates. DNS correctness precedes TLS: clients must reach the intended endpoint before certificate and protocol checks can succeed.

# Decision boundaries

Certificate DNS validation records prove control of a name; they do not route application traffic. Alias or ordinary records must target the intended service and avoid stale alternate endpoints.

# Evidence and diagnosis

Query the exact record and resolver path, verify authoritative name servers, validation CNAME name and value, TTL and propagation, endpoint target, and requested hostname.

# Safe operations

Automate validation records in controlled zones, preserve them for managed renewal, use change review for public records, and test resolution from the client environment before changing TLS.

# Related decisions

- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [Encryption in transit](../concepts/encryption-in-transit.md)

# Domain 5: DNS, Resolver, and routing

Route 53 provides authoritative public/private zones, Resolver endpoints and rules, routing policies, health checks, and query evidence. A DNS answer selects an address; it does not proxy or prove the target path.

Inbound Resolver endpoints accept external queries into AWS; outbound endpoints forward matching VPC queries to external DNS. Most-specific zone/rule selection, VPC association, endpoint network path, and cache TTL determine the observed answer.

Routing policies select eligible records by weights, latency, failover role, geography, proximity, multivalue health, or source CIDR. Failover includes detection plus caches and can fail open when every record is unhealthy.

- [DNS resolution selection](../decision-guides/dns-resolution-selection.md)
- [DNS routing policy selection](../decision-guides/dns-routing-policy-selection.md)
- [DNS resolution failure](../playbooks/dns-resolution-failure.md)

# Sources

- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
