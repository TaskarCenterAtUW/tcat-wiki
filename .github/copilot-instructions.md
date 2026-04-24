<!-- @format -->

# TCAT Wiki - AI Coding Agent Instructions

## Project Overview

**TCAT Wiki** is a Zensical-based documentation site for the Taskar Center for Accessible Technology (TCAT). It hosts information, guides, and resources related to TCAT's transportation accessibility projects: **OpenSidewalks** (OSW), the **Transportation Data Exchange Initiative** (TDEI), and **AccessMap**, among others.

## Architecture & Key Concepts

### Single-Source Documentation Site

- **Framework**: Zensical (`zensical.toml` orchestrates everything)
- **Content**: Markdown files in `/docs` structured by topic
- **Navigation**: Auto-generated from directory structure via PowerShell scripts
- **Custom Extensions**: YAML frontmatter titles, abbreviations auto-linking, custom CSS theming

### Directory Structure Pattern

```
docs/
  [topic]/
    index.md              # Topic overview
    specific-guide.md     # Guides alongside topic overview
    subtopic/
      index.md            # Subtopic overview
      specific-guide.md   # Guides within subtopic
```

**Key insight**: Directory hierarchy directly maps to navigation structure. Guides are stored directly in their topic directories (not in nested `guides/` subdirectories). Use `generate-guides-lists.ps1` to auto-generate index files and `generate-nav.ps1` to update the `zensical.toml` navigation structure.

### Abbreviations System

- `/includes/abbreviations.md` auto-links acronyms site-wide (e.g., OSW, TDEI, JOSM)
- Add new acronyms here; they're automatically inserted into all `.md` files via the Zensical snippets plugin

## Version Control & Workflow

This project follows standardized version control conventions:

### Semantic Versioning

The TCAT Wiki uses [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH):

- **Major (X.0.0)**:
    - Core: New major features or upgrades
    - Docs: Changes to structure/navigation that break external links
- **Minor (0.X.0)**:
    - Core: Significant changes to core features
    - Docs: New documentation or major reworks
- **Patch (0.0.X)**:
    - Core: Minor fixes, fixing typos, completing chores
    - Docs: Small updates, fixing typos, adding images

The version number is stored in the `version` field in `zensical.toml`.

### Conventional Commits

