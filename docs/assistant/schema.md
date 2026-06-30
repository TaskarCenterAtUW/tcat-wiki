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

## YAML frontmatter (required keys)

Every file under `docs/assistant/` SHOULD include all of the following keys. Use sensible defaults (for example `draft` review status) rather than omitting keys.

| Field                | Type   | Purpose                                                                                                                           |
| :------------------- | :----- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `title`              | string | Human-readable title; used in nav and exports.                                                                                    |
| `slug`               | string | Matches the file's basename exactly (e.g. `accessibility-assumptions` for `accessibility-assumptions.md`).                        |
| `doc_type`           | enum   | One of: `concept`, `workflow`, `policy`. See below.                                                                               |
| `questions`          | list   | Optional. Natural-language phrasings a user might ask that this article answers. Used as retrieval anchors by indexing pipelines. |
| `products`           | list   | Subset of product tags, for example `OS-CONNECT`, `AccessMap`, `Walksheds`, `TDEI`, `Workspaces`.                                 |
| `audiences`          | list   | Intended readers: `planner`, `jurisdiction`, `advocate`, `public`, etc.                                                           |
| `topics`             | list   | Free-form retrieval tags (short slugs).                                                                                           |
| `risk_level`         | enum   | `low`, `medium`, `high` — legal/safety sensitivity for filtering.                                                                 |
| `authority_level`    | enum   | `official`, `explanatory`, `draft` — how strongly the org stands behind wording.                                                  |
| `review_status`      | enum   | `stub`, `draft`, or `reviewed`.                                                                                                   |
| `last_reviewed`      | date   | (`YYYY-MM-DD`) Last human editorial pass on the page (not git mtime).                                                             |
| `retrieval_priority` | enum   | `low`, `medium`, `high` — suggested ranking boost for retrieval.                                                                  |
| `assistant_behavior` | map    | See below.                                                                                                                        |
| `related_pages`      | list   | Paths relative to `docs/` (for example `assistant/workspaces/concept/changesets.md`).                                             |

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

`accessmap`
`aviv-scoutroute`
`cross-platform`
`flexr`
`iospointmapper`
`livability`
`opensidewalks`
`os-connect`
`qa-qc`
`rapid`
`tdei`
`walksheds`
`waykeeper`
`workspaces`

### `doc_type` values

| Value      | Location            | Naming pattern                                                           | Purpose                                                                                                                                                                    |
| :--------- | :------------------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `concept`  | `{topic}/concept/`  | Noun-phrase slug: `dataset-lineage.md`, `mobility-profiles.md`           | Explanatory knowledge: what X is, how X works, why X exists. Covers both broad conceptual background and simple term definitions.                                          |
| `workflow` | `{topic}/workflow/` | Verb-phrase slug: `create-workspace-from-tdei.md`, `export-workspace.md` | Step-by-step procedures with a discrete user outcome.                                                                                                                      |
| `policy`   | `{topic}/index.md`  | One `index.md` per topic                                                 | Rules, constraints, and governance statements for that topic. A topic's single `index.md` carries `doc_type: policy` and consolidates all policy content for that section. |

### `assistant_behavior` map

| Subfield                     | Type            | Purpose                                                                              |
| :--------------------------- | :-------------- | :----------------------------------------------------------------------------------- |
| `allow_inference`            | bool            | If `false`, consumer systems should stick closely to retrieved text.                 |
| `requires_citation`          | bool            | If `true`, answers should cite this wiki (or exported source) when used.             |
| `abstain_if_missing_context` | bool            | If `true`, abstain when user lacks jurisdiction, version, or other critical context. |
| `do_not_claim`               | list of strings | Hard-negative claims for evaluation and prompt grounding.                            |

## Required Markdown sections (in order)

Body content after frontmatter MUST use this heading scaffold so chunks stay structurally aligned for splitting or section-aware retrieval:

1. `# [Page Title]` — matches reader expectation; may mirror `title` frontmatter.
2. `## Short Answer` — one to three short paragraphs; optimized for direct assistant replies.
3. `## Significance` — operational, institutional, or public-education importance (**do not** use "Why This Matters" as the heading text).
4. `## What This Means` — practical definition or resolution of the question.
5. `## What This Does Not Mean` — boundaries, non-claims, common misinterpretations.
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

