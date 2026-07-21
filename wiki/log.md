# Wiki update log

## [2026-07-21] reconcile | Canonical service coverage correction

- **Root cause:** The first coverage schema allowed many distinct services to collapse into one broad facet destination.
- **Governance:** Added canonical short-name service registry, an AWS Feature page type, and atomic facet-item requirements.
- **Correction:** Added 14 canonical Domain 3 service pages and reclassified broad or feature-oriented pages without renaming stable paths.
- **Integration:** Enriched EC2, S3, EventBridge, SNS, and Systems Manager Automation with Domain 3 sources.
- **Migration:** Domains 1-2 remain implemented but are marked needs-reconciliation until their facets are audited atomically.
- **Coverage:** Replaced eight aggregate Domain 3 service facets with 40 atomic service, feature, mechanism, and external-tool items.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] ingest | Domain 3 bootstrap

- **Inventory:** Processed all eight Domain 3 skill sources against the global page plan.
- **Creation:** Added 27 pages covering images, infrastructure as code, diagnostics, cross-account provisioning, deployment strategies, Terraform/Git, fleet operations, and event automation.
- **Coverage:** Validated 31 of 53 corpus skills; Domains 4-5 remain planned.
- **Navigation:** Added Domain 3 indexes and repaired the missing Domain 2 entry in the learning catalogue.
- **Validation:** Resolved structural links and every Domain 3 facet destination.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] ingest | Domain 2 bootstrap

- **Inventory:** Processed all nine Domain 2 skill sources against the global page plan.
- **Creation:** Added 30 pages covering scaling, caching, health checks, fault tolerance, backup, restore, versioning, and disaster recovery.
- **Coverage:** Validated 23 of 53 corpus skills; Domains 3-5 remain planned.
- **Validation:** Resolved structural links and every Domain 2 facet destination.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] reconcile | Global plan and Domain 1 semantic coverage

- **Inventory:** Read all 53 immutable skill files and recorded their blob SHAs.
- **Planning:** Added a 157-page corpus plan covering all five domains and cross-domain reconciliation.
- **Creation:** Added nine missing Domain 1 decision guides.
- **Validation:** Mapped all Domain 1 knowledge facets to concrete pages and named sections.
- **Status:** Domain 1 validated; Domains 2-5 remain planned; corpus reconciliation remains planned.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] ingest | Domain 1 bootstrap

- **Creation:** Generated 23 source-grounded knowledge pages from all 14 Domain 1 skills.
- **Creation:** Added progressive indexes, a Domain 1 learning path, and processing manifest.
- **Synthesis:** Connected observability, automation, compute, storage, database, and troubleshooting knowledge.
- **Validation:** Preserved `raw/`, checked required metadata, sources, internal links, indexes, and duplicate identities.
- **Gap:** No external AWS documentation was imported; knowledge remains bounded by the supplied study sources.

