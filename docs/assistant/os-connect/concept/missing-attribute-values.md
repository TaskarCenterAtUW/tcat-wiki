---
uid: 95748c61-3f42-4832-823b-57835ad89373
title: Why do some features have missing values?
slug: missing-attribute-values
doc_type: concept
questions:
    - Why do some features have missing values?
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
    - assistant/os-connect/concept/accessibility-attribute.md
    - assistant/os-connect/concept/missing-accessibility-information.md
    - assistant/os-connect/concept/required-vs-recommended-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# Why do some features have missing values?

## Short Answer

Features have missing values when an attribute was not collected, could not be determined from the source, is outside the release's scope, or has not yet been validated. The reason depends on the schema, collection method, and dataset version.

## Significance

Missing values identify uncertainty and data-quality gaps. Replacing them with assumptions can create false accessibility, routing, or planning conclusions.

## What This Means

Check the field definition, allowed values, source, collection date, and missing-value convention. Preserve null or unknown values, identify locations for review, and supplement with appropriate evidence.

## What This Does Not Mean

Missing does not mean no, inaccessible, or defective. It also does not prove that the feature was overlooked in every source or that the dataset is unusable for every purpose.

## How To Use This

Treat unknowns explicitly, prioritize consequential fields and locations, and report confirmed omissions through the current workflow.

## Example

A sidewalk has geometry but no surface value. The analyst leaves the surface unknown and seeks local or field evidence rather than assigning an accessible or inaccessible value.

## Assistant Guidance

Name the field, schema, release, and source. Do not infer a value from nearby features, and abstain when the missing-value semantics are undocumented.

## Related Concepts

- [What is an accessibility attribute?](accessibility-attribute.md)
- [What accessibility information is missing from OS-CONNECT?](missing-accessibility-information.md)
- [What attributes are required versus recommended?](required-vs-recommended-attributes.md)