| Topic                                 | Use for                                                                                                                                                                                                     |
| :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workspaces`                          | All Workspaces assistant pages (required baseline)                                                                                                                                                          |
| `tdei-ecosystem`                      | How Workspaces relates to TDEI and sibling products                                                                                                                                                         |
| `sandbox-governance`                  | Sandboxed copies, divergence, private editing                                                                                                                                                               |
| `multi-source-stewardship`            | Collaborative review and enrichment of a workspace using multiple input sources, including imported datasets, imagery, machine-generated outputs, jurisdiction records, and community-collected information |
| `dataset-lineage`                     | Source datasets, traceability, versioning                                                                                                                                                                   |
| `publication-workflow`                | Review, export, release to TDEI                                                                                                                                                                             |
| `workspace-management`                | Dashboard, IDs, lifecycle                                                                                                                                                                                   |
| `onboarding`                          | Creating workspaces, getting started                                                                                                                                                                        |
| `project-groups`                      | TDEI project groups vs workspace teams                                                                                                                                                                      |
| `editing`                             | Geometry, attributes, accessibility features                                                                                                                                                                |
| `osm-interoperability`                | OSM API emulation, editors, private OSM                                                                                                                                                                     |
| `vector-data`                         | Vector vs raster, non-global datasets                                                                                                                                                                       |
| `editing-tools`                       | Rapid, JOSM, AVIV ScoutRoute                                                                                                                                                                                |
| `accessibility-data`                  | Accessibility feature editing                                                                                                                                                                               |
| `imagery`                             | Imagery layers, sources, permissions                                                                                                                                                                        |
| `basemaps`                            | Basemap and tile loading                                                                                                                                                                                    |
| `configuration`                       | Imagery JSON and workspace config                                                                                                                                                                           |
| `collaboration`                       | Multi-user editing coordination                                                                                                                                                                             |
| `teams`                               | Teams, invites, QR codes                                                                                                                                                                                    |
| `roles`                               | Manager, editor, reviewer roles                                                                                                                                                                             |
| `review`                              | Review UI and QA workflows                                                                                                                                                                                  |
| `changesets`                          | Changeset tracking and history                                                                                                                                                                              |
| `qa-qc`                               | Quality assurance in workspaces                                                                                                                                                                             |
| `export`                              | Exporting workspace edits                                                                                                                                                                                   |
| `collaborative-accessibility-editing` | Community and agency collaborative mapping                                                                                                                                                                  |
| `stewardship`                         | Jurisdiction maintenance workflows                                                                                                                                                                          |
| `operational-workflows`               | Who should use Workspaces vs GIS                                                                                                                                                                            |
| `public-support`                      | External partner and helpline context                                                                                                                                                                       |
| `public-vs-private-data`              | Public release vs private sandbox (policy)                                                                                                                                                                  |
| `editing-authority`                   | Who may edit or approve (policy)                                                                                                                                                                            |
| `data-freshness`                      | Currency and staleness (policy)                                                                                                                                                                             |

Other products may use additional topic slugs (for example `gtfs-pathways`, `completeness`); keep tags consistent within a product family.

## Export record shape

`utilities/export_rag.py` emits one JSON object per line (JSONL). Each record includes at minimum:

- `path` — POSIX path relative to `docs/` (for example `assistant/qa-qc/concept/completeness.md`).
- `title`, `slug`, `doc_type`, `products`, `audiences`, `topics`
- `risk_level`, `authority_level`, `retrieval_priority`
- `review_status`, `last_reviewed` when present in frontmatter
- `assistant_behavior` as a nested object when present
- `source_url` — placeholder string beginning with `PLACEHOLDER_SITE_URL/`; replace in your deployment using `site_url` from `zensical.toml` and your HTML permalink rules.
- `content` — Markdown body after the closing `---` of the YAML frontmatter (full page text for the first iteration; section-aware splitting may come later).

Embeddings, vector stores, and LLM API calls are **out of scope** for this repository's default tooling.

## Related

- [Assistant Knowledge Base overview](index.md)
- [Dispatch](dispatch.md)
