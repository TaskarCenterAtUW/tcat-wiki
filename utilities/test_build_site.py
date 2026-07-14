"""Pytest suite for utilities/build-site.py.

Uses temp fixture trees (never the real docs/) to validate each pipeline
step independently, plus the end-to-end prepare() orchestration (excluding
the actual `zensical build`/`serve` subprocess calls, which are out of scope
for unit tests).
"""

import importlib.util
import sys
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).parent / "build-site.py"
spec = importlib.util.spec_from_file_location("build_site", MODULE_PATH)
bs = importlib.util.module_from_spec(spec)
sys.modules["build_site"] = bs
spec.loader.exec_module(bs)


def write_page(path: Path, publication_status: str | None = None, body: str = "# Title\n\nBody.\n"):
    path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = "---\ntitle: Test\n"
    if publication_status is not None:
        frontmatter += f"publication_status: {publication_status}\n"
    frontmatter += "---\n\n"
    path.write_text(frontmatter + body, encoding="utf-8")


@pytest.fixture
def fixture_docs(tmp_path):
    """Build a small docs/ tree mirroring the real repo's relevant shape."""
    docs = tmp_path / "docs"

    # Non-assistant page, never touched by the filter.
    write_page(docs / "index.md",
               body="# Welcome\n\n![Logo](resources/logo.png)\n")

    # Assistant top-level peers.
    write_page(docs / "assistant" / "index.md",
               publication_status="published", body="# Assistant\n\n<!-- @format -->\n\nBody.\n")
    write_page(docs / "assistant" / "schema.md",
               publication_status="published")
    write_page(docs / "assistant" / "dispatch.md", publication_status="draft")

    # Topic "alpha": published index + a published concept page (linked from index)
    # + a stub concept page.
    write_page(
        docs / "assistant" / "alpha" / "index.md",
        publication_status="published",
        body="# Alpha\n\nSee [published page](concept/published-page.md).\n",
    )
    write_page(docs / "assistant" / "alpha" / "concept" / "published-page.md",
               publication_status="published")
    write_page(docs / "assistant" / "alpha" / "concept" / "stub-page.md",
               publication_status="stub")

    # assistant/support/ - always removed regardless of publication status.
    write_page(docs / "assistant" / "support" / "index.md",
               publication_status="published")

    return docs


def test_copy_layers_does_not_mutate_source(tmp_path, fixture_docs):
    human_dir = tmp_path / "human-docs"
    agent_dir = tmp_path / "agent-docs"
    original_files = sorted(p.relative_to(fixture_docs)
                            for p in fixture_docs.rglob("*.md"))

    bs.copy_layers(fixture_docs, human_dir, agent_dir)

    after_files = sorted(p.relative_to(fixture_docs)
                         for p in fixture_docs.rglob("*.md"))
    assert original_files == after_files
    assert (human_dir / "assistant" / "support" / "index.md").exists()
    assert (agent_dir / "assistant" / "support" / "index.md").exists()


def test_filter_removes_support_and_non_published(tmp_path, fixture_docs):
    human_dir = tmp_path / "human-docs"
    bs.copy_layers(fixture_docs, human_dir, tmp_path / "agent-docs")

    info = bs.filter_human_docs(human_dir)

    assert not (human_dir / "assistant" / "support").exists()
    assert not (human_dir / "assistant" / "alpha" /
                "concept" / "stub-page.md").exists()
    assert not (human_dir / "assistant" / "dispatch.md").exists()  # draft
    assert (human_dir / "assistant" / "alpha" /
            "concept" / "published-page.md").exists()
    assert (human_dir / "assistant" / "alpha" / "index.md").exists()
    assert "assistant/support/index.md" in info["removed"]
    assert "assistant/dispatch.md" in info["removed"]


def test_filter_fails_when_published_page_links_to_removed_page(tmp_path, fixture_docs):
    # Make the alpha index link to the stub page (which will be removed).
    write_page(
        fixture_docs / "assistant" / "alpha" / "index.md",
        publication_status="published",
        body="# Alpha\n\nSee [stub page](concept/stub-page.md).\n",
    )
    human_dir = tmp_path / "human-docs"
    bs.copy_layers(fixture_docs, human_dir, tmp_path / "agent-docs")

    with pytest.raises(bs.HumanDocsValidationError) as excinfo:
        bs.filter_human_docs(human_dir)

    assert len(excinfo.value.errors) == 1
    offending_page, link_target = excinfo.value.errors[0]
    assert offending_page.endswith("alpha/index.md")
    assert link_target == "concept/stub-page.md"


def test_filter_passes_when_links_only_target_published_pages(tmp_path, fixture_docs):
    human_dir = tmp_path / "human-docs"
    bs.copy_layers(fixture_docs, human_dir, tmp_path / "agent-docs")
    # Should not raise: alpha/index.md only links to published-page.md.
    bs.filter_human_docs(human_dir)


def test_agent_docs_retains_all_statuses_and_dispatch(tmp_path, fixture_docs):
    agent_dir = tmp_path / "agent-docs"
    bs.copy_layers(fixture_docs, tmp_path / "human-docs", agent_dir)

    assert (agent_dir / "assistant" / "support" / "index.md").exists()
    assert (agent_dir / "assistant" / "alpha" /
            "concept" / "stub-page.md").exists()

    output_path = bs.generate_dispatch(agent_dir)
    assert output_path == agent_dir / "assistant" / "dispatch.md"
    content = output_path.read_text(encoding="utf-8")
    assert "GENERATED FILE" in content
    assert "`stub-page.md`" in content
    assert "`published-page.md`" in content


