---
name: capture-screenshot
description: Capture 1440x900 browser screenshots for TCAT Wiki, using light/dark pairs when supported or one as-is source otherwise, and process them into accessible AVIF links.
argument-hint: "Optional: page title, basename, guide, or screenshot focus"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Capture themed screenshots

Capture the intended shared browser page, process its source image(s) into AVIF variants, and insert accessible Markdown links.

## Before capture

1. Use the active shared page unless another tab/URL is named. Confirm title, URL, product, route, and state.
2. Use the active Markdown selection/cursor under `docs/`; otherwise ask for the file/location.
3. Derive `docs/resources/images/<product>/<guide-or-page>/` and a descriptive lowercase kebab-case basename from the guide's numbering pattern. Ask when unclear.
4. Never capture credentials, private/personal data, unpublished content, or unrelated browser content. Dismiss transient UI only if it does not change the documented state. Do not change product data. Do not overwrite without explicit authorization.

## Capture standard and themes

Use CSS viewport `1440` × `900`, DPR `1`, landscape, viewport-only capture. In Firefox use `F12`, `Ctrl`+`Shift`+`M`, and `[Screenshot] Web - Landscape`; keep DevTools out of the image. Automation must verify before saving:

```javascript
await page.setViewportSize({ width: 1440, height: 900 });
const m = await page.evaluate(() => ({
    width: innerWidth,
    height: innerHeight,
    dpr: devicePixelRatio,
}));
if (m.width !== 1440 || m.height !== 900 || m.dpr !== 1)
    throw new Error(
        `Expected 1440x900 at DPR 1; received ${JSON.stringify(m)}.`
    );
```

If the standard cannot be met, stop and ask for the correct responsive profile/capture. Inspect the source; reject browser chrome, clipping, tiling, unintended scrollbars, loading states, or other artifacts.

- **Site has app-level light/dark controls:** capture both modes. Keep the route, data, layout, scroll position, and viewport identical; the app theme must be the only difference. Select **Light** (or its equivalent), verify the page—not only the browser—uses the light theme, and save `<basename>.light.png`. Then select **Dark**, verify the page theme changed and the content/state did not, and save `<basename>.dark.png`.
- **Site has no app-level theme control:** capture it once as displayed to `<basename>.png`, without a light/dark suffix. The processing utility will derive both Wiki theme variants from that one screenshot.
- **Theme controls exist but the selected mode cannot be confirmed:** stop and ask. Do not substitute browser or operating-system appearance.

Follow the light/dark filename conventions in `CONTRIBUTING.md`. If an existing source or output would be replaced, stop unless the user explicitly authorized replacement.

Do not use a generic source alongside a complete `.light.png`/`.dark.png` pair; the utility skips the generic source when both tagged siblings exist.

## Save and process

1. Inspect neighboring files, create the destination directory, and save the themed pair or single generic source under `docs/resources/images/...`; never write to `site/`, `human-docs/`, or `agent-docs/`.
2. From the repository root, activate the environment and process the source image(s):

    ```powershell
    .\.venv\Scripts\Activate.ps1

    # Site has light/dark controls
    python utilities\process_screenshot.py "<basename>.light.png" "<basename>.dark.png"

    # Site has no theme control
    python utilities\process_screenshot.py "<basename>.png"
    ```

    Add `--overwrite` only when replacement is authorized. A generic source produces `<basename>.avif` plus both `<basename>-light.avif` and `<basename>-dark.avif`; these variants share the original page appearance and differ in Wiki border/shadow treatment. A `.light.png`/`.dark.png` pair produces mode-specific AVIF variants. Non-AVIF sources are removed only after successful processing. Use only the dash-suffixed variants in Markdown, with `#only-light` and `#only-dark`. If processing/output validation fails, do not edit Markdown.

## Insert and verify

Insert immediately after the supporting step, replacing only a matching placeholder/selection. Compute a relative forward-slash path, preserve indentation/attributes, and do not insert the lossless source:

```markdown
![<alt text>](<relative-path>/<basename>-light.avif#only-light)
![<alt text>](<relative-path>/<basename>-dark.avif#only-dark)
```

Use identical concise alt text naming the visible screen and relevant focus/outcome; do not begin `Image of`/`Screenshot of`, describe incidental colors/layout, use empty alt text for informative images, or duplicate an existing pair.

Confirm page/state, viewport/DPR, visual quality, valid AVIF outputs, resolving links, correct fragments/order, equivalent alt text, and only intended files changed. Never edit generated output or `docs/assistant/dispatch.md`. For a new/moved guide, run guide-list/navigation generators; otherwise use the narrowest relevant image/link check. Report page title/URL, final paths, changed Markdown file, and limitations. Do not claim success if capture verification failed.
