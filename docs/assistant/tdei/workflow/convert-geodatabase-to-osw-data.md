---
title: "How can a geodatabase be converted to OpenSidewalks-oriented data?"
slug: convert-geodatabase-to-osw-data
doc_type: workflow
questions:
    - How can I convert a geodatabase to OpenSidewalks-oriented data?
    - What tools may be needed to convert a partner geodatabase?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - formats
    - interoperability
    - automation
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
        - A sample-specific conversion script guarantees a valid statewide dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can a geodatabase be converted to OpenSidewalks-oriented data?

## Short Answer

The discussed converter is a quick, sample-specific Python script that uses `ogr2ogr` to convert a geodatabase into GeoJSON. It maps recognized fields and prefixes other retained attributes with `ext:`.

## Significance

Conversion can reduce repetitive preparation work, but schema mapping remains dataset-specific. Validation and review are still required before upload or release.

## What This Means

Inspect the source conventions, map known fields to OpenSidewalks fields, preserve selected unmatched fields as extensions, and produce the required edge and node data. Test the result with the current validator; statewide processing requires checking field-name assumptions across the full source.

## What This Does Not Mean

A converter does not automatically understand every agency's field names or produce release-ready data. The discussed script was based on a sample dataset and may need changes.

## How To Use This

Retain the original source, document mappings, and test a small sample first. Record any assumptions that must be checked across the full dataset.

## Example

A Carnation sample is converted to GeoJSON, with recognized sidewalk and curb attributes mapped and other retained fields written with an `ext:` prefix. The output is then validated before broader processing.

## Assistant Guidance

Confirm the current script location, command syntax, dependencies, and schema requirements before giving operational instructions. Do not promise that the script supports statewide data without testing.

## Related Concepts

- [How can the OpenSidewalks schema support external attributes?](../../opensidewalks/concept/external-attributes.md)
- [How do I integrate external geospatial data with TDEI?](integrate-external-geospatial-data.md)
