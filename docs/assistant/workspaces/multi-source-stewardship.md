---
title: "Multi-Source Stewardship (Workspaces)"
tags:
    - Assistant
slug: multi-source-stewardship
doc_type: concept
products:
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - multi-source-stewardship
    - sandbox-governance
    - dataset-lineage
    - collaborative-accessibility-editing
risk_level: medium
authority_level: draft
review_status: draft
last_reviewed:
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - imported layers are automatically authoritative
        - imported data is automatically published
        - Workspaces automatically resolves conflicting sources
        - all workspace edits must be made manually feature by feature
related_pages:
    - private-osm
    - workspace-sandbox
    - dataset-lineage
    - workspace-export
    - collaborative-accessibility-editing
---

# Multi-Source Stewardship (Workspaces)

## Short Answer

Workspaces supports collaborative stewardship by allowing teams to bring together multiple sources of pedestrian, accessibility, imagery, and operational data in a sandboxed editing environment.

This means users do not need to rely only on manual feature-by-feature editing. They can use supporting datasets, machine-generated outputs, imagery layers, jurisdictional GIS records, audit data, and community-collected information to guide review, correction, and enrichment.

## Significance

Multi-source stewardship is central to the value of Workspaces because accessibility data is rarely complete, current, or authoritative from a single source.

Pedestrian and accessibility information may come from:
- existing sidewalk inventories,
- machine-learning-derived extractions,
- field audits,
- community observations,
- transit agency records,
- jurisdictional GIS datasets,
- imagery interpretation,
- construction updates,
- or prior OS-CONNECT/TDEI releases.

Workspaces provides a controlled environment where these sources can be compared and reconciled before edits are exported or published.

## What This Means

In a Workspaces workflow, teams may use multiple sources of information to support editing and review. These sources can help identify:
- missing sidewalks,
- incorrect geometry,
- curb ramp gaps,
- crossing issues,
- connectivity problems,
- temporary obstructions,
- conflicting records,
- and areas needing field validation.

The workspace acts as a staging and review environment. It allows users to inspect differences, make corrections, document sources, and prepare updates for broader publication workflows.

Multi-source stewardship can include:
- importing supplementary datasets,
- referencing imagery layers,
- reviewing machine-generated features,
- comparing jurisdiction records,
- validating community-reported observations,
- and reconciling inconsistencies before export.

## What This Does Not Mean

Multi-source stewardship does not mean:
- every imported dataset is automatically authoritative,
- imported records should be accepted without review,
- Workspaces automatically resolves conflicts between datasets,
- all imported layers are suitable for publication,
- all changes are immediately pushed to TDEI or OS-CONNECT,
- or that workspace data reflects current field conditions without validation.

Imported or referenced sources should be treated according to their provenance, freshness, quality, and intended use.

## How To Use This

Use Workspaces as a multi-source review environment when a team needs to compare and improve accessibility or pedestrian data before publication.

Recommended workflow:

1. Start with a source dataset or workspace copy.
2. Add or reference supporting layers.
3. Identify differences between sources.
4. Review possible corrections collaboratively.
5. Resolve conflicts using agreed review criteria.
6. Document source provenance where possible.
7. Conduct field validation when needed.
8. Export only reviewed and approved edits.

This workflow is especially useful for:
- jurisdiction data maintenance,
- OS-CONNECT update review,
- community validation campaigns,
- transit stop access review,
- Safe Routes to School analysis,
- ADA transition planning support,
- and imagery-assisted QA/QC.

## Example

A city wants to improve sidewalk and curb ramp data near several transit stops.

The team creates a workspace from an OS-CONNECT-derived dataset. They then add:
- a local curb ramp inventory,
- machine-generated sidewalk detections,
- community-reported access barriers,
- transit stop accessibility observations,
- and recent imagery.

Reviewers compare these sources in the workspace. They correct geometry, update attributes, flag uncertain features, and identify locations needing field validation.

Only reviewed edits are exported into the broader TDEI workflow.

## Assistant Guidance

When explaining multi-source stewardship, the assistant should:
- clarify that Workspaces supports more than manual element-by-element editing,
- explain that supplementary layers can support review and enrichment,
- distinguish between imported/reference data and authoritative published data,
- emphasize review, provenance, and validation,
- avoid implying automatic conflation, acceptance, or publication.

If the assistant cannot determine the source, freshness, or review status of a layer, it should avoid claiming that the data is authoritative.

## Related Concepts

- [Private OSM](private-osm.md)
- [Workspace Sandbox](workspace-sandbox.md)
- [Dataset Lineage](dataset-lineage.md)
- [Workspace Export](workspace-export.md)
- [Collaborative Accessibility Editing](collaborative-accessibility-editing.md)
- Data Freshness (see assistant policies)
- Publication Workflow (see export and TDEI release docs)
- Review and QA/QC (see changesets and review workflows)
