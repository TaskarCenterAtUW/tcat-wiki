---
uid: eb972a50-0a11-44a8-8193-796ce9e7383c
title: OS-CONNECT — Assistant Knowledge Base
slug: os-connect-index
doc_type: policy
questions:
    - What assistant-facing information and policies are covered in the OS-CONNECT knowledge base?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - workspaces
    - tdei-ecosystem
    - dataset-lineage
    - accessibility-data
risk_level: high
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/workspaces/index.md
    - assistant/walksheds/index.md
    - assistant/accessmap/index.md
tags:
    - Assistant
---

<!-- @format -->

# OS-CONNECT — Assistant Knowledge Base

## Short Answer

This section contains question pages for OS-CONNECT, the public pedestrian network data viewer and dataset published by TCAT. OS-CONNECT exposes Washington state pedestrian infrastructure data — sidewalks, crossings, curb ramps, and more — through a web viewer and the TDEI data portal.

## Significance

Planners, jurisdictions, advocates, and the public ask about OS-CONNECT data accuracy, correction reports, ADA transition planning, equity analysis, GIS interoperability, and stewardship. This section organizes assistant-facing answers about those topics and their evidence limits.

## What This Means

- Pages in `os-connect/` address specific questions about the OS-CONNECT viewer, the underlying dataset, correction reporting, data attributes, and use cases.
- More than 200 draft pages cover viewer UI, data attributes, correction workflows, community engagement, AI-assisted stewardship, equity analysis, and long-term maintenance.
- Several questions overlap with [Walksheds](../walksheds/index.md), [AccessMap](../accessmap/index.md), and [TDEI](../tdei/index.md) — cross-product support questions are in [support/](../support/index.md).

## What This Does Not Mean

- OS-CONNECT completeness scores are not ADA compliance determinations. ADA-related pages can have different risk levels; check each page's `risk_level` and `abstain_if_missing_context` metadata.
- Not a substitute for the [OS-CONNECT data documentation](../../os-connect/index.md) for authoritative attribute definitions.

## How To Use This

**Agents**: For viewer UI questions (colors, layers, features), prefer [viewer overview](concept/viewer-overview.md), [map layers](concept/map-layers.md), and [feature selection](concept/feature-selection-display.md). For error reporting, start with [report an error](workflow/report-data-error.md). For ADA questions, check `risk_level` before answering.

## Example

A transit planner asks: _"Can I use OS-CONNECT for an ADA transition plan?"_ Retrieve [Can OS-CONNECT be used for ADA transition planning?](concept/ada-transition-planning.md), note its `risk_level: high`, and cite the limitations on using data for legal determinations.

## Assistant Guidance

For questions about whether OS-CONNECT data satisfies a legal requirement, follow the policy guidance in [Cross-Platform](../cross-platform/index.md). For correction reports, distinguish successful submission from a verified data change; the [viewer feedback manual](../../os-connect/data-viewer/user-manual/feedback.md) does not specify issue review or release timing.

## Related Concepts

- [Walksheds knowledge base](../walksheds/index.md)
- [AccessMap knowledge base](../accessmap/index.md)
- [TDEI knowledge base](../tdei/index.md)
- [Cross-product support](../support/index.md)
- [Policies — ADA and safety boundaries](../cross-platform/index.md)
- [Dispatch — full file registry](../dispatch.md)
