---
type: Troubleshooting Playbook
title: Network request tracing
description: Correlates network, edge, protection, load-balancer, container, and application logs to locate the first failing layer.
tags: ["soa-c03", "domain-5", "troubleshooting", "network-logs", "tracing"]
timestamp: 2026-07-21T22:45:00+02:00
skill_ids: ["5.3.2"]
domain_ids: ["5"]
sources:
  - /raw/skills/5.3.2-collect-and-interpret-networking-logs.md
status: verified
---

# Trigger

A request fails, is blocked, is slow, or lacks an expected log, and the responsible network/application layer is unclear.

# Evidence path

1. Normalize UTC time, source/client and transformed addresses, destination, protocol/port, host/path, request ID, and expected route.
2. Confirm logging scope, filter, destination, permissions, KMS, retention, and delivery health.
3. Start at the first expected layer and find the last observed request.
4. Inspect Flow Log action/status and exact ENI/direction.
5. Inspect WAF terminating action, CloudFront result/status/Age, or ELB/target status and processing time.
6. Inspect proxy/sidecar/container/application and dependency logs.
7. Use route/SG/NACL/policy and CloudTrail/Config changes to explain the first bad transition.
8. Reproduce one known request after the minimal correction.

# Failure map

| Evidence | Direction |
| --- | --- |
| Flow REJECT | candidate SG/NACL at captured ENI |
| Flow ACCEPT, no app log | OS/listener/proxy/application or return path |
| ELB log, target absent | listener/rule/healthy target/connectivity |
| Target status present | target/application result |
| WAF BLOCK | terminating rule |
| WAF ALLOW, app 403 | origin/application after WAF |
| CloudFront hit, no origin log | expected cached response |
| No expected log | no traffic, cache/bypass, scope/filter/delivery failure |

# Safe action

Preserve evidence, enable temporary logging narrowly, change the exact rule/path/listener/application cause, reproduce, and remove sensitive debug verbosity while retaining required audit logs.

# Verification

Confirm the known request appears with expected status and timing in every traversed layer and the user/application result succeeds.

# Rollback

Restore the prior configuration if the correction changes unrelated traffic; retain the captured evidence and test request.

# Escalation

Provide correlated timestamps/IDs, last-good and first-bad logs, configuration state, missing-log validation, and application impact.

# Related pages

- [Network logging](../concepts/network-logging.md)
- [Network log selection](../decision-guides/network-log-selection.md)

# Sources

- [Skill 5.3.2](../../raw/skills/5.3.2-collect-and-interpret-networking-logs.md)
