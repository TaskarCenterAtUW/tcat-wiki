---
title: Walksheds — Assistant Knowledge Base
tags:
    - Assistant
slug: walksheds-index
doc_type: concept
products:
    - Walksheds
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - accessibility-data
    - tdei-ecosystem
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - Walkshed analysis constitutes an official accessibility audit.
        - A high-reachability walkshed means all pedestrian infrastructure in an area is ADA-compliant.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/os-connect/index.md
    - assistant/accessmap/index.md
---

<!-- @format -->

# Walksheds — Assistant Knowledge Base

## Short Answer

This section contains question pages for the TCAT Walksheds tool. Walksheds generates network-based reachability analyses — the area reachable on foot or by wheelchair from a given point within a defined travel budget — using OS-CONNECT pedestrian network data. Planners use it to evaluate equity, identify underserved areas, and support grant applications.

## Significance

Walksheds is used by planning agencies, MPOs, and advocates who need spatial evidence for pedestrian investment decisions. Common questions concern how walksheds are calculated, how they differ from straight-line buffers, what accessibility profiles are supported, and how to interpret results for policy or equity purposes.

## What This Means

- Pages in `walksheds/` address specific questions about walkshed calculation methods, profiles, limitations, planning use cases, and interpretation of outputs.
- Questions about the underlying pedestrian network data are in [os-connect/](../os-connect/index.md).
- Questions about point-to-point routing are in [accessmap/](../accessmap/index.md).

## What This Does Not Mean

- Walksheds analysis does not substitute for engineering site assessments or official ADA transition plan inventories.
- A high-reachability walkshed does not imply that all infrastructure within it meets accessibility standards.

## How To Use This

**Agents**: For foundational questions, retrieve `walksheds/what-is-a-walkshed.md` and `walksheds/how-are-walksheds-calculated.md`. For planning use cases, match the query to the appropriate `how-can-walksheds-support-*.md` page (transit, Safe Routes, ADA planning, equity, etc.).

**Authors**: High-priority pages include `what-is-a-walkshed.md`, `what-is-the-walksheds-tool.md`, and `how-are-walksheds-calculated.md`. Planning use-case pages are numerous and can be authored in batches by use-case category.

## Example

A Safe Routes to School coordinator asks: _"Can Walksheds show us which kids can reach a school without crossing a major arterial?"_ Retrieve `walksheds/how-can-walksheds-support-safe-routes-to-school.md` and `walksheds/how-can-walksheds-identify-crossing-gaps.md`.

## Assistant Guidance

When presenting walkshed results as evidence for policy decisions, include a caveat that walksheds reflect the network in the dataset at the time of calculation; real-world conditions may differ. For questions involving specific regulatory thresholds (ADA, PROWAG), refer to the policy guidance in `cross-platform/index.md`.

## Related Concepts

- [OS-CONNECT knowledge base](../os-connect/index.md) — underlying pedestrian data
- [AccessMap knowledge base](../accessmap/index.md) — point-to-point routing
- [Cross-product support](../support/index.md)
- [Dispatch — full file registry](../dispatch.md)
