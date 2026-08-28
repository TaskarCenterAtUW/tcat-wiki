"""Pytest suite for utilities/check_links.py."""

from __future__ import annotations

import importlib.util
import io
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).parent / "check_links.py"
spec = importlib.util.spec_from_file_location("check_links", MODULE_PATH)
cl = importlib.util.module_from_spec(spec)
sys.modules["check_links"] = cl
spec.loader.exec_module(cl)


def write_text(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


@pytest.fixture
def docs_tree(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    write_text(
        docs / "index.md",
        (
            "---\n"
            "title: Test Page\n"
            "# [Ignored Meta Link](meta.md)\n"
            "---\n\n"
            "See [Getting Started](getting-started.md).\n"
            "Jump to [Overview](#overview).\n"
            "External [GitHub](https://github.com).\n"
            "Image ![Logo](images/logo.png)\n"
            "<!-- [Hidden](hidden.md) -->\n"
            "```md\n"
            "[Fake](fake.md)\n"
            "```\n"
            "Use `[inline](inline.md)` syntax.\n"
        ),
    )
    write_text(docs / "getting-started.md", "# Getting Started\n")
    write_text(docs / "images" / "logo.png", "")
    write_text(docs / "guides" / "guide.md", "See [Home](../index.md)\n")
    return docs


def test_get_markdown_links_extracts_standard_links():
    links = cl.get_markdown_links(
        "Check [Google](https://google.com) and [Guide](../guides/my-guide.md)."
    )
    assert links == [
        cl.MarkdownLink("Google", "https://google.com"),
        cl.MarkdownLink("Guide", "../guides/my-guide.md"),
    ]


def test_get_markdown_links_strips_frontmatter_comments_and_code_and_excludes_images():
    content = (
        "---\n"
        "title: Test\n"
        "description: [Ignored](meta.md)\n"
        "---\n\n"
        "[Real](real.md)\n"
        "<!-- [Commented](commented.md) -->\n"
        "```python\n"
        "[Code](code.md)\n"
        "```\n"
        "Use `[inline](inline.md)` syntax.\n"
        "![Alt](image.png)\n"
    )
    links = cl.get_markdown_links(content)
    assert links == [cl.MarkdownLink("Real", "real.md")]


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://example.com", True),
        ("http://example.com/path", True),
        ("../page.md", False),
        ("page.md", False),
        ("#section", False),
        ("mailto:user@example.com", False),
        ("tel:+1234567890", False),
    ],
)
def test_is_external_url(url: str, expected: bool):
    assert cl.is_external_url(url) is expected


def test_is_internal_link_valid_handles_relative_paths_fragments_and_special_schemes(
    docs_tree: Path,
):
    index = docs_tree / "index.md"
    guide = docs_tree / "guides" / "guide.md"
    assert cl.is_internal_link_valid(index, "getting-started.md")
    assert cl.is_internal_link_valid(index, "getting-started.md#section")
    assert cl.is_internal_link_valid(guide, "../index.md")
    assert cl.is_internal_link_valid(index, "#overview")
    assert cl.is_internal_link_valid(index, "mailto:user@example.com")
    assert not cl.is_internal_link_valid(index, "missing.md")


def test_check_external_url_valid_skips_known_domains():
    result = cl.check_external_url_valid(
        "https://marketplace.visualstudio.com/items?itemName=test"
    )
    assert result["valid"] is True
    assert "Skipped" in result["status"]
    assert result["isTimeout"] is False


def test_check_external_url_valid_falls_back_from_head_to_get(monkeypatch: pytest.MonkeyPatch):
    calls: list[str] = []

    def fake_request_status(url: str, method: str) -> int:
        calls.append(method)
        if method == "HEAD":
            raise RuntimeError("HEAD blocked")
        return 200

    monkeypatch.setattr(cl, "_request_status", fake_request_status)
    result = cl.check_external_url_valid("https://example.com")
    assert result == {"valid": True, "status": 200, "isTimeout": False}
    assert calls == ["HEAD", "GET"]


def test_check_external_url_valid_formats_http_errors(monkeypatch: pytest.MonkeyPatch):
    def fake_request_status(url: str, method: str) -> int:
        raise urllib.error.HTTPError(
            url=url,
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )

    import urllib.error

    monkeypatch.setattr(cl, "_request_status", fake_request_status)
    result = cl.check_external_url_valid("https://example.com/missing")
    assert result["valid"] is False
    assert result["status"] == "HTTP 404: Not Found"
    assert result["isTimeout"] is False


def test_check_external_url_valid_detects_timeouts(monkeypatch: pytest.MonkeyPatch):
    def fake_request_status(url: str, method: str) -> int:
        raise TimeoutError("timed out")

    monkeypatch.setattr(cl, "_request_status", fake_request_status)
    result = cl.check_external_url_valid("https://example.com/slow")
    assert result["valid"] is False
    assert result["isTimeout"] is True


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://example.com", "example.com"),
        ("https://www.example.com/path", "www.example.com"),
        ("https://example.com:8080/api", "example.com"),
        ("not-a-valid-url", "unknown"),
        ("", "unknown"),
    ],
)
def test_get_url_domain(url: str, expected: str):
    assert cl.get_url_domain(url) == expected


