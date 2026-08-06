<!-- @format -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/) and [Conventional Commits](https://www.conventionalcommits.org/).

<!--

## Unreleased: v0.0.0 (2026-00-00)

### Features

- **Core**:
- **Docs**:

### Fixes

- **Core**:
- **Docs**:

-->

## v15.1.0 (2026-08-05)

### Features

- **Docs**: Refresh docs\os-connect\data-viewer
- **Docs**: Refresh docs\tdei\portal\user-manual\jobs
- **Docs**: Update Assistant Knowledge Base articles
- **Core**: Optimize avif encoding settings

## v15.0.0 (2026-08-03)

### Features

- **Core**: Reduce file size of screenshots by switching to AVIF

## v14.6.0 (2026-08-03)

### Features

- **Docs**: Update homepage 'User Journeys' section

## v14.5.0 (2026-07-31)

### Features

- **Core**: Bump Zensical to 0.0.52
- **Docs**: Update Assistant Knowledge Base articles
- **Docs**: Add authority level count table to dispatch generator
- **Docs**: Update abbreviations list

### Fixes

- **Docs**: Remove outdated UI description in AccessMap User Manual
- **Docs**: Fix miscellaneous minor issues in the Assistant Knowledge Base

## v14.4.0 (2026-07-27)

### Features

- **Docs**: Update Assistant Knowledge Base articles
- **Docs**: Update os-connect/#dataset-name-suffixes with info about dataset relationships
- **Docs**: Refresh os-connect/data-viewer/user-manual/feedback

## v14.3.0 (2026-07-24)

### Features

- **Docs**: Update Assistant Knowledge Base articles

### Fixes

- **Core**: Fix AKB dispatch generator to use CRLF line endings

## v14.2.0 (2026-07-22)

### Features

- **Core**: Bump Zensical to 0.0.51
- **Docs**: Ingest TCAT Office Hours transcripts into Assistant Knowledge Base content
- **Docs**: Ingest TCAT Wiki content into Assistant Knowledge Base content

### Fixes

- **Core**: Improve transcript compression utility's filtering of filler speech patterns

## v14.1.0 (2026-07-16)

### Features

- **Docs**: Add assistant guidance for TDEI dataset lineage, source and derivative datasets, external attributes, integration workflows, and Workspaces project group roles

## v14.0.0 (2026-07-16)

### Features

- **Core**: Refresh project-wide coding instructions with current build, generated-file, documentation, and validation guidance

## v13.4.1 (2026-07-15)

### Fixes

- **Docs**: Fix formatting error in OpenSidewalks schema table

## v13.4.0 (2026-07-15)

### Features

- **Core**: Add OpenSidewalks logo

## v13.3.0 (2026-07-13)

### Features

- **Core**: Validate that every Assistant Knowledge Base Markdown file has valid YAML frontmatter containing all schema-required keys in the correct order, and include the check in the utility test runner

### Fixes

- **Core**: Update Assistant Knowledge Base frontmatter enum tests to validate the current `publication_status` and `authority_level` schema fields

- **Core**: Complete missing AKB frontmatter keys and normalize required-key ordering across all assistant articles
- **Core**: Fix the glossary generator's AKB frontmatter key order
- **Core**: Replace AKB `review_status` with `publication_status` and migrate publication-aware generators, build filtering, tests, and articles
- **Core**: Replace the ambiguous `draft` authority level with `provisional`
- **Docs**: Ensure every Assistant Knowledge Base `questions` entry is phrased as an article-relevant question
- **Docs**: Update product-folder index questions to describe their assistant-facing structure and policies rather than product definitions
- **Core**: Repair malformed YAML frontmatter in the Safe Routes to School Walksheds workflow article

## v13.2.0 (2026-07-10)

### Features

- **Core**: Add per-status article counts to the generated Assistant Knowledge Base dispatch status legend

## v13.1.0 (2026-07-09)

### Features

- **Core**: Upgrade Zensical to 0.0.50
- **Docs**: Add to abbreviations list
- **Docs**: Add new `topics` slugs to the AKB schema's themed vocabulary tables
- **Docs**: Add a `Slug` column to the AKB schema's Product tags table (matching each product's `docs/assistant/{topic}/` directory name), rename the `topics` section to "Topic tags", and add a "Product slugs" table duplicating those slugs as first-class `topics` values, with a short rationale for the intentional duplication
- **Core**: Add `test_akb_content.py` tests, enforcing that (1) the first `products` entry for single-product topic folders matches that folder's owning product, (2) the first `topics` entry matches the parent topic folder's own slug, and (3) every `products` entry has its schema slug present somewhere in `topics`; `cross-platform/` and `support/` are exempt from checks 1-2 as cross-cutting, multi-product sections
- **Docs**: Expand the AKB schema's product tags table to list all first-class products, and align the generated dispatch registry's `products` frontmatter to match
- **Docs**: Restructure the AKB schema's controlled `topics` vocabulary into themed tables covering every product area
- **Docs**: Standardize the "Related Concepts" section across `assistant/index.md`, `assistant/schema.md`, `assistant/intents.md`, and the generated `assistant/dispatch.md` to link to each other with shared, consistent text; update `utilities/akb-generate-dispatch.py` accordingly
- **Core**: Add `test_akb_content.py` tests validating that every AKB article's `products` and `topics` frontmatter values exactly match the controlled vocabularies in `assistant/schema.md`
- **Docs**: Add full frontmatter to AKB schema doc

