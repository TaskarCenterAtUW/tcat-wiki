---
uid: 9afa9a04-a794-4066-967f-6a67dc64286d
title: How do I export a workspace?
slug: export-workspace
doc_type: workflow
questions:
    - How do I export a workspace?
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
last_reviewed:
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Exporting a workspace automatically publishes it as a public TDEI release.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I export a workspace?

## Short Answer

Review the workspace, choose the appropriate export path, provide the required project-group and dataset context, and inspect the exported result before publication.

## Significance

Export is the boundary between sandbox editing and downstream dataset workflows.

## What This Means

Confirm the workspace ID, source lineage, edits, target format, project group, and review status. Export locally or to TDEI according to the approved workflow.

## What This Does Not Mean

An export is not automatically a validated or published release.

## How To Use This

Complete human review, preserve the workspace and source identifiers, validate the output, and publish only through the intended TDEI process.

## Example

A manager reviews a workspace, exports an `.osm` representation for inspection, then separately exports an approved dataset to TDEI.

## Assistant Guidance

Ask whether the user wants a local OSM export or a TDEI publication workflow. Do not request API keys in chat.

## Related Concepts

- [How is workspace data different from public data?](../concept/workspace-public-vs-private-data.md)
- [What is dataset lineage?](../concept/dataset-lineage.md)
