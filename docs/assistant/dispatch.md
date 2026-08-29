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
last_reviewed: 2026-08-28
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
     Produced by utilities/akb_generate_dispatch.py. Re-run the script
     (or utilities/build_site.py) to refresh this file after adding,
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

**Authors**: Write or edit files directly under `docs/assistant/`; do not hand-edit this file. Re-run `utilities/akb_generate_dispatch.py` (or the full `utilities/build_site.py` pipeline) to refresh the registry after adding a page or changing its `publication_status`.

**Maintainers**: This file is a generated build artifact. To change its structure, edit `utilities/akb_generate_dispatch.py`.

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
| `stub` | 57 | Frontmatter and heading scaffold exist; body is `TODO` |
| `draft` | 732 | Content authored; awaiting TCAT editorial review |
| `published` | 1 | Available in the human-facing site |
| `archived` | 0 | Retained for agents but not published |

## Authority Legend

| Authority level | Count | Meaning |
| :-------------- | ----: | :------ |
| `provisional` | 464 | Early or limited-confidence guidance |
| `explanatory` | 324 | Established explanation without formal policy authority |
| `official` | 2 | Formally endorsed organizational guidance |

## Registry

## AccessMap — Assistant Knowledge Base

See [accessmap/index.md](accessmap/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/accessmap/concept/`

| File | Status |
| :--- | :----- |
| `accessibility-assumptions.md` | draft |
| `accessibility-mobility-metrics.md` | draft |
| `accessibility-needs.md` | draft |
| `accessibility-preference-routing.md` | draft |
| `accessible-routes-appear-longer.md` | draft |
| `accessmap.md` | draft |
| `ada-compliance-support.md` | draft |
| `agency-routing-customization.md` | draft |
| `avoid-missing-curb-ramps.md` | draft |
| `avoid-steep-slopes.md` | draft |
| `blind-low-vision-support.md` | draft |
| `campus-accessibility.md` | draft |
| `combined-crossing-accessibility.md` | draft |
| `community-accessibility-priorities.md` | draft |
| `comparison-apple-maps.md` | draft |
| `construction-routing-effect.md` | draft |
| `coverage-outside-washington.md` | draft |
| `critical-pedestrian-corridors.md` | draft |
| `curb-ramp-routing.md` | draft |
| `data-sources.md` | draft |
| `disconnected-sidewalks.md` | draft |
| `emergency-planning.md` | draft |
| `explaining-metrics-publicly.md` | draft |
| `feature-feedback.md` | draft |
| `field-validation.md` | draft |
| `google-maps-comparison.md` | draft |
| `google-maps-design-rationale.md` | draft |
| `gtfs-integration.md` | draft |
| `gtfs-pathways.md` | draft |
| `here-routing-comparison.md` | draft |
| `hospital-campus-support.md` | draft |
| `inaccessible-transit-stations.md` | draft |
| `local-datasets-routing-quality.md` | draft |
| `longer-route-selection.md` | draft |
| `manual-wheelchair-support.md` | draft |
| `missing-accessibility-data.md` | draft |
| `missing-curb-ramps-effect.md` | draft |
| `mobility-profiles.md` | draft |
| `network-redundancy.md` | draft |
| `opensidewalks-data-consumption.md` | draft |
| `operational-use.md` | draft |
| `paratransit-planning-support.md` | draft |
| `pedestrian-resilience.md` | draft |
| `planned-capabilities.md` | draft |
| `powered-wheelchair-support.md` | draft |
| `prioritization-metrics.md` | draft |
| `profile-responsive-map.md` | draft |
| `public-engagement.md` | draft |
| `route-calculation.md` | draft |
| `route-planning-and-navigation.md` | draft |
| `route-reliability.md` | draft |
| `routing-limitations.md` | draft |
| `routing-profiles.md` | draft |
| `routing-system-comparison.md` | draft |
| `routing-tradeoffs.md` | draft |
| `school-use.md` | draft |
| `slope-routing.md` | draft |
| `steep-slopes-effect.md` | draft |
| `temporary-barriers.md` | draft |
| `tourism-accessibility.md` | draft |
| `transit-pedestrian-routing-integration.md` | draft |
| `transit-wayfinding.md` | draft |
| `update-cadence.md` | draft |

### Workflows

Base: `assistant/accessmap/workflow/`

| File | Status |
| :--- | :----- |
| `follow-a-route-with-location.md` | draft |
| `get-accessmap-set-up-for-your-region.md` | draft |
| `plan-and-share-a-route.md` | draft |
| `prioritize-pedestrian-investments.md` | draft |
| `report-routing-problems.md` | draft |
| `validate-routing-results.md` | draft |

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
| `quest-answer-dependency-logic.md` | draft |
| `quest-contributions.md` | draft |
| `quest-definition-application.md` | draft |
| `quest-definition-creator.md` | draft |
| `quest-definition-custom-icons.md` | draft |
| `quest-definition-element-icons.md` | draft |
| `quest-definition-element-targeting.md` | draft |
| `quest-definition-feature-presets.md` | draft |
| `quest-definition-picture-questions.md` | draft |
| `quest-definition-query-syntax.md` | draft |
| `quest-definition-resurvey-interval.md` | draft |
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
| `renumber-quest-definition.md` | draft |
| `undo-a-quest-submission.md` | draft |
| `update-quest-definition-in-workspace.md` | draft |
| `upgrade-quest-definition.md` | draft |

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
| `crossing-links.md` | draft |
| `data-freshness.md` | draft |
| `data-viewer-portal-workspaces-relationship.md` | draft |
| `documentation-audience-baseline.md` | draft |
| `documentation-guide-types.md` | draft |
| `help-desk-questions-as-knowledge-sources.md` | draft |
| `how-should-ai-outputs-be-validated.md` | draft |
| `knowledge-base-domain-review.md` | draft |
| `mobile-and-web-validation-differences.md` | draft |
| `os-connect-vs-gtfs-pathways.md` | draft |
| `public-vs-internal-content.md` | draft |
| `qa-qc-report-audience.md` | draft |
| `rural-pedestrian-data-value.md` | draft |
| `topic-based-assistant-content.md` | draft |
| `walksheds.md` | draft |
| `what-are-the-risks-of-automated-accessibility-analysis.md` | draft |
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
| `accessibility-attribute.md` | draft |
| `accessibility-data-gaps.md` | draft |
| `accessibility-equity.md` | draft |
| `accessibility-improvement.md` | draft |
| `accessibility-tradeoff-communication.md` | draft |
| `ada-title-ii-requirements.md` | draft |
| `ada-transition-data-requirements.md` | draft |
| `ada-transition-planning.md` | draft |
| `adoption-barriers.md` | draft |
| `advocacy-group-role.md` | draft |
| `advocacy-group-use.md` | draft |
| `advocacy-participation.md` | draft |
| `advocate-contribution.md` | draft |
| `agency-correction-reporting.md` | draft |
| `agency-data-integration.md` | draft |
| `ai-barrier-identification.md` | draft |
| `ai-curb-ramp-detection.md` | draft |
| `ai-data-risks.md` | draft |
| `ai-inequity-identification.md` | draft |
| `ai-infrastructure-prioritization.md` | draft |
| `ai-sidewalk-quality-estimation.md` | draft |
| `ai-stewardship-assistance.md` | draft |
| `attribute-documentation-location.md` | draft |
| `automated-data-risks.md` | draft |
| `automated-system-limitations.md` | draft |
| `batch-correction-alternatives.md` | draft |
| `bulk-correction-submission.md` | draft |
| `campus-handling.md` | draft |
| `capital-planning.md` | draft |
| `centrality-metrics.md` | draft |
| `common-errors.md` | draft |
| `community-comment-review.md` | draft |
| `community-correction-contribution.md` | draft |
| `community-data-quality-checks.md` | draft |
| `community-data-usability.md` | draft |
| `community-engagement-pathways.md` | draft |
| `community-feedback-use.md` | draft |
| `community-gap-identification.md` | draft |
| `community-participation-pathways.md` | draft |
| `community-validation-role.md` | draft |
| `completeness-score-interpretation.md` | draft |
| `completeness-vs-ada-compliance.md` | draft |
| `complex-intersection-handling.md` | draft |
| `confidence-measures.md` | draft |
| `conflicting-data-sources.md` | draft |
| `connectivity-depends-on-geometry.md` | draft |
| `construction-changes.md` | draft |
| `context-aware-routing.md` | draft |
| `coordinate-system.md` | draft |
| `correction-confirmation.md` | draft |
| `correction-propagation.md` | draft |
| `correction-release-lag.md` | draft |
| `correction-tracking.md` | draft |
| `correction-validation.md` | draft |
| `county-update-coordination.md` | draft |
| `cross-state-lessons.md` | draft |
| `crossing-attributes.md` | draft |
| `crossing-edge.md` | draft |
| `crossing-inference.md` | draft |
| `crowdsourcing-role.md` | draft |
| `curb-ramp-attributes.md` | draft |
| `curb-ramp-identification.md` | draft |
| `curb-ramp-inventories.md` | draft |
| `data-accuracy.md` | draft |
| `data-collection-history.md` | draft |
| `data-issue-reporting-requirements.md` | draft |
| `data-licensing.md` | draft |
| `data-maintenance-challenges.md` | draft |
| `data-ownership.md` | draft |
| `dataset-scope-relationships.md` | draft |
| `destination-access-analysis.md` | draft |
| `disability-community-contribution.md` | draft |
| `disconnected-dataset-problem.md` | draft |
| `disconnected-sidewalk-identification.md` | draft |
| `elevation-routing-effects.md` | draft |
| `excluded-infrastructure-types.md` | draft |
| `feature-selection-display.md` | draft |
| `field-validation-role.md` | draft |
| `field-validation.md` | draft |
| `geographic-coverage.md` | draft |
| `gis-software-compatibility.md` | draft |
| `governance-models.md` | draft |
| `gtfs-pathways-generation.md` | draft |
| `human-review.md` | draft |
| `imagery-role.md` | draft |
| `inaccessible-area-reporting.md` | draft |
| `included-infrastructure-types.md` | draft |
| `incomplete-coverage.md` | draft |
| `interoperable-accessibility-ecosystem.md` | draft |
| `intersection-attributes.md` | draft |
| `issue-report-auto-update.md` | draft |
| `issue-report-follow-up.md` | draft |
| `issue-report-reviewers.md` | draft |
| `jurisdiction-data-disputes.md` | draft |
| `jurisdiction-engagement-pathways.md` | draft |
| `jurisdiction-participation-pathways.md` | draft |
| `jurisdiction-stewardship.md` | draft |
| `jurisdiction-update-maintenance.md` | draft |
| `lived-experience-importance.md` | draft |
| `local-data-validation.md` | draft |
| `local-vs-statewide-coordination.md` | draft |
| `long-term-maintenance-workflows.md` | draft |
| `long-term-stewardship-requirements.md` | draft |
| `long-term-stewardship-responsibility.md` | draft |
| `machine-learning-role.md` | draft |
| `major-event-accessibility-planning.md` | draft |
| `manual-wheelchair-profile.md` | draft |
| `map-color-legend.md` | draft |
| `map-layers.md` | draft |
| `mapper-training-materials.md` | draft |
| `mapping-prioritization.md` | draft |
| `mapwithai-workflow-history.md` | draft |
| `maximum-travel-cost.md` | draft |
| `missing-accessibility-information.md` | draft |
| `missing-attribute-values.md` | draft |
| `missing-infrastructure-identification.md` | draft |
| `missing-street-names-for-vendors.md` | draft |
| `mobility-equity.md` | draft |
| `mobility-justice.md` | draft |
| `mpo-contribution.md` | draft |
| `mpo-role.md` | draft |
| `multimodal-accessibility-analysis.md` | draft |
| `national-data-standards-evolution.md` | draft |
| `nationwide-system-requirements.md` | draft |
| `node-vs-edge.md` | draft |
| `nondriver-mobility.md` | draft |
| `older-adult-contribution.md` | draft |
| `open-source-community-role.md` | draft |
| `opensidewalks-community-mapping-groups.md` | draft |
| `opensidewalks-schema-usage.md` | draft |
| `opensidewalks-schema.md` | draft |
| `opensidewalks.md` | draft |
| `operational-agency-use.md` | draft |
| `os-connect-local-gis-relationship.md` | draft |
| `os-connect-maintenance.md` | draft |
| `os-connect-origin.md` | draft |
| `os-connect-problem-statement.md` | draft |
| `os-connect-tdei-relationship.md` | draft |
| `os-connect-vs-openstreetmap.md` | draft |
| `os-connect-vs-traditional-inventories.md` | draft |
| `os-connect.md` | draft |
| `outdated-data-handling.md` | draft |
| `outdated-imagery.md` | draft |
| `participatory-accessibility-mapping.md` | draft |
| `participatory-mapping.md` | draft |
| `partnership-needs.md` | draft |
| `pedestrian-data-complexity.md` | draft |
| `pedestrian-equity.md` | draft |
| `pedestrian-feature-attributes.md` | draft |
| `pedestrian-only-facilities.md` | draft |
| `planned-capabilities.md` | draft |
| `planner-data-validation.md` | draft |
| `planning-with-known-errors.md` | draft |
| `poi-grouping-rationale.md` | draft |
| `post-collection-next-steps.md` | draft |
| `private-facilities.md` | draft |
| `public-data-value.md` | draft |
| `qa-qc-report-infrastructure.md` | draft |
| `qa-qc-report.md` | draft |
| `recommended-sidewalk-tagging-pattern.md` | draft |
| `reportable-errors.md` | draft |
| `required-vs-recommended-attributes.md` | draft |
| `resident-participation.md` | draft |
| `routable-graph.md` | draft |
| `routing-assumptions.md` | draft |
| `routing-personalization.md` | draft |
| `rural-area-handling.md` | draft |
| `rural-community-participation.md` | draft |
| `safe-routes-to-school.md` | draft |
| `safety-improvement.md` | draft |
| `school-participation.md` | draft |
| `separated-sidewalk-mapping.md` | draft |
| `service-planning.md` | draft |
| `sidewalk-attributes.md` | draft |
| `sidewalk-disconnection-causes.md` | draft |
| `sidewalk-street-name-association.md` | draft |
| `state-stewardship-role.md` | draft |
| `statewide-data-importance.md` | draft |
| `statewide-inventory.md` | draft |
| `stewardship-roles.md` | draft |
| `stewardship-sustainability.md` | draft |
| `street-name-routing-importance.md` | draft |
| `street-name-tags-for-routing.md` | draft |
| `street-name-vs-is-sidepath-of-name.md` | draft |
| `surface-attribute.md` | draft |
| `tcat-mapping-project-support.md` | draft |
| `trail-handling.md` | draft |
| `transit-accessibility-analysis.md` | draft |
| `transit-agency-contribution.md` | draft |
| `transit-pedestrian-integration.md` | draft |
| `university-role.md` | draft |
| `unreachable-destinations.md` | draft |
| `update-cadence.md` | draft |
| `update-responsibility.md` | draft |
| `urban-map-density.md` | draft |
| `urgent-correction-process.md` | draft |
| `viewer-overview.md` | draft |
| `viewer-vs-tdei-portal.md` | draft |
| `vision-zero.md` | draft |
| `volunteer-data-contribution.md` | draft |
| `walkshed-advocacy.md` | draft |
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
| `import-into-arcgis.md` | draft |
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
| `accessibility-island.md` | draft |
| `attribute-completeness.md` | draft |
| `attribute-presence-vs-feature-completeness.md` | draft |
| `before-after-walkshed-analysis.md` | draft |
| `bottleneck-hotspots.md` | draft |
| `centrality-and-redundancy.md` | draft |
| `centrality-metric-selection.md` | draft |
| `centrality-sampling-and-repeatability.md` | draft |
| `centrality-tile-generation.md` | draft |
| `centrality.md` | draft |
| `completeness-vs-accessibility-gaps.md` | draft |
| `completeness-vs-ada-compliance.md` | draft |
| `completeness.md` | draft |
| `conditional-attribute-completeness.md` | draft |
| `connected-pedestrian-graph.md` | draft |
| `crossing-count.md` | draft |
| `curb-completeness-metrics.md` | draft |
| `degree-centrality.md` | draft |
| `disconnected-poi.md` | draft |
| `edge-betweenness-centrality.md` | draft |
| `edge-betweenness-operational-use.md` | draft |
| `edge-betweenness.md` | draft |
| `eigenvector-centrality-display.md` | draft |
| `eigenvector-centrality-interpretation.md` | draft |
| `eigenvector-centrality-network-importance.md` | draft |
| `eigenvector-centrality.md` | draft |
| `field-verification-hotspots.md` | draft |
| `intersection-quality-metric.md` | draft |
| `intersection-tile.md` | draft |
| `local-poi-corrections.md` | draft |
| `log-normalized-value.md` | draft |
| `metric-boundaries.md` | draft |
| `metric-coverage-and-interpretation.md` | draft |
| `node-betweenness-centrality-operational-use.md` | draft |
| `node-betweenness-centrality.md` | draft |
| `node-betweenness-operational-use.md` | draft |
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
| `identify-accessibility-islands.md` | draft |
| `interpret-report-sections.md` | draft |
| `use-report-for-ada-planning.md` | draft |

## Rapid — Assistant Knowledge Base

See [rapid/index.md](rapid/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/rapid/concept/`

| File | Status |
| :--- | :----- |
| `rapid.md` | draft |

### Workflows

Base: `assistant/rapid/workflow/`

| File | Status |
| :--- | :----- |
| `add-sidewalk-using-rapid.md` | draft |

## Support — Assistant Knowledge Base

See [support/index.md](support/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/support/concept/`

| File | Status |
| :--- | :----- |
| `accessmap-vs-walksheds.md` | draft |
| `cross-team-followup-ownership.md` | draft |
| `data-citation.md` | draft |
| `dataset-authority.md` | draft |
| `ecosystem-overview.md` | draft |
| `fallback-when-gtfs-pathways-missing.md` | draft |
| `gtfs-pathways-agency-adoption.md` | draft |
| `mappy-hours-eligibility.md` | draft |
| `opensidewalks-contact.md` | draft |
| `os-connect-contact.md` | draft |
| `osm-pedestrian-paths-vs-gtfs-pathways.md` | draft |
| `partner-response-time.md` | draft |
| `staff-email-antipatterns.md` | draft |
| `tdei-contact.md` | draft |
| `tdei-os-connect-osm-differences.md` | draft |

### Workflows

Base: `assistant/support/workflow/`

| File | Status |
| :--- | :----- |
| `check-gtfs-feed-pathways.md` | draft |
| `choose-dataset-for-arcgis.md` | draft |
| `choose-dataset-for-planning.md` | draft |
| `choose-dataset-for-transit-stations.md` | draft |
| `communicate-uncertainty.md` | draft |
| `frame-future-plans.md` | draft |
| `handle-unknown-questions.md` | draft |
| `internal-verification-language.md` | draft |
| `introduce-related-tools.md` | draft |
| `mappy-hours-referral-decision.md` | draft |

## TDEI — Assistant Knowledge Base

See [tdei/index.md](tdei/index.md) for per-topic assistant guidance and policies.

### Concepts

Base: `assistant/tdei/concept/`

| File | Status |
| :--- | :----- |
| `api-key-rotation.md` | draft |
| `dataset-download-formats.md` | draft |
| `dataset-identifier.md` | draft |
| `dataset-level-vs-feature-level-operations.md` | draft |
| `dataset-purpose-and-representation.md` | draft |
| `dataset-version-selection.md` | draft |
| `dataset-visibility.md` | draft |
| `derived-dataset-lineage.md` | draft |
| `environment-separation.md` | draft |
| `external-attribute-release.md` | draft |
| `feedback-management.md` | draft |
| `file-formats.md` | draft |
| `interoperability.md` | draft |
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
| `mislabeled-dataset-handling.md` | draft |
| `osw-download-contents.md` | draft |
| `osw-edges-and-nodes.md` | draft |
| `osw-vs-osm-format.md` | draft |
| `portal-dashboard.md` | draft |
| `project-group-roles.md` | draft |
| `project-group.md` | draft |
| `release-versioning.md` | draft |
| `released-dataset-viewer.md` | draft |
| `released-dataset.md` | draft |
| `services-and-project-groups.md` | draft |
| `source-and-derivative-datasets.md` | draft |
| `tdei-architecture.md` | draft |
| `tdei-data-security.md` | draft |
| `tdei-job-processing.md` | draft |
| `tdei-services.md` | draft |
| `tdei.md` | draft |
| `test-dataset-in-portal.md` | draft |

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
| `accessibility-islands.md` | draft |
| `accessibility-profile-inequity-analysis.md` | draft |
| `accessibility-profiles.md` | draft |
| `accuracy-vs-straight-line.md` | draft |
| `ada-planning.md` | draft |
| `barrier-incorporation.md` | draft |
| `before-after-comparison.md` | draft |
| `bus-stop-access-analysis.md` | draft |
| `complete-streets-planning.md` | draft |
| `crossing-effects.md` | draft |
| `crossing-gap-identification.md` | draft |
| `destination-exclusion.md` | draft |
| `disconnected-network-handling.md` | draft |
| `downtown-revitalization.md` | draft |
| `economic-development.md` | draft |
| `elevation-effects.md` | draft |
| `emergency-resilience-planning.md` | draft |
| `equity-analysis.md` | draft |
| `external-dataset-joins.md` | draft |
| `grant-applications.md` | draft |
| `hospital-access-analysis.md` | draft |
| `infrastructure-scenario-comparison.md` | draft |
| `max-cost.md` | draft |
| `neighborhood-comparison.md` | draft |
| `network-assumptions.md` | draft |
| `os-connect-data-usage.md` | draft |
| `park-access-analysis.md` | draft |
| `pedestrian-bottleneck-identification.md` | draft |
| `pedestrian-vs-wheelchair-walkshed.md` | draft |
| `pedestrian-walkshed.md` | draft |
| `planned-capabilities.md` | draft |
| `planner-assumptions.md` | draft |
| `poi-origin-analysis-limits.md` | draft |
| `prioritization-workflows.md` | draft |
| `profile-variation.md` | draft |
| `public-explanation.md` | draft |
| `reachable-area.md` | draft |
| `rural-transportation-planning.md` | draft |
| `safe-routes-to-school.md` | draft |
| `school-accessibility-analysis.md` | draft |
| `senior-mobility-analysis.md` | draft |
| `transit-planning.md` | draft |
| `travel-limits.md` | draft |
| `travel-profiles.md` | draft |
| `uncertainty-communication.md` | draft |
| `underserved-area-identification.md` | draft |
| `vision-zero.md` | draft |
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
| `walkshed-limitations.md` | draft |
| `walkshed-map-symbols.md` | draft |
| `walkshed-point-features.md` | draft |
| `walkshed-quality.md` | draft |
| `walkshed-result-statistics.md` | draft |
| `walkshed-router-building.md` | draft |
| `walkshed-router-processing.md` | draft |
| `walkshed-scenario-statistics.md` | draft |
| `walkshed-scenarios.md` | draft |
| `walkshed-travel-cost.md` | draft |
| `walkshed-vs-buffer.md` | draft |
| `walkshed.md` | draft |
| `walksheds-tool.md` | draft |
| `wheelchair-walkshed.md` | draft |

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
| `accessibility-feature-editing.md` | draft |
| `asr-imagery-list-repo.md` | draft |
| `attribute-editing.md` | draft |
| `aviv-scoutroute.md` | draft |
| `basemap-loading.md` | draft |
| `change-authorship.md` | draft |
| `change-editor-tracking.md` | draft |
| `changeset-tracking.md` | draft |
| `changesets.md` | draft |
| `collaborative-edit-management.md` | draft |
| `collaborative-editing-support.md` | draft |
| `collaborative-editing.md` | draft |
| `community-workflow-support.md` | draft |
| `compatible-editors.md` | draft |
| `compatible-tools.md` | draft |
| `continuing-feature-edits.md` | draft |
| `custom-imagery-configuration.md` | draft |
| `custom-imagery.md` | draft |
| `dataset-lineage-in-tdei.md` | draft |
| `dataset-lineage.md` | stub |
| `edit-attribution.md` | draft |
| `edit-auditing.md` | draft |
| `edit-history.md` | draft |
| `edit-metadata.md` | draft |
| `edit-reviewers.md` | draft |
| `edit-source-tracking.md` | draft |
| `edit-types.md` | draft |
| `edit-upload-to-tdei.md` | draft |
| `editing-coordination.md` | draft |
| `export-overwrite-behavior.md` | draft |
| `export-process.md` | draft |
| `export-timing.md` | draft |
| `export-versioning.md` | draft |
| `format-specific-data-generator-roles.md` | draft |
| `geometry-editing.md` | draft |
| `gis-staff-role.md` | draft |
| `gis-tool-decision.md` | draft |
| `imagery-json-configuration.md` | draft |
| `imagery-layer-access.md` | draft |
| `imagery-layer-configuration-boundaries.md` | draft |
| `imagery-layer-definition.md` | draft |
| `imagery-layer-mechanics.md` | draft |
| `imagery-layer-overview.md` | draft |
| `imagery-layers.md` | stub |
| `imagery-misconfiguration.md` | draft |
| `imagery-permissions.md` | draft |
| `imagery-raw-json-requirement.md` | draft |
| `imagery-resource-variation.md` | draft |
| `imagery-sources.md` | draft |
| `intended-audience.md` | draft |
| `internal-qa-qc-data-access.md` | draft |
| `josm.md` | draft |
| `keeping-edits-private.md` | draft |
| `manager-edit-review.md` | draft |
| `manager-role.md` | draft |
| `mobile-point-feature-creation.md` | draft |
| `multi-source-stewardship.md` | draft |
| `multiple-workspaces-per-dataset.md` | draft |
| `non-global-dataset-rationale.md` | draft |
| `notes-as-field-issue-reports.md` | draft |
| `osm-api-emulation.md` | draft |
| `osm-connection.md` | draft |
| `osm-editing-emulation-rationale.md` | draft |
| `osm-editor-benefits.md` | draft |
| `osm-tool-compatibility-rationale.md` | draft |
| `parallel-workspace-editing.md` | draft |
| `post-export-behavior.md` | draft |
| `private-osm-explained.md` | draft |
| `private-osm.md` | stub |
| `project-group-and-workspace-roles.md` | draft |
| `project-group-definition.md` | draft |
| `project-group-operations.md` | draft |
| `project-group-referral-access.md` | draft |
| `project-groups.md` | stub |
| `public-availability-of-quest-photos.md` | draft |
| `qa-review-support.md` | draft |
| `qr-code-name-change.md` | draft |
| `quest-definition-url-requirements.md` | draft |
| `rapid-imagery-integration.md` | draft |
| `rapid-versions.md` | draft |
| `rapid.md` | stub |
| `raster-and-vector-basemaps.md` | draft |
| `recommended-publication-workflow.md` | draft |
| `recommended-workflows.md` | stub |
| `review-interface.md` | stub |
| `roles.md` | stub |
| `sandbox.md` | stub |
| `source-dataset-tracing.md` | stub |
| `stewardship-support.md` | stub |
| `target-users.md` | stub |
| `tdei-ecosystem-fit.md` | stub |
| `tdei-vs-workspaces.md` | stub |
| `team-invitations.md` | draft |
| `teams-vs-project-groups.md` | draft |
| `teams.md` | draft |
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
| `invite-to-workspace-team.md` | draft |
| `open-dataset-for-inspection.md` | draft |
| `pre-export-review.md` | stub |
| `publish-jurisdiction-updates.md` | stub |
| `review-quest-contributions.md` | draft |
| `review-workspace-edits.md` | stub |
| `search-project-groups.md` | stub |
| `set-up-tasking-manager-project.md` | draft |
| `use-workspaces-for-community-validation.md` | stub |
| `use-workspaces-for-jurisdiction-stewardship.md` | stub |
