---
title: How should agencies validate the data locally?
slug: local-data-validation
doc_type: concept
questions:
    - How should agencies validate the data locally?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - data-quality
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
    - assistant/os-connect/concept/field-validation.md
    - assistant/os-connect/concept/planner-data-validation.md
    - assistant/os-connect/concept/conflicting-data-sources.md
tags:
    - Assistant
---

<!-- @format -->

# How should agencies validate the data locally?

## Short Answer

Agencies should validate OS-CONNECT locally by comparing the exact release with authoritative local records, imagery, field observations, and staff or community knowledge for the intended use.

## Significance

Local validation helps identify differences in coverage, currency, geometry, attributes, ownership, and physical conditions before an agency relies on the data.

## What This Means

Define the decision and sample, record source and dates, check geometry and connectivity, inspect relevant attributes, document discrepancies, and preserve unresolved conflicts. Prioritize high-consequence and low-confidence locations.

## What This Does Not Mean

Local validation does not make the whole dataset complete, current, accessible, or legally sufficient. A local record is not automatically authoritative for every feature or use.

## How To Use This

Use risk-based sampling and the agency's own acceptance criteria, keep local operational data distinct from shared releases, and report supported corrections with evidence.

## Example

A city checks a sample of crossings against its current inventory and field observations, records missing attributes, and uses the results to scope a broader review.

## Assistant Guidance

Ask for the jurisdiction, release, decision, and authority of comparison data. Cite the validation method and abstain from broad accuracy claims beyond the sample.

## Related Concepts

- [How should field validation be incorporated?](field-validation.md)
- [How should planners validate the data?](planner-data-validation.md)
- [How should conflicting data sources be handled?](conflicting-data-sources.md)
