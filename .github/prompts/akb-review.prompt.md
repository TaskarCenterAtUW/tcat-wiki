---
description: "Review an Assistant Knowledge Base article for schema compliance, structure, and quality."
name: "akb-review"
argument-hint: "Path to docs/assistant/**/*.md to review, or leave blank to review the active file"
agent: "AKB Reviewer"
---

<!-- @format -->

Review the specified Assistant Knowledge Base article in `docs/assistant/` against the schema in `docs/assistant/schema.md`.

Requirements:

- Review only; do not edit files.
- Check frontmatter completeness and validity.
- Check the nine required headings and their order.
- Check `Short Answer`, boundary-setting, audience fit, and assistant guidance quality.
- Apply the correct expectations for the article's `doc_type`.
- Do not update `docs/assistant/dispatch.md`; remind the human to do that manually.

If no file path is provided, review the active file only if it is under `docs/assistant/`. Otherwise, ask for a target file.
