---
name: akb-expand-stub
description: Expand a minimal human-provided answer into a schema-compliant assistant knowledge base page
disable-model-invocation: true
---

<!-- @format -->

# Expand Minimal Answer into Assistant Knowledge Base Page

The user has provided a stub file path or slug and a minimal answer. Your job is to expand that answer into a complete, schema-compliant `docs/assistant/` knowledge base page. Follow every step in order. Do not skip or combine steps.

## Inputs

The user's message will contain:

1. **Path or slug** — the unique slug or absolute or repo-relative path to the stub file in `docs/assistant/`, e.g. `docs/assistant/os-connect/concept/error-reporting.md`.
2. **Minimal answer** — the human-provided seed content. This may be a few sentences, a list, or rough notes. Treat it as authoritative fact; do not contradict or discard it.

If either input is missing, ask the user before proceeding.

## Step 1 — Read the stub and the schema

Read the stub file at the path given. Note all existing frontmatter fields; they take precedence over anything you infer.

Then read the schema from `docs/assistant/schema.md`. Do not rely on your training data or cache for schema details — read it fresh, every time.

## Step 2 — Infer frontmatter values

Using the stub's existing frontmatter as the starting point, fill in or confirm every required field. Rules:

- `title` — derive from the file name if not set: convert the kebab-case stem to title case, e.g. `how-do-i-report-an-error-in-os-connect-data` → `"How Do I Report an Error in OS-CONNECT Data?"`.
- `slug` — use the file stem (kebab-case), unchanged.
- `doc_type` — infer from directory or filename:
    - Files in `concept/` subdirectories → `concept`.
    - Files in `workflow/` subdirectories → `workflow`.
    - Files named `index.md` → `policy`.
- `products` — infer from the directory (`os-connect/` → `OS-CONNECT`, `workspaces/` → `Workspaces`, `accessmap/` → `AccessMap`, `walksheds/` → `Walksheds`, `tdei/` → `TDEI`, `support/` → all relevant products). Use the controlled list from the schema.
- `audiences` — list several relevant audiences (`planner`, `jurisdiction`, `advocate`, `public`, `developer`, etc.) unless the content is clearly specialist-only.
- `topics` — select from the controlled vocabulary in the schema. Add no more than five tags. Choose the most specific applicable tags.
- `risk_level` — `low` by default. Use `medium` if the page touches ADA compliance, legal authority, data accuracy claims, or correction workflows. Use `high` only for pages with direct legal or safety consequences.
- `authority_level` — `explanatory` by default. Use only the schema's valid values: `provisional`, `explanatory`, or `official`; `draft` is a publication status, not an authority level.
- `publication_status` — set to `draft` for a newly expanded stub unless the human explicitly directs another schema-valid status.
- `last_reviewed` — preserve an existing value. If it is absent, request the date of the last human editorial pass; do not represent an agent edit as human review.
- `retrieval_priority` — `high` for the most important pages in a section, `medium` for most pages, `low` for supporting or supplementary content.
- `assistant_behavior`:
    - `allow_inference: false` for all pages (default).
    - `requires_citation: true` for all pages (default).
    - `abstain_if_missing_context: true` for pages where the correct answer depends on the user's jurisdiction, dataset version, or other context not provided; `false` otherwise.
    - `do_not_claim` — list approximately one to five specific false or over-reaching claims an assistant might make that this page corrects. Phrase each as a complete declarative sentence. Leave empty (`[]`) if no obvious over-claims apply.
- `related_pages` — list approximately two to five paths relative to `docs/` for closely related pages. Always include the section `index.md` (e.g. `assistant/os-connect/index.md`). Check `docs/assistant/dispatch.md` for available paths.

## Step 3 — Write the nine body sections

Write the full Markdown body in this exact order. Every heading must appear, spelled exactly as shown.

### `# [Page Title]`

The H1 must match the `title` frontmatter value exactly.

### `## Short Answer`

One to three short paragraphs. This is the text an assistant will surface directly in a reply. It must:

- State the answer to the question (or define the concept/policy) clearly and completely.
- Be self-contained — a reader with no other context should understand the answer.
- Incorporate the user's provided minimal answer as its factual core. Do not paraphrase in ways that change meaning.
- Stay under ~200 words.
- Not contain "Yes" or "No" alone; provide a substantive statement.

