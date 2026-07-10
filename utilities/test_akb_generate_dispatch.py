"""Pytest suite for utilities/akb-generate-dispatch.py.

Uses a temp fixture tree (never the real docs/assistant/) to validate the
dispatch generator's structure, status reporting, and edge-case handling.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).parent / "akb-generate-dispatch.py"
spec = importlib.util.spec_from_file_location(
    "akb_generate_dispatch", MODULE_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f"could not load module spec from {MODULE_PATH}")
gad = importlib.util.module_from_spec(spec)
sys.modules["akb_generate_dispatch"] = gad
spec.loader.exec_module(gad)


def write_article(path: Path, title: str, review_status: str, body: str = "TODO"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
title: {title}
slug: {path.stem}
doc_type: concept
review_status: {review_status}
---

# {title}

## Short Answer

{body}
""",
        encoding="utf-8",
    )


@pytest.fixture
def assistant_dir(tmp_path):
    root = tmp_path / "assistant"
    root.mkdir()

    # Top-level peers - must never appear as topic dirs or registry rows.
    (root / "index.md").write_text(
        "---\ntitle: Assistant Knowledge Base\n---\n\n# Assistant Knowledge Base\n",
        encoding="utf-8",
    )
    (root / "schema.md").write_text(
        "---\ntitle: Schema\n---\n\n# Schema\n", encoding="utf-8")
    (root / "intents.md").write_text(
        "---\ntitle: Intents\n---\n\n# Intents\n", encoding="utf-8")

    # Topic "alpha": has index, concept articles, no workflow articles.
    (root / "alpha" / "index.md").parent.mkdir(parents=True, exist_ok=True)
    (root / "alpha" / "index.md").write_text(
        "---\ntitle: Alpha — Assistant Knowledge Base\n---\n\n# Alpha\n",
        encoding="utf-8",
    )
    write_article(root / "alpha" / "concept" / "what-is-alpha.md",
                  "What is Alpha?", "reviewed")
    write_article(root / "alpha" / "concept" / "why-alpha.md",
                  "Why Alpha?", "stub")

    # Topic "beta": no index.md (title falls back to dir name), has workflow only.
    write_article(root / "beta" / "workflow" / "do-a-thing.md",
                  "Do A Thing", "draft")

    return root


def test_top_level_peers_excluded(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    registry = content.split("## Registry", 1)[1]
    assert "`schema.md`" not in registry
    assert "`intents.md`" not in registry
    assert "`index.md`" not in registry
    # dispatch.md never lists itself
    assert "`dispatch.md`" not in registry


def test_topic_headings_and_index_link(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    assert "## Alpha — Assistant Knowledge Base" in content
    assert "[alpha/index.md](alpha/index.md)" in content
    # beta has no index.md -> title-cased fallback, no "See ... index.md" line
    assert "## Beta" in content
    assert "beta/index.md" not in content


def test_status_reflects_frontmatter(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    assert "| `what-is-alpha.md` | reviewed |" in content
    assert "| `why-alpha.md` | stub |" in content
    assert "| `do-a-thing.md` | draft |" in content


def test_status_legend_includes_article_counts(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    legend = content.split("## Status Legend", 1)[1].split("## Registry", 1)[0]
    assert "| Status | Count | Meaning |" in legend
    assert "| `stub` | 1 |" in legend
    assert "| `draft` | 1 |" in legend
    assert "| `reviewed` | 1 |" in legend


def test_empty_subdir_section_omitted(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    # alpha has no workflow/ articles -> no "### Workflows" under Alpha section
    alpha_block = content.split("## Alpha", 1)[1].split("## Beta", 1)[0]
    assert "### Workflows" not in alpha_block
    assert "### Concepts" in alpha_block

    # beta has no concept/ articles -> no "### Concepts" under Beta section
    beta_block = content.split("## Beta", 1)[1]
    assert "### Concepts" not in beta_block
    assert "### Workflows" in beta_block


def test_base_path_lines_correct(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    assert "Base: `assistant/alpha/concept/`" in content
    assert "Base: `assistant/beta/workflow/`" in content


def test_last_reviewed_is_today(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    assert "last_reviewed: 2026-07-06" in content


def test_filenames_are_bare_in_table_cells(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    assert "`what-is-alpha.md`" in content
    assert "alpha/concept/what-is-alpha.md" not in content


def test_write_dispatch_creates_file(assistant_dir):
    output_path = gad.write_dispatch(assistant_dir, today="2026-07-06")
    assert output_path == assistant_dir / "dispatch.md"
    assert output_path.exists()
    text = output_path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    assert "GENERATED FILE" in text


def test_topics_sorted_alphabetically(assistant_dir):
    content = gad.build_dispatch(assistant_dir, today="2026-07-06")
    alpha_pos = content.index("## Alpha")
    beta_pos = content.index("## Beta")
    assert alpha_pos < beta_pos


def test_no_topics_produces_empty_registry(tmp_path):
    root = tmp_path / "assistant"
    root.mkdir()
    (root / "index.md").write_text(
        "---\ntitle: X\n---\n\n# X\n", encoding="utf-8")
    content = gad.build_dispatch(root, today="2026-07-06")
    registry = content.split("## Registry", 1)[1].strip()
    assert registry == ""
