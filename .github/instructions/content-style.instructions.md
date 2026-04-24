---
description: Editorial style guide for TCAT Wiki Markdown content
applyTo: "docs/**/*.md"
---

<!-- @format -->

# TCAT Wiki Content Style Guide

## Golden sample set

Use the golden samples in [../../templates/content/README.md](../../templates/content/README.md) when creating, reviewing, or revising pages under `docs/`. Choose the closest match for the page type:

- [../../templates/content/topic-index.md](../../templates/content/topic-index.md) for topic landing pages
- [../../templates/content/tutorial.md](../../templates/content/tutorial.md) for single-page tutorials
- [../../templates/content/user-manual-index.md](../../templates/content/user-manual-index.md) for user manual index pages
- [../../templates/content/subpage.md](../../templates/content/subpage.md) for tutorial and user manual subpages

For a multi-page tutorial index, combine the opening pattern from [../../templates/content/tutorial.md](../../templates/content/tutorial.md) with the table-of-contents pattern from [../../templates/content/user-manual-index.md](../../templates/content/user-manual-index.md).

## Core principles

- Write for one clear reader goal per page.
- Prefer concise, procedural writing over long exposition.
- Use plain language and active voice.
- Preserve domain accuracy. Do not invent undocumented UI, workflows, prerequisites, or outputs.

## Page opening pattern

- Start with frontmatter that includes `title:` and the appropriate `tags:`.
- Use one `##` page heading that matches the frontmatter title.
- The first prose sentence must identify the page type:
    - Tutorials and tutorial index pages begin with `This tutorial...`
    - User manual index pages begin with `This user manual...`
    - Tutorial and user manual subpages begin with `This section...`
- For guide pages, place the standard Guides List reference immediately after the opening sentence, then add a horizontal rule.

## Structure

- Use `###` headings for major phases, tasks, or conceptual sections.
- Use `####` headings only when a major section genuinely needs subsections.
- Keep headings specific and action-oriented.
- Break procedures into ordered steps. Each step should focus on one action or decision.
- For topic landing pages, follow the overview-plus-guides pattern in [../../templates/content/topic-index.md](../../templates/content/topic-index.md).
- When a workflow has clear phases, use named sections such as `### Step 1`, `### Step 2`, and `### Step 3`, as shown in [../../templates/content/tutorial.md](../../templates/content/tutorial.md).
- For user manual landing pages, follow the `### Table of Contents` pattern in [../../templates/content/user-manual-index.md](../../templates/content/user-manual-index.md).
- Avoid more than two levels of list nesting. If a procedure becomes deeper than that, split it into headings or separate steps.

## Steps and prose

- Start steps with imperative verbs such as `Open`, `Select`, `Download`, `Run`, or `Navigate`.
- Use bold formatting for exact UI labels, menu items, buttons, status values, and field names.
- Use code formatting for filenames, extensions, IDs, placeholders, request headers, commands, and literal values.
- Explain placeholders once before the code block or example that uses them.
- When a reader must choose between paths, label the options clearly and state which one is recommended.
- Keep supporting explanation close to the step it belongs to instead of collecting it later.
- Prefer short paragraphs. Remove filler, repetition, and marketing language.

## Examples, code, and values

- When useful, provide both a generic template and a concrete example, as shown in [../../templates/content/tutorial.md](../../templates/content/tutorial.md).
- Keep code blocks minimal, runnable, and easy to copy.
- Put structured outputs such as JSON in fenced code blocks.
- If a long URL or request must be copied or modified by the reader, place it on its own line or in a code block rather than burying it in a paragraph.
- Name expected outputs clearly, including file extensions when relevant.

## Links, images, and callouts

- Link the first mention of a product, external tool, or related TCAT Wiki guide that the reader may need.
- Prefer relative links for TCAT Wiki content.
- Do not overlink repeated terms in the same short section.
- Add screenshots only when they remove ambiguity or confirm the expected state.
- Place screenshots immediately after the step they support.
- Write alt text that describes both the visible screen and the relevant focus or outcome.
- Use light and dark image variants and follow the existing screenshot naming conventions.
- Use admonitions sparingly for cautions, waiting states, tips, or success confirmations that materially help the reader.

## AI editor rules

- Treat the golden samples as structural baselines, not as text to copy mechanically.
- Preserve subject-matter content supplied by human authors. Improve structure, consistency, wording, and formatting without changing meaning.
- Do not add steps for UI elements, parameters, or outputs unless they are verified from source material or existing TCAT Wiki content.
- Prefer tightening and reorganizing prose over expanding it.
- Keep existing frontmatter, tags, and page-type conventions unless the task requires changing them.

## Final check

- Is the page goal clear from the title and opening sentence?
- Does the first sentence use the required page-type wording?
- Are headings and steps easy to scan?
- Are UI labels bolded and literal values monospaced?
- Are examples, screenshots, and callouts attached to the exact step they support?
- Would a first-time reader know what to do next after each section?
