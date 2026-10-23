---
name: zensical-page-collage
description: "Capture full-page screenshots of every built Zensical page under a directory and assemble a filename-labeled image collage. Use for documentation page collages, screenshot grids, and visual review of an entire section."
argument-hint: "Source docs directory or built site directory"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Capture a Zensical page collage

Capture every built HTML page in a source documentation directory's corresponding `site/` directory, save individual screenshots and a filename-labeled collage under ignored `local-storage/`, and do not edit source documentation based on the collage.

## Procedure

1. Activate the repository virtual environment and ensure the deploy-parity site is built:

    ```powershell
    .\.venv\Scripts\Activate.ps1
    python utilities\build_site.py --build
    ```

2. Run the [collage capture script](./scripts/capture_collage.py), passing a source directory under `docs/` or its built directory under `site/`:

    ```powershell
    python .agents\skills\zensical-page-collage\scripts\capture_collage.py docs\aviv-scoutroute\user-manual
    ```

    To capture through the running preview or a local static server, pass `--base-url http://127.0.0.1:8000`.

    The default output is `local-storage/page-collages/`; each full-page PNG is named after its built route and theme, and `collage.png` contains the labeled thumbnails in four columns. Use `--theme both` to capture light and dark variants. The script compares light and dark screenshot dimensions in that mode and warns when they differ. It also warns about stale screenshots left in a reused output directory; those files are not included in the new collage. Keep custom output paths outside `docs/`, `site/`, `human-docs/`, and `agent-docs/`. Optional arguments control the site root, output path, local preview URL, viewport, theme, tile width, and collage columns; see `--help`.

3. Open `collage.png` to review that each page is present and legible. If a build, capture, or collage step fails, report the error rather than claiming completion.

The script uses Playwright Chromium with a 1440×900 CSS viewport and DPR 1 by default. It accepts a source directory under `docs/` or a directory in the built site; pass `--site-dir` when the build output is not `site/`. For a running local site, pass its root URL with `--base-url`; the script blocks HTTP(S) requests outside that origin (or all HTTP(S) requests when capturing local built pages). If the palette control does not switch themes within two seconds, the script forces the requested palette and warns; features that depend on blocked external scripts (such as Mermaid rendering) may remain unavailable in screenshots. Visible article images must decode successfully or the capture fails with the affected URL. Playwright and its browser must be installed in the repository environment (`python -m pip install playwright`; `python -m playwright install chromium`). Output is for internal visual review, not publication. This skill captures and arranges screenshots only; it does not assess or alter documentation content.
