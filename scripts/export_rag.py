#!/usr/bin/env python3
"""
Export docs/assistant/**/*.md into JSONL for downstream RAG ingestion.

Usage (from repository root):
    python scripts/export_rag.py
    python scripts/export_rag.py -o rag_exports/chunks.jsonl

Requires PyYAML (installed with Zensical / project dependencies).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

def json_friendly(value):
    """Convert YAML-loaded types (e.g. datetime.date) to JSON-serializable values."""
    if isinstance(value, dict):
        return {k: json_friendly(v) for k, v in value.items()}
    if isinstance(value, list):
        return [json_friendly(v) for v in value]
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return value


try:
    import yaml
except ImportError as exc:  # pragma: no cover - runtime guard
    print("PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(1) from exc


def split_frontmatter(raw: str) -> tuple[dict, str]:
    """Return (metadata_dict, markdown_body). Empty dict if no valid YAML frontmatter."""
    text = raw.lstrip("\ufeff")
    if not text.startswith("---"):
        return {}, raw
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, raw
    fm_block = m.group(1)
    body = text[m.end() :]
    try:
        meta = yaml.safe_load(fm_block) or {}
        if not isinstance(meta, dict):
            return {}, raw
        return meta, body
    except yaml.YAMLError:
        return {}, raw


def extract_title(body: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


def build_source_url_placeholder(rel_md: str) -> str:
    """
    Placeholder URL for static site publishing. Replace PLACEHOLDER_SITE_URL with
    the deployed site root (see zensical.toml site_url) and adjust path suffixes
    if your HTML permalink strategy differs.
    """
    stem = rel_md[: -len(".md")] if rel_md.endswith(".md") else rel_md
    return f"PLACEHOLDER_SITE_URL/{stem}/"


def iter_markdown_files(root: Path) -> list[Path]:
    paths = sorted(root.rglob("*.md"))
    return [p for p in paths if p.is_file()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=Path("docs"),
        help="Path to docs directory (default: ./docs)",
    )
    parser.add_argument(
        "--assistant-subdir",
        default="assistant",
        help="Subdirectory under docs-root to export (default: assistant)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("rag_exports/chunks.jsonl"),
        help="Output JSONL path",
    )
    args = parser.parse_args()

    assistant_root = args.docs_root / args.assistant_subdir
    if not assistant_root.is_dir():
        print(f"Assistant directory not found: {assistant_root}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)

    written = 0
    with args.output.open("w", encoding="utf-8") as out:
        for path in iter_markdown_files(assistant_root):
            rel = path.relative_to(args.docs_root).as_posix()
            raw = path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            meta = json_friendly(meta)
            title = meta.get("title") if isinstance(meta.get("title"), str) else None
            if not title:
                title = extract_title(body, path.stem)

            record = {
                "path": rel,
                "title": title,
                "slug": meta.get("slug", ""),
                "doc_type": meta.get("doc_type", ""),
                "products": meta.get("products") or [],
                "audiences": meta.get("audiences") or [],
                "topics": meta.get("topics") or [],
                "risk_level": meta.get("risk_level", ""),
                "authority_level": meta.get("authority_level", ""),
                "retrieval_priority": meta.get("retrieval_priority", ""),
                "review_status": meta.get("review_status", ""),
                "last_reviewed": meta.get("last_reviewed", ""),
                "assistant_behavior": meta.get("assistant_behavior") or {},
                "source_url": build_source_url_placeholder(rel),
                "content": body.strip(),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

    print(f"Wrote {written} records to {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
