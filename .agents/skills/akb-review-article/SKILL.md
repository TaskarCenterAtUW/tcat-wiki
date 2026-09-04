---
name: akb-review-article
description: Review one TCAT Assistant Knowledge Base article for schema compliance, retrieval quality, and assistant safety.
argument-hint: "Path to article, or blank for the active file"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Review an AKB article

Read-only review of exactly one page under `docs/assistant/`; do not edit, regenerate, or approve it. Use `$args`, or the active file only when it is under `docs/assistant/`; otherwise ask for a path. Read `docs/assistant/schema.md` fresh and the complete target article. Do not inspect `dispatch.md` or invent facts, policy, missing evidence, or replacement prose.

## Review checklist

Report only actionable findings as **Error** (schema, correctness, safety) or **Warning** (quality, clarity, retrieval, maintainability).

- **Location:** `topic/index.md` = `policy`; `topic/concept/*.md` = `concept`; `topic/workflow/*.md` = `workflow`.
- **Metadata:** required `uid`, `title`, `slug`, `doc_type`, `questions`, `products`, `audiences`, `topics`, `risk_level`, `authority_level`, `publication_status`, `last_reviewed`, `retrieval_priority`, `assistant_behavior`, `related_pages`. Check filename/slug, path/type, valid statuses (`stub`, `draft`, `published`, `archived`), enums (`risk_level`, `authority_level`, `retrieval_priority`), lists, plausible `YYYY-MM-DD`, and metadata/content consistency.
- **Behavior:** `assistant_behavior` has boolean `allow_inference`, `requires_citation`, `abstain_if_missing_context`, and string-list `do_not_claim`. Each claim is a complete misleading/false claim corresponding to `What This Does Not Mean`, not a negated instruction.
- **Links/vocabulary:** `related_pages` uses existing docs-relative `assistant/...` paths and stays in the assistant layer; flag unsupported/inconsistent controlled vocabulary when it harms retrieval.
- **Structure:** exactly once and in order: `# [Page Title]`, `## Short Answer`, `## Significance`, `## What This Means`, `## What This Does Not Mean`, `## How To Use This`, `## Example`, `## Assistant Guidance`, `## Related Concepts`. Optional subheadings are fine. Only stubs may use clearly marked TODO scaffolds.
- **Content:** `Short Answer` is self-contained and one to three short paragraphs; `Significance` explains civic/operational importance; `What This Means` answers/defines; boundaries state meaningful non-claims; use guidance fits audiences; `Example` is concrete; `Assistant Guidance` matches metadata and includes caveats/citations; related links do not replace substance. Check all claims, examples, metadata, boundaries, and product capabilities agree.
- **Type fit:** concepts define/explain; workflows provide a usable procedure and outcome; policies state governance rules and consequences in the topic index.

## Required response

Use exactly these sections:

### Summary

One short sentence with overall status and context.

### Errors

Numbered actionable failures, or `None.`

### Warnings

Numbered actionable concerns, or `None.`

### Pass/Fail

Exactly `Pass` or `Fail`; any Error means `Fail`.

### Human follow-up

Say whether the page appears ready for editorial sign-off. If a later approved change affects registry inventory/metadata, regenerate `docs/assistant/dispatch.md` with `python utilities/akb_generate_dispatch.py`; never edit it manually.
