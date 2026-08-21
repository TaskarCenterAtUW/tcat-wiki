---
title: What does path count mean in QA/QC reports?
slug: path-count
doc_type: concept
questions:
    - What does path count mean in QA/QC reports?
    - What is path count?
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
    - os-connect
    - walksheds
    - accessibility-metrics
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-20
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Path count is the total number of paths in the dataset
        - Path count is the number of paths reachable from each POI separately
        - Path count is the number of trips that use the paths
related_pages:
    - assistant/qa-qc/concept/crossing-count.md
    - assistant/walksheds/concept/poi-origin-analysis-limits.md
tags:
    - Assistant
---

<!-- @format -->

# What does path count mean in QA/QC reports?

## Short Answer

Path count is the number of paths in a dataset that are reachable for a given profile after walksheds are run from each point of interest (POI) and the resulting walksheds are merged.

## Significance

It summarizes the paths reachable in the modeled area for the selected profile and POIs. The value is therefore an analysis result, not simply an inventory total from the dataset.

## What This Means

The analysis runs a walkshed from each POI using a specified profile. After those walksheds are merged, the report counts the paths that fall within the merged reachable area. The profile and the set of POIs determine which paths are reachable.

## What This Does Not Mean

Path count is not the total number of paths in the dataset. It is also not a separate count of paths for every POI, nor is it a count of trips that use those paths.

## How To Use This

Interpret path count together with the profile, POI set, walkshed settings, and dataset version used for the report. Compare values only when those inputs are comparable.

## Example

If paths reachable from two POIs fall within the same merged walkshed area, interpret the result as the path count for the merged area rather than adding two independent POI counts.

## Assistant Guidance

Explain that path count measures reachable paths after POI-origin walksheds are merged.

## Related Concepts

- [What does crossing count mean in QA/QC reports?](crossing-count.md)
- [What are the limits of POI-origin walkshed analysis?](../../walksheds/concept/poi-origin-analysis-limits.md)
