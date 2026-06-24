---
title: Assistant Knowledge Base — Dispatch
tags:
    - Assistant
slug: assistant-dispatch
doc_type: workflow
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
    - Workspaces
audiences:
    - developer
topics:
    - assistant-layer
    - governance
risk_level: low
authority_level: official
review_status: draft
last_reviewed: 2026-06-18
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/schema.md
---

<!-- @format -->

# Assistant Knowledge Base — Dispatch

## Short Answer

This file is the registry for all pages in the `docs/assistant/` knowledge base. It is the single source of truth for canonical file paths, authoring status, and section structure. External agents should fetch this file first to enumerate available knowledge-base pages before retrieving individual articles.

## Significance

A stable registry decouples retrieval pipelines from the filesystem. Authors use this file to track what has been written, what is still a stub, and what needs review. Integrators can use it to detect new pages without crawling the entire site.

## What This Means

- Every planned or published page in `docs/assistant/` has a row in this registry.
- **Status** is one of: `stub` (placeholder exists, body is TODO), `draft` (content authored, awaiting review), or `reviewed` (approved by TCAT staff).
- The **RAG source path** column shows where the file originates in `local-storage/rag/docs/assistant/` before being moved to `docs/assistant/` by the human author.
- Section index files (e.g., `workspaces/index.md`) provide the full per-section file listing with richer metadata.

## What This Does Not Mean

- This file does not replace the [schema](schema.md), which governs authoring conventions.
- This file does not replace section indexes, which provide richer per-section context.
- A `stub` status does not mean the content is wrong — it means the body has not yet been authored.

## How To Use This

**Agents**: Fetch `dispatch.md`, parse the registry tables, filter by `status`, `products`, or section, then retrieve individual pages by constructing their URL from the `File` column path relative to `docs/assistant/`.

**Authors**: Find your assigned file in the relevant section table. Change `status` from `stub` → `draft` once content is written, and from `draft` → `reviewed` once another TCAT editor approves it. Update `last_reviewed` in the file's own frontmatter.

**Maintainers**: Add a row to the relevant section table whenever a new file is added to `docs/assistant/`. Remove rows only if a file is permanently deleted.

## Example

An agent looking for Workspaces content: fetches this file, filters rows where `Section` is `workspaces`, selects high `retrieval_priority` rows, then fetches those individual pages.

## Assistant Guidance

This page should be fetched fresh rather than cached aggressively; its registry reflects the current authoring state of the knowledge base. If a file listed here returns 404, it has not yet been moved from the staging area.

## Related Concepts

- [Assistant Knowledge Base Overview](index.md)
- [Article Schema](schema.md)

## Status Legend

| Status | Meaning |
|--------|---------|
| `stub` | Placeholder file exists in RAG staging; content is TODO |
| `draft` | Content authored; awaiting TCAT editorial review |
| `reviewed` | Reviewed and approved by TCAT staff |

## Registry

### Top-Level Files

| File | Type | Status |
|------|------|--------|
| `index.md` | concept | draft |
| `dispatch.md` | workflow | draft |
| `schema.md` | schema | draft |

### `workspaces/` — Workspaces

See [workspaces/index.md](workspaces/index.md) for a richer, annotated listing.

#### Questions

