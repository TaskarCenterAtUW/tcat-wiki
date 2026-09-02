---
uid: 56090dfc-f09d-445c-a3c1-f66a3dd2d564
title: How should conflicting data sources be handled?
slug: conflicting-data-sources
doc_type: concept
questions:
    - How should conflicting data sources be handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - conflicts
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
    - assistant/support/concept/dataset-authority.md
    - assistant/os-connect/concept/local-data-validation.md
    - assistant/os-connect/concept/correction-validation.md
tags:
    - Assistant
---

<!-- @format -->

# How should conflicting data sources be handled?

## Short Answer

When data sources conflict, document the sources, versions, scope, collection dates, definitions, and intended use before deciding how to proceed. There may be no single source that is authoritative for every feature or decision.

## Significance

Unresolved conflicts can change maps, metrics, and planning conclusions. Making the disagreement visible is safer than silently selecting the most convenient value.

## What This Means

Compare provenance, currency, coverage, accuracy evidence, stewardship, and authority for the specific question. Consult the responsible jurisdiction or steward, preserve both source records, and document the resolution or unresolved status.

## What This Does Not Mean

A local inventory shows a curb ramp that is absent from an OS-CONNECT release. The analyst records both versions, checks the collection dates and field evidence, and reports or reconciles the difference through the applicable workflow.

## How To Use This

The newest or most detailed-looking source is not automatically authoritative. Resolving a conflict does not prove that the physical condition is current or accessible.

## Example

Define the decision and required authority, compare sources systematically, seek local confirmation for high-stakes uses, and do not overwrite one source with another without a documented process.

## Assistant Guidance

State which source supports each conclusion and identify remaining disagreement. Cite metadata and validation evidence, and abstain when authority or scope cannot be established.

## Related Concepts

- [How do I know whether a dataset is authoritative?](../../support/concept/dataset-authority.md)
- [How should agencies validate the data locally?](local-data-validation.md)
- [How are agency-submitted corrections validated?](correction-validation.md)
