---
uid: ad85460d-4e34-4025-9a31-754fa1b493e5
title: How does TDEI support interoperability?
slug: interoperability
doc_type: concept
questions:
    - How does TDEI support interoperability?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - interoperability
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
    - assistant/tdei/concept/file-formats.md
    - assistant/tdei/concept/dataset-identifier.md
    - assistant/tdei/concept/source-and-derivative-datasets.md
tags:
    - Assistant
---

<!-- @format -->

# How does TDEI support interoperability?

## Short Answer

TDEI supports interoperability by organizing datasets, identifiers, releases, formats, schemas, processing jobs, and metadata so compatible tools and organizations can exchange and interpret data. The exact compatibility depends on the source, format, schema, version, and consuming workflow.

## Significance

Interoperability reduces avoidable translation and lineage problems when pedestrian and related transportation data move between systems.

## What This Means

Use documented formats and schemas, preserve identifiers and provenance, validate conversions, record versions, and confirm that the consuming tool supports the relevant fields and semantics.

## What This Does Not Mean

Interoperability does not mean that every dataset, format, attribute, or product is interchangeable or automatically synchronized. Conversion does not guarantee that meaning or quality is preserved.

## How To Use This

Check the exact source and target formats, schema versions, required fields, licensing, validation jobs, and downstream assumptions before integrating data.

## Example

An agency converts a supported dataset to a different format, validates the result, and retains the source identifier and release so users can trace the derived file.

## Assistant Guidance

Name the source, target, schema, and version. Do not claim compatibility without evidence, and abstain when the conversion or consumer requirements are undocumented.

## Related Concepts

- [What file formats are available?](file-formats.md)
- [What is the dataset identifier?](dataset-identifier.md)
- [Source and derivative datasets](source-and-derivative-datasets.md)
