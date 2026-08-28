#!/usr/bin/env python3
# Name: TCAT Wiki - Link Checker
# Version: 5.1.0
# Date: 2026-08-28
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

"""Link validation script for the TCAT Wiki.

Checks all ``.md`` files in the repository ``docs/`` directory for broken
internal and external links. External links are checked in parallel with
light domain-based throttling and results are cached to disk for performance.

CLI usage (run from any working directory; paths resolve relative to this
file's repo):

    python utilities/check_links.py
    python utilities/check_links.py --internal
    python utilities/check_links.py --external --no-cache
"""

from __future__ import annotations

import argparse
import json
import re
import socket
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timedelta
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, TextIO

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.resolve()
DOCS_DIR = REPO_ROOT / "docs"
CACHE_FILE_PATH = SCRIPT_DIR / ".link-cache.json"
CACHE_TTL_HOURS = 12
MAX_EXTERNAL_WORKERS = 5
EXTERNAL_TIMEOUT_SECONDS = 5
USER_AGENT = (
    "TCAT-Wiki-LinkChecker/5.1.0 "
    "(+https://github.com/TaskarCenterAtUW/tcat-wiki)"
)

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n?", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FENCED_CODE_RE = re.compile(r"```[\s\S]*?```")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
SPECIAL_SCHEME_RE = re.compile(r"^(mailto|tel|javascript|ftp|file):", re.IGNORECASE)
TIMEOUT_RE = re.compile(r"Timeout|timed out|HttpClient\.Timeout", re.IGNORECASE)
SKIP_DOMAINS = (
    "*visualstudio.com*",
    "*docs.google.com*",
    "*maps.app.goo.gl*",
    "*firebase*",
    "*osm.workspaces-stage.sidewalks.washington.edu/api*",
    "*join.slack.com*",
    "*accessmap.app*",
)


@dataclass(frozen=True)
class MarkdownLink:
    text: str
    url: str


@dataclass(frozen=True)
class BrokenInternalLink:
    file: str
    text: str
    url: str


@dataclass(frozen=True)
class BrokenExternalLink:
    url: str
    status: str | int


@dataclass(frozen=True)
class ValidationSummary:
    markdown_files: int
    internal_links_checked: int
    broken_internal_links: list[BrokenInternalLink]
    external_urls_checked: int
    broken_external_links: list[BrokenExternalLink]
    timeout_warnings: list[BrokenExternalLink]
    cache_hits: int
    exit_code: int


def strip_ignored_markdown(text: str) -> str:
    """Remove non-content regions before extracting Markdown links."""
    text = FRONTMATTER_RE.sub("", text)
    text = HTML_COMMENT_RE.sub("", text)
    text = FENCED_CODE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def get_markdown_links(content: str) -> list[MarkdownLink]:
    """Return Markdown inline links after removing ignored regions."""
    stripped = strip_ignored_markdown(content)
    return [MarkdownLink(match.group(1), match.group(2)) for match in LINK_RE.finditer(stripped)]


def is_external_url(url: str) -> bool:
    """Return True when url is an absolute HTTP(S) URL."""
    return url.startswith("http://") or url.startswith("https://")


def is_internal_link_valid(file_path: Path | str, link_url: str) -> bool:
    """Validate an internal relative link against the source Markdown file."""
    if link_url.startswith("#"):
        return True
    if SPECIAL_SCHEME_RE.match(link_url):
        return True

    clean_url = link_url.split("#", 1)[0]
    if not clean_url:
        return True

    resolved_path = (Path(file_path).resolve().parent / clean_url).resolve()
    return resolved_path.exists()


def get_url_domain(url: str) -> str:
    """Extract a URL host suitable for throttling."""
    if not url or not url.strip():
        return "unknown"
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return "unknown"
    if not parsed.scheme or not parsed.hostname:
        return "unknown"
    return parsed.hostname


