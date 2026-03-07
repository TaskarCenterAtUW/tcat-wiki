"""Shared utilities for TCAT Wiki event report generation.

Provides common functions used by the orchestrator, stats generators,
and section generators:

  - Path helpers (repo root, event directories)
  - Frontmatter parsing and validation
  - HTTP / JSON fetching
  - Haversine distance and way-length computation
  - Template placeholder filling and cleanup
"""

import json
import math
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request


# =============================================================================
# Path helpers
# =============================================================================

def repo_root():
    """Return the repository root directory."""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def events_dir():
    """Return the ``docs/events/`` directory path."""
    return os.path.join(repo_root(), "docs", "events")


def event_dir(event_slug):
    """Return the directory for a specific event."""
    return os.path.join(events_dir(), event_slug)


def templates_dir():
    """Return the ``templates/events/`` directory path."""
    return os.path.join(repo_root(), "templates", "events")


def utilities_dir():
    """Return the ``utilities/`` directory path."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# =============================================================================
# Frontmatter parsing
# =============================================================================

def parse_frontmatter(text):
    """Parse YAML frontmatter from a Markdown file into a flat dict.

    Handles simple ``key: value`` pairs and quoted strings.
    Skips blank lines, comments (``#``), and list items (``- value``).
    """
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    props = {}
    for line in match.group(1).split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # Strip inline comments while respecting quoted strings
        if "#" in value:
            q = value[0] if value and value[0] in ('"', "'") else None
            if q:
                # Find closing quote, then strip any trailing comment
                close = value.find(q, 1)
                if close != -1:
                    value = value[:close + 1] + value[close + 1:].split("#")[0]
                    value = value.strip()
            else:
                value = value[:value.index("#")].strip()
        # Strip surrounding quotes
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        props[key] = value
    return props


def read_event_frontmatter(event_slug):
    """Read frontmatter from ``docs/events/<slug>/index.md``.

    Returns the frontmatter dict.  Exits with an error if the file
    does not exist.
    """
    index_path = os.path.join(event_dir(event_slug), "index.md")
    if not os.path.isfile(index_path):
        print(f"✗ Event index not found: {index_path}", file=sys.stderr)
        sys.exit(1)

    with open(index_path, encoding="utf-8") as f:
        text = f.read()

    return parse_frontmatter(text)


def validate_required_fields(fm, required, context=""):
    """Exit with an error if any *required* keys are missing from *fm*.

    *context* is an optional label included in the error message.
    """
    missing = [k for k in required if not fm.get(k)]
    if missing:
        label = f" ({context})" if context else ""
        print(
            f"✗ Missing required frontmatter{label}: {', '.join(missing)}",
            file=sys.stderr,
        )
        sys.exit(1)


# =============================================================================
# HTTP helpers
# =============================================================================

_USER_AGENT = (
    "TCAT-Wiki-EventReport/2.0 "
    "(https://github.com/TaskarCenterAtUW/tcat-wiki)"
)
_TIMEOUT = 360  # seconds


def make_request(url, data=None, headers=None):
    """Build a ``urllib.request.Request`` with a proper User-Agent."""
    req = urllib.request.Request(url, data=data)
    req.add_header("User-Agent", _USER_AGENT)
    req.add_header("Accept", "application/json, application/geo+json, */*")
    if headers:
        for key, value in headers.items():
            req.add_header(key, value)
    return req


def fetch_json(url, data=None, headers=None):
    """Fetch JSON from *url*, optionally POSTing *data* (bytes)."""
    req = make_request(url, data=data, headers=headers)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=_TIMEOUT, context=ctx) as resp:
        body = resp.read()
        if not body:
            raise RuntimeError(
                f"Empty response from {url} "
                f"(status {resp.status}, "
                f"content-type: {resp.headers.get('Content-Type')})"
            )
        try:
            return json.loads(body.decode("utf-8"))
        except json.JSONDecodeError:
            preview = body[:500].decode("utf-8", errors="replace")
            raise RuntimeError(
                f"Non-JSON response from {url} "
                f"(status {resp.status}, "
                f"content-type: {resp.headers.get('Content-Type')})\n"
                f"Body preview: {preview}"
            )


def fetch_bytes(url, headers=None):
    """Fetch raw bytes from *url*.  Returns ``(body_bytes, content_type)``."""
    req = make_request(url, headers=headers)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=_TIMEOUT, context=ctx) as resp:
        body = resp.read()
        return body, resp.headers.get("Content-Type", "")


# =============================================================================
# Geometry helpers
# =============================================================================

METERS_PER_MILE = 1_609.344


def haversine(lat1, lon1, lat2, lon2):
    """Great-circle distance in **meters** between two points."""
    R = 6_371_000  # Earth mean radius (m)
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = (math.sin(dp / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def way_length_m(coords):
    """Total length in meters of a way given its coordinate list.

    *coords* can be either:
      - Overpass JSON geometry: ``[{"lat": ..., "lon": ...}, ...]``
      - Simple tuples: ``[(lat, lon), ...]``
    """
    total = 0.0
    for i in range(len(coords) - 1):
        if isinstance(coords[i], dict):
            lat1, lon1 = coords[i]["lat"], coords[i]["lon"]
            lat2, lon2 = coords[i + 1]["lat"], coords[i + 1]["lon"]
        else:
            lat1, lon1 = coords[i]
            lat2, lon2 = coords[i + 1]
        total += haversine(lat1, lon1, lat2, lon2)
    return total


# =============================================================================
# Template helpers
# =============================================================================

def fill_template(text, replacements):
    """Replace ``{{PLACEHOLDER}}`` tokens in *text* using *replacements* dict."""
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", str(value))
    return text


def strip_html_comments(text):
    """Remove HTML comments, preserving ``<!-- @format -->``."""
    def _replace(match):
        comment = match.group(0)
        if comment.strip() == "<!-- @format -->":
            return comment
        return ""
    return re.sub(r"<!--.*?-->", _replace, text, flags=re.DOTALL)


def fix_article(text):
    """Fix ``a`` → ``an`` before vowel-initial words."""
    text = re.sub(r"\ba ([aeiou])", r"an \1", text)
    text = re.sub(r"\bA ([aeiou])", r"An \1", text)
    return text


def clean_blank_lines(text):
    """Collapse runs of 3+ blank lines to 2 and trim trailing whitespace."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


# =============================================================================
# Interactive prompts
# =============================================================================

def prompt_for_file(label, download_url=None):
    """Ask the user for a local file path, or skip.

    Returns the entered path (stripped) or ``None``.
    """
    if download_url:
        print(f"\n  You can download the {label} from:")
        print(f"    {download_url}")
    print(f"  Enter the path to the {label} file, or press Enter to skip.")
    try:
        response = input(f"  {label}> ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    return response or None


# =============================================================================
# JSON I/O
# =============================================================================

def write_json(path, data):
    """Write *data* as pretty-printed JSON to *path*, creating dirs."""
    out_dir = os.path.dirname(os.path.abspath(path))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def read_json(path):
    """Read and return parsed JSON from *path*."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# =============================================================================
# Printing helpers
# =============================================================================

def print_separator(title=None):
    """Print a visual separator, optionally with a centered *title*."""
    if title:
        print(f"\n{'=' * 60}")
        print(f"  {title}")
        print(f"{'=' * 60}")
    else:
        print(f"\n{'-' * 60}")
