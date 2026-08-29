---
title: What versioning occurs during export?
slug: export-versioning
doc_type: concept
questions:
    - What versioning occurs during export?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - export
    - publication-workflow
    - dataset-lineage
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/export-process.md
    - assistant/workspaces/concept/dataset-lineage-in-tdei.md
    - assistant/tdei/concept/release-versioning.md
tags:
    - Assistant
---

<!-- @format -->

# What versioning occurs during export?

## Short Answer

Export versioning records how an exported workspace result relates to its source dataset, workspace state, changesets, processing, and resulting TDEI dataset or release. The exact identifier and version fields depend on the current workflow.

## Significance

Version and lineage records make it possible to reproduce a result, identify what changed, and distinguish an exported result from its source.

## What This Means

Record source and workspace identifiers, changeset or edit scope, export date, processing result, target dataset, release or version, and validation status.

## What This Does Not Mean

Export versioning does not prove that all edits are correct or that a new release is current, complete, accessible, or compliant.

## How To Use This

Use exact portal metadata, preserve prior versions, compare changes deliberately, and cite the resulting identifier in downstream work.

## Example

A workspace export creates a later dataset version tied to a source release and reviewed changesets. The project retains both identifiers for audit and comparison.

## Assistant Guidance

Do not invent numbering rules or infer semantic meaning from an identifier. Cite the exact release metadata and abstain when the lineage cannot be verified.

## Related Concepts

- [What happens during export?](export-process.md)
- [What is dataset lineage in TDEI?](dataset-lineage-in-tdei.md)
- [How are TDEI releases versioned?](../../tdei/concept/release-versioning.md)
