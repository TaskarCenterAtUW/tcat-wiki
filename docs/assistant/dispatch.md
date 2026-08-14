---
title: Assistant Knowledge Base — Dispatch
slug: dispatch
doc_type: workflow
questions:
    - What articles are available in the TCAT Wiki Assistant Knowledge Base?
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
    - assistant-layer
    - governance
risk_level: low
authority_level: official
publication_status: draft
last_reviewed: 2026-08-14
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/schema.md
    - assistant/intents.md
tags:
    - Assistant
---

<!-- @format -->

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Produced by utilities/akb-generate-dispatch.py. Re-run the script
     (or utilities/build-site.py) to refresh this file after adding,
     removing, or re-statusing pages under docs/assistant/. -->

# Assistant Knowledge Base — Dispatch

## Short Answer

This file is the registry for all pages in the `docs/assistant/` knowledge base. It is the single source of truth for canonical file paths, authoring status, and section structure. External agents should fetch this file first to enumerate available knowledge-base pages before retrieving individual articles.

Related: [Overview](index.md) · [Schema](schema.md) · [Intents](intents.md)

## Significance

A stable registry decouples retrieval pipelines from the filesystem. Authors use this file to track what has been written, what is still a stub, and what needs review. Integrators can use it to detect new pages without crawling the entire site.

## What This Means

- Every article that physically exists in `docs/assistant/` has a row in this registry; nothing here is aspirational.
- **Publication status** is one of: `stub` (placeholder exists, body is `TODO`), `draft` (content authored, awaiting review), `published` (available in the human layer), or `archived` (retained for agents but not published).
- Every page listed here is served as raw Markdown at the same URL with an `.md` extension, regardless of status. See [schema](schema.md) for the human-layer vs. agent-layer distinction.
- Section index files (e.g., `workspaces/index.md`) carry that topic's policy content and per-topic assistant guidance.

## What This Does Not Mean

- This file does not replace the [schema](schema.md), which governs authoring conventions.
- This file does not replace section indexes, which provide richer per-section context.
- A `stub` status does not mean the content is wrong — it means the body has not yet been authored.

## How To Use This

**Agents**: Fetch `dispatch.md`, parse the registry tables, filter by `Status` or topic heading, then retrieve individual pages by constructing their URL as `https://taskarcenteratuw.github.io/tcat-wiki/` + the `Base:` path shown under the relevant heading + the filename in the table.

**Authors**: Write or edit files directly under `docs/assistant/`; do not hand-edit this file. Re-run `utilities/akb-generate-dispatch.py` (or the full `utilities/build-site.py` pipeline) to refresh the registry after adding a page or changing its `publication_status`.

**Maintainers**: This file is a generated build artifact. To change its structure, edit `utilities/akb-generate-dispatch.py`.

## Example

An agent looking for Workspaces content: fetches this file, finds the `## Workspaces` heading, selects a relevant row from its `### Concepts` or `### Workflows` table, then fetches that page using the `Base:` prefix plus the filename.

## Assistant Guidance

This page should be fetched fresh rather than cached aggressively; its registry reflects the current authoring state of the knowledge base. If a file listed here returns 404, the generator has not yet been re-run since the file was added.

## Related Concepts

- [Assistant Knowledge Base Index](index.md) — Overview of this retrieval-oriented TCAT knowledge base
- [Assistant Knowledge Base Schema](schema.md) — Authoring contract for Assistant Knowledge Base articles
- [Assistant Knowledge Base Intents](intents.md) — Mapping of retrieval intents to article paths

## Status Legend

| Status | Count | Meaning |
| :----- | ----: | :------ |
| `stub` | 432 | Frontmatter and heading scaffold exist; body is `TODO` |
| `draft` | 348 | Content authored; awaiting TCAT editorial review |
| `published` | 1 | Available in the human-facing site |
| `archived` | 0 | Retained for agents but not published |

## Authority Legend

| Authority level | Count | Meaning |
| :-------------- | ----: | :------ |
| `provisional` | 415 | Early or limited-confidence guidance |
| `explanatory` | 364 | Established explanation without formal policy authority |
| `official` | 2 | Formally endorsed organizational guidance |

## Registry

## AccessMap — Assistant Knowledge Base

