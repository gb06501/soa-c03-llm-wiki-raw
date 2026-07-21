---
type: Troubleshooting Playbook
title: Third-party deployment failure
description: Diagnoses Terraform initialization, plan, lock, state, partial apply, drift, account, and Git release failures.
tags: [soa-c03, domain-3, terraform, git, troubleshooting]
timestamp: 2026-07-21T16:00:00+02:00
skill_ids: ["3.1.6"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md
status: verified
---

# Trigger

Terraform cannot initialize, plan, apply, or reconcile safely, or the deployed code identity and ownership are uncertain.

# Evidence path

1. Verify exact Git commit/tag and inspect unresolved merge changes.
2. Verify backend, workspace, provider alias, account, Region, and caller identity.
3. Run init, validate, and a fresh plan; inspect every destroy or replacement.
4. Check state lock owner and whether its operation is still active.
5. Compare configuration, state address/ID, and the real resource.
6. After partial apply, read provider error and successful changes before replanning.
7. Check whether another tool or manual edit owns the same object/property.

# Failure map

| Symptom | Direction |
| --- | --- |
| Init fails | backend/provider/module credentials, network, or version |
| Wrong environment plan | provider account/Region, workspace, backend |
| Unexpected destroy/create | address change, missing move/import, configuration drift |
| Lock held | active operation or proven stale lock |
| Apply partially succeeds | provider error plus new state and AWS reality |
| Import followed by changes | configuration does not match imported object |
| Merge is text-clean but unsafe | new semantic plan differs |
| Secret committed | rotate/revoke before cleanup |

# Safe action

Do not force-unlock, edit state, or apply an unreviewed plan. Restore one clear owner, repair configuration or mapping, preserve/version the remote state, create a fresh plan, and apply only the reviewed commit and plan.

# Verification

Confirm state lock release, state-to-AWS mapping, correct account/Region, no unexpected destroy/replace, healthy application behavior, protected backend history, and clean secret scanning/release identity.

# Related concepts

- [Terraform and Git controls](/concepts/third-party-deployment-tools.md)
- [Tool selection](/decision-guides/deployment-tool-selection.md)

# Sources

- [Skill 3.1.6](../../raw/skills/3.1.6-use-and-manage-third-party-deployment-tools.md)
