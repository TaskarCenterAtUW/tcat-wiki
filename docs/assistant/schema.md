---
title: Assistant Knowledge Base article schema
slug: schema
doc_type: concept
questions:
    - What is the schema for the TCAT Wiki Assistant Knowledge Base articles?
audiences:
    - developer
products:
    - AccessMap
    - AVIV ScoutRoute
    - Cross-Platform
    - FleXR
    - iOSPointMapper
    - LivAbility
    - OpenSidewalks
    - OS-CONNECT
    - QA-QC Reports
    - Rapid
    - TDEI
    - Walksheds
    - WayKeeper
    - Workspaces
topics:
    - support
    - governance
    - assistant-behavior
    - accessmap
    - aviv-scoutroute
    - cross-platform
    - flexr
    - iospointmapper
    - livability
    - opensidewalks
    - os-connect
    - qa-qc
    - rapid
    - tdei
    - walksheds
    - waykeeper
    - workspaces
risk_level: high
authority_level: official
publication_status: draft
last_reviewed: 2026-07-13
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: true
    do_not_claim:
        -
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/intents.md
tags:
    - Assistant
---

<!-- @format -->

# Assistant Knowledge Base article schema

This document is the authoring contract for [`docs/assistant/`](../assistant/index.md) pages that feed `utilities/export_rag.py` and future indexing pipelines. Product manuals elsewhere in `docs/` keep their existing conventions; only assistant-layer pages must follow this schema end-to-end.

## Design goals

- **Citation grounding**: metadata flags when an answer must cite retrieved text, not paraphrase from memory alone.
- **Governance**: `risk_level`, `authority_level`, and `publication_status` let operators filter or gate high-stakes content.
- **Retrieval control**: `retrieval_priority` and `topics` tune ranking without rewriting prose for every deployment.
- **Abstention**: `assistant_behavior` encodes per-page guardrails for public assistants.

## Build and serving model

The site publishes two parallel layers at the same URL space:

- **Human layer** — Zensical-built HTML pages. Inside `docs/assistant/`, only `publication_status: published` pages outside `support/` are built to HTML.
- **Agent layer** — every assistant page is served as raw Markdown at its docs-relative source path, including the `.md` filename (for example `https://taskarcenteratuw.github.io/tcat-wiki/assistant/qa-qc/concept/completeness.md`), regardless of `publication_status`, including `support/` pages and stubs. Human index-page URLs omit `index`, while agent URLs retain it: the human URL `https://taskarcenteratuw.github.io/tcat-wiki/accessmap/` corresponds to the agent URL `https://taskarcenteratuw.github.io/tcat-wiki/accessmap/index.md`.

Consequences for authors:

- `publication_status` controls human-layer visibility: `stub`, `draft`, and `archived` pages are agent-only; a page appears as an HTML page only once it is `published`.
- Because every page is served as raw `.md` at its docs-relative source path, stubs MUST still contain valid frontmatter and the required heading scaffold (with `TODO` placeholders) so the `.md` resolves to well-formed content.
- A `published` human page MUST NOT link to a page that is not built to HTML (a `stub`, a `draft`, an `archived` page, or anything under `support/`). Such links are treated as authoring errors and fail the build.
- `dispatch.md` is a generated registry of the agent layer, produced by `utilities/akb_generate_dispatch.py`. Do not manually edit it.

## YAML frontmatter (required keys)

Every file under `docs/assistant/` MUST include all of the following keys. Use sensible defaults (for example `draft` publication status) rather than omitting keys.

| Field                | Type   | Details                                                                                  | Example                                             |
| :------------------- | :----- | :--------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| `title`              | string | Human-readable title                                                                     | `What is a workspace?`                              |
| `slug`               | string | Matches the file's basename exactly                                                      | `workspace`                                         |
| `doc_type`           | enum   | `concept`, `workflow`, or `policy` — determined by path                                  | `concept`                                           |
| `questions`          | list   | What a user might ask that this article answers                                          | `- What is a workspace?`                            |
| `products`           | list   | Relevant product tags                                                                    | `- Workspaces` `- TDEI`                             |
| `audiences`          | list   | Intended readers                                                                         | `- developer` `- jurisdiction`                      |
| `topics`             | list   | Free-form retrieval tags                                                                 | `- workspaces` `- sandbox-governance`               |
| `risk_level`         | enum   | `low`, `medium`, or `high` — legal/safety sensitivity                                    | `low`                                               |
| `authority_level`    | enum   | `provisional`, `explanatory`, or `official` — how strongly the org stands behind content | `explanatory`                                       |
| `publication_status` | enum   | `stub`, `draft`, `published`, or `archived` — controls human-layer visibility            | `draft`                                             |
| `last_reviewed`      | date   | `YYYY-MM-DD` — last human editorial pass on the page                                     | `2026-07-01`                                        |
| `retrieval_priority` | enum   | `low`, `medium`, or `high` — suggested ranking boost for retrieval                       | `high`                                              |
| `assistant_behavior` | map    | See below                                                                                | `allow_inference: false` `requires_citation: true`  |
| `related_pages`      | list   | Paths relative to `docs/`                                                                | `- assistant/workspaces/concept/dataset-lineage.md` |

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

