# Wiki update log

## [2026-07-22] repair | Global service models and deterministic sources

- **Root cause:** Incremental domain batches appended their sources and knowledge to shared pages without re-evaluating the page's corpus-global identity.
- **Service models:** Reframed 11 cross-domain service descriptions and primary models around the service itself; retained networking, cost, security, performance, and recovery knowledge as scoped applications.
- **Source order:** Sorted `skill_ids`, `domain_ids`, frontmatter sources, and readable source links numerically across every affected semantic page.
- **Traceability:** Expanded two legacy Domain 1 aggregate source sections so every declared raw skill has an exact readable link.
- **Governance:** Added a standard-library semantic validator for deterministic metadata, exact source parity, and batch-neutral service framing, and added it to pull-request checks.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-22] repair | Learner-facing semantic headings

- **Root cause:** Incremental build labels such as “Domain 5” and “Corpus reconciliation” leaked from generation batches into global service and concept pages.
- **Repair:** Replaced batch-history headings with subject headings while retaining all underlying knowledge and source metadata.
- **Coverage:** Updated every affected named-section destination so atomic coverage still resolves.
- **Scope:** Machine-readable `skill_ids`, `domain_ids`, and tags remain metadata; learner-facing knowledge is domain-neutral.
- **Source:** No file under `raw/` changed.

## [2026-07-22] reconcile | Complete-corpus atomic coverage

- **Scope:** Reconciled all 53 immutable skills after the five domain bootstraps.
- **Atomic coverage:** Replaced the 23 legacy Domain 1-2 aggregate service facets with 231 atomic service, feature, and mechanism items; all five domains and all 53 skills are now validated.
- **Identity repair:** Merged the duplicate planned `evidence-selection.md` identity into Observability signal selection and removed the last planned semantic destination.
- **Creation:** Added 20 exact pages for 13 canonical AWS services/products and 7 service-owned features that previously lacked independent identities.
- **Integration:** Enriched 35 shared service pages and the observability concept with Domain 1-2 sources, decisions, evidence, failure boundaries, and recovery behavior.
- **Corpus checks:** Reconciled canonical service identity, generated navigation, cross-domain dependencies, duplicate titles, orphan visibility, and full-tree links.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] generate | Domain 5 networking and content delivery

- **Scope:** Processed all 12 immutable Domain 5 skills with 122 atomic service, feature, mechanism, concept, decision, and troubleshooting coverage items.
- **Knowledge:** Added 58 semantic pages: 10 canonical AWS service/product pages, 15 AWS feature pages, 10 concepts, 11 decision guides, 10 troubleshooting playbooks, 1 exam-trap page, and 1 learning path.
- **Integration:** Enriched nine shared service pages with Domain 5 source material while retaining their stable identities and paths.
- **Identity repair:** Reclassified nine broad planned service bundles as features or concepts and registered only exact AWS service/product identities.
- **State:** Marked every Domain 5 facet destination validated and updated the page plan, manifest, service registry, indexes, and generated navigation.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] generate | Domain 4 security and compliance

- **Scope:** Processed all 10 immutable Domain 4 skills with 86 atomic service, feature, and mechanism coverage items.
- **Knowledge:** Added 58 semantic pages: 25 canonical AWS service/product pages, 2 AWS feature pages, 11 concepts, 10 decision guides, 8 troubleshooting playbooks, 1 exam-trap page, and 1 learning path.
- **Identity repair:** Reclassified six broad planned service bundles as concepts and registered only exact AWS service/product identities.
- **State:** Marked every Domain 4 facet destination validated and updated the page plan, manifest, service registry, indexes, and generated navigation.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] repair | Root navigation deduplication

- **Root cause:** Domain sections repeated global service, concept, decision-guide, and playbook catalogue links without applying a domain filter.
- **Repair:** Replaced the repeated sections with one domain list, one skill entry, and one canonical knowledge-type catalogue.
- **Governance:** Global knowledge-type links now appear once; domain-specific navigation belongs in generated domain views.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] generate | Domain and skill navigation

- **Navigation:** Added deterministic views for all five domains and all 53 skill IDs.
- **Traceability:** Each skill view links its immutable raw source, coverage status, implemented knowledge, planned knowledge, and processing state.
- **Retrieval:** Each domain view groups skills and generated pages while keeping planned destinations non-clickable.
- **Governance:** Kept frontmatter identifiers machine-readable and treated tags as search metadata rather than generating low-value tag pages.
- **Automation:** Added a reproducible navigation generator and freshness check.
- **Source:** No file under `raw/` changed and no external knowledge was added.

## [2026-07-21] repair | Repository-wide navigation consistency

- **Root cause:** Bundle-root links such as `/concepts/...` were validated as if `wiki/` were a web root, but GitHub renders them from the site root.
- **Repair:** Converted 129 links in 42 pages to GitHub-safe file-relative paths.
- **Indexes:** Standardized Domain 1-3 headings and entry formats across the root, concept, decision-guide, playbook, exam-trap, and learning catalogues.
- **Governance:** Required full-tree link validation and prohibited clickable links to destinations that do not exist.
- **Automation:** Added a repository validator and pull-request quality workflow.
- **Source:** No file under `raw/` changed and no external knowledge was added.

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



