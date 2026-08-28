---
description: Project-wide instructions for the TCAT Wiki workspace
applyTo: "**"
---

<!-- @format -->

# TCAT Wiki workspace

## Environment and generated files

- Before running Python, Zensical, pip, or utility commands, activate the repository virtual environment with `.\.venv\Scripts\Activate.ps1`. Do not assume it is already active.
- Do not edit generated or build-output directories: `site/`, `human-docs/`, `agent-docs/`, or the generated `zensical.build.toml`. Make source changes in `docs/`, `includes/`, `overrides/`, `resources/`, `templates/`, or `utilities/` instead.
- Use `.\utilities\serve.ps1` for local previews. Do not run `zensical serve` directly against the committed `zensical.toml`; the wrapper creates the deploy-equivalent human and agent documentation layers.

## Documentation changes

- When editing Markdown under `docs/`, follow [the content style guide](content-style.instructions.md) and the applicable accessibility instructions.
- Preserve frontmatter titles and tags. For new or moved documentation pages, run the navigation and guide-list generators from `utilities/` before validating the build.
- Do not hand-edit `docs/assistant/dispatch.md`; regenerate it with `utilities/akb_generate_dispatch.py`.

## Validation and changelog

- Validate changes with the narrowest relevant existing checks. For documentation changes, prefer the repository utility tests and the deploy-parity build workflow.
- Record only versioned release updates in `CHANGELOG.md`; its commented-out `## Unreleased` section is not tracked. Do not create or use Git tags or GitHub releases for update tracking. Follow `.agents/skills/update-changelog/SKILL.md` when preparing a versioned entry.
- Search excludes `site/`, `human-docs/`, and `agent-docs/`; include ignored files only when investigating generated output.