## Product tags (`products`)

First-class `products` values for assistant-layer pages:

| Product           | Slug              | Notes                                      |
| :---------------- | :---------------- | :----------------------------------------- |
| `AccessMap`       | `accessmap`       | Accessibility-aware routing                |
| `AVIV ScoutRoute` | `aviv-scoutroute` | Mobile survey application                  |
| `Cross-Platform`  | `cross-platform`  | Multi-platform shared functionality        |
| `FleXR`           | `flexr`           | WebXR plugin for custom input methods      |
| `iOSPointMapper`  | `iospointmapper`  | Semi-automated data collection on iOS      |
| `LivAbility`      | `livability`      | Community livability assessment platform   |
| `OpenSidewalks`   | `opensidewalks`   | Pedestrian network schema and standards    |
| `OS-CONNECT`      | `os-connect`      | WA pedestrian network data and viewer      |
| `QA-QC Reports`   | `qa-qc`           | QA/QC reports for OS-CONNECT datasets      |
| `Rapid`           | `rapid`           | Fast web-based OSM editor                  |
| `TDEI`            | `tdei`            | Portal, APIs, dataset storage and releases |
| `Walksheds`       | `walksheds`       | Reachability analysis platform             |
| `WayKeeper`       | `waykeeper`       | Navigation layer for TCAT's resources      |
| `Workspaces`      | `workspaces`      | Collaborative editing and sandboxing       |

