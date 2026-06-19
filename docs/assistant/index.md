---
title: Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-knowledge-base
doc_type: concept
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - assistant-layer
    - governance
    - RAG
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-04
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - This layer replaces official product manuals or legal advice.
related_pages:
    - assistant/dispatch.md
    - assistant/schema.md
    - assistant/policies/public-vs-internal-content.md
    - assistant/policies/assistant-abstention.md
---

# Assistant Knowledge Base

## Short Answer

This section is a governed, retrieval-oriented knowledge base for explaining OS-CONNECT, AccessMap, Walksheds, TDEI, and Workspaces to the public through AI assistants. It sits beside the existing product documentation: human-facing procedures and deep manuals stay where they are; here you find stable answers, explicit limits, and assistant-safe phrasing.

## Significance

Public assistants need concise answers, explicit limits on claims, and pointers to authoritative sources. Without a dedicated layer, models over-generalize from fragmented docs or invent compliance interpretations. This knowledge base aligns language across products and channels while preserving the TCAT Wiki as the human-facing source of truth.

## What This Means

- Each page carries machine-readable metadata (`products`, `risk_level`, `authority_level`, `retrieval_priority`) for filtering and grounding.
- Questions, concepts, workflows, policies, and glossary entries share a common section scaffold so chunks stay structurally aligned for RAG splitting.
- The [dispatch file](dispatch.md) is the single source of truth for all pages in this library and tracks their authoring status.
- The [schema](schema.md) documents the authoring contract: required frontmatter fields and the required heading sections every page must follow.

## What This Does Not Mean

- Not a replacement for jurisdiction counsel, ADA legal determinations, or engineering sign-off.
- Not a shortcut to skip reading official manuals when making operational changes.
- Not an endorsement of any particular LLM vendor or hosting environment.

## How To Use This

**External AI agents**: Retrieve pages by URL path (`https://taskarcenteratuw.github.io/tcat-wiki/assistant/**/*.md`). Start with [dispatch.md](dispatch.md) to enumerate available pages and their authoring status. Parse YAML frontmatter for metadata-aware retrieval.

**Content authors**: Follow the [schema](schema.md) and refer to the [dispatch](dispatch.md) file. Use `review_status: draft` until another human TCAT editor has approved the page.

**Integrators**: All pages are valid Markdown with YAML frontmatter. The `assistant_behavior` map encodes per-page guardrails. `retrieval_priority` suggests ranking adjustments. `do_not_claim` provides hard-negative strings for evaluation and prompt grounding.

## Example

A public assistant receives: _"Can I use OS-CONNECT data for an ADA transition plan?"_ It retrieves [os-connect/can-os-connect-be-used-for-ada-transition-planning.md](os-connect/can-os-connect-be-used-for-ada-transition-planning.md), notes `risk_level: medium`, checks `assistant_behavior.abstain_if_missing_context`, and cites the page when answering.

## Assistant Guidance

When a user asks a general question about TCAT products, consult the relevant section index first to identify the most targeted page. Prefer pages with `review_status: reviewed` and `authority_level: official` over drafts. For pages with `risk_level: high`, always cite the source and note that the answer does not constitute legal or engineering advice.

## Related Concepts

- [Dispatch — full registry and authoring status](dispatch.md)
- [Schema — authoring contract for assistant knowledge base pages](schema.md)
- [Workspaces knowledge base](workspaces/index.md)
- [OS-CONNECT knowledge base](os-connect/index.md)
- [AccessMap knowledge base](accessmap/index.md)
- [Walksheds knowledge base](walksheds/index.md)
- [TDEI knowledge base](tdei/index.md)
- [Cross-product concepts](concepts/index.md)
- [Policies](policies/index.md)
- [Workflows](workflows/index.md)
- [Glossary](glossary/index.md)
- [Support Q&A](support/index.md)
