---
name: update-changelog
description: Generate a versioned changelog entry from recent commits and insert it after the inactive Unreleased block
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Update the changelog

`CHANGELOG.md` is the sole update-tracking record. Its commented `## Unreleased` block must remain untouched; do not create/use tags, releases, or another version source.

## Collect and classify

1. Read `CHANGELOG.md` and identify the newest versioned entry.
2. Inspect the relevant unrecorded commits with `git log --pretty=format:"%s"`; do not use `git describe`, tags, release metadata, or another version file. Ask when the range, version, release date, or scope is unclear.
3. Use the user-provided version/date. Classify updates as **Added**, **Fixed**, or **Changed**. Omit version-bump and merge commits.
4. Rewrite cryptic subjects in plain English, retain useful scopes, group related commits, omit empty headings, and keep each bullet's main line to one line. Add minimal indented `Details: _..._` lines for necessary extra detail.

Use this shape:

```markdown
## vX.Y.Z (YYYY-MM-DD)

### Added

- **Scope**: Description

### Changed

- **Scope**: Description

### Fixed

- **Scope**: Description
    - Details: _Additional detail_
```

## Edit and report

Insert the entry immediately after the commented Unreleased block and before the newest existing version. Preserve all other content. Report the entry added, commits omitted by the rules, and any apparent type/description miscategorizations.
