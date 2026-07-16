---
name: akb-review-article
description: Review one TCAT Assistant Knowledge Base article for schema compliance, retrieval quality, and assistant safety.
disable-model-invocation: true
argument-hint: "Path to docs/assistant/**/*.md to review, or leave blank to review the active file"
---
<!-- @format -->

# AKB article review

Review exactly one Assistant Knowledge Base article in `docs/assistant/` against the current contract in `docs/assistant/schema.md`. This is a read-only review: do not edit the article, rewrite it, update generated files, or approve content on behalf of TCAT staff.

## Target and source of truth

1. Use `$args` as the target path. If it is empty, use the active document only when it is under `docs/assistant/`. Otherwise, ask for a target path.
2. Read `docs/assistant/schema.md` fresh before reviewing the article. Treat it as authoritative if this skill and the schema differ.
3. Read the complete target article, including frontmatter. Review only that article; do not inspect or validate `docs/assistant/dispatch.md`.
4. Do not invent product facts, policy interpretations, missing evidence, or replacement prose.

## Review checklist

Classify each finding as an **Error** (schema violation, missing required content, or misleading/unsafe behavior) or a **Warning** (quality, clarity, retrieval, or maintainability concern). Report only actionable findings.

### 1. Location and frontmatter

- Confirm the file is inside `docs/assistant/` and its path matches the schema layout: `{topic}/index.md` for `policy`, `{topic}/concept/*.md` for `concept`, or `{topic}/workflow/*.md` for `workflow`.
- Check every required key: `title`, `slug`, `doc_type`, `questions`, `products`, `audiences`, `topics`, `risk_level`, `authority_level`, `publication_status`, `last_reviewed`, `retrieval_priority`, `assistant_behavior`, and `related_pages`.
- Check that `slug` exactly matches the file basename; `doc_type` matches both the path and the allowed values (`concept`, `workflow`, `policy`); and `publication_status` is one of `stub`, `draft`, `published`, or `archived`. Do not require `publication_status: draft`.
- Check valid enum values for `risk_level` (`low`, `medium`, `high`), `authority_level` (`provisional`, `explanatory`, `official`), and `retrieval_priority` (`low`, `medium`, `high`).
- Check that `questions`, `products`, `audiences`, `topics`, and `related_pages` are lists; `last_reviewed` is a plausible `YYYY-MM-DD` date; and metadata is specific and consistent with the article.
- Check `assistant_behavior` contains boolean `allow_inference`, `requires_citation`, and `abstain_if_missing_context`, plus a string list `do_not_claim`.
- For each `do_not_claim` entry, verify it is a complete false or misleading claim the assistant must not make—not a negated instruction—and that it corresponds to a boundary in `## What This Does Not Mean`.
- Check `related_pages` uses docs-relative paths in `assistant/...` form and does not point outside the assistant layer. Do not resolve links through `dispatch.md`.
- Prefer prescribed product and topic vocabulary from the schema. Flag unsupported or inconsistent tags when they reduce retrieval quality; do not treat a merely new topic as an error if the schema permits it and it is appropriate.

### 2. Required structure

After frontmatter, verify these headings appear exactly once, in this order, with the canonical text:

1. `# [Page Title]` — mirrors `title`.
2. `## Short Answer`
3. `## Significance`
4. `## What This Means`
5. `## What This Does Not Mean`
6. `## How To Use This`
7. `## Example`
8. `## Assistant Guidance`
9. `## Related Concepts`

Optional subheadings are acceptable when they do not replace, duplicate, or reorder the canonical headings. For `stub`, `draft`, and `archived` pages, a valid scaffold with clearly marked `TODO` placeholders is acceptable; do not demand publication-ready prose solely because the page is not a stub.

### 3. Content and retrieval quality

- `Short Answer` should be self-contained, direct, and limited to one to three short paragraphs.
- `Significance` should explain operational, institutional, or public-education importance.
- `What This Means` should resolve the user's question with a practical definition or explanation.
- `What This Does Not Mean` must state meaningful boundaries, non-claims, and common misinterpretations in explanatory prose. Ensure its main boundaries are represented in `do_not_claim`.
- `How To Use This` should identify useful actions or implications for the listed audiences (such as planners, jurisdictions, advocates, public users, or integrators).
- `Example` should contain one concrete, article-relevant scenario.
- `Assistant Guidance` should give explicit chatbot behavior, including caveats, abstention conditions, and citation requirements consistent with `assistant_behavior`.
- `Related Concepts` should contain relevant links or a justified absence of links, without replacing substantive content.
- Check that metadata, headings, claims, examples, audience guidance, and boundaries agree with one another and do not overstate certainty, authority, compliance, or product capabilities.

### 4. `doc_type` fit

- **concept:** `Short Answer` clearly and precisely defines the concept; the page explains what it is, how it works, or why it exists.
- **workflow:** the page describes a practical procedure with a discrete user outcome, not only a definition; steps and prerequisites are usable by the listed audiences.
- **policy:** the page states rules or governance constraints, and `What This Means` explains their practical consequences. Policy content belongs in the topic's `index.md`.

## Required response format

Use exactly these sections, in this order:

### Summary

One short paragraph stating the overall review status and the most important context.

### Errors

A numbered list of actionable schema, safety, or correctness failures. If none, write `None.`

### Warnings

A numbered list of actionable quality or maintainability concerns. If none, write `None.`

### Pass/Fail

Write exactly one of `Pass` or `Fail`. Use `Fail` when any Error is present; warnings alone may still pass.

### Human follow-up

State whether the article appears ready for human editorial sign-off. If a subsequent approved edit changes the article inventory or metadata used by the registry, regenerate `docs/assistant/dispatch.md` with `python utilities/akb-generate-dispatch.py`; never edit the generated file manually.
