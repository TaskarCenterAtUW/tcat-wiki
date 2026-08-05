<!-- @format -->

# TCAT Wiki Agent Guide

TCAT Wiki is a Zensical documentation site for Taskar Center for Accessible Technology transportation-accessibility projects. Markdown under `docs/` is organized by topic; its directory hierarchy drives generated navigation. This is the repository-wide operational index. The detailed, task-specific sources below are authoritative for their scopes.

## Non-negotiable rules

- Activate the repository virtual environment before Python, Zensical, pip, or utility commands:

    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

- Change source files only. Never edit generated `site/`, `human-docs/`, `agent-docs/`, `zensical.build.toml`, or `docs/assistant/dispatch.md`; regenerate the latter with `python utilities/akb-generate-dispatch.py`.
- Keep changes narrow. Use the smallest relevant existing validation; do not add tooling or fix unrelated issues.
- `CHANGELOG.md` is the only update-tracking record. Leave its commented `## Unreleased` block untouched. Record versioned release entries only, and do not create or use Git tags or GitHub releases for update tracking. Use [.agents/skills/update-changelog/SKILL.md](.agents/skills/update-changelog/SKILL.md).

## Route work to the canonical guidance

| Work | Source of truth |
|------|-----------------|
| Workspace and generated-file rules | [.agents/instructions/main.instructions.md](.agents/instructions/main.instructions.md) |
| Markdown structure, tone, page types, links, and screenshots | [.agents/instructions/content-style.instructions.md](.agents/instructions/content-style.instructions.md) and [templates/content/README.md](templates/content/README.md) |
| WCAG 2.2 AA authoring | [.agents/instructions/a11y.instructions.md](.agents/instructions/a11y.instructions.md) |
| Assistant Knowledge Base (AKB) contract | [docs/assistant/schema.md](docs/assistant/schema.md) |
| AKB transcript ingestion, review, or stub expansion | [.agents/skills/](.agents/skills/) |
| Screenshot processing and insertion | [.agents/skills/insert-image/SKILL.md](.agents/skills/insert-image/SKILL.md) |
| Human contribution workflow and detailed authoring procedures | [CONTRIBUTING.md](CONTRIBUTING.md) |

For substantive guides, preserve human subject-matter meaning. Improve only verified structure, clarity, consistency, and proofreading; do not invent facts, UI behavior, prerequisites, or outcomes.

## Authoring and navigation

- Place content in the appropriate `docs/<topic>/` subtree. Guides live beside their topic overview, not in `guides/` subdirectories.
- Guide pages need frontmatter `title:` and suitable `tags:`. Supported guide types are `Guide`, `User Manual`, and `Tutorial`; supported audience/product tags are listed in the content-style guidance.
- Use relative links. Add abbreviations to `includes/abbreviations.md`; the snippets plugin inserts them site-wide.
- For new or moved pages, run `utilities/generate-guides-lists.ps1` and `utilities/generate-nav.ps1` from `utilities/`.
- Preserve both `nav-item.html`/`extra.css` visual ordering and `extra.js` (`sortNavByOrder`) semantic ordering when changing `nav_order` behavior.
- The content-style guidance defines guide-list exclusions and the required opening wording and generated-list behavior for tutorials and user manuals.

## Build, preview, and validation

The deploy uses a human Zensical layer and an agent raw-Markdown layer. [utilities/build-site.py](utilities/build-site.py) prepares both, filters non-published AKB pages from the human layer, checks filtered-page links, regenerates dispatch, strips agent-irrelevant syntax, and overlays agent Markdown. A published page must not link to a stub, draft, archived, or `assistant/support/` page.

Do not serve directly from committed `zensical.toml`; it exposes non-deployed AKB content. Use the deploy-parity wrapper:

```powershell
.\.venv\Scripts\Activate.ps1
.\utilities\serve.ps1
```

Equivalent build commands are `python utilities/build-site.py`, `python utilities/build-site.py --build`, and `python utilities/build-site.py --serve`. The preview does not live-reload `docs/` changes; restart it. Generated artifacts are ignored and must not be committed.

Use `utilities/run-utils.ps1` for the complete established workflow, or targeted commands as needed:

```powershell
cd utilities
.\generate-guides-lists.ps1
.\generate-nav.ps1
.\check-links.ps1 -internal
.\check-links.ps1 -external -NoCache
```

External-link results are cached for 12 hours; `-NoCache` bypasses the cache. `run-utils.ps1` supports `-TestsOnly`, `-SkipLinkCheck`, `-NoCache`, and `-SkipTests`; its last two options are mutually exclusive. Python utility tests run with `python -m pytest utilities -q`; PowerShell utility tests require Pester v5+.

## Specialized workflows

- **Screenshots:** `utilities/process-screenshot.py` converts sources to lossless AVIF and creates near-lossless `-light.avif` and `-dark.avif` variants. Use Windows paths in commands, forward slashes in Markdown, equivalent alt text, and `#only-light`/`#only-dark` fragments. See the insert-image skill and [CONTRIBUTING.md](CONTRIBUTING.md).
- **Event reports:** [utilities/generate-event-report.py](utilities/generate-event-report.py) orchestrates Tasking Manager and AVIV ScoutRoute reports. Required event frontmatter, generator options, templates, JSON, fragments, and `report.md` are documented in [CONTRIBUTING.md](CONTRIBUTING.md) and the utility help.
- **AKB:** The schema governs paths, metadata, headings, status, links, and behavior. Transcript ingestion must propose evidence-grounded changes and receive explicit approval before edits. `dispatch.md` is generated inventory, never an authoring source.

## Version control and project map

Use Semantic Versioning: major for breaking structure/navigation changes or major upgrades; minor for substantial new documentation or rework; patch for corrections and small updates. Use scoped Conventional Commits (for example, `feat(docs-accessmap): add user manual page`) and, when available, branches named `type/scope/<work-item-number>-short-description`. The normal flow is feature branch, conventional commit, and pull request to `main`.

Primary content areas are `docs/accessmap/`, `docs/aviv-scoutroute/`, `docs/josm/`, `docs/opensidewalks/`, `docs/rapid/`, `docs/tdei/`, `docs/tdei-walkshed/`, and `docs/workspaces/`. `docs/resources/` holds assets; `local-storage/` is ignored temporary storage; `utilities/` holds generation, validation, and reporting tools. Key configuration and customization sources are `zensical.toml`, `includes/abbreviations.md`, `resources/stylesheets/extra.css`, and `overrides/main.html`.

For PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, or ZIP input, use installed `markitdown`; write large temporary conversions under `local-storage/`:

```powershell
python -c "from markitdown import MarkItDown; r = MarkItDown().convert('path/to/file'); print(r.text_content)"
```

Use the official [Zensical documentation](https://zensical.org/) for external framework reference.
