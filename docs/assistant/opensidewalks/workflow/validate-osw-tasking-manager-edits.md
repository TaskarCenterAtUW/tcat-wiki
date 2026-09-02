---
uid: 57966c8d-2cbf-434c-820c-039ff63aca84
title: How do I validate OpenSidewalks edits in the Tasking Manager?
slug: validate-osw-tasking-manager-edits
doc_type: workflow
questions:
    - How do I validate OpenSidewalks edits in the Tasking Manager?
    - What should I check in an OpenSidewalks mapping task?
audiences:
    - advocate
    - planner
    - jurisdiction
products:
    - OpenSidewalks
    - Rapid
topics:
    - opensidewalks
    - rapid
    - review
    - qa-qc
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
        - A Tasking Manager task is well mapped because it has the expected tags alone.
        - Validation guarantees complete or current pedestrian data.
related_pages:
    - ../concept/tasking-manager-roles.md
    - ../concept/network-topology.md
    - ../workflow/map-osw-features-in-tasking-manager.md
    - ../../../opensidewalks/tasking-manager/tutorial/osw-in-osmustm/validation-guide.md
tags:
    - Assistant
---

<!-- @format -->

# How do I validate OpenSidewalks edits in the Tasking Manager?

## Short Answer

Review a mapped task for geometry, alignment, connectivity, required tags, and consistency with available imagery. Submit it as well mapped or return it with constructive comments.

## Significance

Validation catches disconnected or incorrectly tagged pedestrian features before a task is treated as complete.

## What This Means

Use Team `26` for OpenSidewalks validators. Check crossings as ways with curb endpoints and a road connection, curbs as correctly typed nodes, sidewalks along path centerlines, and connectors between curbs and sidewalks. Review task history, fix minor issues when appropriate, and check imagery.

## What This Does Not Mean

A validation pass does not establish that every real-world condition is mapped or that the resulting dataset is physically accessible everywhere.

## How To Use This

Choose a task ready for validation, inspect the History tab, review each feature class, correct errors, then answer the task question. Select **Yes** and submit when the task is well mapped; select **No**, add a comment, and submit when more work is needed.

## Example

A validator finds a crossing that does not share a node with the road, connects it correctly, checks the curb tags, and submits the task as well mapped.

## Assistant Guidance

Ask for the task, schema/project instructions, and specific defect. Distinguish geometry, tagging, connectivity, and source-imagery problems.

## Related Concepts

- [What topology rules apply?](../concept/network-topology.md)
- [How do I map OSW features?](map-osw-features-in-tasking-manager.md)
