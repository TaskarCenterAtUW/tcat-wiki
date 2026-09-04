---
name: insert-image
description: Process a source screenshot into themed variants and insert accessible Markdown image links at the active selection or cursor
argument-hint: "Screenshot filename"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Insert a processed screenshot

Use when the user supplies one absolute or repo-relative source-image path and wants its Markdown inserted into the active Markdown file. The active file receives the replacement at the selection, or insertion after the cursor line. Do not modify unrelated content.

## Validate and resolve sources

Inspect the filename only. If it matches `.*-(dark|light)\.avif$`, respond exactly:

```text
Invalid input: provide the original source image, not an already-processed variant.
```

Otherwise let `dir` be its directory and `stem` its name without extension or optional `.dark`/`.light` suffix. Use `Test-Path` before using companions:

| Input              | Outputs                                                |
| ------------------ | ------------------------------------------------------ |
| `<stem>.png`       | `<stem>.avif`, `<stem>-light.avif`, `<stem>-dark.avif` |
| `<stem>.dark.png`  | `<stem>.dark.avif`, `<stem>-dark.avif`                 |
| `<stem>.light.png` | `<stem>.light.avif`, `<stem>-light.avif`               |

For a mode-tagged input, find the other theme source in this order: matching mode-tagged companion, then generic `<stem>.png`; if neither exists, omit that theme. Apply the same rules for other supported source extensions as appropriate.

## Process

From the repository root, activate the environment and process each selected source once:

```powershell
.\.venv\Scripts\Activate.ps1; python utilities\process_screenshot.py "<source-image-path>" --overwrite
```

Confirm every expected output exists. On failure, report it and do not insert broken Markdown. Non-AVIF sources are replaced by a lossless AVIF after successful processing.

## Write and insert Markdown

Inspect the original image and nearby prose. Use one concise alt-text string for both variants: describe the relevant screen/purpose/outcome, not incidental color/layout; do not begin `Image of` or `Screenshot of`; use empty alt only for decorative images. Compute paths relative to the active file using forward slashes. Insert only existing variants, in this order, without an unnecessary blank line:

```markdown
![<alt text>](<relative-light-path>#only-light)
![<alt text>](<relative-dark-path>#only-dark)
```

Replace only the selection or insert at the cursor. Verify paths resolve, fragments are correct, and only the intended location changed.
