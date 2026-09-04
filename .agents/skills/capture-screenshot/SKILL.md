---
name: capture-screenshot
description: Capture light and dark browser-page screenshots for TCAT Wiki documentation at the standard 1440x810 viewport, save *.light.png and *.dark.png sources, process them into themed AVIF variants, and insert the accessible Markdown image pair.
argument-hint: "Optional: page title, basename, guide, or screenshot focus"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Capture themed screenshots

Capture the intended shared browser page in both its light and dark page themes, save source images, generate themed AVIF variants, and insert accessible Markdown links.

## Before capture

1. Use the active shared page unless another tab/URL is named. Confirm title, URL, product, route, and state.
2. Use the active Markdown selection/cursor under `docs/`; otherwise ask for the file/location.
3. Derive `docs/resources/images/<product>/<guide-or-page>/` and a descriptive lowercase kebab-case basename from the guide's numbering pattern. Ask when unclear.
4. Never capture credentials, private/personal data, unpublished content, or unrelated browser content. Dismiss transient UI only if it does not change the documented state. Do not change product data. Do not overwrite without explicit authorization.

## Capture standard and themes

Use CSS viewport `1440` × `810`, DPR `1`, landscape, viewport-only capture. In Firefox use `F12`, `Ctrl`+`Shift`+`M`, and `[Screenshot] Web - Landscape`; keep DevTools out of the image. Automation must verify before saving:

```javascript
await page.setViewportSize({ width: 1440, height: 810 });
const m = await page.evaluate(() => ({
    width: innerWidth,
    height: innerHeight,
    dpr: devicePixelRatio,
}));
if (m.width !== 1440 || m.height !== 810 || m.dpr !== 1)
    throw new Error(
        `Expected 1440x810 at DPR 1; received ${JSON.stringify(m)}.`
    );
```

If the standard cannot be met, stop and ask for the correct responsive profile/capture. Inspect the source; reject browser chrome, clipping, tiling, unintended scrollbars, loading states, or other artifacts.

Capture both themes while keeping the page state identical:

1. Find the page's visible theme control, if it exists. Select **Light** (or its equivalent), verify that the page—not only the browser—uses the light theme, and save `<basename>.light.png`.
2. Select **Dark**, verify the page theme changed, and save `<basename>.dark.png`.
3. If the page has no theme control, cannot confirm the selected theme, or changing theme changes the documented state, stop and ask the user. Do not substitute browser or operating-system appearance without confirmation.
4. If an existing source or output would be replaced, stop unless the user explicitly authorized replacement.

Use the same viewport and screenshot checks for both captures. Do not save a generic `<basename>.png` when capturing separate page themes.

## Save and process

1. Inspect neighboring files, create the destination directory, and save `<basename>.light.png` and `<basename>.dark.png` under `docs/resources/images/...`; never write to `site/`, `human-docs/`, or `agent-docs/`.
2. From the repository root, activate the environment and process both mode-tagged sources:

    ```powershell
    .\.venv\Scripts\Activate.ps1; python utilities\process_screenshot.py "<basename>.light.png" "<basename>.dark.png"
    ```

    With authorized replacement only, add `--overwrite`. Mode-tagged processing produces `<basename>.light.avif`, `<basename>-light.avif`, `<basename>.dark.avif`, and `<basename>-dark.avif`, then removes the PNG sources. Use only `<basename>-light.avif` and `<basename>-dark.avif` in page content. If processing/output validation fails, do not edit Markdown.

## Insert and verify

Insert immediately after the supporting step, replacing only a matching placeholder/selection. Compute a relative forward-slash path, preserve indentation/attributes, and do not insert the lossless source:

```markdown
![<alt text>](<relative-path>/<basename>-light.avif#only-light)
![<alt text>](<relative-path>/<basename>-dark.avif#only-dark)
```

Use identical concise alt text naming the visible screen and relevant focus/outcome; do not begin `Image of`/`Screenshot of`, describe incidental colors/layout, use empty alt text for informative images, or duplicate an existing pair.

Confirm page/state, viewport/DPR, visual quality, valid AVIF outputs, resolving links, correct fragments/order, equivalent alt text, and only intended files changed. Never edit generated output or `docs/assistant/dispatch.md`. For a new/moved guide, run guide-list/navigation generators; otherwise use the narrowest relevant image/link check. Report page title/URL, final paths, changed Markdown file, and limitations. Do not claim success if capture verification failed.