def test_strip_removes_images_pragma_and_slider(tmp_path):
    text = (
        "# Title\n\n"
        "<!-- @format -->\n\n"
        "![alt text](path/to/image.png)\n\n"
        "Some prose with an inline ![alt](x.png) image.\n\n"
        "<img-comparison-slider>\n"
        "<img slot=\"first\" src=\"a.png\">\n"
        "<img slot=\"second\" src=\"b.png\">\n"
        "</img-comparison-slider>\n\n"
        "## Admonition\n\n"
        "!!! note\n"
        "    This should remain untouched.\n"
    )
    stripped = bs.strip_markdown_text(text)
    assert "@format" not in stripped
    assert "![" not in stripped
    assert "<img-comparison-slider>" not in stripped
    assert "!!! note" in stripped
    assert "This should remain untouched." in stripped


def test_strip_agent_docs_applies_to_all_files(tmp_path, fixture_docs):
    agent_dir = tmp_path / "agent-docs"
    bs.copy_layers(fixture_docs, tmp_path / "human-docs", agent_dir)

    bs.strip_agent_docs(agent_dir)

    assistant_index = (agent_dir / "assistant" /
                       "index.md").read_text(encoding="utf-8")
    assert "@format" not in assistant_index

    root_index = (agent_dir / "index.md").read_text(encoding="utf-8")
    assert "![Logo]" not in root_index


def test_write_build_config_overrides_docs_dir_only(tmp_path):
    source_config = tmp_path / "zensical.toml"
    source_config.write_text(
        '[project]\nsite_name = "Test Site"\nsite_url = "https://example.com/"\n',
        encoding="utf-8",
    )
    build_config = tmp_path / "zensical.build.toml"

    bs.write_build_config(source_config, build_config,
                          docs_dir_name="human-docs")

    import tomlkit
    doc = tomlkit.parse(build_config.read_text(encoding="utf-8"))
    assert doc["project"]["docs_dir"] == "human-docs"
    assert doc["project"]["site_name"] == "Test Site"
    assert doc["project"]["site_url"] == "https://example.com/"


def test_overlay_agent_layer_places_files_at_expected_paths(tmp_path, fixture_docs):
    agent_dir = tmp_path / "agent-docs"
    site_dir = tmp_path / "site"
    bs.copy_layers(fixture_docs, tmp_path / "human-docs", agent_dir)
    write_page(agent_dir / "accessmap" / "index.md", body="# AccessMap\n")
    site_dir.mkdir()

    copied = bs.overlay_agent_layer(agent_dir, site_dir)

    assert "assistant/support/index.md" in copied
    assert (site_dir / "assistant" / "support" / "index.md").exists()
    assert (site_dir / "index.md").exists()
    # navigation.indexes may publish the human page at /accessmap/, but the
    # agent layer preserves its docs-relative source path for a stable URL.
    assert "accessmap/index.md" in copied
    assert (site_dir / "accessmap" / "index.md").exists()


def test_clean_generated_removes_existing_artifacts(tmp_path):
    human_dir = tmp_path / "human-docs"
    agent_dir = tmp_path / "agent-docs"
    build_config = tmp_path / "zensical.build.toml"
    human_dir.mkdir()
    agent_dir.mkdir()
    build_config.write_text("stale", encoding="utf-8")

    bs.clean_generated(human_dir, agent_dir, build_config)

    assert not human_dir.exists()
    assert not agent_dir.exists()
    assert not build_config.exists()


def test_prepare_end_to_end(tmp_path, fixture_docs):
    human_dir = tmp_path / "human-docs"
    agent_dir = tmp_path / "agent-docs"
    source_config = tmp_path / "zensical.toml"
    source_config.write_text(
        '[project]\nsite_name = "Test Site"\n', encoding="utf-8")
    build_config = tmp_path / "zensical.build.toml"

    bs.prepare(fixture_docs, human_dir, agent_dir, source_config, build_config)

    assert not (human_dir / "assistant" / "support").exists()
    assert (agent_dir / "assistant" / "support").exists()
    assert (agent_dir / "assistant" / "dispatch.md").exists()
    assert build_config.exists()
    import tomlkit
    doc = tomlkit.parse(build_config.read_text(encoding="utf-8"))
    assert doc["project"]["docs_dir"] == "human-docs"


def test_prepare_raises_on_broken_link(tmp_path, fixture_docs):
    write_page(
        fixture_docs / "assistant" / "alpha" / "index.md",
        publication_status="published",
        body="# Alpha\n\nSee [stub page](concept/stub-page.md).\n",
    )
    source_config = tmp_path / "zensical.toml"
    source_config.write_text(
        '[project]\nsite_name = "Test Site"\n', encoding="utf-8")

    with pytest.raises(bs.HumanDocsValidationError):
        bs.prepare(
            fixture_docs,
            tmp_path / "human-docs",
            tmp_path / "agent-docs",
            source_config,
            tmp_path / "zensical.build.toml",
        )


def test_main_handles_keyboard_interrupt_during_prepare(monkeypatch, capsys):
    def interrupt():
        raise KeyboardInterrupt

    monkeypatch.setattr(bs, "prepare", interrupt)

    assert bs.main([]) == 130
    assert capsys.readouterr().err == "\nOperation canceled.\n"


def test_main_handles_keyboard_interrupt_during_serve(monkeypatch, capsys):
    def interrupt():
        raise KeyboardInterrupt

    monkeypatch.setattr(bs, "prepare", lambda: None)
    monkeypatch.setattr(bs, "run_zensical_serve", interrupt)

    assert bs.main(["--serve"]) == 130
    assert capsys.readouterr().err == "\nOperation canceled.\n"