| File | Status |
|------|--------|
| `workspaces/index.md` | draft |
| `workspaces/can-attribute-data-be-edited.md` | stub |
| `workspaces/can-custom-imagery-be-added.md` | stub |
| `workspaces/can-geometry-be-edited.md` | stub |
| `workspaces/can-multiple-workspaces-exist-from-the-same-dataset.md` | stub |
| `workspaces/does-editing-a-workspace-change-the-tdei-dataset.md` | stub |
| `workspaces/does-export-overwrite-the-original-dataset.md` | stub |
| `workspaces/how-are-accessibility-features-edited.md` | stub |
| `workspaces/how-are-basemaps-loaded.md` | stub |
| `workspaces/how-are-changesets-tracked.md` | stub |
| `workspaces/how-are-collaborative-edits-managed.md` | stub |
| `workspaces/how-are-edits-attributed-to-users.md` | stub |
| `workspaces/how-are-edits-uploaded-back-to-tdei.md` | stub |
| `workspaces/how-are-imagery-permissions-handled.md` | stub |
| `workspaces/how-can-edits-be-audited.md` | stub |
| `workspaces/how-can-managers-review-edits.md` | stub |
| `workspaces/how-can-multiple-people-coordinate-editing.md` | stub |
| `workspaces/how-can-users-continue-editing-an-existing-feature.md` | stub |
| `workspaces/how-can-users-identify-who-made-a-change.md` | stub |
| `workspaces/how-can-users-inspect-edit-history.md` | stub |
| `workspaces/how-can-users-trace-the-source-dataset.md` | stub |
| `workspaces/how-do-i-create-a-workspace-from-existing-osm-data.md` | stub |
| `workspaces/how-do-i-create-a-workspace-from-tdei.md` | stub |
| `workspaces/how-do-i-create-a-workspace.md` | stub |
| `workspaces/how-do-i-export-a-workspace.md` | stub |
| `workspaces/how-do-i-search-for-project-groups.md` | stub |
| `workspaces/how-do-imagery-layers-work-in-workspaces.md` | stub |
| `workspaces/how-do-managers-interact-with-workspaces.md` | stub |
| `workspaces/how-do-project-groups-work.md` | stub |
| `workspaces/how-do-team-invitations-work.md` | stub |
| `workspaces/how-do-teams-differ-from-project-groups.md` | stub |
| `workspaces/how-do-technical-gis-staff-interact-with-workspaces.md` | stub |
| `workspaces/how-do-vector-maps-differ-from-raster-maps.md` | stub |
| `workspaces/how-does-a-workspace-diverge-from-the-original-dataset.md` | stub |
| `workspaces/how-does-workspaces-emulate-osm-apis.md` | stub |
| `workspaces/how-does-workspaces-fit-into-the-tdei-ecosystem.md` | stub |
| `workspaces/how-does-workspaces-support-collaborative-accessibility-editing.md` | stub |
| `workspaces/how-does-workspaces-support-qa-review.md` | stub |
| `workspaces/how-does-workspaces-support-stewardship.md` | stub |
| `workspaces/how-should-jurisdictions-publish-updates.md` | stub |
| `workspaces/how-should-review-happen-before-export.md` | stub |
| `workspaces/is-a-workspace-a-copy-or-the-original-dataset.md` | stub |
| `workspaces/is-workspaces-connected-to-the-public-osm-database.md` | stub |
| `workspaces/what-are-imagery-layers.md` | stub |
| `workspaces/what-are-qr-code-invites-used-for.md` | stub |
| `workspaces/what-are-teams-in-workspaces.md` | stub |
| `workspaces/what-are-the-different-workspace-creation-methods.md` | stub |
| `workspaces/what-are-tile-layers.md` | stub |
| `workspaces/what-does-private-osm-mean.md` | stub |
| `workspaces/what-does-sandbox-mean-in-workspaces.md` | stub |
| `workspaces/what-does-the-workspace-dashboard-show.md` | stub |
| `workspaces/what-editor-created-a-change.md` | stub |
| `workspaces/what-editors-work-with-workspaces.md` | stub |
| `workspaces/what-happens-after-export-to-tdei.md` | stub |
| `workspaces/what-happens-during-export.md` | stub |
| `workspaces/what-happens-if-imagery-is-configured-incorrectly.md` | stub |
| `workspaces/what-happens-if-two-groups-edit-separate-copies.md` | stub |
| `workspaces/what-happens-when-i-create-a-workspace-from-a-tdei-dataset.md` | stub |
| `workspaces/what-imagery-sources-are-available.md` | stub |
| `workspaces/what-is-a-project-group.md` | stub |
| `workspaces/what-is-a-workspace-in-technical-terms.md` | stub |
| `workspaces/what-is-aviv-scoutroute.md` | stub |
| `workspaces/what-is-dataset-lineage-in-tdei.md` | stub |
| `workspaces/what-is-josm.md` | stub |
| `workspaces/what-is-rapid-2-versus-rapid-3.md` | stub |
| `workspaces/what-is-rapid.md` | stub |
| `workspaces/what-is-the-asr-imagery-list-repo.md` | stub |
| `workspaces/what-is-the-benefit-of-using-existing-osm-editors.md` | stub |
| `workspaces/what-is-the-difference-between-viewer-users-and-editor-users.md` | stub |
| `workspaces/what-is-the-imagery-json-configuration.md` | stub |
| `workspaces/what-is-the-recommended-publication-workflow.md` | stub |
| `workspaces/what-is-the-relationship-between-workspaces-and-os-connect.md` | stub |
| `workspaces/what-is-the-relationship-between-workspaces-and-the-tdei-portal.md` | stub |
| `workspaces/what-is-the-review-interface.md` | stub |
| `workspaces/what-is-the-workspace-id-used-for.md` | stub |
| `workspaces/what-is-workspaces.md` | stub |
| `workspaces/what-kinds-of-community-workflows-are-supported.md` | stub |
| `workspaces/what-kinds-of-edits-can-be-made-in-workspaces.md` | stub |
| `workspaces/what-kinds-of-users-are-workspaces-designed-for.md` | stub |
| `workspaces/what-limitations-exist-compared-to-openstreetmap.md` | stub |
| `workspaces/what-metadata-is-stored-for-edits.md` | stub |
| `workspaces/what-metadata-is-stored-with-a-workspace.md` | stub |
| `workspaces/what-roles-exist-in-workspaces.md` | stub |
| `workspaces/what-sources-were-used-for-an-edit.md` | stub |
| `workspaces/what-tools-work-with-workspaces.md` | stub |
| `workspaces/what-versioning-occurs-during-export.md` | stub |
| `workspaces/what-workflows-are-best-suited-for-workspaces.md` | stub |
| `workspaces/when-should-a-city-use-external-gis-tools.md` | stub |
| `workspaces/when-should-a-city-use-workspaces-instead-of-gis-software.md` | stub |
| `workspaces/when-should-edits-be-exported-back-to-tdei.md` | stub |
| `workspaces/when-should-edits-remain-private.md` | stub |
| `workspaces/which-editor-should-i-use.md` | stub |
| `workspaces/who-can-review-edits.md` | stub |
| `workspaces/who-is-workspaces-intended-for.md` | stub |
| `workspaces/why-are-vector-maps-preferred-for-accessibility-editing.md` | stub |
| `workspaces/why-do-imagery-resources-differ-between-workspaces.md` | stub |
| `workspaces/why-does-workspaces-emulate-osm-editing.md` | stub |
| `workspaces/why-does-workspaces-exist-separately-from-tdei.md` | stub |
| `workspaces/why-is-the-dataset-not-global-like-osm.md` | stub |
| `workspaces/why-is-workspaces-compatible-with-osm-tools.md` | stub |
| `workspaces/why-must-imagery-use-raw-json-links.md` | stub |

#### Concepts

| File | Status |
|------|--------|
| `workspaces/changesets.md` | stub |
| `workspaces/collaborative-accessibility-editing.md` | stub |
| `workspaces/dataset-lineage.md` | stub |
| `workspaces/imagery-layers.md` | stub |
| `workspaces/multi-source-stewardship.md` | stub |
| `workspaces/private-osm.md` | stub |
| `workspaces/project-groups.md` | stub |
| `workspaces/tdei-vs-workspaces.md` | stub |
| `workspaces/workspace-editors.md` | stub |
| `workspaces/workspace-export.md` | stub |
| `workspaces/workspace-sandbox.md` | stub |

#### Policies

| File | Status |
|------|--------|
| `workspaces/policies/index.md` | stub |

#### Workflows

