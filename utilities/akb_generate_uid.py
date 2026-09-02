#!/usr/bin/env python3
"""Generate and assign durable UUIDv4 values for assistant pages.

With no file argument, prints a new canonical UUIDv4. With ``--file``, inserts
that value into a Markdown file's frontmatter. Existing values are protected
unless ``--replace`` is explicitly supplied.
"""

import argparse
import re
import sys
import uuid
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
ASSISTANT_DIR = REPO_ROOT / "docs" / "assistant"
RETIRED_PATH = SCRIPT_DIR / "akb-retired-uuids.txt"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
UID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
UID_LINE_RE = re.compile(r"(?m)^uid:\s*(\S+)\s*$")


def read_retired(path: Path = RETIRED_PATH) -> set[str]:
    """Read non-comment UUID values from the retired-ID ledger."""
    if not path.exists():
        return set()
    return {
        line.strip().lower()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def live_uids(assistant_dir: Path = ASSISTANT_DIR) -> set[str]:
    """Return UUID values already assigned to assistant Markdown files."""
    values = set()
    if not assistant_dir.is_dir():
        return values
    for path in assistant_dir.rglob("*.md"):
        match = UID_LINE_RE.search(path.read_text(encoding="utf-8"))
        if match:
            values.add(match.group(1).lower())
    return values


def new_uid(existing: set[str] | None = None,
            retired: set[str] | None = None) -> str:
    """Mint a UUIDv4 absent from the supplied live and retired values."""
    existing = existing or set()
    retired = retired or set()
    while True:
        value = str(uuid.uuid4())
        if value not in existing and value not in retired:
            return value


def assign_uid(path: Path, value: str, replace: bool = False) -> None:
    """Insert ``value`` into a Markdown file's frontmatter."""
    if not UID_RE.fullmatch(value):
        raise ValueError(f"UID is not a canonical UUIDv4: {value}")
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"file has no YAML frontmatter: {path}")
    existing = UID_LINE_RE.search(match.group(1))
    if existing and not replace:
        raise ValueError(f"file already has a uid; refusing to overwrite: {path}")
    if existing:
        updated_frontmatter = UID_LINE_RE.sub(f"uid: {value}", match.group(1), count=1)
    else:
        updated_frontmatter = f"uid: {value}\n{match.group(1)}"
    updated = f"---\n{updated_frontmatter}\n---\n" + text[match.end():]
    path.write_text(updated, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, help="Markdown file to assign a UID")
    parser.add_argument("--replace", action="store_true",
                        help="Explicitly replace an existing file UID")
    args = parser.parse_args(argv)

    retired = read_retired()
    existing = live_uids()
    value = new_uid(existing, retired)
    if args.file is None:
        print(value)
        return 0
    path = args.file.resolve()
    try:
        assign_uid(path, value, replace=args.replace)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
