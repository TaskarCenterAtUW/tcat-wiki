---
uid: ce7a0d43-f792-472d-9c35-74ed27745081
title: How do I complete and submit an AVIV ScoutRoute quest?
slug: complete-and-submit-a-quest
doc_type: workflow
questions:
    - How do I complete an AVIV ScoutRoute quest?
    - How do I submit an AVIV ScoutRoute quest?
audiences:
    - advocate
    - public
    - planner
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - field-data-collection
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-04
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Submitting a quest guarantees that the recorded observation is correct or immediately published.
related_pages:
    - ../concept/quest.md
    - ../concept/field-observation.md
    - undo-a-quest-submission.md
    - ../../../aviv-scoutroute/user-manual/completing-quests.md
tags:
    - Assistant
---

<!-- @format -->

# How do I complete and submit an AVIV ScoutRoute quest?

## Short Answer

Zoom in to find a quest, open it, observe the highlighted feature, review any prefilled prior answers, answer all applicable questions, and select **Submit**. Submission commits the result to the workspace's database through a changeset.

## Significance

This workflow turns a direct field observation into a targeted project contribution.

## What This Means

Quest icons may stack when zoomed out. After opening a quest, read its instructions, inspect the real-world feature, and use the requested input type and units, if applicable. Previously submitted answers may be prefilled; unsaved answers from a form that is closed are discarded. Conditional questions that do not apply are hidden and do not block completion. Select **Submit** when the applicable answers are ready; the result is immediately committed to the workspace through a changeset and the completed quest then disappears from the map.

If a response is cleared or deselected and submitted, its data is deleted. Changing an earlier answer also purges follow-up answers that no longer apply. If the new response conflicts with an existing answer, resolve the conflict in the app before submitting by choosing whether to overwrite the previous answer or restore it.

## What This Does Not Mean

Submission does not prove that the answer is correct, remove the need for review, or publish the entire dataset. The changeset is not held in a separate pre-review state; review occurs after the workspace commit.

## How To Use This

Review all selected and prefilled options before submitting, and use group selection only when every selected feature has the same characteristics. When revalidating an existing answer after the recency period, submit the confirmed answer if it remains accurate.

## Example

A contributor reopens a crossing quest after its recency period. The prior markings and signal answers are prefilled. The contributor confirms that the feature is unchanged, submits the answers, and the app commits a new changeset that refreshes the element's edited timestamp.

## Assistant Guidance

Ask which quest type, input control, workspace, and Quest Definition are involved. Explain whether the contributor is answering an unanswered question or revalidating a prior answer. Encourage direct observation, conflict resolution before submission, and review of the committed changeset; do not advise guessing.

## Related Concepts

- [What input types are available?](../concept/quest-input-types.md)
- [Why should quests be answered from direct observation?](../concept/field-observation.md)