### Fixes

- **Core**: Document and test that agent-layer URLs preserve docs-relative source paths, including `index.md`, while human index pages retain directory URLs
- **Core**: Handle interrupted site preparation and local preview serving without printing a Python traceback
- **Core**: Remove explicit Python Markdown association settings file, no longer needed as of Zensical Studio 0.1.2
- **Docs**: Rename or case-normalize non-conforming `topics` values in AKB articles to match the schema's updated controlled vocabulary
- **Docs**: Reorder AKB article `products`/`topics` frontmatter so the first `products` entry matches the owning product for the article's parent topic folder, the first `topics` entry matches that folder's slug, and every listed product's slug is present in `topics`, per the new `test_akb_content.py` checks; regenerate `assistant/dispatch.md` afterward
- **Docs**: Fix a stray `QA/QC Reports` `products` value (should be `QA-QC Reports`) and its missing `qa-qc` `topics` slug in `assistant/cross-platform/concept/abbreviations.md`
- **Docs**: Compact the dispatch registry's status legend table formatting
- **Docs**: Fix AKB article `products` frontmatter values that did not match the schema's canonical casing
- **Docs**: Update AKB article `products` frontmatter values for AKB root docs

## v13.0.0 (2026-07-06)

### Features

- **Core**: Refactor build system to publish two parallel layers: Zensical-built human-facing HTML docs + assistant-optimized Markdown

## v12.5.1 (2026-07-01)

### Fixes

- **Docs**: Update knowledge base article slugs and fix broken links

## v12.5.0 (2026-07-01)

### Features

- **Core**: Add AKB transcript ingestion pipeline
    - Details: _Added `utilities/akb-compress-transcript.py` to strip VTT headers, timestamps, and blank lines from WebVTT transcripts, producing a clean `.compressed.txt` file. Added `.github/prompts/akb-ingest-transcript.prompt.md` and `.github/agents/akb-transcript-ingester.agent.md` to power the `/akb-ingest-transcript` command, which compresses a transcript, analyzes it against the AKB `dispatch.md` and `schema.md`, proposes bucketed new-article and update changes in chat, and applies them after user approval._

## v12.4.1 (2026-06-30)

### Fixes

- **Docs**: Fix broken image comparison sliders

## v12.4.0 (2026-06-30)

### Features

- **Docs**: Add abbreviations and acronyms glossary with automated build process integrated into utility runner script

### Fixes

- **Docs**: Fix links

## v12.3.0 (2026-06-29)

### Features

- **Docs**: Restructure the assistant knowledge base, updating the schema and reorganizing sections

### Fixes

- **Docs**: Fix broken links, dash and apostrophe encoding issues, and author-facing link annotations across AKB pages
- **Docs**: Fix AKB page slugs; align instructions with the updated AKB schema; clean up stale files and paths

## v12.2.0 (2026-06-24)

### Features

- **Core**: Update `run-utils` utility to support skipping internal or external links

## v12.1.0 (2026-06-24)

### Fixes

- **Docs**: Improve table formatting

