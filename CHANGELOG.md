<!-- @format -->

# Changelog

Changes to the TCAT Wiki are documented here.

This project adheres to [Semantic Versioning](https://semver.org/) and
[Conventional Commits](https://www.conventionalcommits.org/).

## v11.8.1 (2026-04-22)

### Fixes

- **Core**: Fix `nav_order` keyboard/screen-reader focus order.
    - Details: _The CSS `order` property was already correcting the visual sequence, but DOM order (which screen readers and keyboard tab navigation follow) remained alphabetical. A new `sortNavByOrder` function in `extra.js` reads each item's `style.order` value and reappends DOM nodes in sorted order after every navigation event, aligning reading/focus order with visual order (WCAG SC 1.3.2, SC 2.4.3)._
- **Core**: Update padding on breadcrumbs and left sidebar sections to prevent clipping of keyboard focus ring

## v11.8.0 (2026-04-21)

### Features

- **Core**: Add insert-image prompt

## v11.7.0 (2026-04-20)

### Features

- **Docs**: Update image paths; replace outdated screenshots

### Fixes

- **Docs**: Reorganize TDEI Portal images into `images/tdei/portal/` subdirectory structure

## v11.6.0 (2026-04-17)

### Features

- **Docs**: Refresh the Workspaces section

## v11.5.1 (2026-04-16)

### Fixes

- **(Core)**: Improve build-and-deploy workflow

## v11.5.0 (2026-04-16)

### Features

- **Core**: Add Google Analytics with cookie consent dialog
- **Core**: Add footer "Change cookie settings" link, relocated after the "Made with Zensical" credit

### Fixes

- **Core**: Fix vertical alignment of checkbox list item text

## v11.4.1 (2026-04-15)

### Fixes

- **Core**: Fix top-of-page padding
- **Core**: Clean up `extra.css`

## v11.4.0 (2026-04-07)

### Features

- **Docs**: Add WAGISA abbreviation

### Fixes

- **Docs**: Remove misleading "(PDF)" label from the Jurisdiction Snapshot link on the home page
- **Docs**: Remove TDEI architecture chart from the home page

## v11.3.0 (2026-04-03)

### Features

- **Docs**: Add tip in the TDEI Portal Datasets page explaining that the Dataset filter returns all partial matches, not just exact matches, with a visual example

### Fixes

- **Docs**: Improve alt text on TDEI Portal Datasets page images for better accessibility

## v11.2.0 (2026-04-03)

### Features

- **Docs**: Add dataset name suffix reference with table, examples, and visual guide to OS-CONNECT documentation

## v11.1.0 (2026-04-02)

### Features

- **Core**: Add GitHub repo link and view/edit page action buttons; repositioned into the right sidebar "On this page" header to keep them accessible but visually unobtrusive

## v11.0.0 (2026-03-30)

### Features

- **Core**: Add changelog
