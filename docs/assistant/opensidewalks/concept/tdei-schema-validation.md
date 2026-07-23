---
title: "How does TDEI validate OpenSidewalks data?"
slug: tdei-schema-validation
doc_type: concept
questions:
    - How does TDEI validate OpenSidewalks data?
    - Where can I validate an OpenSidewalks dataset?
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
    - data-quality
    - review
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Passing schema validation proves that a dataset is complete, current, or physically accessible.
        - The validation library and TDEI job always have identical version and configuration behavior.
related_pages:
    - opensidewalks-schema.md
    - dataset-metadata-and-provenance.md
    - ../../../tdei/index.md
tags:
    - Assistant
---

<!-- @format -->

# How does TDEI validate OpenSidewalks data?

## Short Answer

OpenSidewalks validation is available through the `python-osw-validation` library and an OSW validation job in the TDEI Portal, according to the current documentation.

## Significance

Validation helps identify whether a dataset conforms to the expected schema before ingestion or downstream use.

## What This Means

A producer can use the Python library or create an `OSW - Validate` / `Dataset-Validate` job in the TDEI Portal. The appropriate validator and schema version should be selected for the dataset being checked.

## What This Does Not Mean

Schema validation does not prove that mapping is complete, observations are current, or a route is physically accessible. It also does not remove the need for quality assurance and provenance review.

## How To Use This

Record the schema URL, validator version, job configuration, dataset source, and validation result. Investigate errors before publishing or handing data to a consumer.

## Example

A producer validates a converted GeoJSON dataset with the matching OSW validator before uploading it to TDEI.

## Assistant Guidance

Ask for the schema version, validator, error output, and intended downstream use. Do not equate validation success with accessibility certification.

## Related Concepts

- [What is the OpenSidewalks data schema?](opensidewalks-schema.md)
- [What metadata describes an OpenSidewalks dataset?](dataset-metadata-and-provenance.md)