| File | Status |
|------|--------|
| `workspaces/workflows/index.md` | stub |
| `workspaces/workflows/configure-imagery-layers.md` | stub |
| `workspaces/workflows/create-a-workspace-from-tdei.md` | stub |
| `workspaces/workflows/edit-accessibility-features-in-a-workspace.md` | stub |
| `workspaces/workflows/export-workspace-edits-to-tdei.md` | stub |
| `workspaces/workflows/invite-a-team-to-a-workspace.md` | stub |
| `workspaces/workflows/review-workspace-edits.md` | stub |
| `workspaces/workflows/use-workspaces-for-community-validation.md` | stub |
| `workspaces/workflows/use-workspaces-for-jurisdiction-stewardship.md` | stub |

### `os-connect/` — OS-CONNECT

See [os-connect/index.md](os-connect/index.md) for a richer, annotated listing.

| File | Status |
|------|--------|
| `os-connect/index.md` | draft |
| `os-connect/can-agencies-provide-their-own-sidewalk-or-curb-ramp-data-for-integration.md` | stub |
| `os-connect/can-agencies-submit-priority-areas-for-review.md` | stub |
| `os-connect/can-ai-automatically-detect-curb-ramps.md` | stub |
| `os-connect/can-ai-automatically-identify-pedestrian-barriers.md` | stub |
| `os-connect/can-ai-estimate-sidewalk-quality.md` | stub |
| `os-connect/can-ai-help-identify-accessibility-inequities.md` | stub |
| `os-connect/can-ai-help-prioritize-infrastructure-investment.md` | stub |
| `os-connect/can-an-agency-submit-a-batch-of-known-corrections-instead-of-reporting-one-issue-at-a-time.md` | stub |
| `os-connect/can-i-use-this-in-arcgis-or-qgis.md` | stub |
| `os-connect/can-mapping-volunteers-contribute-data-that-agencies-can-use.md` | stub |
| `os-connect/can-os-connect-be-used-for-ada-transition-planning.md` | stub |
| `os-connect/can-os-connect-generate-gtfs-pathways-data.md` | stub |
| `os-connect/can-os-connect-support-bus-stop-planning.md` | stub |
| `os-connect/can-os-connect-support-capital-planning.md` | stub |
| `os-connect/can-os-connect-support-fifa-or-major-event-accessibility-planning.md` | stub |
| `os-connect/can-os-connect-support-pedestrian-access-analysis-around-schools-clinics-grocery-stores-and-other-destinations.md` | stub |
| `os-connect/can-os-connect-support-service-planning-and-reliability-analysis.md` | stub |
| `os-connect/can-routing-systems-personalize-accessibility-preferences.md` | stub |
| `os-connect/can-tcat-help-set-up-a-sidewalk-mapping-project-in-the-osm-us-tasking-manager.md` | stub |
| `os-connect/can-this-data-support-curb-ramp-inventories.md` | stub |
| `os-connect/can-this-data-support-safe-routes-to-school.md` | stub |
| `os-connect/can-this-data-support-transit-accessibility-analysis.md` | stub |
| `os-connect/can-this-data-support-vision-zero.md` | stub |
| `os-connect/do-reported-issues-automatically-update-the-public-dataset.md` | stub |
| `os-connect/does-a-correction-update-os-connect-openstreetmap-tdei-or-all-of-them.md` | stub |
| `os-connect/how-accurate-is-the-data.md` | stub |
| `os-connect/how-are-agency-submitted-corrections-validated.md` | stub |
| `os-connect/how-are-campuses-handled.md` | stub |
| `os-connect/how-are-community-comments-reviewed.md` | stub |
| `os-connect/how-are-complex-intersections-handled.md` | stub |
| `os-connect/how-are-construction-changes-handled.md` | stub |
| `os-connect/how-are-corrections-tracked-across-releases.md` | stub |
| `os-connect/how-are-crossings-inferred.md` | stub |
| `os-connect/how-are-curb-ramps-identified.md` | stub |
| `os-connect/how-are-disconnected-sidewalks-identified.md` | stub |
| `os-connect/how-are-pedestrian-only-facilities-handled.md` | stub |
| `os-connect/how-are-private-facilities-handled.md` | stub |
| `os-connect/how-are-rural-areas-handled.md` | stub |
| `os-connect/how-are-trails-handled.md` | stub |
| `os-connect/how-can-advocacy-groups-use-os-connect.md` | stub |
| `os-connect/how-can-advocacy-organizations-participate.md` | stub |
| `os-connect/how-can-ai-assist-stewardship.md` | stub |
| `os-connect/how-can-an-agency-confirm-that-a-submitted-correction-was-incorporated.md` | stub |
| `os-connect/how-can-communities-identify-accessibility-gaps.md` | stub |
| `os-connect/how-can-communities-identify-missing-infrastructure.md` | stub |
| `os-connect/how-can-communities-use-walksheds-to-advocate-for-change.md` | stub |
| `os-connect/how-can-community-members-contribute-corrections.md` | stub |
| `os-connect/how-can-disability-communities-contribute.md` | stub |
| `os-connect/how-can-local-governments-use-community-feedback.md` | stub |
| `os-connect/how-can-older-adults-contribute.md` | stub |
| `os-connect/how-can-people-report-inaccessible-areas.md` | stub |
| `os-connect/how-can-residents-participate.md` | stub |
| `os-connect/how-can-rural-communities-participate.md` | stub |
| `os-connect/how-can-schools-participate.md` | stub |
| `os-connect/how-can-stewardship-remain-sustainable-after-funding-ends.md` | stub |
| `os-connect/how-can-this-data-support-freedom-of-movement-for-nondrivers.md` | stub |
| `os-connect/how-can-trip-planners-use-sidewalk-street-name-tags-to-produce-better-walking-instructions.md` | stub |
| `os-connect/how-could-accessibility-stewardship-become-sustainable.md` | stub |
| `os-connect/how-could-national-accessibility-data-standards-evolve.md` | stub |
| `os-connect/how-could-transit-and-pedestrian-systems-integrate-more-deeply.md` | stub |
| `os-connect/how-do-elevation-constraints-affect-routing.md` | stub |
| `os-connect/how-do-i-connect-this-to-gis-software.md` | stub |
| `os-connect/how-do-i-download-data-from-the-viewer.md` | stub |
| `os-connect/how-do-i-import-os-connect-osw-geojson-into-arcgis.md` | stub |
| `os-connect/how-do-i-report-an-error-in-os-connect-data.md` | stub |
| `os-connect/how-do-i-search-for-a-jurisdiction.md` | stub |
| `os-connect/how-do-opensidewalks-mapping-efforts-relate-to-local-community-mapping-groups-such-as-maptimela.md` | stub |
| `os-connect/how-does-os-connect-support-accessibility-equity.md` | stub |
| `os-connect/how-does-os-connect-support-mobility-justice.md` | stub |
| `os-connect/how-does-this-improve-accessibility.md` | stub |
| `os-connect/how-does-this-improve-mobility-equity.md` | stub |
| `os-connect/how-does-this-improve-safety.md` | stub |
| `os-connect/how-is-os-connect-different-from-openstreetmap.md` | stub |
| `os-connect/how-is-os-connect-related-to-tdei.md` | stub |
| `os-connect/how-long-do-corrections-take-to-appear-in-a-public-release.md` | stub |
| `os-connect/how-often-is-the-dataset-updated.md` | stub |
| `os-connect/how-should-accessibility-advocates-contribute.md` | stub |
| `os-connect/how-should-accessibility-tradeoffs-be-communicated.md` | stub |
| `os-connect/how-should-agencies-report-corrections.md` | stub |
| `os-connect/how-should-agencies-treat-os-connect-data-in-planning-workflows-when-known-errors-exist.md` | stub |
| `os-connect/how-should-agencies-use-this-data-operationally.md` | stub |
| `os-connect/how-should-agencies-validate-the-data-locally.md` | stub |
| `os-connect/how-should-communities-decide-which-areas-to-map-first.md` | stub |
| `os-connect/how-should-conflicting-data-sources-be-handled.md` | stub |
| `os-connect/how-should-counties-coordinate-updates.md` | stub |
| `os-connect/how-should-field-validation-be-incorporated.md` | stub |
| `os-connect/how-should-human-review-be-incorporated.md` | stub |
| `os-connect/how-should-jurisdictions-maintain-updates.md` | stub |
| `os-connect/how-should-jurisdictions-participate-in-stewardship.md` | stub |
| `os-connect/how-should-mpos-contribute.md` | stub |
| `os-connect/how-should-transit-agencies-contribute.md` | stub |
| `os-connect/how-should-municipalities-interpret-completeness-scores.md` | stub |
| `os-connect/how-should-planners-validate-the-data.md` | stub |
| `os-connect/how-should-separately-mapped-sidewalks-be-associated-with-street-names-in-osm.md` | stub |
| `os-connect/how-was-os-connect-collected.md` | stub |
| `os-connect/is-completeness-ada-compliance.md` | stub |
| `os-connect/is-this-a-statewide-inventory.md` | stub |
| `os-connect/what-accessibility-information-is-missing-from-os-connect.md` | stub |
| `os-connect/what-additional-data-is-needed-for-ada-transition-plans.md` | stub |
| `os-connect/what-am-i-looking-at-in-this-viewer.md` | stub |
| `os-connect/what-are-the-biggest-barriers-to-adoption.md` | stub |
| `os-connect/what-are-the-community-engagement-pathways.md` | stub |
| `os-connect/what-are-the-community-participation-pathways.md` | stub |
| `os-connect/what-are-the-different-map-layers.md` | stub |
| `os-connect/what-are-the-jurisdiction-engagement-pathways.md` | stub |
| `os-connect/what-are-the-jurisdiction-participation-pathways.md` | stub |
| `os-connect/what-are-the-risks-of-relying-solely-on-automated-data.md` | stub |
| `os-connect/what-attributes-are-collected-for-crossings.md` | stub |
| `os-connect/what-attributes-are-collected-for-curb-ramps.md` | stub |
| `os-connect/what-attributes-are-collected-for-intersections.md` | stub |
| `os-connect/what-attributes-are-collected-for-sidewalks.md` | stub |
| `os-connect/what-attributes-are-included-for-sidewalks-crossings-curb-ramps-and-related-pedestrian-features.md` | stub |
| `os-connect/what-attributes-are-required-vs-recommended.md` | stub |
| `os-connect/what-comes-after-statewide-collection.md` | stub |
| `os-connect/what-confidence-measures-exist.md` | stub |
| `os-connect/what-coordinate-system-is-used.md` | stub |
| `os-connect/what-do-the-colors-mean.md` | stub |
| `os-connect/what-do-walkshed-metrics-represent.md` | stub |
| `os-connect/what-does-ada-title-ii-part-b-require.md` | stub |
| `os-connect/what-does-avoid-curbs-mean.md` | stub |
| `os-connect/what-does-centrality-mean.md` | stub |
| `os-connect/what-does-completeness-mean.md` | stub |
| `os-connect/what-does-connected-pedestrian-graph-mean.md` | stub |
| `os-connect/what-does-crossing-count-mean.md` | stub |
| `os-connect/what-does-it-mean-that-os-connect-uses-the-opensidewalks-schema.md` | stub |
| `os-connect/what-does-long-term-stewardship-actually-require-operationally.md` | stub |
| `os-connect/what-does-participatory-mapping-mean.md` | stub |
| `os-connect/what-does-path-count-mean.md` | stub |
| `os-connect/what-does-street-avoidance-mean.md` | stub |
| `os-connect/what-does-surface-mean.md` | stub |
| `os-connect/what-does-this-selected-feature-represent.md` | stub |
| `os-connect/what-does-width-mean-in-the-dataset.md` | stub |
| `os-connect/what-future-capabilities-are-planned-for-os-connect.md` | stub |
| `os-connect/what-gaps-still-exist-in-accessibility-data.md` | stub |
| `os-connect/what-geographic-areas-are-covered.md` | stub |
| `os-connect/what-governance-models-are-possible.md` | stub |
| `os-connect/what-happened-to-the-older-opensidewalks-mapwithai-tasking-manager-workflow.md` | stub |
| `os-connect/what-happens-after-i-submit-an-issue-report.md` | stub |
| `os-connect/what-happens-when-data-becomes-outdated.md` | stub |
| `os-connect/what-happens-when-imagery-is-outdated.md` | stub |
| `os-connect/what-happens-when-jurisdictions-disagree-with-the-data.md` | stub |
| `os-connect/what-information-should-agencies-include-when-reporting-a-data-issue.md` | stub |
| `os-connect/what-is-a-crossing-edge.md` | stub |
| `os-connect/what-is-a-node-versus-an-edge.md` | stub |
| `os-connect/what-is-a-routable-graph.md` | stub |
| `os-connect/what-is-an-accessibility-attribute.md` | stub |
| `os-connect/what-is-an-accessibility-island.md` | stub |
| `os-connect/what-is-an-interoperable-accessibility-ecosystem.md` | stub |
| `os-connect/what-is-context-aware-routing.md` | stub |
| `os-connect/what-is-edge-betweenness.md` | stub |
| `os-connect/what-is-eigenvector-centrality.md` | stub |
| `os-connect/what-is-multimodal-accessibility-analysis.md` | stub |
| `os-connect/what-is-opensidewalks.md` | stub |
| `os-connect/what-is-os-connect.md` | stub |
| `os-connect/what-is-participatory-accessibility-mapping.md` | stub |
| `os-connect/what-is-the-difference-between-street-name-and-is-sidepath-of-name.md` | stub |
| `os-connect/what-is-the-difference-between-the-viewer-and-the-tdei-portal.md` | stub |
| `os-connect/what-is-the-manual-wheelchair-profile.md` | stub |
| `os-connect/what-is-the-maximum-travel-cost.md` | stub |
| `os-connect/what-is-the-opensidewalks-schema.md` | stub |
| `os-connect/what-is-the-qa-qc-report.md` | stub |
| `os-connect/what-is-the-relationship-between-local-ownership-and-statewide-coordination.md` | stub |
| `os-connect/what-is-the-relationship-between-os-connect-and-local-gis.md` | stub |
| `os-connect/what-kinds-of-errors-are-most-common.md` | stub |
| `os-connect/what-kinds-of-errors-should-be-reported-through-the-os-connect-viewer.md` | stub |
| `os-connect/what-kinds-of-partnerships-are-needed.md` | stub |
| `os-connect/what-kinds-of-pedestrian-infrastructure-are-included.md` | stub |
| `os-connect/what-kinds-of-pedestrian-infrastructure-are-not-included.md` | stub |
| `os-connect/what-lessons-could-other-states-adopt.md` | stub |
| `os-connect/what-lessons-has-washington-learned.md` | stub |
| `os-connect/what-licensing-governs-the-data.md` | stub |
| `os-connect/what-makes-accessibility-data-difficult-to-maintain.md` | stub |
| `os-connect/what-makes-community-mapped-sidewalk-data-usable-for-agency-workflows.md` | stub |
| `os-connect/what-makes-os-connect-different-from-traditional-inventories.md` | stub |
| `os-connect/what-makes-pedestrian-data-uniquely-complex.md` | stub |
| `os-connect/what-makes-pedestrian-infrastructure-equitable.md` | stub |
| `os-connect/what-operational-roles-are-needed-for-stewardship.md` | stub |
| `os-connect/what-operational-workflows-still-need-improvement.md` | stub |
| `os-connect/what-problem-is-os-connect-trying-to-solve.md` | stub |
| `os-connect/what-quality-checks-are-needed-before-community-mapped-data-can-support-planning-or-routing.md` | stub |
| `os-connect/what-risks-exist-in-ai-generated-accessibility-data.md` | stub |
| `os-connect/what-role-could-advocacy-groups-play.md` | stub |
| `os-connect/what-role-could-crowdsourcing-play.md` | stub |
| `os-connect/what-role-could-mpos-play.md` | stub |
| `os-connect/what-role-could-open-source-communities-play.md` | stub |
| `os-connect/what-role-could-states-play-in-stewardship.md` | stub |
| `os-connect/what-role-could-universities-play.md` | stub |
| `os-connect/what-role-did-community-validation-play.md` | stub |
| `os-connect/what-role-did-field-validation-play.md` | stub |
| `os-connect/what-role-did-imagery-play.md` | stub |
| `os-connect/what-role-did-machine-learning-play.md` | stub |
| `os-connect/what-routing-assumptions-are-used.md` | stub |
| `os-connect/what-should-agencies-do-if-they-need-a-correction-sooner-than-the-next-public-release.md` | stub |
| `os-connect/what-should-mappers-do-when-a-sidewalk-is-separated-from-the-road-geometry.md` | stub |
| `os-connect/what-should-trip-planning-vendors-do-when-osm-pedestrian-paths-do-not-include-street-names.md` | stub |
| `os-connect/what-training-materials-are-available-for-new-sidewalk-mappers.md` | stub |
| `os-connect/what-workflows-support-long-term-maintenance.md` | stub |
| `os-connect/what-would-a-nationwide-os-connect-like-system-require.md` | stub |
| `os-connect/where-are-opensidewalks-attribute-definitions-documented.md` | stub |
| `os-connect/which-sidewalk-to-street-name-tagging-pattern-is-currently-recommended.md` | stub |
| `os-connect/who-is-responsible-for-long-term-stewardship.md` | stub |
| `os-connect/who-is-responsible-for-updates.md` | stub |
| `os-connect/who-maintains-os-connect.md` | stub |
| `os-connect/who-owns-os-connect-data.md` | stub |
| `os-connect/who-reviews-submitted-issue-reports.md` | stub |
| `os-connect/why-are-disconnected-pedestrian-datasets-a-problem.md` | stub |
| `os-connect/why-are-lived-experiences-important.md` | stub |
| `os-connect/why-are-pois-grouped-together.md` | stub |
| `os-connect/why-are-sidewalks-disconnected.md` | stub |
| `os-connect/why-are-some-destinations-unreachable.md` | stub |
| `os-connect/why-are-some-sidewalks-disconnected.md` | stub |
| `os-connect/why-are-z-scores-used.md` | stub |
| `os-connect/why-can-a-city-have-high-completeness-but-still-accessibility-gaps.md` | stub |
| `os-connect/why-can-automated-systems-miss-accessibility-barriers.md` | stub |
| `os-connect/why-do-different-profiles-produce-different-walksheds.md` | stub |
| `os-connect/why-do-some-areas-appear-incomplete.md` | stub |
| `os-connect/why-do-some-features-have-missing-values.md` | stub |
| `os-connect/why-do-street-names-matter-for-walking-directions.md` | stub |
| `os-connect/why-does-pedestrian-data-matter-statewide.md` | stub |
| `os-connect/why-is-the-map-slow-or-dense-in-urban-areas.md` | stub |
| `os-connect/why-should-the-public-care-about-pedestrian-data.md` | stub |
| `os-connect/why-was-os-connect-created.md` | stub |

