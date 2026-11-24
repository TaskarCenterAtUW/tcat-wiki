---
uid: 3ed3b5c7-4bec-4e82-8f0a-676f7393ce02
title: What sources can create a workspace?
slug: workspace-source-options
doc_type: concept
questions:
    - What sources can create a workspace?
    - What types of datasets can I work with in Workspaces, including OSW, GTFS-Pathways, and GTFS-Flex?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - onboarding
    - formats
    - dataset-lineage
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/workspace-creation-methods.md
    - assistant/workspaces/concept/workspaces-api.md
    - assistant/tdei/concept/file-formats.md
    - assistant/workspaces/workflow/import-osm-data-into-workspaces.md
tags:
    - Assistant
---

<!-- @format -->

# What sources can create a workspace?

## Short Answer

TDEI lists dataset types as OSW, Flex (GTFS-Flex), and Pathways (GTFS-Pathways); the Workspaces creation API's `WorkspaceCreate` schema lists `osw`, `pathways`, and `flex`. The current Workspaces manual documents OpenSidewalks and GTFS Pathways for blank and file-based creation; it does not document Flex for those methods.

## Significance

The source type and creation method determine what data can be loaded and what lineage is recorded.

## What This Means

For a TDEI import, choose from the datasets available in the current **Create From TDEI** form and verify the displayed type. For blank creation or file upload, use only the types documented for that form: OpenSidewalks and GTFS Pathways in the current manual. The API's type values do not establish that every type is supported by every UI creation method.

## What This Does Not Mean

A dataset type listed in TDEI or the API does not establish that it is accepted through every creation method. Do not promise a GTFS-Flex file upload or blank Flex workspace without current product documentation.

## How To Use This

Confirm the project group, dataset type, source file if applicable, and environment before creating the workspace. Select a creation method, then verify the type against that method's current form; do not infer support from TDEI's dataset catalog or the API schema.

## Example

A team selects a GTFS-Flex dataset shown in the **Create From TDEI** form, verifies its type, and creates a workspace from it. The team does not assume that the same data can be uploaded from a local Flex ZIP or used for a blank workspace, because the current manual documents only OpenSidewalks and GTFS Pathways for those methods.

## Assistant Guidance

Distinguish TDEI dataset types from types supported by each creation method. Cite the [TDEI file-format guidance](../../tdei/concept/file-formats.md), [Workspaces API article](workspaces-api.md), and [Workspaces creation manual](../../../workspaces/user-manual/create.md); abstain on unsupported file-import combinations.

## Related Concepts

- [What are the different workspace creation methods?](workspace-creation-methods.md)
- [What APIs does Workspaces provide?](workspaces-api.md)
- [What file formats are available in TDEI?](../../tdei/concept/file-formats.md)
- [How can OSM data be imported into Workspaces?](../workflow/import-osm-data-into-workspaces.md)
