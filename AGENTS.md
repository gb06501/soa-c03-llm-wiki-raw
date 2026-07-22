# AGENTS.md

## Purpose

This repository is a persistent, source-grounded study wiki for the **AWS Certified CloudOps Engineer - Associate (SOA-C03)** exam.

The repository must help the learner:

1. Understand AWS mechanisms, not only memorize answers.
2. Choose the correct service or configuration from scenario clues.
3. Diagnose operational problems from evidence.
4. Recognize exam traps, exceptions, and misleading wording.
5. Connect knowledge that is currently distributed across multiple official skills.
6. Accumulate reusable knowledge instead of re-deriving it in each chat.

Use short, precise language with high information density. Prefer decision tables, causal chains, comparisons, and concrete scenarios over long narrative prose.

## Authority and source boundaries

### Default authority

The files under `raw/` are the repository's source of truth.

- Treat `raw/` as immutable.
- Never rewrite, normalize, summarize in place, rename, move, or delete a raw file.
- Generated knowledge must be written under `wiki/`.
- Every material claim in `wiki/` must be traceable to one or more files under `raw/`.
- Do not silently add AWS knowledge from model memory.
- If the repository does not support a claim, label it as a knowledge gap.

### External research

Do not browse or add external knowledge unless the user explicitly requests current verification or research.

When external research is requested:

1. Prefer official AWS documentation.
2. Save imported source material or a source record under `raw/references/`.
3. Record the retrieval date and canonical URL.
4. Distinguish external facts from the original SOA-C03 study source.
5. Update generated pages only after the external source is preserved and cited.
6. Never silently replace source-grounded content with newer information.

## Repository layers

| Path | Ownership | Purpose |
| --- | --- | --- |
| `raw/source/` | Human/source-owned | Complete original study document |
| `raw/skills/` | Human/source-owned | The 53 immutable skill-level source files |
| `raw/references/` | Human-approved | Optional imported authoritative references |
| `wiki/` | Agent-maintained | Cross-linked, generated knowledge |
| `wiki/index.md` | Agent-maintained | Progressive-disclosure catalogue |
| `wiki/domains/` | Agent-generated | Domain views across source skills and generated knowledge |
| `wiki/skills/` | Agent-generated | Skill-ID views linking raw sources, coverage status, and generated pages |
| `wiki/log.md` | Agent-maintained | Append-only history of ingests and material updates |
| `state/manifest.yaml` | Agent-maintained | Source versions and processing state |
| `state/coverage.yaml` | Agent-maintained | Corpus-wide skill, knowledge-facet, and page coverage |
| `AGENTS.md` | Human and agent co-maintained | Operating contract for the wiki |

The raw layer and generated wiki layer must remain visibly separate.

## Generated wiki structure

Use this initial structure:

```text
wiki/
  index.md
  log.md
  domains/
  skills/
  services/
  concepts/
  comparisons/
  decision-guides/
  playbooks/
  exam-traps/
  learning/
    paths/
    questions/
    knowledge-gaps/
```

Create subdirectory `index.md` files when a directory has enough pages that progressive disclosure becomes useful.

For every domain-aware catalogue:

- use `## Domain N: Domain name` for each implemented domain;
- use the same heading depth and entry format for every domain;
- use optional `###` topic groups consistently beneath domain headings;
- never leave Domain 1 entries unheaded while later domains have explicit headings.

### Page types

Use a small, stable vocabulary:

- `AWS Service` — exactly one canonical AWS service or AWS product recorded in `state/aws-service-registry.yaml`.
- `AWS Feature` — a named feature, component, or control surface owned by one or more canonical AWS services.
- `Concept` — an operational or architectural mechanism.
- `Comparison` — two or more choices that exam scenarios commonly contrast.
- `Decision Guide` — clue-to-choice rules for selecting an AWS solution.
- `Troubleshooting Playbook` — symptom, evidence, cause, action, and verification.
- `Exam Trap` — a misconception, tempting wrong choice, or important exception.
- `Learning Path` — an ordered study sequence across related knowledge.
- `Practice Set` — scenario questions and evaluated answers.
- `Knowledge Gap` — missing, uncertain, contradictory, or weakly supported knowledge.

Do not invent new page types when an existing type is adequate.

### Canonical service identity

