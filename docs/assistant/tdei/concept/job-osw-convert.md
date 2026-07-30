---
title: What does the TDEI OSW Convert job do?
slug: job-osw-convert
doc_type: concept
questions:
    - What does the TDEI OSW Convert job do?
products:
    - TDEI
    - OpenSidewalks
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - opensidewalks
    - interoperability
    - formats
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
        - Format conversion guarantees semantic equivalence for every consumer.
related_pages:
    - job-processing.md
    - ../concept/osw-vs-osm-format.md
    - ../../../tdei/portal/user-manual/jobs/osw-convert.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI OSW Convert job do?

## Short Answer

The OSW Convert job converts between OSW and OSM formats using an explicit source format, target format, and compatible input file.

## Significance

Conversion supports exchange between schema-aware workflows and OSM-compatible tools.

## What This Means

Choose `OSW` or `OSM` as source and target. OSM input can use `.pbf`, `.osm`, or `.xml`; OSW input uses `.zip` according to the current portal guide. Record the job ID and inspect the output.

## What This Does Not Mean

Conversion does not guarantee that all fields, topology, or semantics are preserved identically for every consumer.

## How To Use This

Confirm source and target formats, use the allowed extension, validate the result, and compare important attributes and connectivity.

## Example

A producer converts an OSW archive to OSM for an editor, then validates the resulting representation before exchange.

## Assistant Guidance

Ask for source format, target format, schema version, and intended consumer.

## Related Concepts

- [What does the OSW Validate job do?](job-osw-validate.md)
- [Which formats can a TDEI dataset download use?](dataset-download-formats.md)
