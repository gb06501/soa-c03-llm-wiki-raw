---
type: AWS Service
title: Service Catalog
service_id: service-catalog
description: Publishes approved infrastructure products with controlled versions, principals, constraints, and launch roles.
tags: [soa-c03, domain-3, service-catalog, governance]
timestamp: 2026-07-21T18:00:00+02:00
skill_ids: ["3.1.2", "3.1.3"]
domain_ids: ["3"]
sources:
  - /raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md
  - /raw/skills/3.1.3-identify-and-remediate-deployment-issues.md
status: verified
---

# Core model

```text
portfolio -> product -> provisioning artifact/version -> constraints
          -> principal access
launch -> provisioned product -> underlying CloudFormation stack
```

# Permission boundary

A launch constraint role allows an authorized user to provision an approved product without receiving every permission used by the underlying template. User access, portfolio association, launch role, `PassRole`, constraints, CloudFormation permissions, resource policies, and KMS remain separate gates.

# Selection

Use Service Catalog when a central team must expose approved, versioned infrastructure while limiting consumer choices and underlying service permissions. Use direct CloudFormation or CDK when the operator owns the stack definition and deployment permissions.

# Evidence and failures

If the product is absent, inspect portfolio sharing, principal association, and artifact version. If launch is denied, inspect the launch constraint role and `PassRole`. If provisioning starts and fails, follow the provisioned product into the underlying CloudFormation stack and its first failed resource.

# Verification

Confirm the intended product version and constraints, successful provisioned-product status, healthy underlying resources, and the expected separation between consumer and launch-role permissions.

# Related concepts

- [CloudFormation](/services/cloudformation.md)
- [Infrastructure provisioning selection](/decision-guides/infrastructure-provisioning-selection.md)

# Sources

- [Skill 3.1.2](../../raw/skills/3.1.2-create-and-manage-resources-with-cloudformation-and-cdk.md)
- [Skill 3.1.3](../../raw/skills/3.1.3-identify-and-remediate-deployment-issues.md)
