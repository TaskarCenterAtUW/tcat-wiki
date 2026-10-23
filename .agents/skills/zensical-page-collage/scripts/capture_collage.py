from __future__ import annotations

import argparse
import asyncio
import re
import sys
import tempfile
import textwrap
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from PIL import Image, ImageDraw, ImageFont
from playwright.async_api import Error as PlaywrightError
from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from playwright.async_api import Route
from playwright.async_api import async_playwright


def page_label(path: Path, site_root: Path) -> str:
    return path.relative_to(site_root).as_posix()


def wrap_label(text: str, width: int) -> list[str]:
    words = textwrap.wrap(text, width=max(18, width // 8),
                          break_long_words=True, break_on_hyphens=False)
    return words or [text]


def safe_name(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9._-]+", "-", text).strip("-.")
    return text or "page"


def positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a positive integer") from exc
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def url_origin(url: str) -> tuple[str, str, int | None]:
    parsed = urlsplit(url)
    return parsed.scheme.lower(), (parsed.hostname or "").casefold(), parsed.port


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Capture every built Zensical page under a directory and create a labeled screenshot collage."
    )
    parser.add_argument(
        "directory", help="Source docs directory or corresponding built site directory")
    parser.add_argument("--site-dir", type=Path, default=Path("site"),
                        help="Built site root (default: site)")
    parser.add_argument("--output-dir", type=Path,
                        default=Path("local-storage/page-collages"))
    parser.add_argument("--width", type=positive_int,
                        default=1440, help="Screenshot viewport width")
    parser.add_argument("--height", type=positive_int,
                        default=900, help="Screenshot viewport height")
    parser.add_argument("--columns", type=positive_int,
                        default=4, help="Number of collage columns")
    parser.add_argument("--tile-width", type=positive_int,
                        default=480, help="Collage thumbnail width per page")
    parser.add_argument("--theme", choices=("light",
                        "dark", "both"), default="light")
    parser.add_argument(
        "--base-url", help="Optional local site root URL, such as http://127.0.0.1:8000")
    args = parser.parse_args()

    root = Path.cwd().resolve()
    site_root = (args.site_dir if args.site_dir.is_absolute()
                 else root / args.site_dir).resolve()
    docs_root = (root / "docs").resolve()
    source = Path(args.directory)
    if not source.is_absolute():
        source = root / source
    source = source.resolve()
    if not source.is_dir():
        parser.error(f"Directory not found: {source}")
    if source.is_relative_to(site_root):
        pages_root = source
    elif source.is_relative_to(docs_root):
        rel = source.relative_to(docs_root)
        pages_root = site_root / rel
    else:
        parser.error(
            f"Directory must be under {docs_root} or {site_root}: {source}")
    if not pages_root.is_dir():
        parser.error(
            f"Built site directory not found: {pages_root}; run python utilities/build_site.py --build first")
    html_files = sorted(pages_root.rglob("*.html"))
    if not html_files:
        parser.error(f"No built HTML pages found under {pages_root}")

    labels = {html_path: page_label(html_path, site_root)
              for html_path in html_files}
    names: dict[str, str] = {}
    for label in labels.values():
        name = safe_name(label)
        if name in names and names[name] != label:
            parser.error(
                f"Page paths {names[name]!r} and {label!r} map to the same output filename")
        names[name] = label

    themes = ("light", "dark") if args.theme == "both" else (args.theme,)
    expected_screenshots = {
        f"{name}.{theme}.png" for name in names for theme in themes}
    base_url = None
    allowed_origin = None
    if args.base_url:
        parsed_base_url = urlsplit(args.base_url)
        if parsed_base_url.scheme not in {"http", "https"} or not parsed_base_url.netloc:
            parser.error("--base-url must be an absolute HTTP or HTTPS URL")
        if parsed_base_url.query or parsed_base_url.fragment:
            parser.error("--base-url must not include a query or fragment")
        try:
            allowed_origin = url_origin(args.base_url)
        except ValueError as exc:
            parser.error(f"Invalid --base-url: {exc}")
        base_url = f"{args.base_url.rstrip('/')}/"

    output_dir = (args.output_dir if args.output_dir.is_absolute()
                  else root / args.output_dir).resolve()
    protected_directories = (
        docs_root,
        site_root,
        (root / "human-docs").resolve(),
        (root / "agent-docs").resolve(),
    )
    for protected_directory in protected_directories:
        if output_dir.is_relative_to(protected_directory):
            parser.error(
                f"Output directory must not be inside {protected_directory}")
    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[tuple[str, str, Path]] = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            page = await browser.new_page(
                viewport={"width": args.width, "height": args.height}, device_scale_factor=1
            )

            async def restrict_http_requests(route: Route) -> None:
                request = route.request
                if allowed_origin is not None and url_origin(request.url) == allowed_origin:
                    await route.continue_()
                else:
                    await route.abort()

            await page.route("http://**/*", restrict_http_requests)
            await page.route("https://**/*", restrict_http_requests)
            for html_path in html_files:
                label = labels[html_path]
                if base_url:
                    site_path = html_path.relative_to(site_root).as_posix()
                    url = urljoin(base_url, site_path)
                else:
                    url = html_path.as_uri()
                for theme in themes:
                    await page.goto(url, wait_until="networkidle", timeout=60000)
                    reject_cookies = page.get_by_role(
                        "button", name=re.compile(r"reject all", re.IGNORECASE))
                    if await reject_cookies.count() and await reject_cookies.first.is_visible():
                        await reject_cookies.first.click()
                        await page.wait_for_timeout(250)
                    await page.evaluate("document.fonts.ready")
                    color_scheme = "default" if theme == "light" else "slate"
                    theme_input = page.locator(
                        f'input[data-md-color-scheme="{color_scheme}"]')
                    if await theme_input.count() != 1:
                        raise RuntimeError(
                            f"Missing {theme} theme control on {url}")
                    current_scheme = await page.locator("body").get_attribute("data-md-color-scheme")
                    if current_scheme != color_scheme:
                        await page.wait_for_timeout(1500)
                        await theme_input.evaluate("e => e.click()")
                        try:
                            await page.wait_for_function(
                                "scheme => document.body.dataset.mdColorScheme === scheme",
                                arg=color_scheme,
                                timeout=2000,
                            )
                        except PlaywrightTimeoutError:
                            current_scheme = await page.locator("body").get_attribute("data-md-color-scheme")
                            print(
                                f"Warning: theme control did not switch {url} to {theme}; "
                                f"forcing palette from {current_scheme!r}.",
                                file=sys.stderr,
                            )
                            await page.evaluate(
                                """scheme => {
                                    document.body.dataset.mdColorScheme = scheme;
                                    const palette = document.querySelector('form[data-md-component="palette"]');
                                    for (const input of palette.querySelectorAll('input[data-md-color-scheme]')) {
                                        input.checked = input.dataset.mdColorScheme === scheme;
                                    }
                                    for (const label of palette.querySelectorAll('label[for]')) {
                                        const input = document.getElementById(label.htmlFor);
                                        if (input?.matches('[data-md-color-scheme]')) {
                                            label.hidden = input.dataset.mdColorScheme === scheme;
                                        }
                                    }
                                    for (const typeset of document.querySelectorAll('.md-typeset')) {
                                        typeset.style.color = 'var(--md-typeset-color)';
                                    }
                                }""",
                                color_scheme,
                            )
                            await page.wait_for_function(
                                "scheme => document.body.dataset.mdColorScheme === scheme",
                                arg=color_scheme,
                            )
                    await page.wait_for_timeout(150)
                    images = page.locator("article.md-content__inner img")
                    for image_index in range(await images.count()):
                        image = images.nth(image_index)
                        if await image.evaluate("img => getComputedStyle(img).display !== 'none'"):
                            image_src = await image.get_attribute("src")
                            try:
                                await image.evaluate("img => { img.loading = 'eager'; return img.decode(); }")
                            except PlaywrightError as exc:
                                raise RuntimeError(
                                    f"Could not decode visible image {image_src!r} on {url}"
                                ) from exc
                    await page.evaluate("window.scrollTo(0, 0)")
                    await page.wait_for_timeout(150)
                    screenshot = output_dir / f"{safe_name(label)}.{theme}.png"
                    await page.screenshot(path=str(screenshot), full_page=True, animations="disabled", timeout=60000)
                    records.append((label, theme, screenshot))
        finally:
            await browser.close()

    stale_screenshots = sorted(
        path.name
        for path in output_dir.iterdir()
        if path.is_file()
        and path.name.endswith((".light.png", ".dark.png"))
        and path.name not in expected_screenshots
    )
    if stale_screenshots:
        print(
            f"Warning: {len(stale_screenshots)} stale screenshot(s) remain in {output_dir} "
            "but are not included in this collage:",
            file=sys.stderr,
        )
        for screenshot_name in stale_screenshots:
            print(f"  {screenshot_name}", file=sys.stderr)

    gutter = 18
    label_height = 40
    thumb_width = args.tile_width
    tiles = []
    page_sizes: dict[str, dict[str, tuple[int, int]]] = {}
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
    except OSError:
        font = ImageFont.load_default()
    for label, theme, screenshot in records:
        with Image.open(screenshot) as screenshot_image:
            image = screenshot_image.convert("RGB")
        page_sizes.setdefault(label, {})[theme] = image.size
        thumb_height = round(image.height * thumb_width / image.width)
        image = image.resize((thumb_width, thumb_height),
                             Image.Resampling.LANCZOS)
        label_lines = wrap_label(f"{label} [{theme}]", thumb_width)
        actual_label_height = max(
            label_height, 8 + len(label_lines) * (font.size + 3))
        tile = Image.new("RGB", (thumb_width, thumb_height +
                         actual_label_height), "white")
        tile.paste(image, (0, actual_label_height))
        draw = ImageDraw.Draw(tile)
        for line_number, line in enumerate(label_lines):
            draw.text((6, 4 + line_number * (font.size + 3)),
                      line, font=font, fill="black")
        tiles.append(tile)
    if args.theme == "both":
        for label, sizes in page_sizes.items():
            light_size = sizes.get("light")
            dark_size = sizes.get("dark")
            if light_size and dark_size and light_size != dark_size:
                print(
                    f"Warning: light and dark screenshots differ in size for {label}: "
                    f"light {light_size[0]}x{light_size[1]}, dark {dark_size[0]}x{dark_size[1]}",
                    file=sys.stderr,
                )

    columns = args.columns
    rows = (len(tiles) + columns - 1) // columns
    row_heights = [max(tile.height for tile in tiles[i: i + columns])
                   for i in range(0, len(tiles), columns)]
    canvas = Image.new(
        "RGB",
        (
            gutter * (columns + 1) + columns * thumb_width,
            gutter * (rows + 1) + sum(row_heights),
        ),
        "#d4d4d4",
    )
    y = gutter
    for row in range(rows):
        for col, tile in enumerate(tiles[row * columns: (row + 1) * columns]):
            canvas.paste(tile, (gutter + col * (thumb_width + gutter), y))
        y += row_heights[row] + gutter
    collage = output_dir / "collage.png"
    temporary_collage: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(dir=output_dir, prefix=".collage-", suffix=".png", delete=False) as temp:
            temporary_collage = Path(temp.name)
        canvas.save(temporary_collage, format="PNG", optimize=True)
        temporary_collage.replace(collage)
    except OSError as exc:
        raise RuntimeError(
            f"Could not save collage to {collage}: {exc}") from exc
    finally:
        if temporary_collage is not None:
            temporary_collage.unlink(missing_ok=True)
    print(
        f"Captured {len(html_files)} pages as {len(records)} screenshots "
        f"({args.width}x{args.height}, DPR 1, {args.theme} theme)."
    )
    print(f"Screenshots: {output_dir}")
    print(f"Collage: {collage} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    asyncio.run(main())