- Use short, recognizable service names such as `EC2`, `ECR`, `CloudFormation`, and `Systems Manager`; an `AWS` or `Amazon` display prefix is optional.
- Every page with `type: AWS Service` must represent exactly one entry in `state/aws-service-registry.yaml`.
- Its `title` must equal that registry entry's `display_name`, and its `service_id` must equal the registry key.
- Activity, outcome, and multi-service names such as “EC2 optimization,” “compute scaling,” “shared storage,” and “image management” are not AWS Service identities.
- Use `AWS Feature` for a service-owned feature. Include `parent_services` with registry display names.
- Use `Concept` when a mechanism spans multiple services or describes an operational model.
- Keep stable file paths when correcting an existing page's type or title unless a rename has clear navigation value and all inbound links are updated.
- The service index must distinguish canonical service pages from feature and cross-service pages.
- Canonical service pages are corpus-global; they are not owned by the domain or batch that first created them.
- The `description` and primary content section must define the service independently of an exam domain, source file, or ingestion history.
- Put security, cost, networking, performance, availability, and recovery applications in subject-specific sections after the global service model.
- When a later skill adds a material use case, reassess the global description and primary model instead of only appending a batch-shaped section.
- Derive the global service model from the union of the page's declared sources; do not broaden it with uncited model memory.
- If the available sources support only a narrow service use case, keep the page explicitly partial or record a knowledge gap instead of inventing a comprehensive definition.

## OKF v0.1 conventions

The `wiki/` directory is the OKF knowledge bundle.

Each concept file must be UTF-8 Markdown with YAML frontmatter. At minimum, use:

```yaml
---
type: Decision Guide
title: Choosing an AWS monitoring mechanism
description: Selects metrics, logs, traces, events, or audit records from scenario clues.
tags: [soa-c03, monitoring, selection]
timestamp: 2026-07-21T00:00:00Z
skill_ids: ["1.1.1", "1.2.1"]
domain_ids: ["1"]
sources:
  - /raw/skills/1.1.1-configure-monitoring-and-logging-for-workloads.md
  - /raw/skills/1.2.1-analyze-performance-metrics-and-automate-remediation.md
status: verified
---
```

Rules:

- `type` is required.
- `title` must be human-readable and specific.
- `description` must be one concise sentence.
- `tags` must use lowercase stable terms.
- `timestamp` records the last meaningful content change in ISO 8601 format.
- `skill_ids` and `domain_ids` identify exam coverage.
- `sources` contains bundle-root-relative links to supporting raw files.
- Keep `skill_ids` and `domain_ids` unique and numerically sorted.
- Sort `sources` by numeric raw skill ID, followed by any non-skill references in lexical path order.
- The final readable `# Sources` links must exactly match the frontmatter source set and order.
- `status` is one of `verified`, `partial`, `disputed`, or `needs-research`.
- Preserve unknown frontmatter fields when updating a page.
- Use lowercase kebab-case filenames without spaces.
- A file path is the stable concept identity; do not rename pages casually.
- `AWS Service` pages require `service_id`.
- `AWS Feature` pages require `parent_services`.

The root `wiki/index.md` may declare:

```yaml
---
okf_version: "0.1"
---
```

Other index files should remain simple Markdown catalogues.

### Metadata navigation

Keep `tags`, `skill_ids`, and `domain_ids` as plain identifiers in YAML frontmatter. Do not replace them with Markdown links or nested URL objects.

Generate navigable projections instead:

- `wiki/domains/domain-N.md` collects every source skill, implemented page, planned page, and coverage status for one domain.
- `wiki/skills/ID.md` links one skill ID to its immutable raw source, implemented knowledge, planned knowledge, and processing state.
- `wiki/domains/index.md` and `wiki/skills/index.md` provide corpus-wide entry points.
- The root `wiki/index.md` lists each navigation dimension once. Global knowledge-type links must not be repeated inside domain sections; domain-specific navigation belongs in `wiki/domains/domain-N.md`.
- These files are derived catalogues, not new semantic knowledge objects, and do not add a page type or change coverage counts.
- Tags remain retrieval metadata. Do not generate one page per tag unless a demonstrated human workflow justifies the additional maintenance surface.
- Run `python3 scripts/generate_navigation.py` after raw skill metadata, wiki frontmatter, coverage status, or the page plan changes.
- Generated navigation files must not be edited manually.

## Content model

### Preferred structure

