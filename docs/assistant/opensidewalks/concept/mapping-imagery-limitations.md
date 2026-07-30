---
title: How should imagery be used when mapping OpenSidewalks features?
slug: mapping-imagery-limitations
doc_type: concept
questions:
    - How should imagery be used when mapping OpenSidewalks features?
    - What are the limits of aerial and street-level imagery?
audiences:
    - advocate
    - public
    - planner
products:
    - OpenSidewalks
    - Rapid
topics:
    - opensidewalks
    - rapid
    - data-freshness
    - review
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Aerial imagery always shows current pedestrian conditions.
        - A feature should be added when imagery does not provide enough evidence.
related_pages:
    - ../workflow/map-osw-features-in-tasking-manager.md
    - ../workflow/validate-osw-tasking-manager-edits.md
    - ../../../opensidewalks/tasking-manager/tutorial/osw-in-osmustm/mapping-guide.md
tags:
    - Assistant
---

<!-- @format -->

# How should imagery be used when mapping OpenSidewalks features?

## Short Answer

Use aerial imagery for general geometry and street-level imagery such as Bing Streetside or Mapillary to inspect details that are difficult to determine from above. Do not guess when imagery is unclear or stale.

## Significance

Imagery supports accurate placement and tagging, but its date, alignment, and resolution limit what can be confidently inferred.

## What This Means

Rapid can show aerial sources and optional street-level photo overlays. If imagery layers are offset, use the editor's imagery-offset controls or temporary reference points, then delete temporary markers. Compare sources for clarity and recency.

## What This Does Not Mean

Imagery is evidence, not a guarantee of current ground conditions. A visible feature may have changed, and an unclear feature should not be assigned a detailed tag without support.

## How To Use This

Check the imagery date when available, align layers before tracing, use street-level coverage for curb types and tactile paving, and leave uncertain details unmapped or for field verification.

## Example

A validator switches from aerial imagery to Bing Streetside to determine whether a curb is lowered and whether tactile paving is visible.

## Assistant Guidance

Ask which imagery source, date, and feature are involved. Recommend field verification when imagery cannot resolve the condition.

## Related Concepts

- [How do I map OSW features?](../workflow/map-osw-features-in-tasking-manager.md)
- [What metadata describes an OpenSidewalks dataset?](dataset-metadata-and-provenance.md)
