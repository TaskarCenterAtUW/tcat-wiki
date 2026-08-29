---
title: Why are POIs grouped together?
slug: poi-grouping-rationale
doc_type: concept
questions:
    - Why are POIs grouped together?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - qa-qc
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
    - assistant/os-connect/concept/qa-qc-report.md
    - assistant/os-connect/concept/destination-access-analysis.md
    - assistant/livability/concept/poi-source.md
tags:
    - Assistant
---

<!-- @format -->

# Why are POIs grouped together?

## Short Answer

POIs may be grouped together in an analysis to organize destinations by category, simplify reporting, and compare network access to similar types of places. The exact grouping rules depend on the source and report.

## Significance

Grouping can make large destination datasets easier to interpret and can connect walkshed or network metrics to planning questions.

## What This Means

Check the source, category definitions, inclusion rules, coordinates, duplicates, and report scope. Treat groups as analytical categories rather than assuming they represent identical services or importance.

## What This Does Not Mean

Grouping does not prove that every POI is current, open, accessible, or equally important. A POI category is not a community or policy priority automatically.

## How To Use This

Use the report's definitions, document the source and date, validate important destinations, and explain exclusions or uncertain classifications.

## Example

A QA/QC report groups clinics and hospitals to summarize access, while the analyst checks individual entrances and services before making a facility-specific conclusion.

## Assistant Guidance

Name the POI source and grouping rule. Do not infer service quality or equity from categories alone, and abstain when definitions are unavailable.

## Related Concepts

- [What is the QA/QC report?](qa-qc-report.md)
- [Destination access analysis](destination-access-analysis.md)
- [What is the source for the POIs in LivAbility?](../../livability/concept/poi-source.md)