Choose sections that fit the page type. Typical sections include:

- `# Core model`
- `# When to use`
- `# When not to use`
- `# Decision rules`
- `# Evidence`
- `# Configuration path`
- `# Failure modes`
- `# Verification`
- `# Exam traps`
- `# Examples`
- `# Related concepts`
- `# Sources`

Do not force every heading into every page.

### Writing rules

- Lead with the decision or mechanism.
- Use short sentences and concrete AWS terminology.
- Avoid introductory filler and repeated definitions.
- Explain cause and effect explicitly.
- Separate availability, scalability, performance, security, and cost.
- Separate control-plane configuration from data-plane behavior.
- Separate diagnosis evidence from remediation action.
- Always include post-remediation verification in playbooks.
- Preserve exact qualifiers such as Region, Availability Zone, account, public, private, synchronous, asynchronous, managed, and customer-managed.
- State important exceptions next to the general rule.
- Do not use unsupported numeric limits, prices, defaults, or timing claims.
- Do not convert examples into universal rules.
- Use subject headings in semantic pages. Do not expose generation history such as “Corpus reconciliation,” “bootstrap,” “ingest,” or a contributing domain as the heading for global knowledge.
- Domain labels are appropriate only in explicitly domain-scoped navigation, learning, coverage, or assessment pages.

### Study-specific patterns

Prefer these reusable patterns:

```text
scenario clue -> required property -> AWS choice
symptom -> evidence -> likely cause -> safe action -> verification
requirement -> constraint -> rejected options -> selected option
tempting answer -> why it is wrong -> correct mental model
```

## Page granularity and deduplication

Create a new page when the subject:

- is a distinct reusable service, mechanism, decision, playbook, or misconception;
- is referenced by more than one skill or page; or
- deserves an independent lifecycle.

Update an existing page when new information concerns the same conceptual identity.

Shared-page integration is a whole-page revision, not an append-only operation. Read the existing page and its declared sources, classify new material as global identity or a scoped application, merge overlapping sections, remove redundant explanations, and keep one subject-based section hierarchy. Processing order must not determine the page description, heading order, or emphasis.

Do not:

- generate one wiki page merely because one raw file exists;
- copy whole raw sections into `wiki/`;
- create duplicate pages for synonyms;
- split a concept so narrowly that each page lacks independent value;
- combine unrelated concepts into a large generic page.

Prefer synthesis across skills. For example, an RDS availability page may draw from performance, fault-tolerance, backup, deployment, security, and networking skills.

Compactness does not override coverage. A decision boundary may live inside a service page instead of a standalone Decision Guide only when `state/coverage.yaml` identifies the containing page and section. Do not count a source as covered merely because it appears in frontmatter.

Coverage facets are containers, not atomic knowledge items. Each facet may contain multiple independently tracked `items`. Do not represent several services, decisions, evidence paths, or failure modes with one aggregate status merely because they share a source skill.

An item needs its own identity when it has an independent object model, configuration surface, permission boundary, evidence source, failure mode, or lifecycle. Several items may share a page only when the page contains a named section for each item and the combined page remains a coherent conceptual identity.

A `standalone` item must point to a page whose identity matches that item. A generic summary page is not a standalone destination for every service named inside it.

## Coverage model

Plan from the entire 53-skill corpus before generating or completing any individual domain. The global plan establishes stable concept identities and reveals cross-domain relationships; implementation may then proceed in reviewable domain-sized batches.

For every raw skill, inventory these knowledge facets:

- services, features, and mechanisms;
- scenario clues and requirements;
- decision boundaries and rejected alternatives;
- comparisons;
- evidence, metrics, logs, and diagnostic sequence;
- remediation choices and safety controls;
- failure modes and verification;
- exam traps and exceptions;
- cross-domain dependencies.

Record every applicable facet in `state/coverage.yaml`. Each facet must enumerate all applicable atomic items. Each item must map to one of:

- `standalone`: represented by a dedicated wiki page;
- `embedded`: represented by a named section in another page;
- `planned`: identified but not yet generated;
- `gap`: insufficient or contradictory source support;
- `not_applicable`: reviewed and intentionally omitted, with a reason.

A skill is `validated` only when every applicable facet item is mapped, every material decision boundary has a page-and-section destination, and every named AWS service is reconciled with `state/aws-service-registry.yaml`. Source citation alone is traceability, not coverage.