## v12.0.0 (2026-06-23)

### Features

- **Core**: Add assistant knowledge base
- **Core**: Update build and deployment workflow to publish Assistant Knowledge Base pages as both user-facing Zensical-built HTML and raw Markdown
- **Core**: Upgrade Zensical to 0.0.46

## v11.12.1 (2026-06-02)

### Fixes

- **Core**: Remove extra colon in Dependabot commit message prefix

## v11.12.0 (2026-05-22)

### Features

- **Core**: Configure Dependabot for root Python dependencies and GitHub Actions updates
- **Docs**: Expand the site-wide abbreviations list

### Fixes

- **Core**: Pin `zensical` to `0.0.43` so framework upgrades remain manual

## v11.11.0 (2026-05-11)

### Features

- **Core**: Improve AI-consumption support with `llms.txt` and `robots.txt` files
- **Docs**: Add minimal NDA event pages and supporting stats

### Fixes

- **Docs**: Repair links and anchors and escape non-link bracket text
- **Core**: Prevent an unnecessary trailing comma in generated nav output

## v11.10.1 (2026-04-29)

### Fixes

- **Docs**: Fix embedded converter iframe on "Import Curb Ramp Data into the TDEI" tutorial

## v11.10.0 (2026-04-29)

### Features

- **Core**: Add AccessMap sprites
    - Details: _Extracted individual sprites from https://www.accessmap.app/sprite.svg and saved each as a separate image._

## v11.9.0 (2026-04-24)

### Features

- **Core**: Add content style guidance system
    - Details: _Added golden sample templates per page type and updated both user-focused and AI-targeted documentation guidance._

## v11.8.1 (2026-04-22)

### Fixes

- **Core**: Fix `nav_order` keyboard/screen-reader focus order.
    - Details: _The CSS `order` property was already correcting the visual sequence, but DOM order (which screen readers and keyboard tab navigation follow) remained alphabetical. A new `sortNavByOrder` function in `extra.js` reads each item's `style.order` value and reappends DOM nodes in sorted order after every navigation event, aligning reading/focus order with visual order (WCAG SC 1.3.2, SC 2.4.3)._
- **Core**: Update padding on breadcrumbs and left sidebar sections to prevent clipping of keyboard focus ring

## v11.8.0 (2026-04-21)

### Features

- **Core**: Add insert-image prompt

## v11.7.0 (2026-04-20)

### Features

- **Docs**: Update image paths; replace outdated screenshots

### Fixes

- **Docs**: Reorganize TDEI Portal images into `images/tdei/portal/` subdirectory structure

## v11.6.0 (2026-04-17)

### Features

- **Docs**: Refresh the Workspaces section

## v11.5.1 (2026-04-16)

### Fixes

- **(Core)**: Improve build-and-deploy workflow

## v11.5.0 (2026-04-16)

### Features

- **Core**: Add Google Analytics with cookie consent dialog
- **Core**: Add footer "Change cookie settings" link, relocated after the "Made with Zensical" credit

### Fixes

- **Core**: Fix vertical alignment of checkbox list item text

## v11.4.1 (2026-04-15)

### Fixes

- **Core**: Fix top-of-page padding
- **Core**: Clean up `extra.css`

## v11.4.0 (2026-04-07)

### Features

- **Docs**: Add WAGISA abbreviation

### Fixes

- **Docs**: Remove misleading "(PDF)" label from the Jurisdiction Snapshot link on the home page
- **Docs**: Remove TDEI architecture chart from the home page

## v11.3.0 (2026-04-03)

### Features

- **Docs**: Add tip in the TDEI Portal Datasets page explaining that the Dataset filter returns all partial matches, not just exact matches, with a visual example

### Fixes

- **Docs**: Improve alt text on TDEI Portal Datasets page images for better accessibility

## v11.2.0 (2026-04-03)

### Features

- **Docs**: Add dataset name suffix reference with table, examples, and visual guide to OS-CONNECT documentation

## v11.1.0 (2026-04-02)

### Features

- **Core**: Add GitHub repo link and view/edit page action buttons; repositioned into the right sidebar "On this page" header to keep them accessible but visually unobtrusive

## v11.0.0 (2026-03-30)

### Features

- **Core**: Add changelog
