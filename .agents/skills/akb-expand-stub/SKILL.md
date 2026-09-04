---
name: akb-expand-stub
description: Expand a minimal human-provided answer into a schema-compliant assistant knowledge base page
argument-hint: "Slug or path to an article under docs/assistant/"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Expand an AKB stub

Expand the user's minimal answer into one complete page under `docs/assistant/`. Treat the seed as authoritative: preserve its meaning, never invent facts, and ask for the path/slug or answer if either is missing.

## Workflow

1. Read the target stub and `docs/assistant/schema.md` fresh. Existing frontmatter takes precedence.
2. Fill required metadata:
    - Preserve `uid`; generate a new canonical UUIDv4 with `python utilities/akb_generate_uid.py` only for a new page.
    - `title` mirrors the filename in title case if absent; `slug` is the unchanged file stem.
    - `doc_type`: `concept/` = `concept`, `workflow/` = `workflow`, `index.md` = `policy`.
    - Use schema-controlled `products`, `audiences`, and `topics` (no more than five topics); infer only when supported by the content.
    - Default `risk_level: medium`, `authority_level: provisional`, `publication_status: draft`, `allow_inference: false`, and `requires_citation: true`. Raise risk only for legal, accuracy, correction, safety, or ADA implications; use `abstain_if_missing_context: true` when jurisdiction, dataset version, or other missing context changes the answer.
    - Preserve `last_reviewed`; do not create a human review date. Set `retrieval_priority` to `high`, `medium`, or `low` based on importance.
    - `do_not_claim` contains one to five complete false/overreaching claims matching the boundaries below. `related_pages` uses existing `docs/`-relative `assistant/...` paths and includes the section index plus one to four related pages when available; check `dispatch.md`.
3. Replace the stub with these headings, exactly once and in order:
   `# [Page Title]`, `## Short Answer`, `## Significance`, `## What This Means`, `## What This Does Not Mean`, `## How To Use This`, `## Example`, `## Assistant Guidance`, `## Related Concepts`.
    - `Short Answer`: self-contained, direct, one short paragraph, under about 200 words, incorporating the seed.
    - `Significance`: one to four sentences on operational or civic importance.
    - `What This Means`: practical definition or answer in bullets/short prose.
    - `What This Does Not Mean`: two to four explicit boundaries and plausible misinterpretations; align `do_not_claim`.
    - `How To Use This`: only applicable audience-specific actions; not instructions for agents.
    - `Example`: one concrete scenario with a plausible actor and resolution.
    - `Assistant Guidance`: one to five sentences covering citations, missing context, boundaries, and advice.
    - `Related Concepts`: Markdown links computed relative to the authored page; always include the section index.
4. Before writing, verify nonempty required metadata, valid UUID/status/enums, preserved seed meaning, ordered headings, docs-relative existing links, and no omitted section.
5. Write the file, then regenerate the generated registry from the repository root:

    ```powershell
    python utilities/akb_generate_dispatch.py
    ```

## Rules and report

Do not add extra canonical headings, contradict the seed, redefine TCAT products, invent links, or hand-edit `docs/assistant/dispatch.md`. Report the path and any factual gaps needing human review.