`Slug` is the matching kebab-case `docs/assistant/{topic}/` directory name for that product, also usable as its corresponding `topics` entry (see [Product slugs](#product-slugs)).

## Topic tags (`topics`)

This is the **prescribed vocabulary going forward** — the set of kebab-case slugs authors should draw from when tagging `topics`, regardless of how many pages currently use a given term. It intentionally covers every product in [Product tags](#product-tags-products), including thin sections (LivAbility, FleXR, iOSPointMapper, WayKeeper) so that early pages in those areas are tagged consistently with where each product is headed, not just where it is today.

Strongly prefer a term from this list. Only add a new slug if none of these fit; and if you do, add it to the relevant theme table below in the same pull request. Themes are cross-cutting — any topic may be combined with any product's pages when relevant.

### Product slugs

Every value from the [Product tags](#product-tags-products) table's `Slug` column is also a valid `topics` entry, used to tag a page with its owning product/section for retrieval:

| Topic             |
| :---------------- |
| `accessmap`       |
| `aviv-scoutroute` |
| `cross-platform`  |
| `flexr`           |
| `iospointmapper`  |
| `livability`      |
| `opensidewalks`   |
| `os-connect`      |
| `qa-qc`           |
| `rapid`           |
| `tdei`            |
| `walksheds`       |
| `waykeeper`       |
| `workspaces`      |

This duplicates the `products` list in slug form so a page's owning section is filterable from `topics` alone (e.g. by a retrieval pipeline that only indexes `topics`), without requiring a `products`-to-slug lookup elsewhere.

### Ecosystem & data lifecycle

| Topic                    | Use for                                                 |
| :----------------------- | :------------------------------------------------------ |
| `tdei-ecosystem`         | How a product relates to TDEI and sibling products      |
| `dataset-lineage`        | Source datasets, traceability, versioning               |
| `data-freshness`         | Currency, staleness, and update cadence                 |
| `data-quality`           | Accuracy, confidence, and reliability of data           |
| `completeness`           | Coverage gaps vs. full data capture                     |
| `vector-data`            | Vector vs. raster data, non-global dataset handling     |
| `interoperability`       | OSW/OSM format compatibility, cross-tool data exchange  |
| `formats`                | File formats and schema structures                      |
| `releases`               | Dataset releases, versioning, and publication in TDEI   |
| `publication-workflow`   | Review, export, and release of edits into the ecosystem |
| `public-vs-private-data` | Public release vs. private sandbox boundaries           |
| `comparison`             | Comparative analysis across datasets or tools           |
| `overview`               | High-level product or dataset overview                  |
| `connectivity`           | Network connectivity and data linkages                  |
| `limitations`            | Known limitations and constraints                       |
| `os-connect-overview`    | OS-CONNECT system overview and architecture             |
| `arcgis`                 | ArcGIS integration and compatibility                    |
| `documentation`          | User guides and technical documentation                 |
| `licensing`              | Data licensing and usage rights                         |
| `standards`              | Standards adherence and compliance                      |
| `open-source`            | Open-source software and communities                    |
| `opensidewalks-overview` | OpenSidewalks system overview and architecture          |
| `complexity`             | System or data complexity considerations                |
| `assumptions`            | Assumptions and dependencies                            |
| `publishers`             | Data publishers and data provenance                     |
| `tdei-overview`          | TDEI system overview and architecture                   |
| `glossary`               | Terminology and glossary definitions                    |
| `abbreviations`          | Acronyms and abbreviations                              |
| `acronyms`               | Extended acronym definitions and meanings               |
| `openstreetmap`          | OpenStreetMap and how it relates to TCAT's work         |

### Editing & collaboration

| Topic                      | Use for                                                          |
| :------------------------- | :--------------------------------------------------------------- |
| `editing-tools`            | Rapid, JOSM, AVIV ScoutRoute, and other editors                  |
| `editing`                  | Geometry, attributes, and accessibility feature editing          |
| `editing-authority`        | Who may edit or approve changes                                  |
| `osm-interoperability`     | OSM API emulation, editors, private OSM model                    |
| `teams`                    | Teams, invites, QR codes                                         |
| `roles`                    | Manager, editor, reviewer roles                                  |
| `sandbox-governance`       | Sandboxed copies, divergence, private editing                    |
| `workspace-management`     | Dashboard, IDs, lifecycle of a workspace                         |
| `onboarding`               | Creating a workspace or project, getting started                 |
| `project-groups`           | TDEI project groups vs. workspace teams                          |
| `multi-source-stewardship` | Collaborative review and enrichment using multiple input sources |
| `collaborative-editing`    | Community and agency collaborative mapping                       |
| `review`                   | Review UI and QA workflows                                       |
| `changesets`               | Changeset tracking and history                                   |
| `qa-qc`                    | Quality assurance and review workflows                           |
| `export`                   | Exporting edits to TDEI or other destinations                    |
| `imagery`                  | Imagery layers, sources, permissions                             |
| `basemaps`                 | Basemap and tile loading                                         |
| `configuration`            | Tool and workspace configuration                                 |
| `issue-reporting`          | Reporting and tracking issues and errors                         |
| `conflicts`                | Conflict resolution and merge handling                           |
| `ownership`                | Data and content ownership and stewardship                       |

### Accessibility & routing

| Topic                   | Use for                                                      |
| :---------------------- | :----------------------------------------------------------- |
| `accessibility-data`    | Accessibility feature data                                   |
| `routing`               | Route calculation, preferences, and tradeoffs                |
| `mobility-profiles`     | Wheelchair, low-vision, and other user profiles              |
| `walksheds`             | Reachability and walkshed analysis                           |
| `transit`               | Transit stop access and pedestrian-transit integration       |
| `gtfs`                  | GTFS, GTFS-Flex, and GTFS-Pathways integration               |
| `equity`                | Equity analysis across accessibility profiles or communities |
| `scoring`               | Community livability assessment and scoring                  |
| `accessibility-metrics` | Quantified accessibility or livability indicators            |
| `elevation`             | Elevation data and terrain analysis                          |
| `curb-ramps`            | Curb ramp inventory and accessibility                        |
| `crossings`             | Street crossing infrastructure and accessibility             |
| `intersections`         | Intersection geometry and accessibility                      |
| `destinations`          | Destination accessibility and proximity analysis             |
| `sidewalks`             | Sidewalk inventory and connectivity                          |
| `slope`                 | Slope and grade data for accessibility                       |
| `trails`                | Trail networks and pedestrian pathways                       |
| `buffers`               | Buffer zones and walking distance analysis                   |

### Field data collection & mobile tools

| Topic                   | Use for                                                    |
| :---------------------- | :--------------------------------------------------------- |
| `field-data-collection` | Surveying, mapping, and data capture in the field          |
| `data-collection`       | General survey and collection workflows                    |
| `quests`                | AVIV ScoutRoute quest-based data collection                |
| `device-compatibility`  | Supported devices, OS versions, hardware requirements      |
| `xr-accessibility`      | XR/AR accessibility tooling                                |
| `assistive-input`       | Alternative/assistive input methods for XR or mobile tools |
| `webxr`                 | WebXR platform-specific concerns                           |
| `tasking-manager`       | Tasking Manager project setup and coordination             |
| `automation`            | Automated data collection and processing                   |
| `testing`               | Testing workflows and quality assurance                    |

### Planning & analysis

| Topic                  | Use for                                                        |
| :--------------------- | :------------------------------------------------------------- |
| `planning`             | Infrastructure, capital, and transition planning               |
| `ada`                  | ADA-related planning, requirements, or compliance context      |
| `legal-boundaries`     | Legal or compliance boundaries assistants must not overstate   |
| `prioritization`       | Ranking or prioritizing pedestrian investments                 |
| `ai`                   | AI/ML-assisted analysis, generation, or risk                   |
| `graph-metrics`        | Network/graph analysis metrics (centrality, betweenness, etc.) |
| `community`            | Community engagement and participation                         |
| `communication`        | Communication strategies and outreach                          |
| `gis`                  | GIS tools and spatial analysis                                 |
| `roadmap`              | Product roadmaps and strategic direction                       |
| `advocacy`             | Advocacy and policy support                                    |
| `contacts`             | Contact databases and organizational structure                 |
| `construction`         | Construction projects and impacts                              |
| `schools`              | School-related planning and data                               |
| `risk`                 | Risk assessment and management                                 |
| `strategy`             | Strategic planning and implementation                          |
| `rural`                | Rural-specific planning considerations                         |
| `campus`               | Campus-specific planning and walkability                       |
| `emergency`            | Emergency response and resilience planning                     |
| `health`               | Health outcomes and public health implications                 |
| `vision-zero`          | Vision Zero and traffic safety initiatives                     |
| `vendors`              | Vendor management and procurement                              |
| `mpo`                  | Metropolitan Planning Organization activities                  |
| `mappy-hours`          | Mappy Hours accessibility audit events                         |
| `economic-development` | Economic development and business impacts                      |
| `cost`                 | Cost-benefit analysis and budgeting                            |
| `resilience`           | Resilience and adaptation planning                             |
| `tourism`              | Tourism accessibility and promotion                            |
| `helpline`             | Helpline and user support services                             |
| `adoption`             | Technology adoption and implementation                         |
| `capital`              | Capital improvement and funding                                |
| `maintenance`          | Maintenance and stewardship                                    |
| `other-states`         | Examples and practices from other states                       |
| `events`               | Events and community gatherings                                |
| `training`             | Training programs and capacity building                        |
| `national`             | National-level initiatives and standards                       |
| `partnerships`         | Partnerships and collaboration agreements                      |
| `private-property`     | Private property considerations                                |
| `srts`                 | Safe Routes To School initiatives                              |
| `safety`               | Pedestrian and traffic safety                                  |
| `sustainability`       | Sustainable transportation and land use                        |
| `universities`         | University-related planning and walkability                    |
| `washington`           | Washington state-specific context                              |
| `sla`                  | Service level agreements and performance metrics               |
| `escalation`           | Escalation procedures and issue resolution                     |
| `before-after`         | Before-and-after analysis and impact assessment                |
| `complete-streets`     | Complete streets and street design                             |
| `grants`               | Grant funding and sources                                      |
| `scenarios`            | Scenario planning and modeling                                 |
| `parks`                | Park planning and greenspace accessibility                     |
| `bottlenecks`          | Identifying and addressing bottlenecks                         |
| `interpretation`       | Data interpretation and visualization                          |
| `agencies`             | Agency coordination and inter-organizational workflows         |

### Support, feedback & governance

| Topic                   | Use for                                                    |
| :---------------------- | :--------------------------------------------------------- |
| `feedback`              | Reporting errors, issues, or corrections                   |
| `support`               | Helpline and partner support interactions                  |
| `governance`            | Assistant-layer policy, abstention, and content governance |
| `assistant-behavior`    | Assistant guardrails, abstention rules                     |
| `stewardship`           | Jurisdiction or agency data maintenance                    |
| `operational-workflows` | Who should use which tool for a given operational need     |
| `public-support`        | External partner and helpline context                      |

Other pages may use additional topic slugs not listed here only when nothing above fits; keep new tags kebab-case, add them to the matching theme table above, and keep them consistent within a product family.

## Related Concepts

- [Assistant Knowledge Base Index](index.md) — Overview of this retrieval-oriented TCAT knowledge base
- [Assistant Knowledge Base Dispatch](dispatch.md) — Generated registry of all pages in the knowledge base
- [Assistant Knowledge Base Intents](intents.md) — Mapping of retrieval intents to article paths
