---
title: Workspaces Policies — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-workspaces-policies
doc_type: policy
products:
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - sandbox-governance
    - publication-workflow
risk_level: medium
authority_level: official
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - Editing a workspace constitutes publishing data to the public.
        - Workspaces imposes no limits on what data can be published.
related_pages:
    - assistant/workspaces/index.md
    - assistant/policies/index.md
    - assistant/dispatch.md
---

# Workspaces Policies — Assistant Knowledge Base

## Short Answer

This section contains Workspaces-specific policy pages governing what assistants may and may not claim about data authority, editing scope, export processes, and data freshness within the Workspaces platform.

## Significance

Workspaces operates as a sandboxed editing environment, and the boundaries between a workspace, a TDEI dataset, and a public OS-CONNECT release are frequently misunderstood. Policy pages encode hard guardrails to prevent assistants from overclaiming about data authority, publication state, or edit permanence.

## What This Means

- Pages in `workspaces/policies/` address abstention boundaries, data freshness, editing authority, export caveats, and public vs. private data distinctions within Workspaces.
- Cross-product policies (ADA compliance, abstention, AI validation) are in [policies/](../../policies/index.md).

## What This Does Not Mean

- These policies govern AI assistant behavior, not human staff procedures or jurisdiction agreements.
- Workspaces policies do not create or limit contractual obligations between TCAT and jurisdictions.

## How To Use This

**Agents**: Before answering questions about whether workspace edits are "live," "published," or "visible," retrieve the relevant policy page. The sandbox boundary — workspace data stays private until explicitly exported and published — is the core constraint.

**Authors**: Policy pages require TCAT editorial review before being marked `review_status: reviewed`. Draft pages should note open questions for reviewer attention.

## Example

An agent is about to say: _"Your edits in Workspaces are now live on OS-CONNECT."_ It retrieves `workspaces/policies/workspace-export-and-publication-caveats.md`, finds the export-and-release constraint, and reformulates to: _"Your edits are saved in your workspace. They will appear in OS-CONNECT after you export them to TDEI and they are included in a public release."_

## Assistant Guidance

Always enforce the sandbox boundary in Workspaces answers. Edits are not published until explicitly exported, reviewed, and released through TDEI. The workspace-to-TDEI-to-OS-CONNECT pipeline is multi-step and involves human review.

## Related Concepts

- [Workspaces knowledge base](../index.md)
- [Cross-product policies](../../policies/index.md)
- [Dispatch — full file registry](../../dispatch.md)

## Planned Pages

| File | Scope |
|------|-------|
| `workspaces/policies/workspace-abstention-boundaries.md` | When to abstain from answering Workspaces questions |
| `workspaces/policies/workspace-data-freshness.md` | How to communicate workspace data currency limitations |
| `workspaces/policies/workspace-editing-authority.md` | Who has authority to edit and publish workspace data |
| `workspaces/policies/workspace-export-and-publication-caveats.md` | Caveats about the workspace export and TDEI publication process |
| `workspaces/policies/workspace-public-vs-private-data.md` | What data is public vs. private in Workspaces |