def test_is_cache_entry_valid_within_and_outside_ttl():
    fresh = {
        "timestamp": (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat(),
        "valid": True,
        "status": 200,
    }
    stale = {
        "timestamp": (datetime.now(timezone.utc) - timedelta(hours=13)).isoformat(),
        "valid": True,
        "status": 200,
    }
    timeout_entry = {
        "timestamp": (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat(),
        "valid": False,
        "status": "timed out",
        "isTimeout": True,
    }
    assert cl.is_cache_entry_valid(fresh) is True
    assert cl.is_cache_entry_valid(stale) is False
    assert cl.is_cache_entry_valid(timeout_entry) is True
    assert cl.is_cache_entry_valid({}) is False
    assert cl.is_cache_entry_valid(None) is False


def test_load_and_save_link_cache_round_trip(tmp_path: Path):
    cache_path = tmp_path / ".link-cache.json"
    payload = {
        "https://example.com": {
            "valid": True,
            "status": 200,
            "isTimeout": False,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    }
    cl.save_link_cache(payload, cache_path)
    assert cl.load_link_cache(cache_path) == payload


def test_validate_docs_internal_only_reports_broken_links(tmp_path: Path):
    docs = tmp_path / "docs"
    write_text(docs / "index.md", "See [Good](good.md) and [Bad](missing.md).\n")
    write_text(docs / "good.md", "# Good\n")
    output = io.StringIO()

    summary = cl.validate_docs(
        check_internal=True,
        check_external=False,
        no_cache=False,
        docs_dir=docs,
        cache_path=tmp_path / ".link-cache.json",
        output=output,
    )

    assert summary.markdown_files == 2
    assert summary.internal_links_checked == 2
    assert len(summary.broken_internal_links) == 1
    assert summary.broken_internal_links[0].url == "missing.md"
    assert summary.exit_code == 1
    assert "Broken internal links: 1" in output.getvalue()


def test_validate_docs_uses_fresh_cache_and_rechecks_timeouts(
    docs_tree: Path, tmp_path: Path
):
    cache_path = tmp_path / ".link-cache.json"
    fresh_timestamp = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
    cl.save_link_cache(
        {
            "https://cached.example.com": {
                "valid": True,
                "status": 200,
                "isTimeout": False,
                "timestamp": fresh_timestamp,
            },
            "https://retry.example.com": {
                "valid": False,
                "status": "timed out",
                "isTimeout": True,
                "timestamp": fresh_timestamp,
            },
        },
        cache_path,
    )
    write_text(
        docs_tree / "external.md",
        (
            "[Cached](https://cached.example.com)\n"
            "[Retry](https://retry.example.com)\n"
            "[Fresh](https://fresh.example.com)\n"
        ),
    )
    checked: list[str] = []

    def fake_checker(url: str) -> dict[str, object]:
        checked.append(url)
        return {"valid": True, "status": 200, "isTimeout": False}

    summary = cl.validate_docs(
        check_internal=False,
        check_external=True,
        no_cache=False,
        docs_dir=docs_tree,
        cache_path=cache_path,
        output=io.StringIO(),
        external_checker=fake_checker,
    )

    assert summary.external_urls_checked == 4
    assert summary.cache_hits == 1
    assert sorted(checked) == sorted(
        [
            "https://fresh.example.com",
            "https://github.com",
            "https://retry.example.com",
        ]
    )
    saved_cache = cl.load_link_cache(cache_path)
    assert saved_cache["https://fresh.example.com"]["status"] == 200


def test_validate_docs_no_cache_bypasses_cache(docs_tree: Path, tmp_path: Path):
    cache_path = tmp_path / ".link-cache.json"
    cl.save_link_cache(
        {
            "https://cached.example.com": {
                "valid": True,
                "status": 200,
                "isTimeout": False,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        },
        cache_path,
    )
    write_text(docs_tree / "external.md", "[Cached](https://cached.example.com)\n")
    checked: list[str] = []

    def fake_checker(url: str) -> dict[str, object]:
        checked.append(url)
        return {"valid": True, "status": 200, "isTimeout": False}

    summary = cl.validate_docs(
        check_internal=False,
        check_external=True,
        no_cache=True,
        docs_dir=docs_tree,
        cache_path=cache_path,
        output=io.StringIO(),
        external_checker=fake_checker,
    )

    assert summary.cache_hits == 0
    assert sorted(checked) == sorted(
        ["https://cached.example.com", "https://github.com"]
    )


def test_main_defaults_to_internal_and_external(monkeypatch: pytest.MonkeyPatch):
    captured: dict[str, object] = {}

    def fake_validate_docs(**kwargs):
        captured.update(kwargs)
        return cl.ValidationSummary(0, 0, [], 0, [], [], 0, 0)

    monkeypatch.setattr(cl, "validate_docs", fake_validate_docs)
    assert cl.main([]) == 0
    assert captured["check_internal"] is True
    assert captured["check_external"] is True
    assert captured["no_cache"] is False


def test_main_forwards_cli_flags(monkeypatch: pytest.MonkeyPatch):
    captured: dict[str, object] = {}

    def fake_validate_docs(**kwargs):
        captured.update(kwargs)
        return cl.ValidationSummary(0, 0, [], 0, [], [], 0, 0)

    monkeypatch.setattr(cl, "validate_docs", fake_validate_docs)
    assert cl.main(["--internal", "--no-cache"]) == 0
    assert captured["check_internal"] is True
    assert captured["check_external"] is False
    assert captured["no_cache"] is True