def load_link_cache(cache_path: Path = CACHE_FILE_PATH, no_cache: bool = False) -> dict[str, Any]:
    """Load the external-link cache from disk."""
    if no_cache or not cache_path.exists():
        return {}
    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print("  Warning: Could not read cache file, starting fresh")
        return {}
    return data if isinstance(data, dict) else {}


def save_link_cache(cache: dict[str, Any], cache_path: Path = CACHE_FILE_PATH) -> None:
    """Persist the external-link cache to disk."""
    try:
        cache_path.write_text(
            json.dumps(cache, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    except OSError:
        print("  Warning: Could not save cache file")


def is_cache_entry_valid(
    entry: dict[str, Any] | None,
    ttl_hours: int = CACHE_TTL_HOURS,
    now: datetime | None = None,
) -> bool:
    """Return True when a cache entry exists and is newer than ttl_hours."""
    if not entry or "timestamp" not in entry:
        return False
    try:
        cached_time = datetime.fromisoformat(entry["timestamp"])
    except (TypeError, ValueError):
        return False
    now = now or datetime.now(cached_time.tzinfo)
    return (now - cached_time) < timedelta(hours=ttl_hours)


def _build_request(url: str, method: str) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
        method=method,
    )


def _request_status(url: str, method: str) -> int:
    request = _build_request(url, method)
    with urllib.request.urlopen(request, timeout=EXTERNAL_TIMEOUT_SECONDS) as response:
        return response.getcode()


def _format_http_error(error: urllib.error.HTTPError) -> str:
    return f"HTTP {error.code}: {error.reason}"


def _is_timeout_error(error: BaseException) -> bool:
    return isinstance(error, socket.timeout | TimeoutError) or bool(
        TIMEOUT_RE.search(str(error))
    )


def check_external_url_valid(url: str) -> dict[str, Any]:
    """Check one external URL using HEAD, then GET on HEAD failure."""
    for pattern in SKIP_DOMAINS:
        if fnmatch(url, pattern):
            return {
                "valid": True,
                "status": "Skipped URL listed in skipDomains filter.",
                "isTimeout": False,
            }

    try:
        try:
            status_code = _request_status(url, "HEAD")
        except Exception:
            status_code = _request_status(url, "GET")
        return {
            "valid": status_code < 400,
            "status": status_code,
            "isTimeout": False,
        }
    except urllib.error.HTTPError as error:
        return {
            "valid": False,
            "status": _format_http_error(error),
            "isTimeout": _is_timeout_error(error),
        }
    except Exception as error:
        return {
            "valid": False,
            "status": str(error),
            "isTimeout": _is_timeout_error(error),
        }


class DomainThrottle:
    """Small same-domain delay used during concurrent external checks."""

    def __init__(self, delay_seconds: float = 0.05):
        self.delay_seconds = delay_seconds
        self._gate = threading.Lock()
        self._locks: dict[str, threading.Lock] = {}
        self._next_start: dict[str, float] = {}

    def wait(self, domain: str) -> None:
        with self._gate:
            lock = self._locks.setdefault(domain, threading.Lock())
        with lock:
            now = time.monotonic()
            next_start = self._next_start.get(domain, now)
            if next_start > now:
                time.sleep(next_start - now)
            self._next_start[domain] = time.monotonic() + self.delay_seconds


def _check_external_url_with_throttle(
    url: str,
    throttle: DomainThrottle,
    checker: Any,
) -> dict[str, Any]:
    throttle.wait(get_url_domain(url))
    result = checker(url)
    return {
        "url": url,
        "valid": result["valid"],
        "status": result["status"],
        "isTimeout": result.get("isTimeout", False),
    }


def _emit(stream: TextIO, text: str = "") -> None:
    print(text, file=stream)


def validate_docs(
    *,
    check_internal: bool,
    check_external: bool,
    no_cache: bool,
    docs_dir: Path = DOCS_DIR,
    cache_path: Path = CACHE_FILE_PATH,
    output: TextIO | None = None,
    external_checker: Any = check_external_url_valid,
) -> ValidationSummary:
    """Validate Markdown links and return a summary."""
    stream = output or sys.stdout
    docs_dir = docs_dir.resolve()
    cache_path = cache_path.resolve()

    _emit(stream, "TCAT Wiki Link Validation")
    _emit(stream, "=========================")
    modes = []
    if check_internal:
        modes.append("Internal")
    if check_external:
        modes.append("External")
    _emit(stream, f"Checking: {' and '.join(modes)} links")
    _emit(stream)

    if not docs_dir.exists():
        _emit(stream, f"Error: Docs directory '{docs_dir}' not found!")
        return ValidationSummary(0, 0, [], 0, [], [], 0, 1)

    markdown_files = sorted(docs_dir.rglob("*.md"))
    if not markdown_files:
        _emit(stream, f"No markdown files found in '{docs_dir}'")
        return ValidationSummary(0, 0, [], 0, [], [], 0, 0)

    _emit(stream, f"Found {len(markdown_files)} markdown files to validate")
    _emit(stream)

    external_urls: set[str] = set()
    broken_internal_links: list[BrokenInternalLink] = []
    broken_external_links: list[BrokenExternalLink] = []
    timeout_warnings: list[BrokenExternalLink] = []
    internal_links_checked = 0

    for file_path in markdown_files:
        relative_path = file_path.relative_to(docs_dir).as_posix()
        _emit(stream, f"Validating: {relative_path}")
        try:
            content = file_path.read_text(encoding="utf-8")
        except OSError as error:
            _emit(stream, f"  ERROR reading file: {error}")
            continue

        for link in get_markdown_links(content):
            if is_external_url(link.url):
                if check_external:
                    external_urls.add(link.url)
                continue
            if check_internal:
                internal_links_checked += 1
                if not is_internal_link_valid(file_path, link.url):
                    broken = BrokenInternalLink(relative_path, link.text, link.url)
                    broken_internal_links.append(broken)
                    _emit(stream, f"  [X] Broken internal link: [{link.text}]({link.url})")

    cache_hits = 0
    if check_external:
        _emit(stream)
        _emit(stream, f"Validating {len(external_urls)} unique external URLs...")

        link_cache = load_link_cache(cache_path, no_cache=no_cache)
        urls_to_check: list[str] = []
        cached_results: dict[str, dict[str, Any]] = {}

        for url in sorted(external_urls):
            entry = link_cache.get(url)
            if (
                not no_cache
                and isinstance(entry, dict)
                and is_cache_entry_valid(entry)
                and not entry.get("isTimeout", False)
            ):
                cache_hits += 1
                cached_results[url] = entry
            else:
                urls_to_check.append(url)

        if cache_hits > 0:
            _emit(
                stream,
                f"  Using {cache_hits} cached results (valid within {CACHE_TTL_HOURS}h TTL)",
            )

        for url in sorted(cached_results):
            cached = cached_results[url]
            _emit(stream, f"Testing: {url}")
            if not cached.get("valid", False):
                broken_external_links.append(
                    BrokenExternalLink(url, f"{cached.get('status')} (cached)")
                )
                _emit(stream, f"  [X] Failed (cached): {cached.get('status')}")
            else:
                _emit(stream, f"  [OK] OK (cached): {cached.get('status')}")

        if urls_to_check:
            _emit(stream)
            _emit(
                stream,
                f"Checking {len(urls_to_check)} URLs (parallel with domain throttling)...",
            )
            throttle = DomainThrottle()
            results: list[dict[str, Any]] = []
            with ThreadPoolExecutor(max_workers=MAX_EXTERNAL_WORKERS) as executor:
                futures = {
                    executor.submit(
                        _check_external_url_with_throttle,
                        url,
                        throttle,
                        external_checker,
                    ): url
                    for url in urls_to_check
                }
                for future in as_completed(futures):
                    results.append(future.result())

            for result in sorted(results, key=lambda item: item["url"]):
                url = result["url"]
                _emit(stream, f"Testing: {url}")
                link_cache[url] = {
                    "valid": result["valid"],
                    "status": result["status"],
                    "isTimeout": result["isTimeout"],
                    "timestamp": datetime.now().astimezone().isoformat(),
                }
                if not result["valid"]:
                    if result["isTimeout"]:
                        timeout = BrokenExternalLink(url, result["status"])
                        timeout_warnings.append(timeout)
                        _emit(stream, f"  [!] Timeout: {result['status']}")
                    else:
                        broken = BrokenExternalLink(url, result["status"])
                        broken_external_links.append(broken)
                        _emit(stream, f"  [X] Failed: {result['status']}")
                else:
                    _emit(stream, f"  [OK] OK: {result['status']}")

            save_link_cache(link_cache, cache_path)

    _emit(stream)
    _emit(stream, "VALIDATION SUMMARY")
    _emit(stream, "==================")
    _emit(stream, f"Total markdown files: {len(markdown_files)}")
    if check_internal:
        _emit(stream, f"Internal links checked: {internal_links_checked}")
        _emit(stream, f"Broken internal links: {len(broken_internal_links)}")
    if check_external:
        _emit(stream, f"External URLs checked: {len(external_urls)}")
        _emit(stream, f"Broken external links: {len(broken_external_links)}")
        if cache_hits > 0:
            _emit(stream, f"Cache hits: {cache_hits} (skipped network requests)")
        if timeout_warnings:
            _emit(stream, f"Timeout warnings: {len(timeout_warnings)}")

    if check_internal and broken_internal_links:
        _emit(stream)
        _emit(stream, f"[X] BROKEN INTERNAL LINKS ({len(broken_internal_links)}):")
        for item in broken_internal_links:
            _emit(stream, f"  File: {item.file}")
            _emit(stream, f"  Link: [{item.text}]({item.url})")
            _emit(stream)

    if check_external and broken_external_links:
        _emit(stream)
        _emit(stream, f"[X] BROKEN EXTERNAL LINKS ({len(broken_external_links)}):")
        for item in broken_external_links:
            _emit(stream, f"  URL: {item.url}")
            _emit(stream, f"  Issue: {item.status}")
            _emit(stream)

    if check_external and timeout_warnings:
        _emit(stream)
        _emit(stream, f"[!] TIMEOUT WARNINGS ({len(timeout_warnings)}):")
        _emit(
            stream,
            "    These URLs timed out but may still be valid. "
            "They do not cause the link check to fail.",
        )
        for item in timeout_warnings:
            _emit(stream, f"  URL: {item.url}")
            _emit(stream, f"  Issue: {item.status}")
            _emit(stream)

    total_broken = 0
    if check_internal:
        total_broken += len(broken_internal_links)
    if check_external:
        total_broken += len(broken_external_links)

    if total_broken == 0:
        _emit(stream)
        _emit(stream, "[OK] ALL CHECKED LINKS VALID! No broken links found.")

    return ValidationSummary(
        markdown_files=len(markdown_files),
        internal_links_checked=internal_links_checked,
        broken_internal_links=broken_internal_links,
        external_urls_checked=len(external_urls),
        broken_external_links=broken_external_links,
        timeout_warnings=timeout_warnings,
        cache_hits=cache_hits,
        exit_code=1 if total_broken else 0,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--internal",
        action="store_true",
        help="Check internal relative links.",
    )
    parser.add_argument(
        "--external",
        action="store_true",
        help="Check external absolute links.",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Bypass the cache and force fresh external link checks.",
    )
    args = parser.parse_args(argv)

    check_internal = args.internal
    check_external = args.external
    if not check_internal and not check_external:
        check_internal = True
        check_external = True

    try:
        summary = validate_docs(
            check_internal=check_internal,
            check_external=check_external,
            no_cache=args.no_cache,
        )
        return summary.exit_code
    except KeyboardInterrupt:
        print("\nOperation canceled.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