### `## Significance`

One paragraph (2-4 sentences) explaining why this topic matters to planners, jurisdictions, advocates, the public, or other identified audiences. Focus on operational or civic importance. Do not use the heading "Why This Matters".

### `## What This Means`

Two to five bullet points (or a short paragraph) that unpack the answer in practical terms. If the page is a question, resolve the question definitively. If it is a concept, define it precisely. If it is a policy, state what follows from it.

### `## What This Does Not Mean`

Two to four bullet points of explicit boundaries, non-claims, and common misinterpretations. Each bullet corrects a plausible wrong conclusion a reader might draw. These become `do_not_claim` candidates — if a bullet is strong enough, add it to the frontmatter field too.

### `## How To Use This`

Audience-segmented guidance in one of these forms:

- A short paragraph per audience (planners, jurisdictions, advocates, public, integrators) — only include audiences that actually apply.
- A bulleted list of use cases, prefixed by the audience role in bold.

### `## Example`

One concrete, specific scenario. Name a real-sounding actor (a city planner, a transit agency GIS analyst, a disability advocate, a Safe Routes coordinator), pose the situation in one sentence, and show how this page's content resolves or addresses it.

### `## Assistant Guidance`

Two to five sentences of explicit behavioral instructions for chatbots consuming this page. Address:

- When to cite this page.
- Whether to abstain if context is missing.
- Any `do_not_claim` items to watch for.
- Whether to recommend the user consult a professional for legal, engineering, or safety questions.

### `## Related Concepts`

An unordered list of Markdown links to related pages. Compute each link relative to the page being authored, not to this skill file. For example, a page in `assistant/os-connect/concept/` uses `../index.md` for its section-index target.

Always link the section index. Add two to four additional links to adjacent pages in `docs/assistant/dispatch.md` that are thematically related.

## Step 4 — Validate before writing

Before writing the file, check:

1. All nine headings are present and in order.
2. Every required frontmatter field is populated (no empty strings, no `null`).
3. `publication_status` is schema-valid and matches the user's direction; it defaults to `draft` for a newly expanded stub.
4. `last_reviewed` is preserved or supplied by the human editorial process; an agent edit did not create a false review date.
5. `do_not_claim` items (if any) are complete declarative sentences.
6. `related_pages` paths use the `docs/`-relative format, not file-system paths.
7. The `## Short Answer` does not contradict the user's minimal answer.
8. No section is omitted, even if its content is brief.

If any check fails, fix it before proceeding.

## Step 5 — Write the file

Write the completed file to the path given by the user. Overwrite the stub entirely.

## Step 6 — Update dispatch.md

Regenerate the registry instead of hand-editing it:

```powershell
python utilities/akb_generate_dispatch.py
```

If the repository's generator requires a different documented invocation, follow its current usage. Never manually edit generated `docs/assistant/dispatch.md`.

## Step 7 — Confirm

Tell the user:

- The file path written.
- The `doc_type`, `risk_level`, and `retrieval_priority` values chosen and a very brief reasoning for each.
- Any `do_not_claim` items added, so the user can verify they are accurate.
- Whether `abstain_if_missing_context` was set to `true` and why.
- That the generated dispatch registry was refreshed.

If the user's minimal answer left any factual gap that would require TCAT staff knowledge to fill (e.g. a specific correction timeline, a named contact, a URL), flag it explicitly so the user can supply it in a follow-up review and editing phase.

---

## Quality Rules (apply throughout)

- **Never invent facts.** If the minimal answer does not state something, do not add it as though it were true. Use hedged language ("typically," "generally") only when the schema and product context genuinely support the hedge.
- **Never contradict the minimal answer.** The user's seed content is authoritative.
- **Preserve domain accuracy.** Do not rename, merge, or redefine TCAT products (TDEI, OS-CONNECT, Workspaces, AccessMap, Walksheds, OpenSidewalks, and AVIV ScoutRoute are each distinct).
- **Keep the Short Answer self-contained.** A retrieval system may surface only that section.
- **Match link paths to dispatch.md.** Only link to files that exist in the dispatch registry; do not invent file paths.
- **Do not add extra headings** that duplicate or replace any of the nine required sections.