### `accessmap/` — AccessMap

See [accessmap/index.md](accessmap/index.md) for a richer, annotated listing.

| File | Status |
|------|--------|
| `accessmap/index.md` | draft |
| `accessmap/can-accessmap-integrate-with-gtfs.md` | stub |
| `accessmap/can-accessmap-support-ada-compliance-workflows.md` | stub |
| `accessmap/can-accessmap-support-blind-or-low-vision-users.md` | stub |
| `accessmap/can-accessmap-support-campus-accessibility.md` | stub |
| `accessmap/can-accessmap-support-hospitals-or-medical-campuses.md` | stub |
| `accessmap/can-accessmap-support-manual-wheelchair-users.md` | stub |
| `accessmap/can-accessmap-support-paratransit-planning.md` | stub |
| `accessmap/can-accessmap-support-powered-wheelchair-users.md` | stub |
| `accessmap/can-accessmap-support-tourism-accessibility.md` | stub |
| `accessmap/can-accessmap-support-transit-wayfinding.md` | stub |
| `accessmap/can-agencies-customize-routing-profiles.md` | stub |
| `accessmap/can-communities-define-accessibility-priorities.md` | stub |
| `accessmap/can-temporary-barriers-be-represented.md` | stub |
| `accessmap/how-are-curb-ramps-incorporated-into-routing.md` | stub |
| `accessmap/how-are-inaccessible-transit-stations-represented.md` | stub |
| `accessmap/how-are-slopes-incorporated-into-routing.md` | stub |
| `accessmap/how-can-accessmap-support-emergency-planning.md` | stub |
| `accessmap/how-can-accessmap-support-public-engagement.md` | stub |
| `accessmap/how-can-agencies-compare-routing-systems.md` | stub |
| `accessmap/how-can-agencies-explain-these-metrics-publicly.md` | stub |
| `accessmap/how-can-agencies-identify-critical-pedestrian-corridors.md` | stub |
| `accessmap/how-can-cities-use-accessmap-operationally.md` | stub |
| `accessmap/how-can-schools-use-accessmap.md` | stub |
| `accessmap/how-can-users-report-routing-problems.md` | stub |
| `accessmap/how-do-local-datasets-improve-routing-quality.md` | stub |
| `accessmap/how-do-missing-curb-ramps-affect-route-selection.md` | stub |
| `accessmap/how-do-mobility-profiles-work.md` | stub |
| `accessmap/how-do-steep-slopes-affect-route-selection.md` | stub |
| `accessmap/how-does-accessmap-calculate-accessible-routes.md` | stub |
| `accessmap/how-does-accessmap-consume-opensidewalks-or-os-connect-data.md` | stub |
| `accessmap/how-does-construction-affect-routing.md` | stub |
| `accessmap/how-does-transit-accessibility-integrate-with-pedestrian-routing.md` | stub |
| `accessmap/how-is-accessmap-different-from-google-maps.md` | stub |
| `accessmap/how-often-is-accessmap-updated.md` | stub |
| `accessmap/how-should-municipalities-validate-routing-results.md` | stub |
| `accessmap/how-should-planners-prioritize-pedestrian-investments.md` | stub |
| `accessmap/what-accessibility-assumptions-are-built-into-accessmap.md` | stub |
| `accessmap/what-accessibility-needs-does-accessmap-support.md` | stub |
| `accessmap/what-are-routing-tradeoffs.md` | stub |
| `accessmap/what-are-the-limitations-of-accessmap-routing.md` | stub |
| `accessmap/what-data-powers-accessmap.md` | stub |
| `accessmap/what-does-avoid-missing-curb-ramps-mean.md` | stub |
| `accessmap/what-does-avoid-steep-slopes-mean.md` | stub |
| `accessmap/what-does-edge-betweenness-reveal-operationally.md` | stub |
| `accessmap/what-does-it-mean-to-route-using-accessibility-preferences.md` | stub |
| `accessmap/what-future-capabilities-are-planned-for-accessmap.md` | stub |
| `accessmap/what-happens-when-accessibility-data-is-missing.md` | stub |
| `accessmap/what-happens-when-sidewalks-are-disconnected.md` | stub |
| `accessmap/what-is-accessmap.md` | stub |
| `accessmap/what-is-gtfs-pathways.md` | stub |
| `accessmap/what-is-network-redundancy.md` | stub |
| `accessmap/what-is-pedestrian-resilience.md` | stub |
| `accessmap/what-is-route-reliability.md` | stub |
| `accessmap/what-metrics-best-support-accessibility-prioritization.md` | stub |
| `accessmap/what-metrics-matter-most-for-accessible-mobility.md` | stub |
| `accessmap/what-role-does-field-validation-play.md` | stub |
| `accessmap/what-routing-profiles-are-available.md` | stub |
| `accessmap/why-do-accessibility-aware-routes-sometimes-appear-longer.md` | stub |
| `accessmap/why-does-accessmap-choose-longer-routes.md` | stub |
| `accessmap/why-does-accessmap-differ-from-apple-maps.md` | stub |
| `accessmap/why-does-accessmap-differ-from-google-maps.md` | stub |
| `accessmap/why-does-accessmap-differ-from-here-routing.md` | stub |