See [accessmap/index.md](accessmap/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/accessmap/concept/`

| File | Status |
| :--- | :----- |
| `accessibility-assumptions.md` | stub |
| `accessibility-mobility-metrics.md` | stub |
| `accessibility-needs.md` | stub |
| `accessibility-preference-routing.md` | stub |
| `accessible-routes-appear-longer.md` | stub |
| `accessmap.md` | draft |
| `ada-compliance-support.md` | stub |
| `agency-routing-customization.md` | stub |
| `avoid-missing-curb-ramps.md` | stub |
| `avoid-steep-slopes.md` | stub |
| `blind-low-vision-support.md` | draft |
| `campus-accessibility.md` | stub |
| `combined-crossing-accessibility.md` | draft |
| `community-accessibility-priorities.md` | stub |
| `comparison-apple-maps.md` | stub |
| `construction-routing-effect.md` | stub |
| `coverage-outside-washington.md` | draft |
| `critical-pedestrian-corridors.md` | stub |
| `crossing-links.md` | draft |
| `curb-ramp-routing.md` | stub |
| `data-sources.md` | draft |
| `disconnected-sidewalks.md` | stub |
| `emergency-planning.md` | stub |
| `explaining-metrics-publicly.md` | stub |
| `feature-feedback.md` | draft |
| `field-validation.md` | stub |
| `google-maps-comparison.md` | stub |
| `google-maps-design-rationale.md` | stub |
| `gtfs-integration.md` | stub |
| `gtfs-pathways.md` | draft |
| `here-routing-comparison.md` | stub |
| `hospital-campus-support.md` | stub |
| `inaccessible-transit-stations.md` | stub |
| `local-datasets-routing-quality.md` | stub |
| `longer-route-selection.md` | draft |
| `manual-wheelchair-support.md` | stub |
| `missing-accessibility-data.md` | stub |
| `missing-curb-ramps-effect.md` | stub |
| `mobility-profiles.md` | draft |
| `network-redundancy.md` | stub |
| `opensidewalks-data-consumption.md` | stub |
| `operational-use.md` | stub |
| `paratransit-planning-support.md` | stub |
| `pedestrian-resilience.md` | stub |
| `planned-capabilities.md` | stub |
| `powered-wheelchair-support.md` | stub |
| `prioritization-metrics.md` | stub |
| `profile-responsive-map.md` | draft |
| `public-engagement.md` | stub |
| `route-calculation.md` | draft |
| `route-planning-and-navigation.md` | draft |
| `route-reliability.md` | stub |
| `routing-limitations.md` | stub |
| `routing-profiles.md` | stub |
| `routing-system-comparison.md` | stub |
| `routing-tradeoffs.md` | stub |
| `school-use.md` | stub |
| `slope-routing.md` | stub |
| `steep-slopes-effect.md` | stub |
| `temporary-barriers.md` | draft |
| `tourism-accessibility.md` | stub |
| `transit-pedestrian-routing-integration.md` | stub |
| `transit-wayfinding.md` | stub |
| `update-cadence.md` | stub |

### Workflows

Base: `assistant/accessmap/workflow/`

| File | Status |
| :--- | :----- |
| `follow-a-route-with-location.md` | draft |
| `get-accessmap-set-up-for-your-region.md` | draft |
| `plan-and-share-a-route.md` | draft |
| `prioritize-pedestrian-investments.md` | stub |
| `report-routing-problems.md` | draft |
| `validate-routing-results.md` | stub |

## AVIV ScoutRoute — Assistant Knowledge Base

See [aviv-scoutroute/index.md](aviv-scoutroute/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/aviv-scoutroute/concept/`

| File | Status |
| :--- | :----- |
| `app-enabled-workspaces.md` | draft |
| `aviv-scoutroute.md` | draft |
| `conditional-team-questions.md` | draft |
| `field-observation.md` | draft |
| `group-quest-selection.md` | draft |
| `numeric-quest-input.md` | draft |
| `numeric-quest-validation.md` | draft |
| `offline-data-and-upload.md` | draft |
| `quest-contributions.md` | draft |
| `quest-definition-application.md` | draft |
| `quest-definition-element-icons.md` | draft |
| `quest-definition-element-targeting.md` | draft |
| `quest-definition-picture-questions.md` | draft |
| `quest-definition-query-syntax.md` | draft |
| `quest-dependency-evaluators.md` | draft |
| `quest-input-types.md` | draft |
| `quest-required-or-optional.md` | draft |
| `quest-visibility-and-local-state.md` | draft |
| `quest.md` | draft |

### Workflows

Base: `assistant/aviv-scoutroute/workflow/`

| File | Status |
| :--- | :----- |
| `answer-quest.md` | draft |
| `complete-and-submit-a-quest.md` | draft |
| `design-conditional-follow-up-quests.md` | draft |
| `install-aviv-scoutroute.md` | draft |
| `join-a-project-and-find-quests.md` | draft |
| `manage-quest-visibility.md` | draft |
| `undo-a-quest-submission.md` | draft |
| `update-quest-definition-in-workspace.md` | draft |

## Cross-Platform — Assistant Knowledge Base

See [cross-platform/index.md](cross-platform/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/cross-platform/concept/`

| File | Status |
| :--- | :----- |
| `abbreviations.md` | published |
| `accessibility-islands.md` | draft |
| `accessmap-routing.md` | draft |
| `ada-compliance-boundaries.md` | draft |
| `ada-safety-legal-boundaries.md` | draft |
| `assistant-abstention.md` | draft |
| `completeness.md` | draft |
| `connected-pedestrian-graph.md` | draft |
| `data-freshness.md` | draft |
| `data-viewer-portal-workspaces-relationship.md` | draft |
| `documentation-audience-baseline.md` | draft |
| `documentation-guide-types.md` | draft |
| `help-desk-questions-as-knowledge-sources.md` | draft |
| `how-should-ai-outputs-be-validated.md` | stub |
| `knowledge-base-domain-review.md` | draft |
| `mobile-and-web-validation-differences.md` | draft |
| `os-connect-vs-gtfs-pathways.md` | draft |
| `public-vs-internal-content.md` | draft |
| `qa-qc-report-audience.md` | draft |
| `rural-pedestrian-data-value.md` | draft |
| `topic-based-assistant-content.md` | draft |
| `walksheds.md` | draft |
| `what-are-the-risks-of-automated-accessibility-analysis.md` | stub |
| `workspaces-user-audience.md` | draft |

### Workflows

Base: `assistant/cross-platform/workflow/`

| File | Status |
| :--- | :----- |
| `report-product-issues.md` | draft |
| `review-assistant-article-stubs.md` | draft |
| `review-community-feedback.md` | draft |
| `support-answer-patterns.md` | draft |
| `update-jurisdiction-data.md` | draft |
| `use-accessmap-for-public-engagement.md` | draft |
| `use-os-connect-for-ada-transition-planning.md` | draft |
| `use-walksheds-for-safe-routes-to-school.md` | draft |

## FleXR — Assistant Knowledge Base

See [flexr/index.md](flexr/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/flexr/concept/`

| File | Status |
| :--- | :----- |
| `flexr.md` | draft |

### Workflows

Base: `assistant/flexr/workflow/`

| File | Status |
| :--- | :----- |
| `get-involved-with-flexr.md` | draft |

## iOSPointMapper — Assistant Knowledge Base

See [iospointmapper/index.md](iospointmapper/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/iospointmapper/concept/`

| File | Status |
| :--- | :----- |
| `device-compatibility.md` | stub |

### Workflows

Base: `assistant/iospointmapper/workflow/`

| File | Status |
| :--- | :----- |
| `start-collecting-data.md` | stub |

## LivAbility — Assistant Knowledge Base

See [livability/index.md](livability/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/livability/concept/`

| File | Status |
| :--- | :----- |
| `poi-source.md` | stub |

### Workflows

Base: `assistant/livability/workflow/`

| File | Status |
| :--- | :----- |
| `select-mobility-profile.md` | stub |

## OpenSidewalks — Assistant Knowledge Base

See [opensidewalks/index.md](opensidewalks/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/opensidewalks/concept/`

| File | Status |
| :--- | :----- |
| `adjacent-entities.md` | draft |
| `adjacent-vs-custom-entities.md` | draft |
| `connector-segment-tagging.md` | draft |
| `coordinate-system-and-serialization.md` | draft |
| `custom-entities.md` | draft |
| `dataset-metadata-and-provenance.md` | draft |
| `ext-attributes-and-regional-flexibility.md` | draft |
| `external-attributes.md` | draft |
| `external-data-overlay-boundary.md` | draft |
| `mapping-imagery-limitations.md` | draft |
| `maximum-extent-feasible.md` | draft |
| `network-entities.md` | draft |
| `network-topology.md` | draft |
| `opensidewalks-schema.md` | draft |
| `opensidewalks.md` | draft |
| `point-and-line-feature-workflows.md` | draft |
| `regional-dataset-derivatives.md` | draft |
| `roadside-surface-preferences.md` | draft |
| `tasking-manager-roles.md` | draft |
| `tdei-schema-validation.md` | draft |
| `workspace-editing-tools.md` | draft |

### Workflows

Base: `assistant/opensidewalks/workflow/`

| File | Status |
| :--- | :----- |
| `add-custom-points-to-osw.md` | draft |
| `convert-sidewalk-centerlines-to-osw.md` | draft |
| `find-latest-version.md` | draft |
| `generate-task-polygons.md` | draft |
| `map-osw-features-in-tasking-manager.md` | draft |
| `validate-osw-tasking-manager-edits.md` | draft |

## OS-CONNECT — Assistant Knowledge Base

See [os-connect/index.md](os-connect/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/os-connect/concept/`

| File | Status |
| :--- | :----- |
| `accessibility-attribute.md` | stub |
| `accessibility-data-gaps.md` | stub |
| `accessibility-equity.md` | stub |
| `accessibility-improvement.md` | stub |
| `accessibility-tradeoff-communication.md` | stub |
| `ada-title-ii-requirements.md` | stub |
| `ada-transition-data-requirements.md` | stub |
| `ada-transition-planning.md` | draft |
| `adoption-barriers.md` | stub |
| `advocacy-group-role.md` | stub |
| `advocacy-group-use.md` | stub |
| `advocacy-participation.md` | stub |
| `advocate-contribution.md` | stub |
| `agency-correction-reporting.md` | stub |
| `agency-data-integration.md` | stub |
| `ai-barrier-identification.md` | stub |
| `ai-curb-ramp-detection.md` | stub |
| `ai-data-risks.md` | stub |
| `ai-inequity-identification.md` | stub |
| `ai-infrastructure-prioritization.md` | stub |
| `ai-sidewalk-quality-estimation.md` | stub |
| `ai-stewardship-assistance.md` | stub |
| `attribute-documentation-location.md` | draft |
| `automated-data-risks.md` | stub |
| `automated-system-limitations.md` | stub |
| `batch-correction-alternatives.md` | stub |
| `bulk-correction-submission.md` | stub |
| `campus-handling.md` | stub |
| `capital-planning.md` | stub |
| `centrality-metrics.md` | draft |
| `common-errors.md` | stub |
| `community-comment-review.md` | stub |
| `community-correction-contribution.md` | stub |
| `community-data-quality-checks.md` | stub |
| `community-data-usability.md` | stub |
| `community-engagement-pathways.md` | stub |
| `community-feedback-use.md` | stub |
| `community-gap-identification.md` | stub |
| `community-participation-pathways.md` | stub |
| `community-validation-role.md` | stub |
| `completeness-score-interpretation.md` | draft |
| `completeness-vs-ada-compliance.md` | draft |
| `complex-intersection-handling.md` | stub |
| `confidence-measures.md` | stub |
| `conflicting-data-sources.md` | stub |
| `connectivity-depends-on-geometry.md` | draft |
| `construction-changes.md` | stub |
| `context-aware-routing.md` | stub |
| `coordinate-system.md` | stub |
| `correction-confirmation.md` | draft |
| `correction-propagation.md` | draft |
| `correction-release-lag.md` | draft |
| `correction-tracking.md` | stub |
| `correction-validation.md` | stub |
| `county-update-coordination.md` | stub |
| `cross-state-lessons.md` | stub |
| `crossing-attributes.md` | stub |
| `crossing-edge.md` | stub |
| `crossing-inference.md` | stub |
| `crowdsourcing-role.md` | stub |
| `curb-ramp-attributes.md` | stub |
| `curb-ramp-identification.md` | stub |
| `curb-ramp-inventories.md` | stub |
| `data-accuracy.md` | stub |
| `data-collection-history.md` | stub |
| `data-issue-reporting-requirements.md` | stub |
| `data-licensing.md` | stub |
| `data-maintenance-challenges.md` | stub |
| `data-ownership.md` | stub |
| `dataset-scope-relationships.md` | draft |
| `destination-access-analysis.md` | draft |
| `disability-community-contribution.md` | stub |
| `disconnected-dataset-problem.md` | stub |
| `disconnected-sidewalk-identification.md` | stub |
| `elevation-routing-effects.md` | stub |
| `excluded-infrastructure-types.md` | stub |
| `feature-selection-display.md` | draft |
| `field-validation-role.md` | stub |
| `field-validation.md` | stub |
| `geographic-coverage.md` | draft |
| `gis-software-compatibility.md` | stub |
| `governance-models.md` | stub |
| `gtfs-pathways-generation.md` | stub |
| `human-review.md` | stub |
| `imagery-role.md` | stub |
| `inaccessible-area-reporting.md` | stub |
| `included-infrastructure-types.md` | draft |
| `incomplete-coverage.md` | stub |
| `interoperable-accessibility-ecosystem.md` | stub |
| `intersection-attributes.md` | draft |
| `issue-report-auto-update.md` | draft |
| `issue-report-follow-up.md` | stub |
| `issue-report-reviewers.md` | stub |
| `jurisdiction-data-disputes.md` | stub |
| `jurisdiction-engagement-pathways.md` | stub |
| `jurisdiction-participation-pathways.md` | stub |
| `jurisdiction-stewardship.md` | stub |
| `jurisdiction-update-maintenance.md` | stub |
| `lived-experience-importance.md` | stub |
| `local-data-validation.md` | stub |
| `local-vs-statewide-coordination.md` | stub |
| `long-term-maintenance-workflows.md` | stub |
| `long-term-stewardship-requirements.md` | stub |
| `long-term-stewardship-responsibility.md` | stub |
| `machine-learning-role.md` | stub |
| `major-event-accessibility-planning.md` | stub |
| `manual-wheelchair-profile.md` | stub |
| `map-color-legend.md` | draft |
| `map-layers.md` | draft |
| `mapper-training-materials.md` | stub |
| `mapping-prioritization.md` | stub |
| `mapwithai-workflow-history.md` | stub |
| `maximum-travel-cost.md` | stub |
| `missing-accessibility-information.md` | stub |
| `missing-attribute-values.md` | stub |
| `missing-infrastructure-identification.md` | stub |
| `missing-street-names-for-vendors.md` | stub |
| `mobility-equity.md` | stub |
| `mobility-justice.md` | stub |
| `mpo-contribution.md` | stub |
| `mpo-role.md` | stub |
| `multimodal-accessibility-analysis.md` | stub |
| `national-data-standards-evolution.md` | stub |
| `nationwide-system-requirements.md` | stub |
| `node-vs-edge.md` | stub |
| `nondriver-mobility.md` | stub |
| `older-adult-contribution.md` | stub |
| `open-source-community-role.md` | stub |
| `opensidewalks-community-mapping-groups.md` | stub |
| `opensidewalks-schema-usage.md` | stub |
| `opensidewalks-schema.md` | stub |
| `opensidewalks.md` | stub |
| `operational-agency-use.md` | stub |
| `os-connect-local-gis-relationship.md` | stub |
| `os-connect-maintenance.md` | stub |
| `os-connect-origin.md` | stub |
| `os-connect-problem-statement.md` | stub |
| `os-connect-tdei-relationship.md` | stub |
| `os-connect-vs-openstreetmap.md` | stub |
| `os-connect-vs-traditional-inventories.md` | stub |
| `os-connect.md` | draft |
| `outdated-data-handling.md` | stub |
| `outdated-imagery.md` | draft |
| `participatory-accessibility-mapping.md` | stub |
| `participatory-mapping.md` | stub |
| `partnership-needs.md` | stub |
| `pedestrian-data-complexity.md` | stub |
| `pedestrian-equity.md` | stub |
| `pedestrian-feature-attributes.md` | stub |
| `pedestrian-only-facilities.md` | stub |
| `planned-capabilities.md` | stub |
| `planner-data-validation.md` | stub |
| `planning-with-known-errors.md` | stub |
| `poi-grouping-rationale.md` | stub |
| `post-collection-next-steps.md` | stub |
| `private-facilities.md` | stub |
| `public-data-value.md` | stub |
| `qa-qc-report-infrastructure.md` | draft |
| `qa-qc-report.md` | draft |
| `recommended-sidewalk-tagging-pattern.md` | stub |
| `reportable-errors.md` | draft |
| `required-vs-recommended-attributes.md` | stub |
| `resident-participation.md` | stub |
| `routable-graph.md` | stub |
| `routing-assumptions.md` | stub |
| `routing-personalization.md` | stub |
| `rural-area-handling.md` | stub |
| `rural-community-participation.md` | stub |
| `safe-routes-to-school.md` | stub |
| `safety-improvement.md` | stub |
| `school-participation.md` | stub |
| `separated-sidewalk-mapping.md` | stub |
| `service-planning.md` | stub |
| `sidewalk-attributes.md` | stub |
| `sidewalk-disconnection-causes.md` | draft |
| `sidewalk-street-name-association.md` | stub |
| `state-stewardship-role.md` | stub |
| `statewide-data-importance.md` | stub |
| `statewide-inventory.md` | stub |
| `stewardship-roles.md` | stub |
| `stewardship-sustainability.md` | stub |
| `street-name-routing-importance.md` | stub |
| `street-name-tags-for-routing.md` | stub |
| `street-name-vs-is-sidepath-of-name.md` | draft |
| `surface-attribute.md` | stub |
| `tcat-mapping-project-support.md` | stub |
| `trail-handling.md` | stub |
| `transit-accessibility-analysis.md` | stub |
| `transit-agency-contribution.md` | stub |
| `transit-pedestrian-integration.md` | stub |
| `university-role.md` | stub |
| `unreachable-destinations.md` | stub |
| `update-cadence.md` | stub |
| `update-responsibility.md` | stub |
| `urban-map-density.md` | stub |
| `urgent-correction-process.md` | stub |
| `viewer-overview.md` | draft |
| `viewer-vs-tdei-portal.md` | draft |
| `vision-zero.md` | stub |
| `volunteer-data-contribution.md` | stub |
| `walkshed-advocacy.md` | stub |
| `walkshed-metrics.md` | draft |
| `washington-lessons.md` | stub |
| `width-attribute.md` | stub |
| `workflow-improvement-areas.md` | stub |
| `z-score-usage.md` | stub |

### Workflows

Base: `assistant/os-connect/workflow/`

| File | Status |
| :--- | :----- |
| `bus-stop-planning.md` | draft |
| `connect-to-gis.md` | stub |
| `download-data.md` | draft |
| `import-into-arcgis.md` | stub |
| `report-connectivity-data-error.md` | draft |
| `report-data-error.md` | draft |
| `search-for-jurisdiction.md` | draft |
| `support-pedestrian-access-analysis-around-destinations.md` | draft |

## QA/QC — Assistant Knowledge Base

See [qa-qc/index.md](qa-qc/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/qa-qc/concept/`

| File | Status |
| :--- | :----- |
| `accessibility-island.md` | stub |
| `attribute-completeness.md` | draft |
| `attribute-presence-vs-feature-completeness.md` | draft |
| `before-after-walkshed-analysis.md` | draft |
| `bottleneck-hotspots.md` | draft |
| `centrality-and-redundancy.md` | draft |
| `centrality-metric-selection.md` | draft |
| `centrality-sampling-and-repeatability.md` | draft |
| `centrality-tile-generation.md` | draft |
| `centrality.md` | draft |
| `completeness-vs-accessibility-gaps.md` | stub |
| `completeness-vs-ada-compliance.md` | draft |
| `completeness.md` | draft |
| `conditional-attribute-completeness.md` | draft |
| `connected-pedestrian-graph.md` | stub |
| `crossing-count.md` | draft |
| `curb-completeness-metrics.md` | draft |
| `degree-centrality.md` | draft |
| `disconnected-poi.md` | draft |
| `edge-betweenness-centrality.md` | draft |
| `edge-betweenness-operational-use.md` | stub |
| `edge-betweenness.md` | stub |
| `eigenvector-centrality-display.md` | draft |
| `eigenvector-centrality-interpretation.md` | draft |
| `eigenvector-centrality-network-importance.md` | draft |
| `eigenvector-centrality.md` | stub |
| `field-verification-hotspots.md` | draft |
| `intersection-quality-metric.md` | draft |
| `intersection-tile.md` | draft |
| `local-poi-corrections.md` | draft |
| `log-normalized-value.md` | draft |
| `metric-boundaries.md` | draft |
| `metric-coverage-and-interpretation.md` | draft |
| `node-betweenness-centrality.md` | draft |
| `node-betweenness-operational-use.md` | draft |
| `node-centrality-operational-use.md` | stub |
| `normalized-value.md` | draft |
| `path-count.md` | draft |
| `poi-density-and-prioritization.md` | draft |
| `poi-density.md` | draft |
| `point-of-interest-sources.md` | draft |
| `presence-percent.md` | draft |
| `project-completeness-standard.md` | draft |
| `project-completeness-vs-ada-compliance.md` | draft |
| `projection-for-walkshed-lengths.md` | draft |
| `qa-qc-analysis-limitations.md` | draft |
| `qa-qc-limitations.md` | draft |
| `qa-qc-visual-accessibility.md` | draft |
| `quality-metrics-and-local-priorities.md` | draft |
| `quality-scoring-boundaries.md` | draft |
| `report-data-sources.md` | draft |
| `report-feature-counts-and-lengths.md` | draft |
| `report-glossary.md` | draft |
| `report-map-interpretation.md` | draft |
| `report-provenance.md` | draft |
| `report-purpose-and-limitations.md` | draft |
| `report-question-sections.md` | draft |
| `report-scope-by-jurisdiction.md` | draft |
| `small-dataset-limitations.md` | draft |
| `task-grid-overlays.md` | draft |
| `traversability.md` | draft |
| `walkshed-profile-assumptions.md` | draft |
| `walkshed-profile-comparison.md` | draft |
| `z-score.md` | draft |

### Workflows

Base: `assistant/qa-qc/workflow/`

| File | Status |
| :--- | :----- |
| `identify-accessibility-islands.md` | stub |
| `interpret-report-sections.md` | draft |
| `use-report-for-ada-planning.md` | draft |

## Rapid — Assistant Knowledge Base

See [rapid/index.md](rapid/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/rapid/concept/`

| File | Status |
| :--- | :----- |
| `rapid.md` | stub |

### Workflows

Base: `assistant/rapid/workflow/`

| File | Status |
| :--- | :----- |
| `add-sidewalk-using-rapid.md` | stub |

## Support — Assistant Knowledge Base

See [support/index.md](support/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/support/concept/`

| File | Status |
| :--- | :----- |
| `accessmap-vs-walksheds.md` | stub |
| `cross-team-followup-ownership.md` | stub |
| `data-citation.md` | stub |
| `dataset-authority.md` | stub |
| `ecosystem-overview.md` | stub |
| `fallback-when-gtfs-pathways-missing.md` | stub |
| `gtfs-pathways-agency-adoption.md` | stub |
| `mappy-hours-eligibility.md` | stub |
| `opensidewalks-contact.md` | stub |
| `os-connect-contact.md` | stub |
| `osm-pedestrian-paths-vs-gtfs-pathways.md` | draft |
| `partner-response-time.md` | stub |
| `staff-email-antipatterns.md` | stub |
| `tdei-contact.md` | stub |
| `tdei-os-connect-osm-differences.md` | draft |

### Workflows

Base: `assistant/support/workflow/`

| File | Status |
| :--- | :----- |
| `check-gtfs-feed-pathways.md` | draft |
| `choose-dataset-for-arcgis.md` | stub |
| `choose-dataset-for-planning.md` | draft |
| `choose-dataset-for-transit-stations.md` | draft |
| `communicate-uncertainty.md` | stub |
| `frame-future-plans.md` | stub |
| `handle-unknown-questions.md` | stub |
| `internal-verification-language.md` | stub |
| `introduce-related-tools.md` | stub |
| `mappy-hours-referral-decision.md` | stub |

## TDEI — Assistant Knowledge Base

See [tdei/index.md](tdei/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/tdei/concept/`

| File | Status |
| :--- | :----- |
| `api-key-rotation.md` | draft |
| `dataset-download-formats.md` | draft |
| `dataset-identifier.md` | stub |
| `dataset-level-vs-feature-level-operations.md` | draft |
| `dataset-purpose-and-representation.md` | draft |
| `dataset-version-selection.md` | draft |
| `dataset-visibility.md` | draft |
| `derived-dataset-lineage.md` | draft |
| `environment-separation.md` | draft |
| `external-attribute-release.md` | draft |
| `feedback-management.md` | draft |
| `file-formats.md` | draft |
| `interoperability.md` | stub |
| `interval-survey-points.md` | draft |
| `job-confidence-calculation.md` | draft |
| `job-dataset-tag-road.md` | draft |
| `job-dataset-union.md` | draft |
| `job-filter-dataset-by-bbox.md` | draft |
| `job-flex-validate.md` | draft |
| `job-osw-convert.md` | draft |
| `job-osw-validate.md` | draft |
| `job-pathways-validate.md` | draft |
| `job-processing.md` | draft |
| `job-quality-metric-ixn.md` | draft |
| `job-quality-metric-tag.md` | draft |
| `job-spatial-join.md` | draft |
| `jurisdiction-dataset-coverage.md` | draft |
| `mislabeled-dataset-handling.md` | stub |
| `osw-download-contents.md` | stub |
| `osw-edges-and-nodes.md` | stub |
| `osw-vs-osm-format.md` | stub |
| `portal-dashboard.md` | draft |
| `project-group-roles.md` | draft |
| `project-group.md` | draft |
| `release-versioning.md` | stub |
| `released-dataset-viewer.md` | draft |
| `released-dataset.md` | stub |
| `services-and-project-groups.md` | draft |
| `source-and-derivative-datasets.md` | draft |
| `tdei-architecture.md` | draft |
| `tdei-job-processing.md` | draft |
| `tdei-services.md` | draft |
| `tdei.md` | draft |
| `test-dataset-in-portal.md` | stub |

### Workflows

Base: `assistant/tdei/workflow/`

| File | Status |
| :--- | :----- |
| `access-tdei-api.md` | draft |
| `check-dataset-currency.md` | draft |
| `check-project-group-membership.md` | draft |
| `conflate-jurisdiction-datasets.md` | draft |
| `convert-geodatabase-to-osw-data.md` | draft |
| `convert-osm-pbf-to-osw.md` | draft |
| `create-and-monitor-tdei-job.md` | draft |
| `download-data.md` | draft |
| `download-os-connect-data.md` | draft |
| `download-os-connect-dataset.md` | draft |
| `integrate-external-geospatial-data.md` | draft |
| `register-and-verify-tdei-account.md` | draft |
| `use-tdei-portal.md` | draft |
| `validate-osw-dataset.md` | draft |

## Walksheds — Assistant Knowledge Base

See [walksheds/index.md](walksheds/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/walksheds/concept/`

| File | Status |
| :--- | :----- |
| `accessibility-islands.md` | stub |
| `accessibility-profile-inequity-analysis.md` | draft |
| `accessibility-profiles.md` | draft |
| `accuracy-vs-straight-line.md` | stub |
| `ada-planning.md` | stub |
| `barrier-incorporation.md` | stub |
| `before-after-comparison.md` | stub |
| `bus-stop-access-analysis.md` | draft |
| `complete-streets-planning.md` | stub |
| `crossing-effects.md` | stub |
| `crossing-gap-identification.md` | stub |
| `destination-exclusion.md` | stub |
| `disconnected-network-handling.md` | stub |
| `downtown-revitalization.md` | stub |
| `economic-development.md` | stub |
| `elevation-effects.md` | stub |
| `emergency-resilience-planning.md` | stub |
| `equity-analysis.md` | stub |
| `external-dataset-joins.md` | draft |
| `grant-applications.md` | stub |
| `hospital-access-analysis.md` | stub |
| `infrastructure-scenario-comparison.md` | stub |
| `max-cost.md` | stub |
| `neighborhood-comparison.md` | stub |
| `network-assumptions.md` | stub |
| `os-connect-data-usage.md` | draft |
| `park-access-analysis.md` | stub |
| `pedestrian-bottleneck-identification.md` | stub |
| `pedestrian-vs-wheelchair-walkshed.md` | draft |
| `pedestrian-walkshed.md` | stub |
| `planned-capabilities.md` | stub |
| `planner-assumptions.md` | stub |
| `poi-origin-analysis-limits.md` | draft |
| `prioritization-workflows.md` | stub |
| `profile-variation.md` | stub |
| `public-explanation.md` | stub |
| `reachable-area.md` | stub |
| `rural-transportation-planning.md` | stub |
| `safe-routes-to-school.md` | draft |
| `school-accessibility-analysis.md` | stub |
| `senior-mobility-analysis.md` | stub |
| `transit-planning.md` | stub |
| `travel-limits.md` | stub |
| `travel-profiles.md` | draft |
| `uncertainty-communication.md` | stub |
| `underserved-area-identification.md` | stub |
| `vision-zero.md` | stub |
| `walkshed-application-architecture.md` | draft |
| `walkshed-attribute-availability.md` | draft |
| `walkshed-batch-amenity-input.md` | draft |
| `walkshed-batch-concurrency.md` | draft |
| `walkshed-batch-failures.md` | draft |
| `walkshed-batch-input.md` | draft |
| `walkshed-batch-output.md` | draft |
| `walkshed-batch-profiles.md` | draft |
| `walkshed-calculation.md` | draft |
| `walkshed-cost-factors.md` | draft |
| `walkshed-cost-function.md` | draft |
| `walkshed-custom-cost-function-contract.md` | draft |
| `walkshed-custom-cost-functions.md` | draft |
| `walkshed-data-connectivity.md` | draft |
| `walkshed-data-issue-workflow.md` | draft |
| `walkshed-default-cost-model.md` | draft |
| `walkshed-edge-attributes.md` | draft |
| `walkshed-edit-history.md` | draft |
| `walkshed-edit-limitations.md` | draft |
| `walkshed-feature-edits.md` | draft |
| `walkshed-interface-organization.md` | draft |
| `walkshed-limitations.md` | stub |
| `walkshed-map-symbols.md` | draft |
| `walkshed-point-features.md` | draft |
| `walkshed-quality.md` | stub |
| `walkshed-result-statistics.md` | draft |
| `walkshed-router-building.md` | draft |
| `walkshed-router-processing.md` | draft |
| `walkshed-scenario-statistics.md` | draft |
| `walkshed-scenarios.md` | draft |
| `walkshed-travel-cost.md` | draft |
| `walkshed-vs-buffer.md` | stub |
| `walkshed.md` | draft |
| `walksheds-tool.md` | stub |
| `wheelchair-walkshed.md` | stub |

### Workflows

Base: `assistant/walksheds/workflow/`

| File | Status |
| :--- | :----- |
| `build-walkshed-router.md` | draft |
| `compare-walkshed-profiles.md` | draft |
| `create-walkshed-scenario.md` | draft |
| `generate-walkshed.md` | draft |
| `inspect-and-edit-walkshed-feature.md` | draft |
| `model-infrastructure-change.md` | draft |
| `run-batch-walksheds.md` | draft |
| `run-walkshed-batch-from-csv.md` | draft |
| `save-and-compare-walkshed-scenarios.md` | draft |
| `select-walkshed-dataset.md` | draft |

## Waykeeper — Assistant Knowledge Base

See [waykeeper/index.md](waykeeper/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/waykeeper/concept/`

| File | Status |
| :--- | :----- |
| `waykeeper.md` | stub |

### Workflows

Base: `assistant/waykeeper/workflow/`

| File | Status |
| :--- | :----- |
| `use-waykeeper.md` | stub |

## Workspaces — Assistant Knowledge Base

See [workspaces/index.md](workspaces/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/workspaces/concept/`

| File | Status |
| :--- | :----- |
| `accessibility-feature-editing.md` | stub |
| `asr-imagery-list-repo.md` | stub |
| `attribute-editing.md` | stub |
| `aviv-scoutroute.md` | stub |
| `basemap-loading.md` | stub |
| `change-authorship.md` | stub |
| `change-editor-tracking.md` | stub |
| `changeset-tracking.md` | stub |
| `changesets.md` | draft |
| `collaborative-edit-management.md` | stub |
| `collaborative-editing-support.md` | stub |
| `collaborative-editing.md` | stub |
| `community-workflow-support.md` | stub |
| `compatible-editors.md` | stub |
| `compatible-tools.md` | stub |
| `continuing-feature-edits.md` | stub |
| `custom-imagery-configuration.md` | draft |
| `custom-imagery.md` | stub |
| `dataset-lineage-in-tdei.md` | stub |
| `dataset-lineage.md` | stub |
| `edit-attribution.md` | stub |
| `edit-auditing.md` | stub |
| `edit-history.md` | stub |
| `edit-metadata.md` | stub |
| `edit-reviewers.md` | stub |
| `edit-source-tracking.md` | stub |
| `edit-types.md` | stub |
| `edit-upload-to-tdei.md` | stub |
| `editing-coordination.md` | stub |
| `export-overwrite-behavior.md` | stub |
| `export-process.md` | stub |
| `export-timing.md` | stub |
| `export-versioning.md` | stub |
| `format-specific-data-generator-roles.md` | draft |
| `geometry-editing.md` | stub |
| `gis-staff-role.md` | stub |
| `gis-tool-decision.md` | stub |
| `imagery-json-configuration.md` | stub |
| `imagery-layer-access.md` | draft |
| `imagery-layer-configuration-boundaries.md` | draft |
| `imagery-layer-definition.md` | draft |
| `imagery-layer-mechanics.md` | stub |
| `imagery-layer-overview.md` | stub |
| `imagery-layers.md` | stub |
| `imagery-misconfiguration.md` | stub |
| `imagery-permissions.md` | stub |
| `imagery-raw-json-requirement.md` | stub |
| `imagery-resource-variation.md` | stub |
| `imagery-sources.md` | stub |
| `intended-audience.md` | stub |
| `internal-qa-qc-data-access.md` | draft |
| `josm.md` | stub |
| `keeping-edits-private.md` | stub |
| `manager-edit-review.md` | stub |
| `manager-role.md` | stub |
| `mobile-point-feature-creation.md` | draft |
| `multi-source-stewardship.md` | draft |
| `multiple-workspaces-per-dataset.md` | stub |
| `non-global-dataset-rationale.md` | stub |
| `notes-as-field-issue-reports.md` | draft |
| `osm-api-emulation.md` | stub |
| `osm-connection.md` | stub |
| `osm-editing-emulation-rationale.md` | stub |
| `osm-editor-benefits.md` | stub |
| `osm-tool-compatibility-rationale.md` | stub |
| `parallel-workspace-editing.md` | stub |
| `post-export-behavior.md` | stub |
| `private-osm-explained.md` | stub |
| `private-osm.md` | stub |
| `project-group-and-workspace-roles.md` | draft |
| `project-group-definition.md` | stub |
| `project-group-operations.md` | stub |
| `project-group-referral-access.md` | draft |
| `project-groups.md` | stub |
| `public-availability-of-quest-photos.md` | draft |
| `qa-review-support.md` | stub |
| `qr-code-invites.md` | stub |
| `quest-definition-url-requirements.md` | draft |
| `rapid-imagery-integration.md` | draft |
| `rapid-versions.md` | stub |
| `rapid.md` | stub |
| `raster-and-vector-basemaps.md` | draft |
| `recommended-publication-workflow.md` | stub |
| `recommended-workflows.md` | stub |
| `review-interface.md` | stub |
| `roles.md` | stub |
| `sandbox.md` | stub |
| `source-dataset-tracing.md` | stub |
| `stewardship-support.md` | stub |
| `target-users.md` | stub |
| `tdei-ecosystem-fit.md` | stub |
| `tdei-vs-workspaces.md` | stub |
| `team-invitations.md` | stub |
| `teams-vs-project-groups.md` | draft |
| `teams.md` | stub |
| `tile-layers.md` | stub |
| `vector-map-preference.md` | stub |
| `vector-vs-raster-maps.md` | stub |
| `viewer-vs-editor-users.md` | stub |
| `workspace-abstention-boundaries.md` | stub |
| `workspace-and-tdei-boundary.md` | draft |
| `workspace-app-access-default.md` | draft |
| `workspace-as-dataset-copy.md` | stub |
| `workspace-as-private-osm.md` | draft |
| `workspace-availability-for-new-mappers.md` | draft |
| `workspace-copy-and-divergence.md` | draft |
| `workspace-creation-mechanics.md` | stub |
| `workspace-creation-methods.md` | stub |
| `workspace-dashboard.md` | stub |
| `workspace-data-freshness.md` | stub |
| `workspace-dataset-divergence.md` | stub |
| `workspace-duplicate-copy-risk.md` | draft |
| `workspace-editing-authority.md` | stub |
| `workspace-editing-boundary.md` | draft |
| `workspace-export-and-publication-caveats.md` | stub |
| `workspace-extract.md` | draft |
| `workspace-id.md` | stub |
| `workspace-metadata-and-lineage.md` | draft |
| `workspace-metadata.md` | stub |
| `workspace-per-project-model.md` | draft |
| `workspace-public-vs-private-data.md` | draft |
| `workspace-review-and-publication-gates.md` | draft |
| `workspace-review-interface.md` | draft |
| `workspace-roles-and-project-roles.md` | draft |
| `workspace-source-options.md` | draft |
| `workspace-tdei-isolation.md` | stub |
| `workspace-team-membership.md` | draft |
| `workspace-teams.md` | draft |
| `workspace-technical-definition.md` | stub |
| `workspaces-os-connect-relationship.md` | stub |
| `workspaces-osm-limitations.md` | stub |
| `workspaces-tdei-portal-relationship.md` | stub |
| `workspaces-tdei-separation.md` | stub |
| `workspaces-vs-gis-decision.md` | stub |
| `workspaces.md` | draft |

### Workflows

Base: `assistant/workspaces/workflow/`

| File | Status |
| :--- | :----- |
| `choose-editor.md` | stub |
| `configure-app-enabled-workspace.md` | draft |
| `configure-imagery-layers.md` | draft |
| `create-a-workspace-from-tdei.md` | draft |
| `create-workspace-from-osm.md` | draft |
| `create-workspace-from-tdei-dataset.md` | draft |
| `create-workspace-from-tdei.md` | stub |
| `create-workspace.md` | stub |
| `edit-accessibility-features-in-a-workspace.md` | draft |
| `export-workspace-edits-to-tdei.md` | stub |
| `export-workspace-locally.md` | draft |
| `export-workspace-to-tdei.md` | draft |
| `export-workspace.md` | draft |
| `import-external-geojson-for-reference.md` | draft |
| `import-osm-data-into-workspaces.md` | draft |
| `invite-a-team-to-a-workspace.md` | draft |
| `open-dataset-for-inspection.md` | draft |
| `pre-export-review.md` | stub |
| `publish-jurisdiction-updates.md` | stub |
| `review-quest-contributions.md` | draft |
| `review-workspace-edits.md` | stub |
| `search-project-groups.md` | stub |
| `use-workspaces-for-community-validation.md` | stub |
| `use-workspaces-for-jurisdiction-stewardship.md` | stub |
