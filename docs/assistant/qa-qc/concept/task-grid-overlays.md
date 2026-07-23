---
title: "What are QA/QC task-grid overlays?"
slug: task-grid-overlays
doc_type: concept
questions:
    - What are task-grid overlays in QA/QC reports?
    - Why are QA/QC cells centered on intersections?
audiences:
    - developer
    - planner
products:
    - QA-QC Reports
    - AccessMap
topics:
    - qa-qc
    - accessmap
    - intersections
    - testing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - QA/QC task cells are arbitrary map tiles unrelated to the analyzed intersections.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What are QA/QC task-grid overlays?

## Short Answer

A QA/QC task-grid overlay divides an analysis area into cells associated with pedestrian-network intersections. The overlay can represent how data collection or review tasks were organized.

## Significance

The grid connects report results to concrete network locations. It also explains why the overlay may not follow a jurisdiction boundary exactly.

## What This Means

Interpret each cell in relation to the intersections and network features it covers. Use the overlay as a task or analysis reference, not as a complete administrative boundary; metric units may follow the network rather than administrative areas.

## What This Does Not Mean

A cell boundary does not necessarily represent a jurisdiction boundary or a separate dataset. The exact overlay behavior depends on the report implementation.

## How To Use This

Use the current report legend and metadata to identify the metric and task unit. Compare cells only when the reports use compatible grids.

## Example

A report displays a cell centered on an intersection where mapping work was organized. Neighboring cells may extend across a jurisdiction line if their associated network area does.

## Assistant Guidance

Ask which report and metric produced the overlay. Do not infer administrative meaning from the cell geometry alone.

## Related Concepts

- [What does centrality mean?](centrality.md)