### `walksheds/` — Walksheds

See [walksheds/index.md](walksheds/index.md) for a richer, annotated listing.

| File | Status |
|------|--------|
| `walksheds/index.md` | draft |
| `walksheds/can-walksheds-be-joined-with-census-crash-or-internal-agency-datasets.md` | stub |
| `walksheds/how-are-barriers-incorporated.md` | stub |
| `walksheds/how-are-disconnected-networks-handled.md` | stub |
| `walksheds/how-are-walksheds-calculated.md` | stub |
| `walksheds/how-can-accessibility-profiles-reveal-inequities.md` | stub |
| `walksheds/how-can-agencies-compare-neighborhoods.md` | stub |
| `walksheds/how-can-planners-compare-accessibility-before-and-after-improvements.md` | stub |
| `walksheds/how-can-walksheds-compare-infrastructure-scenarios.md` | stub |
| `walksheds/how-can-walksheds-help-analyze-access-to-bus-stops.md` | stub |
| `walksheds/how-can-walksheds-identify-crossing-gaps.md` | stub |
| `walksheds/how-can-walksheds-identify-pedestrian-bottlenecks.md` | stub |
| `walksheds/how-can-walksheds-identify-underserved-areas.md` | stub |
| `walksheds/how-can-walksheds-support-ada-planning.md` | stub |
| `walksheds/how-can-walksheds-support-complete-streets-planning.md` | stub |
| `walksheds/how-can-walksheds-support-downtown-revitalization.md` | stub |
| `walksheds/how-can-walksheds-support-economic-development.md` | stub |
| `walksheds/how-can-walksheds-support-emergency-resilience-planning.md` | stub |
| `walksheds/how-can-walksheds-support-equity-analysis.md` | stub |
| `walksheds/how-can-walksheds-support-grant-applications.md` | stub |
| `walksheds/how-can-walksheds-support-hospital-access-analysis.md` | stub |
| `walksheds/how-can-walksheds-support-park-access-analysis.md` | stub |
| `walksheds/how-can-walksheds-support-prioritization-workflows.md` | stub |
| `walksheds/how-can-walksheds-support-rural-transportation-planning.md` | stub |
| `walksheds/how-can-walksheds-support-safe-routes-to-school.md` | stub |
| `walksheds/how-can-walksheds-support-school-accessibility-analysis.md` | stub |
| `walksheds/how-can-walksheds-support-senior-mobility-analysis.md` | stub |
| `walksheds/how-can-walksheds-support-srts.md` | stub |
| `walksheds/how-can-walksheds-support-transit-planning.md` | stub |
| `walksheds/how-can-walksheds-support-vision-zero.md` | stub |
| `walksheds/how-do-crossings-affect-walksheds.md` | stub |
| `walksheds/how-does-elevation-affect-walksheds.md` | stub |
| `walksheds/how-does-walksheds-use-os-connect-data.md` | stub |
| `walksheds/how-is-a-walkshed-different-from-a-buffer.md` | stub |
| `walksheds/how-should-uncertainty-be-communicated-in-walkshed-outputs.md` | stub |
| `walksheds/what-accessibility-profiles-are-supported.md` | stub |
| `walksheds/what-are-accessibility-islands-in-walkshed-analysis.md` | stub |
| `walksheds/what-are-good-public-facing-ways-to-explain-walksheds.md` | stub |
| `walksheds/what-are-the-limitations-of-walkshed-analysis.md` | stub |
| `walksheds/what-assumptions-should-planners-understand.md` | stub |
| `walksheds/what-does-a-pedestrian-walkshed-represent.md` | stub |
| `walksheds/what-does-a-wheelchair-walkshed-represent.md` | stub |
| `walksheds/what-does-reachable-area-mean.md` | stub |
| `walksheds/what-future-capabilities-are-planned-for-walksheds.md` | stub |
| `walksheds/what-is-a-walkshed.md` | stub |
| `walksheds/what-is-max-cost.md` | stub |
| `walksheds/what-is-the-difference-between-a-pedestrian-walkshed-and-a-wheelchair-user-walkshed.md` | stub |
| `walksheds/what-is-the-walksheds-tool.md` | stub |
| `walksheds/what-makes-a-walkshed-good-or-bad.md` | stub |
| `walksheds/what-network-assumptions-are-used.md` | stub |
| `walksheds/what-travel-limits-are-used.md` | stub |
| `walksheds/what-travel-profiles-are-available-in-walksheds.md` | stub |
| `walksheds/why-are-some-destinations-excluded.md` | stub |
| `walksheds/why-are-walksheds-more-accurate-than-straight-line-distance.md` | stub |

