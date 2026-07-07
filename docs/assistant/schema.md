---
title: Assistant Knowledge Base article schema
tags:
    - Assistant
---

<!-- @format -->

# Assistant Knowledge Base article schema

This document is the authoring contract for [`docs/assistant/`](../assistant/index.md) pages that feed `utilities/export_rag.py` and future indexing pipelines. Product manuals elsewhere in `docs/` keep their existing conventions; only assistant-layer pages must follow this schema end-to-end.

## Design goals

- **Citation grounding**: metadata flags when an answer must cite retrieved text, not paraphrase from memory alone.
- **Governance**: `risk_level`, `authority_level`, and `review_status` let operators filter or gate high-stakes content.
- **Retrieval control**: `retrieval_priority` and `topics` tune ranking without rewriting prose for every deployment.
- **Abstention**: `assistant_behavior` encodes per-page guardrails for public assistants.

## Build and serving model

The site publishes two parallel layers at the same URL space:

- **Human layer** — Zensical-built HTML pages. Inside `docs/assistant/`, only
  `review_status: reviewed` pages outside `support/` are built to HTML.
- **Agent layer** — every assistant page is served as raw Markdown at the same URL
  with an `.md` extension (for example
  `https://taskarcenteratuw.github.io/tcat-wiki/assistant/qa-qc/concept/completeness.md`),
  regardless of `review_status`, including `support/` pages and stubs.

Consequences for authors:

- `review_status` controls human-layer visibility: `stub` and `draft` pages are
  agent-only; a page appears as an HTML page only once it is `reviewed`.
- Because every page is served as raw `.md`, stubs MUST still contain valid
  frontmatter and the required heading scaffold (with `TODO` placeholders) so the
  `.md` resolves to well-formed content.
- A `reviewed` human page MUST NOT link to a page that is not built to HTML (a
  `stub`, a `draft`, or anything under `support/`). Such links are treated as
  authoring errors and fail the build.
- `dispatch.md` is a generated registry of the agent layer, produced by
  `utilities/akb-generate-dispatch.py`. Do not manually edit it.

## YAML frontmatter (required keys)

Every file under `docs/assistant/` SHOULD include all of the following keys. Use sensible defaults (for example `draft` review status) rather than omitting keys.

| Field                | Type   | Details                                                                            | Example                                             |
| :------------------- | :----- | :--------------------------------------------------------------------------------- | :-------------------------------------------------- |
| `title`              | string | Human-readable title                                                               | `What is a workspace?`                              |
| `slug`               | string | Matches the file's basename exactly                                                | `workspace`                                         |
| `doc_type`           | enum   | `concept`, `workflow`, or `policy` — determined by path                            | `concept`                                           |
| `questions`          | list   | What a user might ask that this article answers                                    | `- What is a workspace?`                            |
| `products`           | list   | Relevant product tags                                                              | `- Workspaces` `- TDEI`                             |
| `audiences`          | list   | Intended readers                                                                   | `- developer` `- jurisdiction`                      |
| `topics`             | list   | Free-form retrieval tags                                                           | `- workspaces` `- sandbox-governance`               |
| `risk_level`         | enum   | `low`, `medium`, or `high` — legal/safety sensitivity                              | `low`                                               |
| `authority_level`    | enum   | `draft`, `explanatory`, or `official` — how strongly the org stands behind content | `explanatory`                                       |
| `review_status`      | enum   | `stub`, `draft`, or `reviewed` — controls human-layer visibility                   | `draft`                                             |
| `last_reviewed`      | date   | `YYYY-MM-DD` — last human editorial pass on the page                               | `2026-07-01`                                        |
| `retrieval_priority` | enum   | `low`, `medium`, or `high` — suggested ranking boost for retrieval                 | `high`                                              |
| `assistant_behavior` | map    | See below                                                                          | `allow_inference: false` `requires_citation: true`  |
| `related_pages`      | list   | Paths relative to `docs/`                                                          | `- assistant/workspaces/concept/dataset-lineage.md` |

### Directory structure

Each top-level topic section follows the same layout:

```
docs/assistant/{topic}/
    index.md          # doc_type: policy — consolidates policy content for this topic
    concept/          # doc_type: concept articles
        *.md
    workflow/         # doc_type: workflow articles
        *.md
```

Top-level sections:

- `accessmap`
- `aviv-scoutroute`
- `cross-platform`
- `flexr`
- `iospointmapper`
- `livability`
- `opensidewalks`
- `os-connect`
- `qa-qc`
- `rapid`
- `tdei`
- `walksheds`
- `waykeeper`
- `workspaces`

### `doc_type` values

| Value      | Location            | Naming pattern                                                           | Purpose                                                                                                                                                                    |
| :--------- | :------------------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `concept`  | `{topic}/concept/`  | Noun-phrase slug: `dataset-lineage.md`, `mobility-profiles.md`           | Explanatory knowledge: what X is, how X works, why X exists. Covers both broad conceptual background and simple term definitions.                                          |
| `workflow` | `{topic}/workflow/` | Verb-phrase slug: `create-workspace-from-tdei.md`, `export-workspace.md` | Step-by-step procedures with a discrete user outcome.                                                                                                                      |
| `policy`   | `{topic}/index.md`  | One `index.md` per topic                                                 | Rules, constraints, and governance statements for that topic. A topic's single `index.md` carries `doc_type: policy` and consolidates all policy content for that section. |

### `assistant_behavior` map

