---
description: Project-wide instructions for the TCAT Wiki workspace
applyTo: "**"
---

<!-- @format -->

IMPORTANT: This project uses a Python virtual environment (`.venv/`). ALWAYS run `.\.venv\Scripts\Activate.ps1` before ANY terminal command (zensical, pip, python, utility scripts, etc.). Never assume the venv is already activated.

When editing Markdown content under `docs/`, also follow `.github/instructions/content-style.instructions.md`.

Every completed development change must update `CHANGELOG.md` in the same changeset.

When using the search tool, consider setting `includeIgnoredFiles` to `true` because `site/`, `human-docs/`, and `agent-docs/` are listed in `files.exclude` and `search.exclude`.
