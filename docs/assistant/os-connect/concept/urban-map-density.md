---
uid: 8a2fe76d-fa50-4ffc-8682-f31a95573410
title: Why is the map slow or dense in urban areas?
slug: urban-map-density
doc_type: concept
questions:
    - Why is the map slow or dense in urban areas?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - public-vs-private-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/map-layers.md
    - assistant/os-connect/concept/incomplete-coverage.md
    - assistant/os-connect/concept/os-connect.md
tags:
    - Assistant
---

<!-- @format -->

# Why is the map slow or dense in urban areas?

## Short Answer

Urban maps can appear slow or dense because many pedestrian features, attributes, layers, labels, and overlapping geometries are displayed or requested at once. Performance also depends on the browser, network, service, zoom, and current configuration.

## Significance

Dense visualization can make it difficult to distinguish features and can affect interaction, but it does not by itself indicate a data-quality problem.

## What This Means

Check active layers, zoom level, feature count, browser and network conditions, and whether the issue affects display or the underlying data. Use filters or smaller areas when supported.

## What This Does Not Mean

A user hides nonessential layers and zooms into a smaller area to inspect crossings without concluding that the dense display means features are duplicated or inaccurate.

## How To Use This

Slow or dense display does not prove that the data are complete, wrong, or current. A missing visual feature may reflect scale, styling, layer state, or loading failure.

## Example

Identify the environment and active layer, capture the release and location, and report reproducible display or data issues through the current channel.

## Assistant Guidance

Distinguish performance from data interpretation. Do not diagnose a source from appearance alone and abstain when the layer or environment is unknown.

## Related Concepts

- [What are the different map layers?](map-layers.md)
- [Why do some areas appear incomplete?](incomplete-coverage.md)
- [What is OS-CONNECT?](os-connect.md)
