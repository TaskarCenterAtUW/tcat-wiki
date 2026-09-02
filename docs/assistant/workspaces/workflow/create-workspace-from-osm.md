---
uid: 9e396bd0-b847-4f5a-9d77-48d8acc76153
title: How do I create a workspace from existing OSM data?
slug: create-workspace-from-osm
doc_type: workflow
questions:
    - How do I create a workspace from existing OSM data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - onboarding
    - project-groups
    - workspace-management
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed:
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Importing OSM data into a workspace changes the public OSM database.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I create a workspace from existing OSM data?

## Short Answer

Download an area of interest from OpenStreetMap, convert it to OSW, and upload the result through the Workspaces workspace-creation flow.

## Significance

The workflow creates a sandbox for editing and review from an OSM-derived starting point.

## What This Means

Use SliceOSM or another approved extract, run the TDEI OSW Convert job from OSM to OSW, then create a Workspaces workspace from the resulting `.zip` and select the project group and OpenSidewalks type.

## What This Does Not Mean

The import does not update OSM or publish a TDEI dataset by itself.

## How To Use This

Verify the extract area, source, conversion status, workspace title, project group, dataset type, and processing completion.

## Example

A team extracts a city area, converts the `.osm.pbf` file to OSW, uploads the resulting archive, and receives a new workspace for review.

## Assistant Guidance

Ask which environment, source area, project group, and conversion job are involved.

## Related Concepts

- [What is Workspaces?](../concept/workspaces.md)
- [How does the OSW Convert job work?](../../tdei/concept/job-osw-convert.md)