### `tdei/` — TDEI

| File | Status |
|------|--------|
| `tdei/index.md` | draft |
| `tdei/how-are-releases-versioned.md` | stub |
| `tdei/how-do-i-access-the-tdei-api.md` | stub |
| `tdei/how-do-i-know-whether-a-dataset-is-current.md` | stub |
| `tdei/how-do-i-use-the-tdei-portal.md` | stub |
| `tdei/how-does-tdei-support-interoperability.md` | stub |
| `tdei/what-are-edges-and-nodes-in-the-osw-download.md` | stub |
| `tdei/what-does-released-dataset-mean-in-tdei.md` | stub |
| `tdei/what-file-formats-are-available.md` | stub |
| `tdei/what-files-are-included-in-an-osw-download.md` | stub |
| `tdei/what-is-a-project-group-in-tdei.md` | stub |
| `tdei/what-is-tdei.md` | stub |
| `tdei/what-is-the-dataset-identifier.md` | stub |
| `tdei/what-is-the-difference-between-downloading-osw-format-and-osm-format.md` | stub |
| `tdei/what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file.md` | stub |
| `tdei/where-can-i-download-the-data.md` | stub |
| `tdei/where-do-i-download-os-connect-data.md` | stub |
| `tdei/why-might-a-test-dataset-appear-in-the-portal.md` | stub |

