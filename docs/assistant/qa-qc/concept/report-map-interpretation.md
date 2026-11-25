---
uid: 77a9a7e4-6462-4f8d-8eaf-68f1c0b5c62c
title: How should QA/QC report maps be interpreted?
slug: report-map-interpretation
doc_type: concept
questions:
    - How should QA/QC report maps be interpreted?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - interpretation
    - gis
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/qa-qc/concept/accessibility-island.md
    - assistant/qa-qc/concept/walkshed-profile-comparison.md
    - assistant/qa-qc/concept/report-feature-counts-and-lengths.md
    - assistant/qa-qc/concept/normalized-value.md
    - assistant/qa-qc/concept/log-normalized-value.md
    - assistant/qa-qc/concept/z-score.md
tags:
    - Assistant
---

<!-- @format -->

# How should QA/QC report maps be interpreted?

## Short Answer

Read each QA/QC map with its legend, metric unit, jurisdiction boundary, dataset version, linked detail, and visual accessibility cues such as contrast, shape, and line width. When multiple walkshed profiles are displayed, the report draws the smaller-reach profile over the larger one regardless of the order in which layers were toggled.

## Significance

Layer order affects which profile is visible where walksheds overlap. The report's fixed overlay order helps show multiple profiles at once, while map scale and geometry simplification can change how close features appear.

## What This Means

Read the legend and profile labels before comparing shapes. In the QA/QC report, a smaller-reach walkshed is drawn on top of a larger-reach walkshed; toggling layers in a different order does not change that display priority.

The report reduces coordinate precision when preparing some geometry to control data size. At very close zoom, this can make lines that represent the same underlying network appear slightly offset. Treat such offsets as a display effect unless the network data show a real difference. Use available map links to inspect the underlying network and imagery.

The report lists raw summary statistics separately from maps and histograms; headings and legends identify whether displayed values are raw, log-normalized, or z-scores of log-scaled tile averages. Eigenvector centrality uses a log-normalized 0–1 display, betweenness uses z-scores, and traversability and degree remain raw in the plots. Read each map heading and legend rather than assuming displayed values match the raw summary table. Interpret clickable tile values using the report's tile-aggregation method.

## What This Does Not Mean

A map color alone is not a complete diagnosis. A transformed display value is not the raw metric or a percentage unless the report explicitly says so. Overlay order does not indicate a profile's importance, and small offsets at close zoom do not necessarily mean that profiles use different network geometry.

## How To Use This

Check the legend, profile label, metric definition, value scale, dataset version, and map scale before comparing areas or values. Distinguish raw summary values from transformed map displays, and account for tile aggregation where it applies. Toggle the profiles you need to see, then account for the report's smaller-over-larger overlay order. Inspect linked network details when an apparent gap or offset affects an interpretation.

## Example

A betweenness tile is shown with a z-score while the summary table lists a raw average. A reader checks the map heading and report method before interpreting the tile as a raw route share or comparing it with another dataset.

## Assistant Guidance

Ask which map, metric, profile, and report version are involved. Explain the overlay order and coordinate-precision limitation where relevant. Do not infer network differences from close-zoom offsets alone.

## Related Concepts

- [Why may QA/QC metric areas differ from jurisdiction boundaries?](metric-boundaries.md)