| Subfield                     | Type            | Purpose                                                                                      |
| :--------------------------- | :-------------- | :------------------------------------------------------------------------------------------- |
| `allow_inference`            | bool            | If `false`, consumer systems should stick closely to retrieved text.                         |
| `requires_citation`          | bool            | If `true`, answers should cite this wiki (or exported source) when used.                     |
| `abstain_if_missing_context` | bool            | If `true`, abstain when user lacks jurisdiction, version, or other critical context.         |
| `do_not_claim`               | list of strings | Affirmative sentences stating the **false or misleading claim** the assistant must not make. |

For `do_not_claim`, each entry reads in context as a complete false statement. Example: `do_not_claim` (that) `"Completeness is the same as ADA compliance"` (not `do_not_claim` (that) `"Completeness is not the same as ADA compliance"`). Used for evaluation guardrails and prompt grounding.

Every entry should correspond to a boundary stated or implied in the page's `## What This Does Not Mean` section — `do_not_claim` is the machine-readable distillation of that section, not a substitute for it. Used for evaluation guardrails and prompt grounding.

## Required Markdown sections (in order)

Body content after frontmatter MUST use this heading scaffold so chunks stay structurally aligned for splitting or section-aware retrieval:

1. `# [Page Title]` — matches reader expectation; must mirror `title` frontmatter.
2. `## Short Answer` — one to three short paragraphs; optimized for direct assistant replies.
3. `## Significance` — operational, institutional, or public-education importance (**do not** use "Why This Matters" as the heading text).
4. `## What This Means` — practical definition or resolution of the question.
5. `## What This Does Not Mean` — boundaries, non-claims, and common misinterpretations, written as human-readable prose with explanation. The main boundaries here should also appear as entries in the `do_not_claim` frontmatter — that field is the machine-readable distillation of this section.
6. `## How To Use This` — planners, jurisdictions, advocates, public users, or integrators.
7. `## Example` — one concrete scenario.
8. `## Assistant Guidance` — explicit behavior for chatbots: caveats, abstention, citation needs.
9. `## Related Concepts` — links to other assistant pages or, sparingly, product manuals.

Optional subheadings under these sections are allowed if they do not duplicate or replace the canonical nine headings.

## Product tags

First-class `products` values for assistant-layer pages:

| Product      | Notes                                             |
| :----------- | :------------------------------------------------ |
| `OS-CONNECT` | Pedestrian network data and viewer                |
| `AccessMap`  | Accessibility-aware routing                       |
| `Walksheds`  | Reachability analysis                             |
| `TDEI`       | Portal, APIs, releases                            |
| `Workspaces` | Collaborative editing, sandboxing, export to TDEI |

## Controlled vocabulary (`topics`)

Use short kebab-case slugs in frontmatter `topics` lists. Prefer terms from this set when they apply; add new tags sparingly and document them here.

| Topic                                 | Use for                                                                         |
| :------------------------------------ | :------------------------------------------------------------------------------ |
| `workspaces`                          | All Workspaces assistant pages (required baseline)                              |
| `tdei-ecosystem`                      | How Workspaces relates to TDEI and sibling products                             |
| `sandbox-governance`                  | Sandboxed copies, divergence, private editing                                   |
| `multi-source-stewardship`            | Collaborative review and enrichment of a workspace using multiple input sources |
| `dataset-lineage`                     | Source datasets, traceability, versioning                                       |
| `publication-workflow`                | Review, export, release to TDEI                                                 |
| `workspace-management`                | Dashboard, IDs, lifecycle                                                       |
| `onboarding`                          | Creating workspaces, getting started                                            |
| `project-groups`                      | TDEI project groups vs workspace teams                                          |
| `editing`                             | Geometry, attributes, accessibility features                                    |
| `osm-interoperability`                | OSM API emulation, editors, private OSM                                         |
| `vector-data`                         | Vector vs raster, non-global datasets                                           |
| `editing-tools`                       | Rapid, JOSM, AVIV ScoutRoute                                                    |
| `accessibility-data`                  | Accessibility feature editing                                                   |
| `imagery`                             | Imagery layers, sources, permissions                                            |
| `basemaps`                            | Basemap and tile loading                                                        |
| `configuration`                       | Imagery JSON and workspace config                                               |
| `collaboration`                       | Multi-user editing coordination                                                 |
| `teams`                               | Teams, invites, QR codes                                                        |
| `roles`                               | Manager, editor, reviewer roles                                                 |
| `review`                              | Review UI and QA workflows                                                      |
| `changesets`                          | Changeset tracking and history                                                  |
| `qa-qc`                               | Quality assurance in workspaces                                                 |
| `export`                              | Exporting workspace edits                                                       |
| `collaborative-accessibility-editing` | Community and agency collaborative mapping                                      |
| `stewardship`                         | Jurisdiction maintenance workflows                                              |
| `operational-workflows`               | Who should use Workspaces vs GIS                                                |
| `public-support`                      | External partner and helpline context                                           |
| `public-vs-private-data`              | Public release vs private sandbox (policy)                                      |
| `editing-authority`                   | Who may edit or approve (policy)                                                |
| `data-freshness`                      | Currency and staleness (policy)                                                 |

Other products may use additional topic slugs (for example `gtfs-pathways`, `completeness`); keep tags consistent within a product family.

## Related

- [Assistant Knowledge Base overview](index.md)
- Dispatch registry — generated agent-layer artifact served at `https://taskarcenteratuw.github.io/tcat-wiki/assistant/dispatch.md` (produced by `utilities/akb-generate-dispatch.py`; not hand-authored).
- [Intents](intents.md) - TPatterns of user queries that map to specific knowledge-base pages.
