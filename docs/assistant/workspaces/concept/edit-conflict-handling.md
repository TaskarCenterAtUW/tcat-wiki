---
uid: 3f594b9b-1fff-4ff4-9288-632b8658d6e8
title: How does Workspaces handle edit conflicts?
slug: edit-conflict-handling
doc_type: concept
questions:
    - How does Workspaces handle concurrent edits?
    - What is the difference between Resolve and Override?
    - How can I avoid overwriting another user's edit?
audiences:
    - planner
    - jurisdiction
    - advocate
    - developer
products:
    - Workspaces
topics:
    - workspaces
    - collaborative-editing
    - conflicts
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Override preserves the other editor's conflicting field values.
        - Resolve automatically determines which conflicting value is correct.
related_pages:
    - assistant/workspaces/concept/collaborative-edit-management.md
    - assistant/workspaces/concept/changesets.md
    - workspaces/user-manual/settings/general.md
tags:
    - Assistant
---

<!-- @format -->

# How does Workspaces handle edit conflicts?

## Short Answer

In **Workspace Settings** under **External Apps**, **Edit Conflict Handling** offers **Resolve** and **Override** modes for cases where two users edit the same feature. **Resolve** prompts for a choice between differing values; **Override** saves the latest editor's submitted values (“last edit wins”).

## Significance

Concurrent edits to the same feature can produce conflicting field values. The selected mode determines how Workspaces handles those values; it does not decide which value is correct for the real-world feature.

## What This Means

- **Resolve** compares values and prompts the editor to choose which value to use for each field that differs.
- **Override** saves all field values submitted by the latest editor.
- The setting is workspace-specific. Confirm the selected mode with the workspace owner or project lead before coordinating concurrent edits.

## What This Does Not Mean

Neither mode guarantees conflict-free collaboration or determines which submitted value is supported by evidence. **Override** does not preserve conflicting values submitted by the other editor.

## How To Use This

Open **Workspace Settings** > **External Apps**, review the selected **Edit Conflict Handling** option, and select the agreed mode before saving. If the control is unavailable, ask a workspace owner or project-group administrator. Coordinate concurrent edits and review changesets regardless of the selected mode.

## Example

Two editors change different values on the same feature. With **Resolve**, the editor is prompted to choose between values for fields that differ. With **Override**, values submitted by the latest editor are saved.

## Assistant Guidance

Ask which workspace and conflict mode are involved. Do not recommend **Resolve** or **Override** as a universal policy, infer that a selected value is correct, or claim that another editor's conflicting values are retained when **Override** is selected.

## Related Concepts

- [How are collaborative edits managed?](collaborative-edit-management.md)
- [How are changesets tracked?](changesets.md)
- [Workspace Settings — General](../../../workspaces/user-manual/settings/general.md)