### `qa-qc/` — QA/QC

| File | Status |
|------|--------|
| `qa-qc/what-are-the-limitations-of-qa-qc-analysis.md` | draft |
| `qa-qc/what-does-edge-betweenness-reveal-operationally.md` | stub |
| `qa-qc/what-does-node-centrality-reveal-operationally.md` | stub |

### `support/` — Cross-Product Support

| File | Status |
|------|--------|
| `support/index.md` | draft |
| `support/helpline-faq-backlog.md` | draft |
| `support/are-sound-transit-or-other-agencies-publishing-gtfs-pathways-data.md` | stub |
| `support/can-agencies-or-community-groups-attend-mappy-hours.md` | stub |
| `support/ecosystem-differences-tdei-os-connect-opensidewalks-osm-accessmap-walksheds-gtfs.md` | stub |
| `support/how-can-i-tell-whether-a-gtfs-feed-includes-pathways-txt.md` | stub |
| `support/how-can-os-connect-and-walksheds-support-bus-stop-planning.md` | stub |
| `support/how-do-i-know-whether-a-dataset-is-authoritative.md` | stub |
| `support/how-is-accessmap-different-from-walksheds.md` | stub |
| `support/how-is-gtfs-pathways-different-from-os-connect.md` | stub |
| `support/how-is-os-connect-different-from-gtfs-pathways.md` | stub |
| `support/how-should-an-agency-cite-os-connect-or-tdei-data.md` | stub |
| `support/how-should-staff-distinguish-current-functionality-from-future-plans.md` | stub |
| `support/how-should-staff-explain-uncertainty-without-sounding-evasive.md` | stub |
| `support/how-should-staff-introduce-related-tools-without-making-the-answer-feel-like-a-sales-pitch.md` | stub |
| `support/what-is-the-difference-between-tdei-os-connect-opensidewalks-and-openstreetmap.md` | stub |
| `support/what-is-the-relationship-between-pedestrian-paths-in-openstreetmap-and-gtfs-pathways.md` | stub |
| `support/what-language-should-staff-use-when-a-question-requires-internal-verification.md` | stub |
| `support/what-response-time-should-external-partners-expect.md` | stub |
| `support/what-should-agencies-do-if-gtfs-pathways-data-are-missing-but-pedestrian-data-exist-in-osm-or-os-connect.md` | stub |
| `support/what-should-staff-avoid-saying-in-external-technical-support-emails.md` | stub |
| `support/what-should-staff-do-when-they-do-not-know-the-answer-to-a-partner-s-question.md` | stub |
| `support/when-should-someone-be-referred-to-mappy-hours-versus-receiving-direct-support.md` | stub |
| `support/which-dataset-and-format-should-an-agency-use-for-pedestrian-walkway-data-in-arcgis.md` | stub |
| `support/which-dataset-should-i-use-if-i-need-pedestrian-walkway-data-for-planning.md` | stub |
| `support/which-dataset-should-i-use-if-i-need-transit-station-pathway-data.md` | stub |
| `support/who-owns-follow-up-when-a-partner-asks-a-question-that-crosses-tools-or-teams.md` | stub |
| `support/who-should-external-partners-contact-for-opensidewalks-mapping-questions.md` | stub |
| `support/who-should-external-partners-contact-for-os-connect-data-questions.md` | stub |
| `support/who-should-external-partners-contact-for-tdei-support.md` | stub |

