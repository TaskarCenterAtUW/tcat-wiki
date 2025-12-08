<!-- @format -->

# TCAT Wiki - AI Coding Agent Instructions

## Project Overview

**TCAT Wiki** is a Material for MkDocs-based documentation site for the Taskar Center for Accessible Technology (TCAT). It hosts information, guides, and resources related to TCAT's transportation accessibility projects: **OpenSidewalks** (OSW), **Transportation Data Exchange Initiative** (TDEI), and **AccessMap**.

## Architecture & Key Concepts

### Single-Source Documentation Site

-   **Framework**: Material for MkDocs (`mkdocs.yml` orchestrates everything)
-   **Content**: Markdown files in `/docs` structured by topic
-   **Navigation**: Auto-generated from directory structure via PowerShell scripts
-   **Custom Extensions**: YAML frontmatter titles, abbreviations auto-linking, custom CSS theming

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

**Key insight**: Directory hierarchy directly maps to navigation structure. Guides are stored directly in their topic directories (not in nested `guides/` subdirectories). Use `generate-guides-lists.ps1` to auto-generate index files and `generate-nav.ps1` to update the mkdocs.yml navigation structure.

### Abbreviations System

-   `/includes/abbreviations.md` auto-links acronyms site-wide (e.g., OSW, TDEI, JOSM)
-   Add new acronyms here; they're automatically inserted into all `.md` files via MkDocs snippets plugin

## Critical Developer Workflows

### Build & Preview Local Site

This project uses a Python virtual environment (`.venv/`) for dependency isolation.

```powershell
# First time only: create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the local development server
mkdocs serve  # http://localhost:8000

# Deactivate when done
deactivate
```

**Note**: The `.venv/` directory is excluded from git and should not be committed.

### Regenerate Navigation After Adding Files

```powershell
cd util
.\generate-guides-lists.ps1        # Auto-generates index.md in guides/ directories
.\generate-nav.ps1                 # Updates mkdocs.yml nav section directly
```

**Why**: Navigation structure and guide indices aren't hand-maintained. These scripts parse `/docs` structure, extract frontmatter titles, and generate the Markdown files accordingly. Generation of the nav section of `mkdocs.yml` is done afterwards to ensure all files are included.

### Validate Links

```powershell
cd util
.\check-links.ps1                   # Check internal + external links
.\check-links.ps1 -internal         # Internal only
.\check-links.ps1 -verboseOutput    # Detailed output
```

## Project-Specific Conventions

### Markdown Conventions

1. **Guide Link**: Every guide should reference the Guides List (`docs/guides-list/index.md`) via a relative path
2. **Tags**: Use `tags: [Guide, OSW 0.3]` for filtering; supported tags: "Guide", "OSW 0.2", "OSW 0.3", "OSW 0.4"
3. **Abbreviations**: Wrap acronyms normally (e.g., "OSW", "TDEI", "JOSM"); abbreviations plugin auto-links them

### Frontmatter Title Pattern

Always include frontmatter titles to override auto-generated names:

```yaml
---
title: Actual Display Title
tags:
    - Guide
    - OSW 0.3
---
```

**Tags**: Tags, restricted to the allowed tags listed in `mkdocs.yml`, are used for categorizing pages. The intended audience is tagged across two axes: Internal-vs-External and Developer-vs-User. Note that "External" implies that it is suitable for "Internal" audience as well, and that "User" implies that it is suitable for "Developer" audience as well. These are explicitly _not_ access restrictions; external users can access all content.

**Exception**: `docs/index.md` has its title commented out to prevent "TCAT Wiki - TCAT Wiki" duplication.

**Excluding Guides from Guide Lists**: If a guide file should not appear in the generated guides lists (e.g., supplementary guides in subfolders), add a `# skip-in-guides-lists: true` comment to the frontmatter. This YAML comment is invisible on the built page but tells `generate-guides-lists.ps1` to exclude the file:

```yaml
---
title: Supplementary Guide
tags:
    - Guide
# skip-in-guides-lists: true
---
```

**Including Topic Index in Guide Lists**: By default, only topic directories that contain guides (after filtering by `skip-in-guides-lists`) appear in the main guides list. To include a topic index that has no direct guides (e.g., because all guides are skipped or nested), add a `# include-in-guides-lists: true` comment to its index.md frontmatter:

```yaml
---
title: User Manual
tags:
    - Guide
# include-in-guides-lists: true
---
```

### Organization

-   **accessmap**: AccessMap documentation and guides
-   **aviv-scoutroute**: AVIV ScoutRoute mobile app user manual and quest definition guides
-   **josm**: JOSM configuration guides for Workspaces editing
-   **opensidewalks**: OpenSidewalks schema guides (organized in `schema/` and `tasking-manager/` subtopics)
-   **rapid**: Rapid editor documentation
-   **tdei**: TDEI platform documentation (organized in `portal/` and `tdei-core/` subtopics)
-   **tdei-walkshed**: TDEI Walkshed tool documentation
-   **workspaces**: Workspaces editing platform guides
-   **resources**: Images and stylesheets (no content pages)
-   **local-storage/**: Directory ignored by git, used as a storage target for temporary local files
-   **util**: Utilities and scripts to make editing this Wiki easier

## Integration Points & Dependencies

### Material for MkDocs Plugins Active

-   `git-revision-date-localized`: Shows creation/modification dates (UTC-7)
-   `git-committers`: Displays last editor info
-   `social`: Tags for social sharing
-   `search`, `tags`, `meta`, `privacy`
-   Markdown extensions: `pymdownx.snippets`, `pymdownx.superfences`, `admonition`, `attr_list`

### Customizations

-   **Theme**: Custom CSS in `/resources/stylesheets/` (ensure file exists before editing)
-   **Overrides**: `/overrides/partials/` extends Material defaults (head.html, extra.html)

## When Adding New Content

1. **Create**: Add `.md` file in appropriate `/docs/[topic]/` subtree
2. **Frontmatter**: Include `title:`, and `tags:` if it's a guide
3. **Links**: Reference guides-list and use relative paths
4. **Regenerate Navigation**: Run `.\generate-nav.ps1` from `util/`
5. **Verify Build**: Run `mkdocs serve` locally before committing

## Assistant Role

**For Guide Content**: The human editor is responsible for writing the substantive content of guides. The AI assistant's role is to:

-   Help with **formatting and structure** (headings, lists, code blocks, links)
-   **Review and suggest improvements** to clarity, tone, and organization
-   **Check logic and consistency** across the documentation
-   **Ensure compliance** with project conventions (frontmatter, tags, abbreviations, etc.)
-   **Proofread** for grammar and spelling

**The assistant should NOT write the core guide content itself!** Guides must reflect the knowledge and perspective of subject matter experts and domain authors.

Planning documents, temporary files, and the like should be saved into local-storage/ by default, unless otherwise instructed.

## Key Files for Reference

-   `mkdocs.yml`: Main config; nav section auto-updated by scripts
-   `util/generate-nav.ps1`: Builds YAML navigation tree from file structure
-   `util/generate-guides-lists.ps1`: Creates guide index markdown files
-   `util/check-links.ps1`: PowerShell validation of links (not standard CI integration)
-   `/includes/abbreviations.md`: Global acronym definitions
-   `/resources/stylesheets/extra.css`: Theming
