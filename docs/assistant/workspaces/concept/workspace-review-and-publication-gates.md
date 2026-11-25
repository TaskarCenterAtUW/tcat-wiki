---
uid: 4cd21f12-6dd9-49e7-bb65-4350ae9de843
title: What are workspace review and publication gates?
slug: workspace-review-and-publication-gates
doc_type: concept
questions:
    - What are workspace review and publication gates?
    - Describe the changeset review process, the AVIV ScoutRoute review process and how they are different?
audiences:
    - jurisdiction
    - planner
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - review
    - publication-workflow
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/workspace-review-interface.md
    - assistant/workspaces/workflow/review-workspace-edits.md
    - assistant/workspaces/workflow/review-quest-contributions.md
    - assistant/workspaces/workflow/set-up-tasking-manager-project.md
tags:
    - Assistant
---

<!-- @format -->

# What are workspace review and publication gates?

## Short Answer

Workspaces changeset review examines edits already committed to a workspace. AVIV ScoutRoute submissions use that same changeset review workflow; automatic flagging can mark contributor changesets for attention but does not delay submission. The separate Tasking-project **Review Required** setting gates task completion on validator review. Export to TDEI is a further, separate step.

## Significance

Gates preserve accountability between collection and public or authoritative data.

## What This Means

There are two distinct review mechanisms:

- **Workspace changeset review** — editors submit changes to the workspace, where they are recorded as changesets. Reviewers inspect the changed features, discuss questions, and, if they are Owners or Validators, can mark flagged changesets as reviewed.
- **AVIV ScoutRoute contributions** — the app submits quest answers directly to the selected workspace through a changeset. The **Auto-flag contributor changesets for review** setting in **Workspace Settings → General** flags contributors' changesets in the review queue. It does not create a separate AVIV holding area or prevent the answer from being saved.
- **Tasking project review** — when a Tasking project's **Review Required** option is enabled, validator review is required before tasks can be completed. This is a task-level gate, not the changeset auto-flag setting.

After review, use the documented export process to upload workspace data to TDEI. Review or export alone does not establish that a dataset is publicly released.

## What This Does Not Mean

AVIV review flagging and Tasking-project validation are not interchangeable. An AVIV answer is committed before changeset review; the Tasking-project setting instead requires task validation before the task is completed. Neither action automatically exports or releases a TDEI dataset.

## How To Use This

Identify whether the work uses AVIV quest submissions, Tasking-project tasks, or general workspace editing. Configure the relevant review control, identify Owners or Validators, define project evidence criteria, and keep export and release steps separate.

## Example

A volunteer submits an AVIV ScoutRoute answer, which is committed as a workspace changeset and automatically flagged for a Validator or Owner to inspect. In a separate Tasking project, the **Review Required** option requires validation before a task can be completed.

## Assistant Guidance

Ask whether the user means a workspace changeset, an AVIV ScoutRoute submission, or a Tasking-project task. Do not describe the Tasking-project **Review Required** gate as a hold on AVIV answers. Cite the current Workspaces review and settings manuals.

## Related Concepts

- [What can the Workspaces review interface show?](workspace-review-interface.md)
- [How do I review workspace edits?](../workflow/review-workspace-edits.md)
- [How do I review AVIV ScoutRoute contributions?](../workflow/review-quest-contributions.md)
- [How do I set up a Tasking Manager project in Workspaces?](../workflow/set-up-tasking-manager-project.md)
- [Workspace Settings — General](../../../workspaces/user-manual/settings/general.md)
- [Validate for a Project](../../../workspaces/user-manual/projects/validate.md)
