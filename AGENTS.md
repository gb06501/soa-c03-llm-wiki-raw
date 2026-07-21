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
| `wiki/log.md` | Agent-maintained | Append-only history of ingests and material updates |
| `state/manifest.yaml` | Agent-maintained | Processing state and source-to-output mapping |
| `AGENTS.md` | Human and agent co-maintained | Operating contract for the wiki |

The raw layer and generated wiki layer must remain visibly separate.

## Generated wiki structure

Use this initial structure:

```text
wiki/
  index.md
  log.md
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

### Page types

Use a small, stable vocabulary:

- `AWS Service` — a service, feature, or important service component.
- `Concept` — an operational or architectural mechanism.
- `Comparison` — two or more choices that exam scenarios commonly contrast.
- `Decision Guide` — clue-to-choice rules for selecting an AWS solution.
- `Troubleshooting Playbook` — symptom, evidence, cause, action, and verification.
- `Exam Trap` — a misconception, tempting wrong choice, or important exception.
- `Learning Path` — an ordered study sequence across related knowledge.
- `Practice Set` — scenario questions and evaluated answers.
- `Knowledge Gap` — missing, uncertain, contradictory, or weakly supported knowledge.

Do not invent new page types when an existing type is adequate.

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
- `status` is one of `verified`, `partial`, `disputed`, or `needs-research`.
- Preserve unknown frontmatter fields when updating a page.
- Use lowercase kebab-case filenames without spaces.
- A file path is the stable concept identity; do not rename pages casually.

The root `wiki/index.md` may declare:

```yaml
---
okf_version: "0.1"
---
```

Other index files should remain simple Markdown catalogues.

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

Do not:

- generate one wiki page merely because one raw file exists;
- copy whole raw sections into `wiki/`;
- create duplicate pages for synonyms;
- split a concept so narrowly that each page lacks independent value;
- combine unrelated concepts into a large generic page.

Prefer synthesis across skills. For example, an RDS availability page may draw from performance, fault-tolerance, backup, deployment, security, and networking skills.

## Cross-linking

- Use standard Markdown links between related wiki pages.
- Prefer bundle-root-relative links, for example `[RDS Multi-AZ](/services/rds-multi-az.md)`.
- Link a concept on its first meaningful mention.
- Add a `Related concepts` section when it materially improves navigation.
- Links must express useful relationships, not merely inflate graph density.
- Avoid isolated pages. If a page is intentionally isolated, record why in the log.
- Broken links may represent planned knowledge, but must be reported as knowledge gaps.

## Source traceability

Every generated page must contain:

1. A `sources` frontmatter list.
2. A final `# Sources` section with readable links.
3. Relevant `skill_ids`.
4. Clear distinction between explicit source content and agent inference.

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

### 2. Bootstrap a domain

Process one exam domain at a time unless the user explicitly requests a full batch.

1. Inventory every raw skill in the domain.
2. Read existing wiki indexes and related pages.
3. Identify reusable services, concepts, comparisons, playbooks, and traps.
4. Propose the page plan before a large generation batch.
5. Create or update pages.
6. Add meaningful cross-links.
7. Update indexes.
8. Append the operation to `wiki/log.md`.
9. Update `state/manifest.yaml`.
10. Run the quality gates.
11. Use a dedicated branch and open a draft PR for human review.

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
- broken internal links;
- duplicate concept identities;
- orphan pages;
- stale indexes;
- manifest entries that do not match source versions;
- contradictions or inconsistent terminology;
- pages with no meaningful synthesis beyond one raw source;
- raw files modified by an agent;
- important recurring concepts that lack a page.

Report findings before applying broad repairs unless the user requested the fixes.

## State and logging

### Manifest

Create `state/manifest.yaml` during the first bootstrap. Track, per raw file:

- path;
- Git blob SHA or stable content hash;
- processed timestamp;
- generated or updated wiki pages;
- processing status;
- unresolved gaps or contradictions.

Use the manifest to avoid reprocessing unchanged sources blindly.

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
5. Internal links resolve, except explicitly recorded planned gaps.
6. Indexes include new and changed pages.
7. The update log and manifest are current.
8. No duplicate concept page was created.
9. The result improves cross-skill understanding rather than copying source text.
10. The content is concise enough to study but complete enough to make operational decisions.
11. Exam-critical exceptions and misleading alternatives are visible.
12. The pull request reports unresolved uncertainty honestly.

## Definition of done

A knowledge-generation task is done when:

- the requested source scope is fully processed;
- generated pages are source-grounded and cross-linked;
- indexes, log, and manifest are updated;
- quality gates pass;
- the learner can navigate from a scenario or AWS service to the relevant decision rules, evidence, playbooks, traps, and source skills;
- a human-reviewable change set is available.

## Recommended user commands

Examples of effective instructions:

### Query

> Using only this repository, answer the following SOA-C03 question. Start with the wiki, fall back to raw skills, cite file paths and skill IDs, and state any missing coverage.

### Bootstrap

> Bootstrap Domain 1 according to AGENTS.md. Treat raw as immutable, propose the page plan, generate the OKF wiki on a branch, run the quality gates, and open a draft PR.

### Persist an insight

> Save this explanation as durable wiki knowledge according to AGENTS.md. Integrate it into existing pages instead of duplicating concepts.

### Practice

> Generate ten difficult SOA-C03 scenarios from skills 1.3.5 and 2.2.2. Use plausible distractors and keep the answer key separate.

### Health check

> Lint the wiki according to AGENTS.md. Report unsupported claims, broken links, duplicates, orphan pages, contradictions, stale indexes, and unprocessed raw sources.
