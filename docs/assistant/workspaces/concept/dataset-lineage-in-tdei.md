---
uid: c3edf51c-147c-4bd9-88cc-4a88fc95d71a
title: What is dataset lineage in TDEI?
slug: dataset-lineage-in-tdei
doc_type: concept
questions:
    - What is dataset lineage in TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - sandbox-governance
    - dataset-lineage
    - publication-workflow
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
    - assistant/workspaces/concept/dataset-lineage.md
    - assistant/tdei/concept/dataset-identifier.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
tags:
    - Assistant
---

<!-- @format -->

# What is dataset lineage in TDEI?

## Short Answer

Dataset lineage in TDEI describes the relationship between a source dataset, a workspace or derivative, its edits, and later releases. It helps users trace where data came from and which transformations or review steps occurred.

## Significance

Lineage supports reproducibility, attribution, correction tracking, and responsible interpretation when datasets are copied, edited, converted, or published.

## What This Means

Record source and derivative identifiers, workspace, versions, contributors, transformations, review status, and export or release events. Use exact portal and workspace metadata for the current system.

## What This Does Not Mean

Lineage does not prove that a derivative is equivalent to its source, that edits are correct, or that an exported dataset is current or compliant.

## How To Use This

Trace the dataset before analysis or publication, preserve metadata during conversion, and identify unresolved changes or breaks in provenance.

## Example

A workspace is created from a TDEI release, receives reviewed edits, and is exported as a later dataset. The project records the source release, workspace, changesets, and resulting identifier.

## Assistant Guidance

Do not invent lineage fields or assume automatic synchronization. Cite the exact metadata, distinguish source, derivative, and release, and abstain when the relationship cannot be verified.

## Related Concepts

- [Dataset lineage](dataset-lineage.md)
- [What is the dataset identifier?](../../tdei/concept/dataset-identifier.md)
- [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
