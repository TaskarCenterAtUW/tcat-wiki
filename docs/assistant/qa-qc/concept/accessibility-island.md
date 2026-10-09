---
uid: 48d0ded2-e1d3-4caa-ad78-40041fd7e4d9
title: What is an accessibility island?
slug: accessibility-island
doc_type: concept
questions:
    - What is an accessibility island?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - accessibility-data
    - os-connect
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Separate QA/QC accessibility islands prove that residents cannot travel between the mapped areas.
        - QA/QC accessibility islands are calculated from manual-wheelchair walksheds.
related_pages:
    - assistant/qa-qc/workflow/identify-accessibility-islands.md
    - assistant/qa-qc/concept/connected-pedestrian-graph.md
    - assistant/qa-qc/concept/completeness-vs-accessibility-gaps.md
tags:
    - Assistant
---

<!-- @format -->

# What is an accessibility island?

## Short Answer

In QA/QC reports, an accessibility island represents a group of points of interest (POIs) connected under the report's sidewalk-only pedestrian analysis but not connected to other such groups. The analysis starts forward walksheds at selected POIs; it does not model every possible trip origin.

## Significance

Islands can help planners and engineers find possible gaps in mapped sidewalk connectivity between destinations. They are a screening view of the analyzed network and selected POIs, not a direct description of all pedestrian access in an area.

## What This Means

The report uses the sidewalk-only pedestrian profile and normal, origin-based walksheds from POIs; it does not use reverse walksheds or the manual-wheelchair profile to form these islands. A POI that is reachable only with a road-inclusive profile is not used as an island origin, because the analysis assumes that it lacks sidewalk coverage.

The islands describe connectivity among the included POI-origin results. A separate island does not establish that every location between the displayed shapes is disconnected, or that travel is possible in both directions. Read the map with its profile, POI coverage, network, cost threshold, and dataset version.

The report also buffers displayed edges for visual clarity. Those displayed edges can extend beyond the bounds used to calculate an island, so the shapes may appear to overlap even when the analyzed network components are not connected.

## What This Does Not Mean

An island is not proof that residents cannot travel between neighborhoods, that an individual can or cannot reach a destination, or that a route works in both directions. It does not prove a physical infrastructure gap: missing data, POI selection, profile rules, or thresholds can affect the result. Visible overlap between buffered shapes does not by itself prove network connectivity.

## How To Use This

Use islands as screening indicators. Confirm the included POIs, profile, threshold, dataset, and display treatment; then inspect mapped paths, crossings, barriers, and endpoints. Validate important locations with local records, field observations, and community knowledge before describing a physical gap or prioritizing action.

## Example

A report shows two POI groups as separate islands, although their buffered map shapes appear to touch. Reviewers inspect the sidewalk-only network and nearby crossings to determine whether the modeled components connect; the visual overlap alone does not answer that question.

## Assistant Guidance

Name the report, dataset version, POI coverage, profile, threshold, and map-display assumptions. Explain that the result is based on forward walksheds from selected POIs and does not establish door-to-door or round-trip access. Avoid judging residents or places from an island map, and abstain when the analysis assumptions are missing.

## Related Concepts

- [How do I use QA/QC Reports to identify accessibility islands?](../workflow/identify-accessibility-islands.md)
- [What does "connected pedestrian graph" mean?](connected-pedestrian-graph.md)
- [Why can a city have high completeness but still accessibility gaps?](completeness-vs-accessibility-gaps.md)