### `concepts/` — Cross-Product Concepts

| File | Status |
|------|--------|
| `concepts/index.md` | draft |
| `concepts/accessibility-islands.md` | stub |
| `concepts/accessmap-routing.md` | stub |
| `concepts/ada-compliance-boundaries.md` | stub |
| `concepts/completeness.md` | stub |
| `concepts/connected-pedestrian-graph.md` | stub |
| `concepts/walksheds.md` | stub |

### `policies/` — Cross-Product Policies

| File | Status |
|------|--------|
| `policies/index.md` | draft |
| `policies/workspace-abstention-boundaries.md` | stub |
| `policies/workspace-data-freshness.md` | stub |
| `policies/workspace-editing-authority.md` | stub |
| `policies/workspace-export-and-publication-caveats.md` | stub |
| `policies/workspace-public-vs-private-data.md` | stub |
| `policies/ada-safety-legal-boundaries.md` | stub |
| `policies/assistant-abstention.md` | stub |
| `policies/assistant-policy-questions-index.md` | stub |
| `policies/data-freshness.md` | stub |
| `policies/how-should-ai-outputs-be-validated.md` | stub |
| `policies/public-vs-internal-content.md` | stub |
| `policies/what-are-the-risks-of-automated-accessibility-analysis.md` | stub |

### `workflows/` — Cross-Product Workflows

| File | Status |
|------|--------|
| `workflows/index.md` | draft |
| `workflows/review-community-feedback.md` | stub |
| `workflows/support-answer-patterns.md` | stub |
| `workflows/update-jurisdiction-data.md` | stub |
| `workflows/use-accessmap-for-public-engagement.md` | stub |
| `workflows/use-os-connect-for-ada-transition-planning.md` | stub |
| `workflows/use-walksheds-for-safe-routes-to-school.md` | stub |

### `glossary/` — Glossary

| File | Status |
|------|--------|
| `glossary/index.md` | stub |
| `glossary/terms.md` | stub |

### `intents/` — Assistant Intents

| File | Status |
|------|--------|
| `intents/index.md` | draft |
| `intents/support-intents.md` | stub |
