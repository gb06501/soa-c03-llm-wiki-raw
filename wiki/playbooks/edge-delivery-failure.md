---
type: Troubleshooting Playbook
title: Edge delivery failure
description: Diagnoses CloudFront behavior, OAC, cache/origin/TLS and Global Accelerator listener, dial, weight, health, and endpoint paths.
tags: ["soa-c03", "domain-5", "troubleshooting", "edge", "cloudfront"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.2.3"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.2.3-configure-content-and-service-distribution.md
status: verified
---

# Trigger

CloudFront or Global Accelerator returns errors, chooses the wrong origin/Region/endpoint, exposes an origin, or fails to deliver through the intended domain, protocol, or access model.

# Evidence path

1. Identify whether the service is CloudFront, Global Accelerator, Route 53, or Regional ELB.
2. Record requested hostname/static IP, protocol/port/path, time, status, and client.
3. For CloudFront, find first matching behavior, policy set, viewer TLS, cache result, and origin selection.
4. For S3, verify REST origin, OAC attachment, bucket policy, object key, and KMS.
5. For custom origin, inspect DNS, listener/port, SG/firewall, TLS name/chain, health, and origin logs.
6. Check direct-origin bypass and WAF coverage.
7. For Global Accelerator, inspect listener, endpoint-group Region/dial, endpoint weight/health, and LB/application.
8. Correlate metrics, edge/flow/access logs, and CloudTrail change.

# Failure map

| Symptom | Direction |
| --- | --- |
| CloudFront S3 403 | OAC, bucket/KMS policy, key/path |
| CloudFront 502 | origin DNS/TLS/listener/protocol |
| CloudFront 504 | origin reachability/latency/health |
| Wrong origin | behavior path/order |
| Direct origin works | missing restriction/bypass |
| GA Region unused | traffic dial or group health |
| GA endpoint unused | endpoint weight/health |
| Static IP unreachable | accelerator/listener/client network |
| Health good, app fails | application beyond service health |

# Safe action

Introduce a tested behavior/origin or low-dial endpoint group, validate privacy and health, shift gradually, close bypass only after proof, and retain previous policy/dial.

# Verification

Prove DNS/static IP, behavior/listener, certificate/policy, cache/origin or dial/weight, endpoint health, logs/metrics, direct-origin restriction, and application result.

# Rollback

Restore prior behavior/origin/policy or accelerator dial/weight and keep previous endpoints healthy.

# Escalation

Provide request evidence, configuration objects, cache/origin or endpoint health, policy/TLS evidence, direct-path test, and recent change.

# Related pages

- [Content and service distribution](../services/content-distribution.md)
- [Content distribution selection](../decision-guides/content-distribution-selection.md)

# Sources

- [Skill 5.2.3](../../raw/skills/5.2.3-configure-content-and-service-distribution.md)
