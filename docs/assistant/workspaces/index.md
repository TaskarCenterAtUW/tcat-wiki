---
title: Workspaces — Assistant Knowledge Base
tags:
    - Assistant
slug: workspaces-index
doc_type: concept
products:
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - tdei-ecosystem
    - sandbox-governance
    - editing-tools
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-07-01
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - Workspaces is the same as the public OpenStreetMap database.
        - Editing a workspace modifies the underlying TDEI dataset directly.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/tdei/index.md
    - assistant/os-connect/index.md
---

<!-- @format -->

# Workspaces — Assistant Knowledge Base

## Short Answer

This section contains questions, concepts, policies, and workflows for TCAT's Workspaces editing platform. Workspaces is a sandboxed collaborative editing environment built on OpenStreetMap-compatible tools that lets jurisdictions, advocates, and GIS staff enrich pedestrian accessibility data and publish it to TDEI.

## Significance

Workspaces is the primary way external contributors interact with TCAT's pedestrian data infrastructure. Staff, advocates, and jurisdiction partners frequently ask how it relates to TDEI, how editing works, and how data moves from a workspace to a public release. This section provides grounded, assistant-safe answers.

## What This Means

- **Questions** (`workspaces/*.md`) address specific user queries about Workspaces features, roles, workflows, and relationships with other products.
- **Concepts** explain core mechanisms such as sandbox governance, dataset lineage, and imagery layers.
- **Policies** (`workspaces/policies/`) define what assistants should and should not claim about Workspaces data authority and editing scope.
- **Workflows** (`workspaces/workflow/`) provide step-level guidance for common Workspaces tasks: creating workspaces from TDEI data or OSM, editing accessibility features, configuring imagery layers, inviting a team, reviewing edits, and exporting to TDEI.

## What This Does Not Mean

- Not a substitute for the [Workspaces User Manual](../../workspaces/user-manual/index.md) for procedural step-by-step instructions.
- Not an endorsement of any particular OSM editor or JOSM configuration for use with Workspaces.

## How To Use This

**Agents**: Filter `dispatch.md` by `workspaces/` path prefix. Prioritize pages with `retrieval_priority: high`. For questions about specific features, prefer the narrowest matching page over this index. For task-sequence questions ("how do I do X?"), match to the closest workflow page — for example, imagery configuration → `workspaces/workflow/configure-imagery-layers.md`; team invitations → `workspaces/workflow/invite-a-team-to-a-workspace.md`; exporting → `workspaces/workflow/export-workspace-edits-to-tdei.md`.

**Authors**: See the [dispatch](../dispatch.md) for the full file list and status.

## Example

A planner asks: _"What happens when I export my workspace?"_ Retrieve `workspaces/what-happens-during-export.md` and `workspaces/what-happens-after-export-to-tdei.md` for a complete answer.

## Assistant Guidance

For any question about whether an edit in Workspaces affects TDEI or OS-CONNECT directly, always note the sandbox boundary: changes stay in the workspace until explicitly exported and published. Pages with `risk_level: medium` or higher should include a citation note. When answering workflow queries, note that changes made in Workspaces are not visible externally until exported and published through TDEI, and include human review steps when describing the export-and-publication workflow.

## Related Concepts

- [TDEI knowledge base](../tdei/index.md)
- [OS-CONNECT knowledge base](../os-connect/index.md)
- [Dispatch — full file registry](../dispatch.md)