Commits follow [Conventional Commits](https://www.conventionalcommits.org/) with scoping:

- `feat(scope): description` - Core features or Docs content
- `fix(scope): description` - Core patches or Docs corrections

Examples:

```
feat(core-plugins): add abbreviations plugin
feat(docs-accessmap): add user manual page
fix(core-util): fix nav generator logic
fix(docs-walksheds): fix typo
```

### Branch Naming

Follow GitHub flow with structured branch names:

**Format**: `type/scope/<work-item-number>-short-description`

**Examples**:

```
feat/core-plugins/1234-add-abbreviations-plugin
feat/docs-accessmap/1024-add-user-manual-page
fix/core-util/9876-fix-nav-generator-logic
fix/docs-walksheds/2048-fix-typo
```

### Pull Request & Release Process

1. Create a feature branch following the naming convention
2. Make commits using conventional commit format
3. Open a pull request to `main`
4. Upon merge to `main`, releases are automated

## Critical Developer Workflows

**IMPORTANT**: This project uses a Python virtual environment (`.venv/`) for dependency isolation. **Always activate the virtual environment before running any commands** (including `zensical serve`, utility scripts, etc.):

```powershell
# Activate the virtual environment (run from repository root)
.\.venv\Scripts\Activate.ps1
```

You'll know the venv is activated when you see `(.venv)` at the beginning of your PowerShell prompt.

### Build & Preview Local Site

```powershell
# First time only: create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the local development server (venv must be activated)
zensical serve  # http://localhost:8000

# Deactivate when done
deactivate
```

**Note**: The `.venv/` directory is excluded from git and should not be committed.

### Regenerate Navigation After Adding Files

```powershell
# Ensure venv is activated first!
.\.venv\Scripts\Activate.ps1

cd utilities
.\generate-guides-lists.ps1        # Auto-generates index.md in guides/ directories
.\generate-nav.ps1                 # Updates zensical.toml nav section directly
```

**Why**: Navigation structure and guide indices aren't hand-maintained. These scripts parse `/docs` structure, extract frontmatter titles, and generate the Markdown files accordingly. Generation of the nav section of `zensical.toml` is done afterwards to ensure all files are included.

### Process Screenshots

The `process-screenshot.py` utility generates themed light/dark variants of screenshots with borders and drop shadows, saved as maximally-compressed lossless PNGs:

```powershell
# Ensure venv is activated first!
..\.venv\Scripts\Activate.ps1

# Process a single screenshot
python .\utilities\process-screenshot.py docs\resources\images\example\screenshot.png

# Process all images in a directory (optionally --recurse for subdirs)
python .\utilities\process-screenshot.py docs\resources\images\example\

# Apply a named custom profile
python .\utilities\process-screenshot.py screenshot.png --profile uw-purple

# Regenerate existing output files
python .\utilities\process-screenshot.py screenshot.png --overwrite
```

**Output**: For each input `image.png`, produces `image-light.png` (dark border + shadow for light pages) and `image-dark.png` (light border + glow for dark pages). Mode-tagged sources (e.g., `image.light.png`) produce only the matching variant.

**Markdown usage**:

```markdown
![Alt text](path/to/image-light.png#only-light)
![Alt text](path/to/image-dark.png#only-dark)
```

Run with `--help` for all options including per-variant color, shadow, and blur overrides.

### Generate Event Reports

Event reports are generated using a modular architecture that supports two event types: **Tasking Manager (TM)** and **AVIV ScoutRoute (ASR)**. Events can be either or both types.

#### Architecture

1. **`generate-event-report.py`** — Orchestrator. Reads event frontmatter, runs the appropriate stats generators, fills section templates, and concatenates intro + sections + outro into a publish-ready `report.md`.
2. **`generate-tm-event-stats.py`** — TM stats generator. Fetches mapping statistics from the Tasking Manager and Overpass APIs, writes `tasking-manager-event-stats.json`.
3. **`generate-asr-event-stats.py`** — ASR stats generator. Fetches workspace data from the Workspaces OSM-like API, writes `aviv-scoutroute-event-stats.json`.
4. **`event-reports/common.py`** — Shared utilities (frontmatter parsing, HTTP helpers, template filling, path helpers, haversine).

#### Report Templates

- `templates/events/event-report-intro.md` — Common report intro (overview, participation)
- `templates/events/event-report-outro.md` — Common report outro (impact, acknowledgments)
- `templates/events/event-report-tm-section.md` — TM activity section
- `templates/events/event-report-asr-section.md` — ASR activity section

```powershell
# Ensure venv is activated first!
.\.venv\Scripts\Activate.ps1

# Generate a complete event report (reads frontmatter, fetches stats, fills template):
python .\utilities\generate-event-report.py --event olympia-connected

# Re-generate report using cached stats (skip all API calls):
python .\utilities\generate-event-report.py --event olympia-connected --skip-stats

# Skip only TM or ASR stats (when event has both):
python .\utilities\generate-event-report.py --event my-event --skip-tm-stats
python .\utilities\generate-event-report.py --event my-event --skip-asr-stats

# Run TM stats generator directly:
python .\utilities\event-reports\generate-tm-event-stats.py --event mny26

# Run ASR stats generator directly:
python .\utilities\event-reports\generate-asr-event-stats.py --event nda-vancouver
```

**Orchestrator options** (`generate-event-report.py`):

- `--event <slug>`: Event folder name under `docs/events/` (required)
- `--skip-stats`: Skip all stats generators (use existing JSON files)
- `--skip-tm-stats`: Skip TM stats generator only
- `--skip-asr-stats`: Skip ASR stats generator only
- `--output` / `-o`: Override output path for final `report.md`
- Pass-through args: `--skip-overpass`, `--overpass-url`, `--aoi-file`, `--tasks-file`, `--pad-before`, `--pad-after` (forwarded to TM stats generator); `--osm-file`, `--api-key-env-var` (forwarded to ASR stats generator)

**TM stats generator options** (`generate-tm-event-stats.py`):

- `--event <slug>`: Event folder name (required); reads `tm_project`, `tm_event_start`, `tm_event_end`, `tm_bbox` from frontmatter
- `--aoi-file` / `--tasks-file`: Local GeoJSON files for the TM project
- `--output` / `-o`: Override output path
- `--json`: Also print JSON to console
- `--ultra`: Print Overpass visualization queries
- `--skip-overpass`: Skip Overpass query (TM task stats only)
- `--overpass-url`: Pin a specific Overpass server
- `--pad-before` / `--pad-after`: Hours of padding around event window

**ASR stats generator options** (`generate-asr-event-stats.py`):

- `--event <slug>`: Event folder name (required); reads `asr_workspace_id`, `asr_workspace_env` from frontmatter
- `--osm-file`: Load OSM XML from file instead of API
- `--api-key-env-var`: Override the TDEI API key environment variable name
- `--output` / `-o`: Override output path
- `--json`: Also print JSON to console

**Event frontmatter**: Each event's `index.md` must include frontmatter with event type flags and prefixed properties:

- **Required**: `tasking_manager_event` (true/false), `aviv_scoutroute_event` (true/false)
- **Common** (unprefixed): `event_name`, `event_date`, `event_time_range`, `event_format`, `event_location`, `target_area`, `organizers`, `event_purpose`, `participant_count`
- **TM** (tm\_ prefix, when `tasking_manager_event: true`): `tm_project`, `tm_project_name`, `tm_event_start`, `tm_event_end`, `tm_bbox`, `tm_geographic_coverage`
- **ASR** (asr\_ prefix, when `aviv_scoutroute_event: true`): `asr_workspace_id`, `asr_workspace_env`, `asr_workspace_name`, `asr_event_start`, `asr_event_end`, `asr_target_area`, `asr_route_description`, `asr_route_distance`, `asr_route_links`, `asr_api_key_env_var`

**Generated artifacts** (per event directory):

- `tasking-manager-event-stats.json` / `aviv-scoutroute-event-stats.json` — Stats JSON
- `tasking-manager-event-report.md.part` / `aviv-scoutroute-event-report.md.part` — Section fragments
- `report.md` — Final concatenated report

### Validate Links

```powershell
# Ensure venv is activated first!
.\.venv\Scripts\Activate.ps1

cd utilities
.\check-links.ps1                   # Check internal + external links
.\check-links.ps1 -internal         # Internal only
.\check-links.ps1 -external         # External only
.\check-links.ps1 -external -NoCache # Force fresh external link checks
```

**Performance features**: External link results are cached for 12 hours (in `.link-cache.json`) and checked in parallel with domain throttling. Use `-NoCache` to bypass the cache when needed.

### Run All Utilities

The `run-utils.ps1` script provides an automated workflow to validate and run all utilities:

```powershell
# Ensure venv is activated first!
.\.venv\Scripts\Activate.ps1

cd utilities
.\run-utils.ps1                     # Run all tests, then all utilities
.\run-utils.ps1 -TestsOnly          # Run only Pester tests
.\run-utils.ps1 -SkipLinkCheck      # Skip external link checker in Phase 2
.\run-utils.ps1 -NoCache            # Force fresh external link checks (bypass cache)
.\run-utils.ps1 -SkipTests          # Skip tests (not recommended)
```

**Note**: `-SkipLinkCheck` and `-NoCache` are mutually exclusive.

**Why**: This script ensures all utilities are tested before running, then executes them in the correct order: `generate-guides-lists.ps1` → `generate-nav.ps1` → `check-links.ps1`. It's the recommended way to update the entire documentation structure.

### Run Pester Tests

Utility scripts have Pester test suites for validation:

```powershell
cd utilities
.\run-utils.ps1 -TestsOnly           # Run all tests (recommended)

# Or run individual test files:
Invoke-Pester .\run-utils.Tests.ps1 -Output Minimal # Test utility runner
Invoke-Pester .\generate-guides-lists.Tests.ps1 -Output Minimal # Test guides lists generator
Invoke-Pester .\generate-nav.Tests.ps1 -Output Minimal # Test nav generator
Invoke-Pester .\check-links.Tests.ps1 -Output Minimal # Test link checker
Invoke-Pester .\check-links.Tests.ps1 -ExcludeTag "Network" -Output Minimal # Skip network tests
```

**Note**: Pester v5+ is required. Install with: `Install-Module -Name Pester -Force -SkipPublisherCheck`

## Project-Specific Conventions

### Markdown Conventions

1. **Guide Tags**:
    - Use `- Guide` tag for regular guide pages
    - Use `- User Manual` tag for user manual index files (e.g., `user-manual/index.md`)
    - Use `- Tutorial` tag for tutorial guides (short tutorials focused on specific goals or use cases)
2. **Other Tags**: Use additional tags for filtering; supported tags: "OSW 0.2", "OSW 0.3", "OSW 0.4", "Internal", "External", "Developer", "User"
3. **Abbreviations**: Wrap acronyms normally (e.g., "OSW", "TDEI", "JOSM"); abbreviations plugin auto-links them

### Frontmatter Title Pattern

Always include frontmatter titles to override auto-generated names:

```yaml
---
title: Actual Display Title
tags:
    - Guide
    - OSW 0.3
    - External
    - User
---
```

Or for user manuals:

```yaml
---
title: Product User Manual
tags:
    - User Manual
    - External
    - User
---
```

Or for tutorials:

```yaml
---
title: "Accomplish Specific Task"
tags:
    - Tutorial
    - External
    - Developer
---
```

**Tags**: Tags are used for categorizing pages. The audience is tagged across two axes: Internal-vs-External and Developer-vs-User. "External" implies suitability for "Internal" audiences as well, and "User" implies suitability for "Developer" audiences as well. These are explicitly _not_ access restrictions; all content is accessible to all users.

**Exception**: `docs/index.md` has its title commented out to prevent "TCAT Wiki - TCAT Wiki" duplication.

**Custom Page Ordering with nav_order**: By default, pages within a directory are sorted alphabetically. To specify a custom order, add the `nav_order` frontmatter property with an integer value. Pages with `nav_order` are sorted by their value (ascending, lower numbers first), followed by pages without `nav_order` (sorted alphabetically). This ordering is local to each directory and applies consistently across navigation structure, parent guides sections, and the main guides list.

**Implementation note**: `nav_order` is implemented in two layers. (1) `nav-item.html` sets `style="order: N"` on each `<li>` and `extra.css` makes `.md-nav__list` a flex container — this produces the correct **visual** order. (2) `extra.js` (`sortNavByOrder`) reads those `style.order` values and reappends DOM nodes in sorted order, so **screen readers and keyboard tab navigation** also follow the intended sequence (satisfying WCAG SC 1.3.2 and SC 2.4.3). Both layers are required; neither alone is sufficient.

Example of ordered pages in a user manual:

```yaml
---
title: Introduction
tags:
    - Guide
nav_order: 1
---
```

```yaml
---
title: Getting Started
tags:
    - Guide
nav_order: 2
---
```

Pages without `nav_order` will appear after all ordered pages, sorted alphabetically.

**Excluding Guides from Guides Lists**: By default, guides appear in both their parent page's guides list and in the main guides list. You can control where each guide appears using frontmatter flags (YAML comments, invisible on the built page):

To exclude a guide from its parent's guides section:

```yaml
---
title: Your Guide Title
tags:
    - Guide
# exclude-from-parent-guides-list
---
```

To exclude a guide from the main guides list:

```yaml
---
title: Your Guide Title
tags:
    - Guide
# exclude-from-main-guides-list
---
```

Both flags can be used together to exclude a guide from all guides lists.

**User Manuals**: Pages tagged with `- User Manual` are treated as guides but handled specially:

- They appear as single entries in parent guides sections (not as section headers)
- In the main guides list, only the user manual itself appears, not its subpages
- Their subpages (e.g., `workspace-settings.md`) appear only in the user manual's own `## Guides` section
- The `index.md` must always begin its first prose sentence with "This user manual..."
- Subpages must always begin their first prose sentence with "This section..."

**Tutorials**: Pages tagged with `- Tutorial` are treated as guides (implies Guide) but handled specially:

- They are short tutorials focused on specific goals or use cases, typically linking to user manuals for details
- They appear first in guides sections under a "Tutorials" subsection header, before user manuals and regular guides
- May be single files or multi-page directories (with `index.md` tagged `- Tutorial`)
- Single-file tutorials may live directly in a topic directory or in a `tutorial/` subdirectory
- Multi-page tutorials may live in a `tutorial/` subdirectory or as direct children of any directory (e.g., `topic/tutorial/example/index.md` + subpages, or `topic/my-tutorial/index.md` + subpages)
- Multi-page tutorials are treated like user manuals: only the index appears in parent/main listings; subpages appear only in the tutorial's own Table of Contents
- The `tutorial/` subdirectory is scanned automatically for both single files and multi-page directories; its contents are attributed to the parent directory
- Multi-page tutorial pages get "### Table of Contents" instead of "### Guides"
- Ordering at every level is: Tutorials → User Manuals → Regular Guides
- Single-file tutorials must always begin their first prose sentence with "This tutorial..."
- Multi-page tutorial `index.md` must always begin its first prose sentence with "This tutorial..."
- Multi-page tutorial subpages must always begin their first prose sentence with "This section..."

### Organization

- **accessmap**: AccessMap documentation and guides
- **aviv-scoutroute**: AVIV ScoutRoute mobile app user manual and quest definition guides
- **josm**: JOSM configuration guides for Workspaces editing
- **opensidewalks**: OpenSidewalks schema guides (organized in `schema/` and `tasking-manager/` subtopics)
- **rapid**: Rapid editor documentation
- **tdei**: TDEI platform documentation (organized in `portal/` and `tdei-core/` subtopics)
- **tdei-walkshed**: TDEI Walkshed tool documentation
- **workspaces**: Workspaces editing platform guides
- **resources**: Images and stylesheets (no content pages)
- **local-storage/**: Directory ignored by git, used as a storage target for temporary local files
- **utilities**: Utilities and scripts to make editing this Wiki easier

## Integration Points & Dependencies

### Customizations

- **Theme**: Custom CSS in `/resources/stylesheets/` (ensure file exists before editing)
- **Overrides**: `/overrides/partials/` extends Zensical templates (head.html, extra.html)

## When Adding New Content

1. **Create**: Add `.md` file in appropriate `/docs/[topic]/` subtree
2. **Frontmatter**: Include `title:`, and `tags:` if it's a guide
3. **Links**: Reference guides-list and use relative paths
4. **Regenerate Navigation**: Run `.\generate-nav.ps1` from `utilities/`
5. **Verify Build**: Run `zensical serve` locally before committing

## Assistant Role

**For Guide Content**: The human editor is responsible for writing the substantive content of guides. The AI assistant's role is to:

- Help with **formatting and structure** (headings, lists, code blocks, links)
- **Review and suggest improvements** to clarity, tone, and organization
- **Check logic and consistency** across the documentation
- **Ensure compliance** with project conventions (frontmatter, tags, abbreviations, etc.)
- **Proofread** for grammar and spelling

**The assistant should NOT write the core guide content itself!** Guides must reflect the knowledge and perspective of subject matter experts and domain authors.

Planning documents, temporary files, and the like should be saved into local-storage/ by default, unless otherwise instructed.

### Working With Non-Markdown Source Files

`markitdown` (installed in the venv) converts binary and proprietary formats to Markdown so the assistant can read and work with them. Use it whenever the user references a PDF, Word doc, PowerPoint, or other non-Markdown file:

```powershell
# Activate venv first, then:
python -c "from markitdown import MarkItDown; r = MarkItDown().convert('path/to/file'); print(r.text_content)"
```

Supported formats include: PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, and ZIP archives. Google Docs/Slides/Sheets work if exported as DOCX/PPTX first.

For large files or batch conversion, write the output to `local-storage/` as a `.md` file and read it from there.

## Resources

### Zensical Documentation

Refer to the official Zensical documentation, which is hosted online at https://zensical.org/, as an authoritative source.

### Key Files for Reference

- `zensical.toml`: Main config; nav section auto-updated by scripts
- `utilities/run-utils.ps1`: Master utility runner - tests and runs all utilities in sequence
- `utilities/run-utils.Tests.ps1`: Pester tests for utility runner
- `utilities/generate-guides-lists.ps1`: Creates guide index markdown files
- `utilities/generate-guides-lists.Tests.ps1`: Pester tests for guides lists generator
- `utilities/generate-nav.ps1`: Builds TOML navigation tree from file structure
- `utilities/generate-nav.Tests.ps1`: Pester tests for nav generator
- `utilities/check-links.ps1`: PowerShell validation of links (not standard CI integration)
- `utilities/check-links.Tests.ps1`: Pester tests for link checker
- `utilities/process-screenshot.py`: Generates themed light/dark screenshot variants with borders, shadows, and maximum lossless PNG compression
- `utilities/generate-event-report.py`: Orchestrator — reads frontmatter, runs stats generators, fills templates, writes report
- `utilities/event-reports/generate-tm-event-stats.py`: TM stats generator — fetches Tasking Manager/Overpass statistics, writes JSON
- `utilities/event-reports/generate-asr-event-stats.py`: ASR stats generator — fetches Workspaces API data, writes JSON
- `utilities/event-reports/common.py`: Shared utilities for event report scripts (frontmatter, HTTP, templates)
- `templates/events/event-report-intro.md`: Common report intro template
- `templates/events/event-report-outro.md`: Common report outro template
- `templates/events/event-report-tm-section.md`: TM activity section template
- `templates/events/event-report-asr-section.md`: ASR activity section template
- `templates/events/index.md`: Event page template with full frontmatter schema
- `.github/instructions/content-style.instructions.md`: Editorial style guide for docs content under `docs/`
- `templates/content/README.md`: Golden sample overview for docs page types
- `templates/content/topic-index.md`: Golden sample for topic landing pages
- `templates/content/tutorial.md`: Golden sample for single-page tutorials
- `templates/content/user-manual-index.md`: Golden sample for user manual index pages
- `templates/content/subpage.md`: Golden sample for tutorial and user manual subpages
- `/includes/abbreviations.md`: Global acronym definitions
- `/resources/stylesheets/extra.css`: Theming
