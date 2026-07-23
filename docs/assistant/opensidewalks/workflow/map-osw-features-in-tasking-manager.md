---
title: "How do I map OpenSidewalks features in the Tasking Manager?"
slug: map-osw-features-in-tasking-manager
doc_type: workflow
questions:
    - How do I map OpenSidewalks features in the Tasking Manager?
    - How do I use Rapid for OpenSidewalks mapping?
audiences:
    - advocate
    - public
    - planner
products:
    - OpenSidewalks
    - Rapid
topics:
    - opensidewalks
    - rapid
    - collaborative-editing
    - editing-tools
    - connectivity
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
        - Mapping a task without validation produces a complete pedestrian network.
        - Imagery is sufficient evidence for every pedestrian feature.
related_pages:
    - ../concept/tasking-manager-roles.md
    - ../concept/mapping-imagery-limitations.md
    - ../workflow/validate-osw-tasking-manager-edits.md
    - ../../../opensidewalks/tasking-manager/tutorial/osw-in-osmustm/mapping-guide.md
tags:
    - Assistant
---

<!-- @format -->

# How do I map OpenSidewalks features in the Tasking Manager?

## Short Answer

Join the OpenSidewalks mapper team, choose a project and task, open the task in Rapid or iD, map crossings, curbs, sidewalks, and connectors, then save the OSM edits and submit the task status.

## Significance

Tasking Manager divides a mapping area into tasks so contributors can work without duplicating effort and validators can review the results.

## What This Means

Use Team `27` for OpenSidewalks mappers. Select an available task, choose Rapid or iD, enable relevant map-data filters and imagery, and map the pedestrian network. Crossings should connect roads and have curb endpoints; sidewalks should follow centerlines; connectors should link curbs to sidewalks.

## What This Does Not Mean

Completing a task does not guarantee that every feature is mapped or correctly connected. Follow current OSM and OpenSidewalks guidance and submit uncertain details for later verification rather than guessing.

## How To Use This

Map crossings first, add curb types at endpoints, connect sidewalks and driveways, use street-level imagery when useful, save with the project changeset information, and submit the task as complete only when the task area is covered.

## Example

A mapper opens a Rapid task, traces a crossing to the road centerline, adds lowered curb nodes, draws sidewalk centerlines, adds a connector, uploads the changes, and submits the task.

## Assistant Guidance

Ask for the project, editor, task status, and feature type. Treat UI labels, imagery availability, and project instructions as current-context requirements.

## Related Concepts

- [What topology rules apply?](../concept/network-topology.md)
- [What roles exist in the Tasking Manager?](../concept/tasking-manager-roles.md)
- [How do I validate edits?](validate-osw-tasking-manager-edits.md)
