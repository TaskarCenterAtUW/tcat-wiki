---
uid: 96c66875-cae9-4efd-994e-bac5b4f02c60
title: What metadata describes an OpenSidewalks dataset?
slug: dataset-metadata-and-provenance
doc_type: concept
questions:
    - What metadata describes an OpenSidewalks dataset?
    - How does OpenSidewalks record data source and freshness?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - OpenSidewalks
    - TDEI
topics:
    - opensidewalks
    - tdei
    - dataset-lineage
    - data-freshness
    - publishers
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
        - An OpenSidewalks dataset without a current timestamp is necessarily current.
        - Dataset validation removes the need to inspect source and provenance metadata.
related_pages:
    - opensidewalks-schema.md
    - regional-dataset-derivatives.md
    - ../workflow/find-latest-version.md
tags:
    - Assistant
---

<!-- @format -->

# What metadata describes an OpenSidewalks dataset?

## Short Answer

OpenSidewalks dataset metadata can identify the schema, source, geographic region, data timestamp, and software pipeline used to produce the data.

## Significance

Provenance and freshness metadata help users decide whether a dataset is appropriate for a particular routing, planning, or analysis task.

## What This Means

The documented metadata includes `$schema`, optional `dataSource`, optional `region`, optional `dataTimestamp`, and optional `pipelineVersion`. Source information can identify OpenStreetMap, imagery, agency data, or combined inputs.

## What This Does Not Mean

Metadata does not guarantee that every feature is complete, current, or accurate. It describes lineage and scope; it does not replace quality review.

## How To Use This

Check source, region, timestamp, pipeline, and schema version before comparing or publishing datasets. Preserve metadata when creating derivatives.

## Example

A derivative records that it came from an agency inventory, covers one county, was generated on a particular date, and was produced by a named pipeline version.

## Assistant Guidance

Ask which metadata fields are present and what decision the user is making. Do not infer freshness from file age alone.

## Related Concepts

- [What is the OpenSidewalks data schema?](opensidewalks-schema.md)
- [How can regional derivatives serve different uses?](regional-dataset-derivatives.md)
