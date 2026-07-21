---
type: AWS Service
title: Shield
service_id: shield
description: Provides baseline and advanced DDoS protection for supported AWS edge and internet-facing resources.
tags: ["soa-c03", "domain-5", "shield", "ddos"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.1.3", "5.2.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.1.3-audit-network-protection-services-in-one-account.md
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
status: verified
---
# Core model

Shield protects against distributed denial-of-service events. Shield Standard provides automatic baseline protection; Shield Advanced adds explicit protected resources, enhanced visibility, response workflows, and supported cost-protection capabilities.

# Advanced operating objects

- Subscription and protected resource
- Protection group
- DDoS event and mitigation evidence
- Associated health check
- Emergency and response contacts
- DDoS Response Team access configuration

# Decision boundaries

Use WAF for application-request patterns such as SQL injection or abusive HTTP rate rules. Use scaling, caching, and origin protection to keep the application resilient. A Shield Advanced subscription alone does not prove eligible resources or response workflows are configured.

# Evidence and diagnosis

Inventory eligible versus protected resources, events and vectors, mitigations, health associations, response contacts, WAF/web behavior, origin load, and alternate exposed paths.

# Safe operations

Protect critical resources explicitly, associate meaningful health checks, rehearse escalation, keep origin paths restricted, and validate application capacity and recovery during simulations or events.

# Related decisions

- [Network protection selection](../decision-guides/network-protection-selection.md)
- [Network protection gap](../playbooks/network-protection-gap.md)

# Sources

- [Skill 5.1.3](../../raw/skills/5.1.3-audit-network-protection-services-in-one-account.md)
- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
