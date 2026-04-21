---
description: Process a screenshot and insert themed image variants at the cursor position
agent: agent
---

<!-- @format -->

The user's message contains an absolute path to a source image. Complete all steps without explanation. Do not apply judgment or reasoning beyond the literal instructions below — follow each step exactly as written.

## Validation

Check the filename (not the full path) against this exact rule: if the filename matches the regex `.*-(?:dark|light)\.png$` (i.e., the stem ends with a hyphen followed by `dark` or `light`), stop immediately and tell the user: "Invalid input: provide the original source image, not an already-processed variant."

Otherwise, proceed unconditionally. Do not invent additional rejection criteria.

## Step 1 — Process the screenshot(s)

The input path may be:

- **Mode-generic** (`example.png`) — a single source used for both themes
- **Mode-tagged dark** (`example.dark.png`) — a dark-UI source screenshot
- **Mode-tagged light** (`example.light.png`) — a light-UI source screenshot

Run the processor from the repo root for each source file that must be processed:

```powershell
.\.venv\Scripts\Activate.ps1; python utilities\process-screenshot.py "<image-path>" --overwrite
```

### Determining which files to process

Let `stem` be the base filename before any mode tag or extension (e.g. `example` for `example.png`, `example.dark.png`, or `example.light.png`). Let `dir` be the input file's directory.

**Case A — mode-generic input (`example.png`)**:
Process `example.png`. This produces `{stem}-light.png` and `{stem}-dark.png`.

**Case B — mode-tagged dark input (`example.dark.png`)**:

1. Process `example.dark.png` → produces `{stem}-dark.png`.
2. Check whether `{dir}\{stem}.light.png` exists:
    - If yes → process `{dir}\{stem}.light.png` → produces `{stem}-light.png`.
    - If no → check whether `{dir}\{stem}.png` exists:
        - If yes → process `{dir}\{stem}.png` → produces `{stem}-light.png`.
        - If no → no `-light.png` output; omit the `#only-light` line from the insertion.

**Case C — mode-tagged light input (`example.light.png`)**:

1. Process `example.light.png` → produces `{stem}-light.png`.
2. Check whether `{dir}\{stem}.dark.png` exists:
    - If yes → process `{dir}\{stem}.dark.png` → produces `{stem}-dark.png`.
    - If no → check whether `{dir}\{stem}.png` exists:
        - If yes → process `{dir}\{stem}.png` → produces `{stem}-dark.png`.
        - If no → no `-dark.png` output; omit the `#only-dark` line from the insertion.

Use `Test-Path` to check for file existence before deciding which files to process.

## Step 2 — Generate alt text

Call `view_image` on the original input image. Write one concise line of alt text that:

- Meets web accessibility criteria and follows alt text best practices
- Conveys the information the image communicates in context — not just a visual description
- Does not repeat text already present in the surrounding document
- Omits irrelevant visual detail (colors, layout, decorative elements)

## Step 3 — Insert into the active file

Compute the relative path from `${file}`'s directory to each output image using forward slashes.

Example: input `…\docs\resources\images\example\nested\data-viewer.png`, active file `…\docs\example\nested\test.md` → `../../resources/images/example/nested/data-viewer-light.png`

Replace `${selection}` using `replace_string_in_file` with exactly the lines that were produced — include the `#only-light` line only if a `-light.png` was generated, and the `#only-dark` line only if a `-dark.png` was generated:

```
![{alt text}]({relative-light-path}#only-light)
![{alt text}]({relative-dark-path}#only-dark)
```

If there is no selection, insert after the cursor line.
