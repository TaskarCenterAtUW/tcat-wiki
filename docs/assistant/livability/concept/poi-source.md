---
uid: f09e5084-ff52-4dd1-8cd1-abd4822c56f5
title: What is the source for the POIs in LivAbility?
slug: poi-source
doc_type: concept
questions:
    - What is the source for the POIs in LivAbility?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - LivAbility
topics:
    - livability
    - accessibility-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every LivAbility POI is field-verified by TCAT.
        - LivAbility POIs are guaranteed to be complete and current.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/amenity-categories.md
    - assistant/livability/concept/livability-analysis.md
tags:
    - Assistant
---

<!-- @format -->

# What is the source for the POIs in LivAbility?

## Short Answer

The available LivAbility material describes points of interest as inputs to amenity and location analysis, but it does not establish one universal source or a complete provenance rule for every POI. The source, date, and verification status should be checked for the specific analysis.

## Significance

POI provenance affects whether an analysis is timely, comparable, and appropriate for a planning decision. A source gap should be visible rather than hidden behind a precise-looking result.

## What This Means

 - Identify the POI source and retrieval or update date when available.
 - Check which amenity categories and geographic area are included.
 - Treat missing, duplicated, or stale POIs as data-quality limitations.

## What This Does Not Mean

The presence of a POI in LivAbility does not prove that the place is open, accessible, safe, or verified by TCAT. A POI layer is not a substitute for local or field validation.

## How To Use This

Ask which LivAbility analysis and source the user means. Do not infer provenance from the category name or from a similar dataset; consult current product documentation when source details matter.

## Example

A planner sees a nearby service in a LivAbility result and checks its source date and local status before presenting it as an available destination.

## Assistant Guidance

The repository does not document a single universal POI provider. Cite the specific source metadata if available and abstain when the source or date is unknown.

## Related Concepts

 - [LivAbility — Assistant Knowledge Base](../index.md)
 - [What are amenity categories?](amenity-categories.md)
 - [What is LivAbility analysis?](livability-analysis.md)
