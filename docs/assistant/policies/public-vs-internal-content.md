---
title: Public vs internal content
slug: public-vs-internal-content
doc_type: policy
products:
  - OS-CONNECT
  - AccessMap
  - Walksheds
  - TDEI
audiences:
  - jurisdiction
  - planner
topics:
  - governance
risk_level: medium
authority_level: draft
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: high
assistant_behavior:
  allow_inference: false
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - Internal runbooks or credentials are part of the public assistant corpus.
related_pages:
  - assistant/policies/assistant-abstention.md
  - assistant/index.md
---

# Public vs internal content

## Short Answer

The assistant knowledge base and linked product manuals on this public wiki are intended for public retrieval. Internal SLAs, credentials, employee directories, and pre-release drafts must stay out of public exports unless explicitly approved and labeled.

## Significance

Prevents accidental indexing of sensitive material and sets expectations for what RAG pipelines may ingest.

## What This Means

Authors mark `authority_level` and `review_status` honestly. Operators restrict crawlers and export scripts to approved roots (`docs/assistant/`, published product paths).

## What This Does Not Mean

- Not a claim that everything under `/docs` is safe for every audience—context still matters.
- Not legal classification of information; organizations retain records policies.

## How To Use This

Pair with access controls on internal wikis; never symlink private notes into `docs/`.

## Example

A draft policy page may remain `review_status: draft` with `authority_level: draft` so downstream systems down-rank or exclude it.

## Assistant Guidance

If retrieval surfaces `draft` policy without a user question that warrants it, prefer reviewed pages. Never expose internal-only URLs.

## Related Concepts

- [Assistant abstention](assistant-abstention.md)
