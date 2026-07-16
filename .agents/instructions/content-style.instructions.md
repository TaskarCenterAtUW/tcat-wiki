---
description: Editorial style guide for TCAT Wiki Markdown content
applyTo: "docs/{accessmap,aviv-scoutroute,events,josm,opensidewalks,os-connect,rapid,tdei,walksheds,workspaces}/**/*.md"
---

<!-- @format -->

# TCAT Wiki Content Style Guide

## Use the golden samples

Use the [golden sample set](../../templates/content/README.md) as the structural reference when creating, reviewing, or revising content. Choose the closest page type:

- [Topic index](../../templates/content/topic-index.md): topic landing pages
- [Tutorial](../../templates/content/tutorial.md): single-page tutorials
- [User manual index](../../templates/content/user-manual-index.md): user manual landing pages
- [Subpage](../../templates/content/subpage.md): tutorial and user manual subpages

For a multi-page tutorial index, combine the tutorial opening with the user-manual table-of-contents pattern. Reuse the samples' structure and formatting, not their placeholder text.

## Core principles

- Write for one clear reader goal per page.
- Use concise, procedural, plain-language, active-voice writing.
- Preserve domain accuracy. Do not invent or infer undocumented UI, workflows, prerequisites, or outcomes.
- Keep human-authored subject-matter meaning intact; improve only structure, clarity, consistency, and formatting.
- Prefer tightening or reorganizing verified content over expanding it.

## Page types and opening

- Start with frontmatter containing `title:` and appropriate `tags:`, then one matching `##` heading.
- Begin the first prose sentence with the required page-type wording:
    - Tutorial and tutorial index: `This tutorial...`
    - User manual index: `This user manual...`
    - Tutorial or user-manual subpage: `This section...`
- On guide pages, put the standard Guides List reference immediately after the opening sentence, followed by a horizontal rule.
- Use the topic index's overview-plus-guides pattern for topic landing pages and the user manual index's `### Table of Contents` pattern for user manual landing pages.

## Structure

- Use `###` headings for major phases, tasks, or conceptual sections.
- Add `####` headings only for necessary subsections.
- Make headings specific and action-oriented. For phased workflows, use named `### Step N: ...` sections.
- Use ordered lists for procedures; each step should contain one action or decision.
- Limit list nesting to two levels. Split deeper procedures into headings or separate steps.

## Steps and prose

- Start steps with imperative verbs such as `Open`, `Select`, `Download`, `Run`, or `Navigate`.
- Use bold formatting for exact UI labels, menu items, buttons, status values, and field names.
- Use code formatting for filenames, extensions, IDs, placeholders, request headers, commands, and literal values.
- Explain each placeholder before its first use.
- Label workflow choices clearly and identify the recommended path.
- Keep explanations adjacent to the step they support. Use short paragraphs and remove filler, repetition, and marketing language.

## Examples, code, and values

- Pair a generic template with a concrete example when readers must adapt a filename, command, URL, or request body.
- Keep code blocks minimal, runnable, and easy to copy. Put structured data, such as JSON, in fenced code blocks.
- Put long or editable URLs and requests on their own line or in a code block.
- State expected outputs explicitly, including file extensions where relevant.

## Links, images, and callouts

- Link the first useful mention of a product, external tool, or related wiki guide. Use relative links for TCAT Wiki content, and do not repeatedly link the same term in a short section.
- Add a screenshot only when it removes ambiguity, confirms an expected state, or makes a hard-to-find control clear. Place it immediately after the supporting step.
- Write alt text that names the visible screen and the relevant focus or outcome. Use paired light/dark variants and established screenshot naming.
- Use admonitions only for material cautions, waiting states, tips, or success confirmations.

## Final check

- Is the goal clear from the title and opening sentence, and does the opening use the required page-type wording?
- Are headings and steps scannable, with UI labels bolded and literal values monospaced?
- Do examples, screenshots, and callouts immediately support the relevant step?
- Does each section tell a first-time reader what to do next?
- Are all added UI details, values, and outcomes verified by source material or existing TCAT Wiki content?
