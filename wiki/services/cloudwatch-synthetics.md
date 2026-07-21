---
type: AWS Feature
title: CloudWatch Synthetics
parent_services: [CloudWatch]
description: Runs scripted canaries that validate DNS, TLS, HTTP, and application transactions on a schedule.
tags: ["soa-c03", "domain-5", "cloudwatch", "synthetics"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.5"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md
status: verified
---

# Core model

A canary executes a controlled user or API journey and records step, latency, screenshot or artifact, and log evidence. It validates more than network reachability.

# Decision boundaries

Use a canary when the question is whether a DNS/TLS/HTTP/application transaction succeeds. Use Network Synthetic Monitor for configured hybrid network probes, Network Flow Monitor for real TCP flows, and Reachability Analyzer for packet-free configuration modeling.

# Evidence and diagnosis

Inspect schedule and run state, VPC configuration if used, DNS/TLS/HTTP step, artifact/log delivery, IAM/KMS, endpoint reachability, application response, and alarm dimensions.

# Safe operations

Use non-destructive test identities/data, protect artifacts, keep the script deterministic, run from relevant locations, and verify both canary recovery and real user/application signals.

# Related pages

- [Network monitor selection](../decision-guides/network-monitor-selection.md)
- [Network performance diagnosis](../playbooks/network-performance-diagnosis.md)

# Sources

- [Skill 5.3.5](../../raw/skills/5.3.5-configure-and-analyze-cloudwatch-network-monitoring-services.md)
