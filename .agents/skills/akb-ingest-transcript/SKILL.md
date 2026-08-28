---
name: akb-ingest-transcript
description: Ingest a TCAT meeting transcript and propose or apply evidence-grounded Assistant Knowledge Base article changes
disable-model-invocation: true
argument-hint: "Repo-relative path to a .txt WebVTT transcript under local-storage/transcripts/"
---

<!-- @format -->

# Ingest TCAT transcript into the Assistant Knowledge Base

Process the transcript at `$args`. This skill is for TCAT Office Hours and other meeting transcripts whose domain knowledge may belong in `docs/assistant/`. Treat the transcript as evidence, not as permission to invent or silently publish facts.

## Guardrails

- Resolve `$args` from the repository root, identified by `zensical.toml`. Accept a repo-relative or absolute path, but require an existing `.txt` WebVTT transcript under `local-storage/transcripts/` unless the user explicitly provides another valid location.
- Do not edit any file during analysis. First produce a proposal and ask for explicit approval.
- Never invent facts, fill gaps from general knowledge, or silently resolve disagreements. Preserve meaningful uncertainty and identify contradictions.
- Do not rewrite existing article sections that are unrelated to the transcript evidence.
- Do not run unrelated utilities, build the site, check links, or create a commit.
- Read the current schema and dispatch on every invocation; do not rely on cached instructions.
- Never use uncommon special characters; for example, use the more standard apostrophe `'` instead of `’`.

## Phase 1 — Prepare the evidence

1. Validate the transcript path and read the original only as needed to confirm its format.
2. From the repository root, run:

    ```powershell
    python utilities/akb_compress_transcript.py <absolute-transcript-path>
    ```

    The utility writes a sibling `<stem>.compressed.txt` file and prints its path. Read that compressed file. Do not edit or commit the generated transcript.

3. Read these files fresh:
    - [`docs/assistant/schema.md`](../../../docs/assistant/schema.md) — authoritative metadata, directory, heading, vocabulary, and build rules.
    - [`docs/assistant/dispatch.md`](../../../docs/assistant/dispatch.md) — generated registry and current article inventory.

## Phase 2 — Extract and classify knowledge

Identify only substantive, reusable domain knowledge: definitions, corrections, constraints, decisions, procedures, prerequisites, limitations, and unresolved follow-up items. Ignore greetings, logistics, screen-sharing narration, speculation without useful context, and information already fully covered by an existing article.

For each candidate, record internally:

- **Evidence** — the relevant speaker statement or faithful paraphrase; do not overstate it.
- **Topic** — one of the schema's top-level sections, such as `qa-qc`, `cross-platform`, `tdei`, `workspaces`, or `os-connect`.
- **Doc type** — `concept` for what/why/meaning, `workflow` for a procedure with a discrete outcome, or `policy` only for topic-level governance that belongs in `{topic}/index.md`.
- **Disposition** — new article, update to an existing article, or no change.
- **Confidence** — distinguish confirmed information from unresolved, contradicted, or explicitly provisional information. For unresolved material, propose a `stub` and preserve the gap with `<!-- TODO: verify — unresolved in transcript -->`; do not convert a conversational guess into a fact.
- **Scope** — the smallest article or section that captures the evidence without duplicating existing coverage.

Use `dispatch.md` as the source of truth for existing paths and statuses. If needed, verify a candidate path with a filesystem scan, but do not invent links or duplicate an existing article.

## Phase 3 — Present the proposal

Use exactly this structure and do not edit files:

---

### Proposed changes from `<transcript filename>`

**Evidence notes**

- `<brief note about material uncertainty, contradiction, or important context>`
- `None.` if no such note is needed.

**1. New articles**

- `docs/assistant/<topic>/<type>/<slug>.md` — `<one-line evidence-grounded scope>`
- _(repeat for each new article, including proposed stubs)_
- `None.` if there are no new articles.

**2. Updates**

- `docs/assistant/<topic>/<type>/<slug>.md` — `<one-line change, evidence, and affected sections>`
- _(repeat for each update)_
- `None.` if there are no updates.

---

End with: **Do you want to make any changes to this plan, or should I proceed with the edits?**

Do not claim that an article was changed until the user approves.

## Phase 4 — Apply an approved proposal

If the user requests changes, revise the proposal and ask again. Only after explicit approval:

1. Re-read each target article before editing it. Apply only transcript-supported changes. Preserve unrelated content and flag any conflict with confirmed existing content in chat rather than choosing a side silently.
2. For each new article, create a complete schema-compliant page:
    - Put `concept` pages in `docs/assistant/{topic}/concept/`, `workflow` pages in `docs/assistant/{topic}/workflow/`, and topic `policy` content only in `docs/assistant/{topic}/index.md`.
    - Include every required frontmatter key: `title`, `slug`, `doc_type`, `questions`, `products`, `audiences`, `topics`, `risk_level`, `authority_level`, `publication_status`, `last_reviewed`, `retrieval_priority`, `assistant_behavior`, and `related_pages`.
    - Use the applicable controlled product/topic vocabulary from the schema.
    - Every newly authored article must use `authority_level: provisional` and `publication_status: draft`. Preserve uncertainty in the prose and assistant guidance. Set `last_reviewed` to the current date for new articles.
    - Include the nine headings, exactly once and in order: `# [Page Title]`, `## Short Answer`, `## Significance`, `## What This Means`, `## What This Does Not Mean`, `## How To Use This`, `## Example`, `## Assistant Guidance`, and `## Related Concepts`.
    - Keep `Short Answer` self-contained and concise. Make `What This Does Not Mean` explanatory, and make each `do_not_claim` value a complete false or misleading claim that corresponds to that section—not a negated instruction.
3. For updates, modify only the affected sections and metadata. Keep existing frontmatter unless the transcript-supported change requires an update. Do not update the `last_reviewed` date: that is the responsibility of the human reviewer.
4. Regenerate the registry instead of hand-editing it:

    ```powershell
    python utilities/akb_generate_dispatch.py
    ```

    If the repository's generator requires a different documented invocation, follow that utility's current usage. Never manually edit generated `docs/assistant/dispatch.md`.

5. Validate the changed pages against the schema: paths and `doc_type` agree; all required fields are present; lists and enums are valid; the nine headings are ordered correctly; links are docs-relative and existing; uncertainty and `do_not_claim` entries are consistent; and no published page links to filtered non-human-layer content.
6. Report changed files, unresolved evidence, and validation performed. Do not run unrelated utilities or commit.

## Source-of-truth rules

- `docs/assistant/schema.md` overrides this skill whenever they differ.
- `docs/assistant/dispatch.md` is generated by `utilities/akb_generate_dispatch.py`; it is an inventory, not an authoring guide.
- Assistant pages are published in two layers: only `publication_status: published` pages outside `assistant/support/` become human-layer HTML, while all assistant pages remain available as raw Markdown in the agent layer. A draft or stub is not human-layer published.
- A published page must not link to a stub, draft, archived page, or any page under `assistant/support/`.
