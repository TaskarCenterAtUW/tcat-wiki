---
uid: 2932c97d-2f41-488f-9054-1e864aeb1f97
title: What are QA/QC bottleneck hotspots?
slug: bottleneck-hotspots
doc_type: concept
questions:
    - What are QA/QC bottleneck hotspots?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - bottlenecks
    - prioritization
    - connectivity
    - accessibility-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/qa-qc/concept/poi-density-and-prioritization.md
    - assistant/qa-qc/concept/node-betweenness-centrality.md
    - assistant/qa-qc/concept/edge-betweenness.md
    - assistant/qa-qc/concept/traversability.md
    - assistant/qa-qc/concept/z-score.md
tags:
    - Assistant
---

<!-- @format -->

# What are QA/QC bottleneck hotspots?

## Short Answer

Bottleneck hotspots are locations where poor traversability intersects with important network or destination connections.

## Significance

They prioritize locations where modeled route dependence and traversal difficulty coincide.

## What This Means

A hotspot combines modeled route dependence with modeled traversal difficulty. The score formula described here converts traversability to a barrier score (`1 - traversability`), log-scales tile-average node and edge betweenness, and standardizes the inputs across eligible tiles. It averages the standardized betweenness values into one route-dependence signal, standardizes that signal and the barrier, adds them, then standardizes the combined result for display.

The formula excludes tiles without a traversability score or either betweenness input. Tiles without a curb node or without a sidewalk or crossing through them lack a required betweenness input. The ranking is relative to eligible tiles in the same analysis. Follow the report's stated focus point and network exclusions when inspecting a hotspot.

## What This Does Not Mean

It is not a confirmed field problem, final design, safety determination, or funding decision. A high score is not a cross-report ranking, and an omitted tile is not evidence that the location is problem-free.

## How To Use This

Check the report's formula and eligible comparison set, then review the tile's traversability and betweenness inputs, nearby mapped features, POI context, and local evidence. Treat a top-ranked list as a review queue; inspect the intersection and surrounding data before proposing a correction or project.

## Example

A highly ranked tile combines a high relative route-dependence signal with low traversability. A reviewer follows its map link and checks the intersection and field conditions before identifying an issue.

## Assistant Guidance

Explain which inputs, transformations, and eligible comparison set produced the hotspot when the report documents them. State that the score is relative to that analysis, disclose excluded or missing inputs, and do not present a hotspot as a confirmed field condition.

## Related Concepts

- [How can POI density inform QA/QC priorities?](poi-density-and-prioritization.md)
