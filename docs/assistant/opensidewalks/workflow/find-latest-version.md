---
title: "Where do I find the latest version of the OpenSidewalks schema?"
slug: find-latest-version
doc_type: workflow
questions:
    - Where do I find the latest version of the OpenSidewalks schema?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A page labeled OSW 0.3 is necessarily the latest OpenSidewalks schema.
        - A schema is suitable for a consumer without checking its version and requirements.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# Where do I find the latest version of the OpenSidewalks schema?

## Short Answer

Find the maintained OpenSidewalks Schema repository, identify the version required by the dataset or consumer, and verify the dataset's `$schema` URL before using it.

## Significance

Schema versions define the fields and interpretations that validation and downstream tools expect.

## What This Means

The wiki includes pages labeled `OSW 0.3`, but labels can become outdated. Use the current schema repository and the `$schema` field in the dataset as the authoritative version references for a given workflow.

## What This Does Not Mean

The latest schema is not automatically compatible with every existing dataset, validator, or consumer.

## How To Use This

Record the schema URL, dataset version, validator version, and target consumer. Validate after conversion or migration.

## Example

A dataset declares an OSW schema URL in `$schema`; an integrator checks that version against the consumer before loading it.

## Assistant Guidance

Ask for the exact schema URL and intended tool. Do not answer "latest" without checking the maintained source.

## Related Concepts

- [What is the OpenSidewalks data schema?](../concept/opensidewalks-schema.md)
