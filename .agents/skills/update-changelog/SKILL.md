---
name: changelog
description: Generate a versioned changelog entry from recent commits and insert it after the inactive Unreleased block
disable-model-invocation: true
---
<!-- @format -->

# Generate Changelog Entry

You are preparing a versioned TCAT Wiki changelog entry from recent git commit history. `CHANGELOG.md` is the sole update-tracking record: its `## Unreleased` section is commented out and must remain untouched. Do not create or use Git tags, GitHub releases, or another version source.

## Step 1 — Collect changes

1. Read `CHANGELOG.md` to identify the most recent versioned entry.
2. Inspect the relevant unrecorded commits with `git log --pretty=format:"%s"`. Do not use `git describe`, `git tag`, release metadata, or another version file.
3. Confirm with the user when the commit range, release version, or intended changelog scope is unclear.

## Step 2 — Build the versioned update

Create a versioned entry using the version and release date provided by the user. Use `### Features` and `### Fixes` headings only when they have entries.

**Inclusion rules:**

- `feat(...):` → **Features**
- `fix(...):` → **Fixes**
- All other types (`chore`, `docs`, `style`, `refactor`, `ci`, version-bump commits, merge commits) → **omit**

**Writing rules:**

- Rewrite terse or cryptic subjects into plain English
- Keep the scope in parentheses if it adds useful context, e.g. `(docs-workspaces)`
- Group closely related commits into a single bullet rather than listing each individually
- Omit the section heading entirely if it would be empty

**Template:**

```markdown
## vX.Y.Z (YYYY-MM-DD)

### Features

- Description of feature one

### Fixes

- Description of fix one
```

## Step 3 — Update CHANGELOG.md

Insert the versioned entry immediately after the commented-out `## Unreleased` block and before the most recent existing versioned entry. Preserve the commented block and all existing release entries. Do not create a Git tag or GitHub release.

## Step 4 — Report back

After editing `CHANGELOG.md`, respond with:

1. The versioned entry added
2. Any commits omitted under the inclusion rules
3. Any commits that appear miscategorized — where the `feat`/`fix` type conflicts with the described change
