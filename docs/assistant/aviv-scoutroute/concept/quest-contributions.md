---
uid: 303f0036-d892-4fb0-8dbb-d29773b9e96c
title: What do AVIV ScoutRoute quest contributions change?
slug: quest-contributions
doc_type: concept
questions:
    - What do AVIV ScoutRoute quest contributions change?
    - Where are submitted AVIV ScoutRoute quest answers saved?
    - Do AVIV ScoutRoute quest answers wait for review before being saved?
    - Does AVIV ScoutRoute submit quest answers directly to OpenStreetMap?
audiences:
    - advocate
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
    - Workspaces
topics:
    - aviv-scoutroute
    - workspaces
    - quests
    - data-collection
    - review
    - changesets
    - public-vs-private-data
    - osm-interoperability
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-04
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Answering a quest replaces the entire source dataset.
        - A submitted AVIV ScoutRoute quest answer is automatically published publicly.
        - A submitted AVIV ScoutRoute quest answer waits in a separate uncommitted review queue.
        - AVIV ScoutRoute submits quest answers directly to the public OpenStreetMap database.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/workflow/join-a-project-and-find-quests.md
    - assistant/aviv-scoutroute/workflow/complete-and-submit-a-quest.md
    - assistant/aviv-scoutroute/concept/quest-definition-resurvey-interval.md
    - assistant/workspaces/workflow/review-quest-contributions.md
    - assistant/workspaces/concept/osm-connection.md
    - assistant/workspaces/concept/private-osm-explained.md
    - assistant/workspaces/concept/workspace-as-private-osm.md
tags:
    - Assistant
---

<!-- @format -->

# What do AVIV ScoutRoute quest contributions change?

## Short Answer

AVIV ScoutRoute quests collect targeted answers or attribute updates for selected features. On submission, AVIV ScoutRoute sends the data to the selected workspace on the TDEI Workspaces platform, where it is saved through a changeset. The data is committed to that workspace before a reviewer examines it, but it is not submitted directly to the public OpenStreetMap database and is not automatically published as a public dataset update.

## Significance

Understanding the difference between workspaces and OpenStreetMap helps make clear where contributors' data is going.

## What This Means

A contributor answers the configured questions for a feature, such as a curb ramp or bus stop. On submission, the answer is sent to the selected workspace on TDEI Workspaces and committed there through a changeset. The contribution becomes part of the project's workspace review and publication workflow.

Workspaces uses an OSM-like stack for each workspace. Depending on context, documentation may call a workspace an **OSM container**, **OSM sandbox**, **OSM instance**, or **private OSM**. These terms describe the workspace's isolated OSM-compatible editing environment, not the public OpenStreetMap database. The workspace can use familiar OSM concepts such as elements, tags, changesets, and compatible editor connections while remaining a separate data environment.

If a new answer conflicts with a previously submitted answer in the workspace, the app may present conflict resolution before submission. Reviewers can later inspect the committed changeset and make follow-up edits, which are also committed through changesets.

## What This Does Not Mean

A quest answer is not automatically a final public release, a replacement for the whole dataset, or an edit to public OpenStreetMap. It is committed to the selected workspace when submitted, while review, export, and release remain separate steps. The review process examines a committed workspace changeset; it does not delay or place a hold on the initial workspace commit.

## How To Use This

Answer only the questions supported by the observed feature and project instructions. Understand that AVIV ScoutRoute is connected to the intended TDEI Workspaces workspace, not to public OpenStreetMap. Review the response before submitting, and report uncertainty through the available options, notes, or feedback process. After submission, follow the project's Changeset Review process for inspection and any follow-up edits.

## Example

A contributor surveys a bus stop and records its sidewalk material through a quest. AVIV ScoutRoute sends the answer to the selected TDEI Workspaces workspace, where submission creates a changeset without editing unrelated features in the surrounding dataset. The public OpenStreetMap database is not changed. A reviewer later inspects the committed workspace changeset before the project exports or releases the data.

## Assistant Guidance

Explain that AVIV ScoutRoute submits a targeted changeset to the selected TDEI Workspaces workspace before review. Distinguish the workspace's OSM-like or so-called 'private OSM' environment from the public OpenStreetMap database, and distinguish a workspace commit from public publication, export, or release. Do not describe the as being held for review or promise immediate public publication. Cite the relevant quest and Workspaces guidance, and ask for the workspace's current review and publication configuration when those details are unclear.

## Related Concepts

- [How do I join a project and find quests in AVIV ScoutRoute?](../workflow/join-a-project-and-find-quests.md)
- [How do I complete and submit an AVIV ScoutRoute quest?](../workflow/complete-and-submit-a-quest.md)
- [What is the AVIV ScoutRoute quest definition resurvey interval?](quest-definition-resurvey-interval.md)
- [How do I review AVIV ScoutRoute contributions in Workspaces?](../../workspaces/workflow/review-quest-contributions.md)
- [Is Workspaces connected to the public OSM database?](../../workspaces/concept/osm-connection.md)
- [What does private OSM mean?](../../workspaces/concept/private-osm-explained.md)
- [What is Workspaces as a private OSM environment?](../../workspaces/concept/workspace-as-private-osm.md)