For shared pages, linking to an existing page is not enough. Add the new source, skill ID, domain ID, and material knowledge to that page, or record the item as planned or intentionally embedded elsewhere.

Coverage is evaluated at three levels:

1. **Skill coverage** — all applicable facets from each raw file are accounted for.
2. **Domain coverage** — domain-specific services, decisions, comparisons, playbooks, traps, and learning paths are navigable.
3. **Corpus coverage** — cross-domain concepts are synthesized once, duplicates are reconciled, and global indexes expose them.

## Cross-linking

- Use standard Markdown links between related wiki pages.
- Use file-relative links that GitHub can render, for example `[RDS](../services/rds-performance.md)`.
- Link a concept on its first meaningful mention.
- Add a `Related concepts` section when it materially improves navigation.
- Links must express useful relationships, not merely inflate graph density.
- Avoid isolated pages. If a page is intentionally isolated, record why in the log.
- Never publish a clickable link to a missing page. Record planned knowledge as plain text in `state/coverage.yaml` or a Knowledge Gap page until the destination exists.

## Source traceability

Every generated page must contain:

1. A `sources` frontmatter list.
2. A final `# Sources` section with readable links.
3. Relevant `skill_ids`.
4. Clear distinction between explicit source content and agent inference.

Use one readable source link for every frontmatter source entry. Keep the same exact paths and order. Do not substitute aggregate labels or range links such as “Skills 1.1.1–1.1.5” for the individual sources.

Use phrasing such as:

- **Source states:** directly supported.
- **Derived rule:** synthesis across cited sources.
- **Inference:** reasonable but not explicitly stated.
- **Knowledge gap:** insufficient support.

Never present an inference as an official AWS fact.

## Operating workflows

### 1. Query

For a read-only question:

1. Read `wiki/index.md` first if it exists.
2. Search relevant generated pages.
3. Fall back to `raw/skills/` when generated coverage is absent or insufficient.
4. Answer with links to the relevant wiki and raw files.
5. Cite skill IDs.
6. State uncertainty or missing coverage.
7. Do not modify the repository unless the user explicitly asks to persist the result.

### 2. Plan coverage and bootstrap domains

Use a **global-plan, incremental-build** workflow.

Before the first domain bootstrap or whenever the source corpus changes materially:

1. Inventory all 53 raw skills, not only the requested domain.
2. Extract candidate services, concepts, decisions, comparisons, playbooks, traps, and cross-domain dependencies.
3. Normalize synonyms and choose stable page identities.
4. Create or update the corpus-wide `state/coverage.yaml`.
5. Propose the global page plan and identify which pages span domains.
6. Mark unbuilt destinations as `planned`; do not call them covered.

For each domain-sized implementation batch:

1. Read the global coverage plan and every raw skill in the domain.
2. Reassess related pages from other domains so shared concepts are updated rather than duplicated.
   - Read the complete affected page, not only its final section.
   - Decide whether the new material changes the corpus-global model or belongs in an existing subject-specific section.
   - Consolidate overlapping sections and citations instead of preserving ingestion-batch boundaries.
   - Do not let domain processing order control presentation order or conceptual emphasis.
3. Create or update pages for every applicable facet.
4. Map every decision boundary to a standalone Decision Guide or a named decision section.
5. Add meaningful cross-links and update all relevant indexes.
6. Append the operation to `wiki/log.md`.
7. Update `state/manifest.yaml` and `state/coverage.yaml`.
8. Run structural and semantic quality gates.
9. Report planned, implemented, embedded, unsupported, and intentionally omitted items separately.
10. Use a dedicated branch and draft pull request for human review.

After the final domain batch, run a corpus reconciliation pass across all 53 skills. Audit every canonical service page against the union of its cited skills: verify its title and registry identity, source-grounded description, primary model, subject-based section taxonomy, and balance across domains. Correct first-domain bias and consolidate overlapping sections. Then merge duplicate identities, repair cross-domain links, verify global navigation, and keep unresolved gaps explicit.

Do not generate every page in one unreviewed batch merely because planning uses the whole corpus.

#### Broad generation requests

When the user asks to create “most” or “all” pages:

