---
name: insert-image
description: Process a source screenshot into themed variants and insert accessible Markdown image links at the active selection or cursor
disable-model-invocation: true
---

<!-- @format -->

# Insert a Processed Screenshot

Use this skill when the user supplies an absolute path to a source screenshot and wants
the processed image Markdown inserted into the active Markdown file.

## Input contract

- The user message must provide one absolute source-image path.
- The active file is the Markdown document receiving the insertion.
- Replace the active selection. If there is no selection, insert after the cursor
  line.
- The processor replaces non-AVIF source files with lossless AVIF after successful output.
- Do not modify unrelated document content.

## Validate the source

Inspect the filename only. If it matches
`.*-(?:dark|light)\.avif$`, stop and respond exactly:

```text
Invalid input: provide the original source image, not an already-processed variant.
```

Otherwise, continue. Do not add rejection criteria.

## Determine source files and outputs

Let:

- `dir` be the input directory.
- `stem` be the filename without its extension and without an optional `.dark`
  or `.light` source-mode suffix.

Use `Test-Path` before relying on a companion source file.

| Input              | Process            | Expected output                                            |
| ------------------ | ------------------ | ---------------------------------------------------------- |
| `{stem}.png`       | `{stem}.png`       | `{stem}.avif`, `{stem}-light.avif`, and `{stem}-dark.avif` |
| `{stem}.dark.png`  | `{stem}.dark.png`  | `{stem}.dark.avif` and `{stem}-dark.avif`                  |
| `{stem}.light.png` | `{stem}.light.png` | `{stem}.light.avif` and `{stem}-light.avif`                |

For a mode-tagged input, find the source for the missing output mode in this
order:

1. The corresponding mode-tagged companion (`{stem}.light.png` or
   `{stem}.dark.png`).
2. The mode-generic companion (`{stem}.png`).
3. If neither exists, do not generate or insert the missing-mode variant.

## Process each selected source

From the repository root, activate the project virtual environment and run the
processor once per selected source:

```powershell
.\.venv\Scripts\Activate.ps1; python utilities\process_screenshot.py "<source-image-path>" --overwrite
```

Confirm every expected output file exists after processing. If processing fails
or an expected output is absent, surface the error and do not insert broken
Markdown.

## Write useful alt text

Inspect the original input image and nearby document context. Produce one
concise alt-text string that communicates the image's relevant information.

- Describe the image's purpose or result, not incidental colors or layout.
- Do not repeat nearby prose or begin with “Image of” or “Screenshot of.”
- Use empty alt text only when the image is purely decorative.

Use the same alt text for both themed variants.

## Insert Markdown

Compute each generated image path relative to the active file's directory.
Use forward slashes in Markdown paths, including on Windows.

For example, an image at
`docs\resources\images\example\nested\data-viewer-light.avif` inserted into
`docs\example\nested\test.md` uses:

```text
../../resources/images/example/nested/data-viewer-light.avif
```

Replace the selection, or insert after the cursor line, with only the variants
that exist, in this order:

```markdown
![{alt text}]({relative-light-path}#only-light)
![{alt text}]({relative-dark-path}#only-dark)
```

Do not add a blank line unless one is needed to preserve valid surrounding
Markdown.

## Final check

Before responding, verify that:

1. The inserted paths resolve to generated files.
2. Each inserted variant has the correct `#only-light` or `#only-dark` fragment.
3. No line was inserted for a missing variant.
4. The replacement affected only the active selection or cursor location.
