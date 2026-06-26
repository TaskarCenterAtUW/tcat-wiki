---
title: OS-CONNECT — Assistant Knowledge Base
tags:
    - Assistant
slug: index
doc_type: concept
products:
    - OS-CONNECT
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - tdei-ecosystem
    - dataset-lineage
    - accessibility-data
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
        - OS-CONNECT data constitutes an official ADA compliance inventory.
        - Completeness scores indicate regulatory compliance status.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/workspaces/index.md
    - assistant/walksheds/index.md
    - assistant/accessmap/index.md
---

<!-- @format -->

# OS-CONNECT — Assistant Knowledge Base

## Short Answer

This section contains question pages for OS-CONNECT, the public pedestrian network data viewer and dataset published by TCAT. OS-CONNECT exposes Washington state pedestrian infrastructure data — sidewalks, crossings, curb ramps, and more — through a web viewer and the TDEI data portal.

## Significance

OS-CONNECT is TCAT's most frequently queried public-facing product. Planners, jurisdictions, advocates, and the public ask about data accuracy, correction workflows, ADA transition planning, equity analysis, GIS interoperability, and stewardship. This section provides stable, grounded answers for assistant retrieval.

## What This Means

- Pages in `os-connect/` address specific questions about the OS-CONNECT viewer, the underlying dataset, correction reporting, data attributes, and use cases.
- Over 200 question stubs cover viewer UI, data attributes, correction workflows, community engagement, AI-assisted stewardship, equity analysis, and long-term maintenance.
- Several questions overlap with [Walksheds](../walksheds/index.md), [AccessMap](../accessmap/index.md), and [TDEI](../tdei/index.md) — cross-product support questions are in [support/](../cross-platform/support/index.md).

## What This Does Not Mean

- OS-CONNECT completeness scores are not ADA compliance determinations. Pages addressing ADA questions carry `risk_level: medium` and `abstain_if_missing_context: true`.
- Not a substitute for the [OS-CONNECT data documentation](../../os-connect/index.md) for authoritative attribute definitions.

## How To Use This

**Agents**: For viewer UI questions (colors, layers, features), prefer `what-am-i-looking-at-in-this-viewer.md`, `what-are-the-different-map-layers.md`, and `what-does-this-selected-feature-represent.md`. For error reporting, start with `how-do-i-report-an-error-in-os-connect-data.md`. For ADA questions, check `risk_level` before answering.

## Example

A transit planner asks: _"Can I use OS-CONNECT for an ADA transition plan?"_ Retrieve `os-connect/can-os-connect-be-used-for-ada-transition-planning.md`, note `risk_level: medium`, and include a citation with a note that the data does not constitute a legal ADA inventory.

## Assistant Guidance

For questions about whether OS-CONNECT data satisfies a legal requirement, always abstain from a direct yes/no and refer to `policies/ada-safety-legal-boundaries.md`. For correction-workflow questions, note the asynchronous nature of corrections and the release cadence.

## Related Concepts

- [Walksheds knowledge base](../walksheds/index.md)
- [AccessMap knowledge base](../accessmap/index.md)
- [TDEI knowledge base](../tdei/index.md)
- [Cross-product support](../cross-platform/support/index.md)
- [Policies — ADA and safety boundaries](../policies/index.md)
- [Dispatch — full file registry](../dispatch.md)