1. Treat the request as authorization to plan the complete requested source scope, not as permission to skip review boundaries.
2. Inventory the full scope and reconcile the global coverage map and page identities before creating pages.
3. Divide implementation into coherent domain- or subject-sized batches, with shared pages assigned deliberately rather than recreated.
4. Use one dedicated branch and draft pull request per independent batch.
5. Pause after each dependent batch for review or merge unless the user explicitly directs continuation.
6. Keep unbuilt destinations marked `planned`; do not report the broad request complete until every applicable facet is implemented, embedded, gapped, or intentionally omitted.

### 3. Ingest a changed or new source

1. Identify the source Git blob SHA or content hash.
2. Check `state/manifest.yaml`.
3. Determine which existing pages the source can affect.
4. Compare new claims with existing claims.
5. Update existing pages before creating duplicates.
6. Flag contradictions; do not silently choose one version.
7. Update links, indexes, log, and manifest.
8. Summarize created, changed, disputed, and missing knowledge.

### 4. Save a useful answer

Only persist an answer when the user asks.

- Save reusable explanations under the appropriate concept type.
- Integrate the answer into existing pages when possible.
- Do not save chat transcripts.
- Remove conversational phrasing.
- Add sources and cross-links.
- Record the update in `wiki/log.md`.

### 5. Practice and assessment

When generating questions:

- Use scenario-based questions rather than definition-only recall.
- Include enough clues for one defensible best answer.
- Make distractors plausible but wrong for a specific reason.
- State whether multiple selections are required.
- Keep answers separate from questions when requested.
- Map every question to skill IDs and source files.

When evaluating an answer:

1. Identify the selected answer and reasoning.
2. Judge correctness from repository sources.
3. Explain the decisive clue.
4. Explain why alternatives fail.
5. Identify the underlying misconception.
6. Suggest the smallest topic to review.
7. Create a `Knowledge Gap` page only when the user asks to track progress.

### 6. Lint and health check

Check for:

- unsupported claims;
- missing or invalid YAML frontmatter;
- missing `type`, title, description, tags, timestamp, status, or sources;
- broken internal links across the complete `wiki/` tree, resolved exactly as GitHub renders them;
- duplicate concept identities;
- `AWS Service` titles absent from the service registry;
- `AWS Feature` pages without valid parent services;
- broad pages incorrectly typed as AWS services;
- facet categories with several source items collapsed into one unitemized status;
- shared pages linked without incorporating the new source and skill ID;
- orphan pages;
- stale indexes;
- manifest entries that do not match source versions;
- contradictions or inconsistent terminology;
- pages with no meaningful synthesis beyond one raw source;
- raw files modified by an agent;
- important recurring concepts that lack a page.
- nondeterministic or mismatched `skill_ids`, `domain_ids`, frontmatter sources, and readable source links;
- canonical service descriptions or primary models shaped around one domain or ingestion batch instead of the service.
- learner-facing process-history headings in global semantic pages;
- append-only shared pages with overlapping or duplicate subject sections;
- global service claims broader than the union of their declared sources;
- aggregate readable source links that do not represent every declared source one-to-one.

Report findings before applying broad repairs unless the user requested the fixes.

## State and logging

### Manifest

Create `state/manifest.yaml` during the first bootstrap. Track, per raw file:

- path;
- Git blob SHA or stable content hash;
- processed timestamp;
- generated or updated wiki pages;
- processing status: `inventoried`, `planned`, `drafted`, or `validated`;
- unresolved gaps or contradictions.

Use the manifest to avoid reprocessing unchanged sources blindly. Use `state/coverage.yaml` for semantic completeness; do not overload the manifest with facet-level coverage.

### Log

Maintain `wiki/log.md` as newest-first, with entries such as:

```markdown
## [2026-07-21] ingest | Domain 1 bootstrap

- **Creation:** Added monitoring decision guides and CloudWatch concept pages.
- **Update:** Linked remediation playbooks to relevant evidence sources.
- **Gap:** Exact coverage for one service behavior requires an authoritative reference.
```

Do not rewrite historical entries except to repair an incorrect link.

## GitHub change policy

- Pure questions are read-only.
- Small explicitly requested documentation corrections may be committed directly.
- Ingestion, restructuring, or multi-file generation must use a dedicated branch and draft pull request.
- Use focused commits with clear messages.
- Never mix raw-source changes with generated-wiki changes.
- Never force-update branches or delete content unless explicitly authorized.
- In a pull request, summarize:
  - sources processed;
  - pages created;
  - pages updated;
  - contradictions and gaps;
  - validation performed.

