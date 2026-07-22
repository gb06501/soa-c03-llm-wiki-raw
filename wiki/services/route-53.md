---
type: AWS Service
title: Route 53
service_id: route-53
description: Provides authoritative DNS, health-aware routing, and VPC DNS resolution and forwarding.
tags: ["soa-c03", "domain-4", "route-53", "dns", domain-5, resolver, dns-routing]
timestamp: 2026-07-22T05:15:00Z
skill_ids: ["2.2.1", "2.2.2", "2.3.2", "2.3.4", "4.2.3", "5.1.3", "5.2.1", "5.2.2", "5.2.3", "5.3.2", "5.3.5"]
domain_ids: ["2", "4", "5"]
sources:
  - /raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md
  - /raw/skills/2.2.2-configure-fault-tolerant-systems.md
  - /raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md
  - /raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md
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

Route 53 answers DNS questions; it does not proxy application traffic. Public and private hosted zones provide authoritative records, routing policies and health checks select eligible answers, and Resolver endpoints and rules connect VPC DNS with external namespaces. The observed answer also depends on delegation, associations, rule selection, TTLs, and caches.

# Decision boundaries

Certificate DNS validation records prove control of a name; they do not route application traffic. Alias or ordinary records must target the intended service and avoid stale alternate endpoints.

# Evidence and diagnosis

Query the exact record and resolver path, verify authoritative name servers, validation CNAME name and value, TTL and propagation, endpoint target, and requested hostname.

# Safe operations

Automate validation records in controlled zones, preserve them for managed renewal, use change review for public records, and test resolution from the client environment before changing TLS.

# Related decisions

- [TLS certificate selection](../decision-guides/tls-certificate-selection.md)
- [Encryption in transit](../concepts/encryption-in-transit.md)

# DNS, Resolver, and routing

Route 53 provides authoritative public/private zones, Resolver endpoints and rules, routing policies, health checks, and query evidence. A DNS answer selects an address; it does not proxy or prove the target path.

Inbound Resolver endpoints accept external queries into AWS; outbound endpoints forward matching VPC queries to external DNS. Most-specific zone/rule selection, VPC association, endpoint network path, and cache TTL determine the observed answer.

Routing policies select eligible records by weights, latency, failover role, geography, proximity, multivalue health, or source CIDR. Failover includes detection plus caches and can fail open when every record is unhealthy.

- [DNS resolution selection](../decision-guides/dns-resolution-selection.md)
- [DNS routing policy selection](../decision-guides/dns-routing-policy-selection.md)
- [DNS resolution failure](../playbooks/dns-resolution-failure.md)

# Health checks and failover

Route 53 health controls DNS answers; it does not change load-balancer target membership or move existing connections. Public checkers cannot directly test private endpoints, so a published metric and alarm may bridge private health.

DNS failover still depends on record association, policy, health state, TTL and resolver cache, healthy destination capacity, and recovered application dependencies.

# Sources

- [Skill 2.2.1](../../raw/skills/2.2.1-configure-and-troubleshoot-elb-and-route-53-health-checks.md)
- [Skill 2.2.2](../../raw/skills/2.2.2-configure-fault-tolerant-systems.md)
- [Skill 2.3.2](../../raw/skills/2.3.2-restore-databases-to-meet-rto-rpo-and-cost-requirements.md)
- [Skill 2.3.4](../../raw/skills/2.3.4-follow-disaster-recovery-procedures-and-best-practices.md)
- [Skill 4.2.3](../../raw/skills/4.2.3-implement-configure-and-troubleshoot-encryption-in-transit.md)
- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.2.1](../../raw/skills/5.2.1-configure-dns-and-route-53-resolver.md)
- [Skill 5.2.2](../../raw/skills/5.2.2-implement-route-53-routing-policies-configurations-and-query-logging.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
