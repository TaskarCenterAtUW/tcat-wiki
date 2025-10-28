<!-- @format -->

# TCAT Wiki - AI Coding Agent Instructions

## Project Overview

**TCAT Wiki** is a Material for MkDocs-based documentation site for the Taskar Center for Accessible Technology (TCAT). It hosts information, guides, and resources related to TCAT's transportation accessibility projects: **OpenSidewalks** (OSW), **Transportation Data Exchange Initiative** (TDEI), and **AccessMap**.

## Architecture & Key Concepts

### Single-Source Documentation Site

-   **Framework**: Material for MkDocs (`mkdocs.yml` orchestrates everything)
-   **Content**: Markdown files in `/docs` structured by topic (opensidewalks, tdei, about, guides-list)
-   **Navigation**: Auto-generated from directory structure via PowerShell scripts
-   **Custom Extensions**: YAML frontmatter titles, abbreviations auto-linking, custom CSS theming

### Directory Structure Pattern

```
docs/
  [topic]/
    index.md              # Topic overview
    guides/
      index.md            # Auto-generated guide index
      specific-guide.md   # Actual guides
```

**Key insight**: Directory hierarchy directly maps to navigation structure. Nested `guides/` directories are special - use `generate-guides-lists.ps1` to auto-generate index files listing all guides in that directory.

### Abbreviations System

-   `/includes/abbreviations.md` auto-links acronyms site-wide (e.g., OSW, TDEI, JOSM)
-   Add new acronyms here; they're automatically inserted into all `.md` files via MkDocs snippets plugin

## Critical Developer Workflows

### Build & Preview Local Site

```powershell
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin mkdocs-git-committers-plugin-2
pip install "mkdocs-material[imaging]"  # For image optimization
mkdocs serve                            # http://localhost:8000
```

### Regenerate Navigation After Adding Files

```powershell
cd util
.\generate-guides-lists.ps1        # Auto-generates index.md in guides/ directories
.\generate-nav.ps1 -updateMkdocs   # Updates mkdocs.yml nav section directly
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

### Frontmatter Title Pattern

Always include frontmatter titles to override auto-generated names:

```yaml
---
title: Actual Display Title
tags:
    - OSW 0.3
---
```

**Note**: The `"    - Guide"` tag does not need to be added to guides, as that tag is inherited from the `.meta.yml` file in that directory.

**Exception**: `docs/index.md` has title commented out to prevent "TCAT Wiki - TCAT Wiki" duplication.

### Markdown Conventions

1. **Guide Link**: Every guide should reference the [Guides List](../docs/guides-list/index.md) via a relative path
2. **Tags**: Use `tags: [Guide, OSW 0.3]` for filtering; supported tags: "Guide", "OSW 0.2", "OSW 0.3", "OSW 0.4"
3. **Abbreviations**: Wrap acronyms normally (e.g., "OSW", "TDEI"); abbreviations plugin auto-links them

### Organization

-   **opensidewalks**: OpenSidewalks schema explorer and guides, Tasking Manager guides
-   **tdei/consumers**: Documentation and guides for data consumers, including AccessMap and the Walkshed tool
-   **tdei/producers**: Documentation and guides for data producers, including Workspaces editing tools such as AVIV ScoutRoute, Rapid, and JOSM
-   **resources**: No content - stores images and stylesheets
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
2. **Frontmatter**: Include `title:` and `tags:` if it's a guide
3. **Links**: Reference guides-list and use relative paths
4. **Regenerate Navigation**: Run `.\generate-nav.ps1 -updateMkdocs` from `util/`
5. **Verify Build**: Run `mkdocs serve` locally before committing

## Key Files for Reference

-   `mkdocs.yml`: Main config; nav section auto-updated by scripts
-   `util/generate-nav.ps1`: Builds YAML navigation tree from file structure
-   `util/generate-guides-lists.ps1`: Creates guide index markdown files
-   `util/check-links.ps1`: PowerShell validation (not standard CI integration)
-   `/includes/abbreviations.md`: Global acronym definitions
-   `/resources/stylesheets/extra.css`: Theming