## Quality gates

Before declaring generation complete, verify:

1. No file under `raw/` changed.
2. Every generated concept has valid OKF frontmatter.
3. Every generated claim has traceable source support or is labelled as inference.
4. All declared source files exist.
5. Every Markdown link in the complete `wiki/` tree resolves from its source file in GitHub; validation must not be limited to changed files.
6. Indexes include new and changed pages.
7. The update log and manifest are current.
8. No duplicate concept page was created.
9. The result improves cross-skill understanding rather than copying source text.
10. The content is concise enough to study but complete enough to make operational decisions.
11. Exam-critical exceptions and misleading alternatives are visible.
12. Every raw skill and applicable knowledge facet appears in `state/coverage.yaml`.
13. Every material decision boundary maps to a standalone guide or a named page section.
14. No item marked `standalone` or `embedded` points to a missing page or section.
15. Items marked `planned`, `gap`, or `not_applicable` are reported and justified.
16. Domain completion is not inferred from source citation counts or page counts.
17. A final corpus reconciliation checks cross-domain duplication and missing global navigation.
18. The pull request reports unresolved uncertainty honestly.
19. Every `AWS Service` page title and `service_id` matches the canonical registry.
20. Every `AWS Feature` page names valid `parent_services`.
21. Every service named materially in the requested raw scope has an atomic coverage item.
22. Generic concept pages are not counted as standalone service coverage.
23. Shared cross-domain service pages incorporate the new source and skill ID, not only a link.
24. Validation reports atomic item counts, not only facet-category counts.
25. Domain-aware indexes use the same `## Domain N: Domain name` structure for every implemented domain.
26. Run `python3 scripts/validate_wiki_links.py`; it must report zero invalid links.
27. Run `python3 scripts/generate_navigation.py --check`; all domain and skill views must match their source state.
28. Every raw skill ID resolves through `wiki/skills/`, and every domain ID resolves through `wiki/domains/`.
29. Run `python3 scripts/validate_wiki_semantics.py`; deterministic metadata, exact source parity, and explicit batch-language checks must pass.
30. Treat semantic-validator success as structural evidence only. Manually review the description, primary section, and subject balance of every affected `AWS Service` page; automation cannot prove semantic neutrality.
31. Every affected shared page has a subject-based hierarchy without duplicate or ingestion-history sections.

## Definition of done

A knowledge-generation task is done when:

- the requested source scope is fully processed at facet level, not merely cited;
- all applicable decision boundaries have explicit destinations;
- `state/coverage.yaml` contains no unexplained omissions for the requested scope;
- generated pages are source-grounded and cross-linked;
- every affected shared page has received a whole-page semantic review rather than an append-only update;
- indexes, log, and manifest are updated;
- quality gates pass;
- the learner can navigate from a scenario or AWS service to the relevant decision rules, evidence, playbooks, traps, and source skills;
- a human-reviewable change set is available.

## Recommended user commands

Examples of effective instructions:

### Query

> Using only this repository, answer the following SOA-C03 question. Start with the wiki, fall back to raw skills, cite file paths and skill IDs, and state any missing coverage.

### Plan the corpus

> Inventory all 53 skills and create the global coverage map and page plan according to AGENTS.md. Do not generate content yet. Account for services, decisions, comparisons, evidence, remediation, playbooks, traps, and cross-domain concepts.

### Bootstrap

> Bootstrap Domain 1 from the global coverage plan according to AGENTS.md. Treat raw as immutable, account for every applicable facet and decision boundary, generate the OKF wiki on a branch, run structural and semantic quality gates, and open a draft PR.

### Reconcile the corpus

> After all domain batches, reconcile the complete wiki against all 53 skills. Resolve duplicate concepts, verify cross-domain navigation, report every planned or unsupported facet, and do not declare corpus completion while unexplained coverage gaps remain.

### Persist an insight

> Save this explanation as durable wiki knowledge according to AGENTS.md. Integrate it into existing pages instead of duplicating concepts.

### Practice

> Generate ten difficult SOA-C03 scenarios from skills 1.3.5 and 2.2.2. Use plausible distractors and keep the answer key separate.

### Health check

> Lint the wiki according to AGENTS.md. Report unsupported claims, broken links, duplicates, orphan pages, contradictions, stale indexes, and unprocessed raw sources.
