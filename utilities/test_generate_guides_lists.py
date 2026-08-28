"""Pytest suite for utilities/generate_guides_lists.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).parent / "generate_guides_lists.py"
spec = importlib.util.spec_from_file_location("generate_guides_lists", MODULE_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f"could not load module spec from {MODULE_PATH}")
ggl = importlib.util.module_from_spec(spec)
sys.modules["generate_guides_lists"] = ggl
spec.loader.exec_module(ggl)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def write_md(
    path: Path,
    *,
    title: str,
    tags: list[str] | None = None,
    nav_order: int | None = None,
    exclude_parent: bool = False,
    exclude_main: bool = False,
    heading_level: int = 1,
    body: str = "",
    line_ending: str = "\r\n",
) -> None:
    lines = ["---", f"title: {title}"]
    if tags is not None:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"    - {tag}")
    if exclude_parent:
        lines.append(f"# {ggl.EXCLUDE_PARENT_FLAG}")
    if exclude_main:
        lines.append(f"# {ggl.EXCLUDE_MAIN_FLAG}")
    if nav_order is not None:
        lines.append(f"nav_order: {nav_order}")
    lines.append("---")
    lines.append("")
    heading = "#" * heading_level
    lines.append(f"{heading} {title}")
    if body:
        lines.append("")
        lines.extend(body.splitlines())
    write_text(path, line_ending.join(lines))


@pytest.fixture
def docs_root(tmp_path):
    docs = tmp_path / "docs"
    (docs / "guides-list").mkdir(parents=True)
    write_md(docs / "guides-list" / "index.md", title="Guides List", body="")
    return docs


def test_get_guide_info_detects_guide(tmp_path):
    file_path = tmp_path / "guide.md"
    write_md(file_path, title="Test Guide", tags=["Guide"], body="This is a test guide.")
    info = ggl.get_guide_info(file_path)
    assert info.is_guide is True
    assert info.is_user_manual is False
    assert info.is_tutorial is False
    assert info.title == "Test Guide"


def test_get_guide_info_detects_user_manual(tmp_path):
    file_path = tmp_path / "manual.md"
    write_md(file_path, title="Test User Manual", tags=["User Manual", "External"])
    info = ggl.get_guide_info(file_path)
    assert info.is_guide is True
    assert info.is_user_manual is True
    assert info.is_tutorial is False


def test_get_guide_info_detects_tutorial_and_preserves_quoted_title(tmp_path):
    file_path = tmp_path / "tutorial.md"
    write_md(file_path, title='"Test Task"', tags=["Tutorial", "External"], body="This is a test tutorial.")
    info = ggl.get_guide_info(file_path)
    assert info.is_guide is True
    assert info.is_tutorial is True
    assert info.is_user_manual is False
    assert info.title == '"Test Task"'


def test_get_guide_info_non_guide(tmp_path):
    file_path = tmp_path / "page.md"
    write_md(file_path, title="Regular Page", body="This is not a guide.")
    info = ggl.get_guide_info(file_path)
    assert info.is_guide is False
    assert info.is_user_manual is False
    assert info.is_tutorial is False


@pytest.mark.parametrize(
    ("exclude_parent", "exclude_main"),
    [(True, False), (False, True), (True, True)],
)
def test_get_guide_info_exclusion_flags(tmp_path, exclude_parent, exclude_main):
    file_path = tmp_path / "excluded.md"
    write_md(
        file_path,
        title="Excluded Guide",
        tags=["Guide"],
        exclude_parent=exclude_parent,
        exclude_main=exclude_main,
    )
    info = ggl.get_guide_info(file_path)
    assert info.exclude_from_parent is exclude_parent
    assert info.exclude_from_main is exclude_main


def test_get_guide_info_does_not_treat_flags_as_tags(tmp_path):
    file_path = tmp_path / "wrong-format.md"
    write_text(
        file_path,
        "---\r\n"
        "title: Incorrectly Formatted Exclusions\r\n"
        "tags:\r\n"
        "    - Guide\r\n"
        "    - exclude-from-parent-guides-list\r\n"
        "    - exclude-from-main-guides-list\r\n"
        "---\r\n\r\n"
        "# Incorrectly Formatted Exclusions\r\n",
    )
    info = ggl.get_guide_info(file_path)
    assert info.is_guide is True
    assert info.exclude_from_parent is False
    assert info.exclude_from_main is False


def test_get_guide_info_nav_order_and_missing_file(tmp_path):
    ordered = tmp_path / "ordered.md"
    write_md(ordered, title="Ordered Guide", tags=["Guide"], nav_order=3)
    assert ggl.get_guide_info(ordered).nav_order == 3
    assert ggl.get_guide_info(tmp_path / "missing.md") == ggl.GuideInfo()


def test_get_guide_info_extracts_description(tmp_path):
    file_path = tmp_path / "description.md"
    write_text(
        file_path,
        "---\r\n"
        "title: Guide With Description\r\n"
        "tags:\r\n"
        "    - Guide\r\n"
        "---\r\n\r\n"
        "## Guide With Description\r\n\r\n"
        "This is the description text that should be extracted.\r\n\r\n"
        "_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../guides-list/index.md)._\r\n",
    )
    assert ggl.get_guide_info(file_path).description == "This is the description text that should be extracted."


def test_get_guide_info_handles_lf_and_crlf_line_endings(tmp_path):
    lf_file = tmp_path / "lf.md"
    crlf_file = tmp_path / "crlf.md"
    write_text(lf_file, "---\ntitle: LF Guide\ntags:\n    - Guide\n---\n\n# LF Guide")
    write_text(crlf_file, "---\r\ntitle: CRLF Guide\r\ntags:\r\n    - Guide\r\n---\r\n\r\n# CRLF Guide")
    assert ggl.get_guide_info(lf_file).title == "LF Guide"
    assert ggl.get_guide_info(crlf_file).title == "CRLF Guide"


def test_get_guide_info_handles_special_characters_and_multiple_tags(tmp_path):
    colon = tmp_path / "colon.md"
    quotes = tmp_path / "quotes.md"
    multi = tmp_path / "multi.md"
    write_md(colon, title='"Guide: With Colon"', tags=["Guide"])
    write_md(quotes, title='Guide "With" Quotes', tags=["Guide"])
    write_md(multi, title="Multi Tag Guide", tags=["Guide", "External", "User", "OSW 0.4"])
    assert ggl.get_guide_info(colon).title == '"Guide: With Colon"'
    assert "Quotes" in ggl.get_guide_info(quotes).title
    assert ggl.get_guide_info(multi).is_guide is True


def test_get_directory_title(tmp_path):
    index_path = tmp_path / "index.md"
    write_md(index_path, title="Directory Title", body="Heading", heading_level=1)
    assert ggl.get_directory_title(index_path) == "Directory Title"
    assert ggl.get_directory_title(tmp_path / "missing.md") == ""


def test_is_user_manual_and_tutorial_directory(tmp_path):
    manual_dir = tmp_path / "manual"
    regular_dir = tmp_path / "regular"
    tutorial_dir = tmp_path / "tutorial-dir"
    write_md(manual_dir / "index.md", title="Manual", tags=["User Manual"])
    write_md(regular_dir / "index.md", title="Regular")
    write_md(tutorial_dir / "index.md", title='"Test Tutorial"', tags=["Tutorial"])
    assert ggl.is_user_manual_directory(manual_dir) is True
    assert ggl.is_user_manual_directory(regular_dir) is False
    assert ggl.is_tutorial_directory(tutorial_dir) is True
    assert ggl.is_tutorial_directory(manual_dir) is False


def test_get_relative_markdown_path_uses_forward_slashes():
    assert ggl.get_relative_markdown_path(Path(r"C:\docs\section"), Path(r"C:\docs\section\page.md")) == "page.md"
    assert ggl.get_relative_markdown_path(Path(r"C:\docs\section\subsection"), Path(r"C:\docs\other\page.md")) == "../../other/page.md"


def test_get_guides_in_directory_basic_sorting(tmp_path):
    root = tmp_path / "guides"
    write_md(root / "index.md", title="Section Index")
    write_md(root / "alpha-guide.md", title="Alpha Guide", tags=["Guide"])
    write_md(root / "beta-guide.md", title="Beta Guide", tags=["Guide"])
    write_md(root / "not-a-guide.md", title="Regular Page")
    result = ggl.get_guides_in_directory(root, exclude_own_index=True, exclude_flag=ggl.EXCLUDE_PARENT_FLAG)
    assert [path.name for path in result] == ["alpha-guide.md", "beta-guide.md"]


def test_get_guides_in_directory_orders_user_manual_when_index_is_included(tmp_path):
    root = tmp_path / "manual-guides"
    write_md(root / "index.md", title="Test User Manual", tags=["User Manual"])
    write_md(root / "um-sub-guide.md", title="UM Sub Guide", tags=["Guide"])
    result = ggl.get_guides_in_directory(root, exclude_own_index=False, exclude_flag=ggl.EXCLUDE_PARENT_FLAG)
    assert [path.name for path in result] == ["index.md", "um-sub-guide.md"]


def test_get_guides_in_directory_orders_nav_order_before_unordered(tmp_path):
    root = tmp_path / "ordered-guides"
    write_md(root / "index.md", title="Section Index")
    write_md(root / "zebra-guide.md", title="Zebra Guide", tags=["Guide"])
    write_md(root / "beta-guide.md", title="Second Guide", tags=["Guide"], nav_order=2)
    write_md(root / "alpha-guide.md", title="First Guide", tags=["Guide"], nav_order=1)
    result = ggl.get_guides_in_directory(root, exclude_own_index=True, exclude_flag=ggl.EXCLUDE_PARENT_FLAG)
    assert [path.name for path in result] == ["alpha-guide.md", "beta-guide.md", "zebra-guide.md"]


def test_get_guides_in_directory_discovers_tutorials_in_tutorial_subdir(tmp_path):
    root = tmp_path / "tutorial-guides"
    write_md(root / "index.md", title="Section Index")
    write_md(root / "regular-guide.md", title="Regular Guide", tags=["Guide"])
    write_md(root / "tutorial" / "do-something.md", title='"Do Something"', tags=["Tutorial"])
    result = ggl.get_guides_in_directory(root, exclude_own_index=True, exclude_flag=ggl.EXCLUDE_PARENT_FLAG)
    assert [path.name for path in result] == ["do-something.md", "regular-guide.md"]


def test_get_guides_in_directory_orders_tutorials_user_manuals_and_regular_guides(tmp_path):
    root = tmp_path / "all-types"
    write_md(root / "index.md", title="Test User Manual", tags=["User Manual"])
    write_md(root / "tutorial-something.md", title='"Something"', tags=["Tutorial"])
    write_md(root / "regular-guide.md", title="Regular Guide", tags=["Guide"])
    result = ggl.get_guides_in_directory(root, exclude_own_index=False, exclude_flag=ggl.EXCLUDE_PARENT_FLAG)
    assert [path.name for path in result] == ["tutorial-something.md", "index.md", "regular-guide.md"]


def test_get_guides_in_directory_discovers_multi_page_tutorial_indexes_only(tmp_path):
    root = tmp_path / "multi-page"
    write_md(root / "index.md", title="Section Index")
    write_md(root / "regular-guide.md", title="Regular Guide", tags=["Guide"])
    write_md(root / "tutorial" / "single-tutorial.md", title='"Single File Tutorial"', tags=["Tutorial"])
    write_md(root / "tutorial" / "multi-tutorial" / "index.md", title='"Multi-Page Tutorial"', tags=["Tutorial"])
    write_md(root / "tutorial" / "multi-tutorial" / "subpage.md", title="Subpage", tags=["Guide"])
    result = ggl.get_guides_in_directory(root, exclude_own_index=True, exclude_flag=ggl.EXCLUDE_PARENT_FLAG)
    assert len(result) == 3
    assert result[-1].name == "regular-guide.md"
    assert sum(path.parent.name == "multi-tutorial" for path in result) == 1


def test_get_subdirectories_exclusions_and_order(tmp_path):
    root = tmp_path / "subdirs"
    write_md(root / "regular-section" / "index.md", title="Regular Section")
    write_md(root / "user-manual" / "index.md", title="User Manual", tags=["User Manual"])
    write_md(root / "resources" / "index.md", title="Resources")
    write_md(root / "tutorial" / "index.md", title="Tutorials")
    (root / "no-index").mkdir(parents=True)
    result = ggl.get_subdirectories(root)
    assert [path.name for path in result] == ["user-manual", "regular-section"]


def test_get_subdirectories_orders_tutorial_user_manual_regular_and_nav_order(tmp_path):
    root = tmp_path / "ordered-subdirs"
    write_md(root / "regular-section" / "index.md", title="Regular Section")
    write_md(root / "user-manual" / "index.md", title="User Manual", tags=["User Manual"], nav_order=2)
    write_md(root / "my-tutorial" / "index.md", title='"My Tutorial"', tags=["Tutorial"], nav_order=1)
    result = ggl.get_subdirectories(root)
    assert [path.name for path in result] == ["my-tutorial", "user-manual", "regular-section"]


def test_build_guide_entry_and_section_header(tmp_path):
    root = tmp_path / "entries"
    write_text(
        root.joinpath("test-guide.md"),
        "---\r\n"
        "title: Test Entry Guide\r\n"
        "tags:\r\n"
        "    - Guide\r\n"
        "---\r\n\r\n"
        "## Test Entry Guide\r\n\r\n"
        "This is the description.\r\n\r\n"
        "_For a list of all guides\r\n",
    )
    guide_file = root / "test-guide.md"
    entry = ggl.build_guide_entry(guide_file, root, "####")
    assert "#### [Test Entry Guide](test-guide.md)" in entry
    assert "This is the description." in entry

    write_md(root / "index.md", title="Test Section")
    header = ggl.build_section_header("Test Section", root / "index.md", tmp_path, "####", False)
    manual_header = ggl.build_section_header("Test Section", root / "index.md", tmp_path, "####", True)
    assert "#### [Test Section](" in header and " Guides" in header
    assert "Guides" not in manual_header


def test_get_all_guides_at_level_orders_types_and_includes_expected_fields(tmp_path):
    root = tmp_path / "all-guides"
    write_md(root / "index.md", title="All Guides Section")
    write_md(root / "regular-guide.md", title="Regular Guide", tags=["Guide"])
    write_md(root / "tutorial-test.md", title='"Test Task"', tags=["Tutorial"])
    write_md(root / "user-manual" / "index.md", title="Sub User Manual", tags=["User Manual"])
    result = ggl.get_all_guides_at_level(root, ggl.EXCLUDE_PARENT_FLAG, [root / "user-manual"])
    assert [entry.type for entry in result] == ["Tutorial", "UserManual", "Guide"]
    assert all(entry.path for entry in result)
    assert all(entry.info for entry in result)
    assert next(entry for entry in result if entry.type == "Tutorial").file is not None
    assert next(entry for entry in result if entry.type == "Guide").file is not None


def test_get_all_guides_at_level_detects_direct_tutorial_directories(tmp_path):
    root = tmp_path / "all-guides-tutorial-dir"
    write_md(root / "index.md", title="Test Section")
    write_md(root / "regular-guide.md", title="Regular Guide", tags=["Guide"])
    write_md(root / "my-tutorial" / "index.md", title='"Multi-Page Tutorial"', tags=["Tutorial"])
    write_md(root / "user-manual" / "index.md", title="Sub User Manual", tags=["User Manual"])
    result = ggl.get_all_guides_at_level(root, ggl.EXCLUDE_PARENT_FLAG, [root / "my-tutorial", root / "user-manual"])
    assert [entry.type for entry in result] == ["Tutorial", "UserManual", "Guide"]
    tutorial_entry = next(entry for entry in result if entry.type == "Tutorial")
    assert tutorial_entry.path.parent.name == "my-tutorial"
    assert tutorial_entry.file and tutorial_entry.file.name == "index.md"


def test_update_parent_guides_section_generates_guides_and_table_of_contents(docs_root):
    topic = docs_root / "test-topic"
    write_md(topic / "index.md", title="Test Topic", body="This is a test topic.")
    write_md(topic / "topic-guide.md", title="Topic Guide", tags=["Guide"], body="This guide is about the topic.")
    write_md(topic / "tutorial" / "test-something.md", title='"Test Something"', tags=["Tutorial"], body="This is a tutorial guide.")
    write_md(topic / "user-manual" / "index.md", title="Topic User Manual", tags=["User Manual"], body="This is the user manual.")
    write_md(topic / "user-manual" / "chapter.md", title="Manual Chapter", tags=["Guide"], body="This is a chapter.")

    changed = ggl.update_parent_guides_section(topic, docs_root)
    assert changed is True
    topic_text = ggl.read_text(topic / "index.md")
    assert "### Guides" in topic_text
    assert "Test Topic Guides" in topic_text
    assert "#### Tutorials" in topic_text
    assert "##### [\"Test Something\"](tutorial/test-something.md)" in topic_text
    assert "#### [Topic User Manual](user-manual/index.md)" in topic_text
    assert "#### [Topic Guide](topic-guide.md)" in topic_text

    changed_manual = ggl.update_parent_guides_section(topic / "user-manual", docs_root)
    assert changed_manual is True
    manual_text = ggl.read_text(topic / "user-manual" / "index.md")
    assert "### Table of Contents" in manual_text
    assert "Topic User Manual Table of Contents" in manual_text
    assert "Guides List" not in manual_text
    assert "#### [Manual Chapter](chapter.md)" in manual_text


def test_update_parent_guides_section_handles_subdir_with_only_guide_index(docs_root):
    parent = docs_root / "parent"
    child = parent / "jobs"
    write_md(parent / "index.md", title="Parent")
    write_md(child / "index.md", title="Jobs", tags=["Guide"], body="Jobs overview.")
    write_md(child / "hidden.md", title="Hidden", tags=["Guide"], exclude_parent=True)
    changed = ggl.update_parent_guides_section(parent, docs_root)
    assert changed is True
    text = ggl.read_text(parent / "index.md")
    assert "#### [Jobs](jobs/index.md)" in text


def test_build_main_guides_list_hierarchical_output(docs_root):
    topic = docs_root / "test-topic"
    write_md(topic / "index.md", title="Test Topic", body="This is a test topic.")
    write_md(topic / "topic-guide.md", title="Topic Guide", tags=["Guide"], body="This guide is about the topic.")
    write_md(topic / "tutorial" / "test-something.md", title='"Test Something"', tags=["Tutorial"], body="This is a tutorial guide.")
    write_md(topic / "user-manual" / "index.md", title="Topic User Manual", tags=["User Manual"], body="This is the user manual.")
    write_md(topic / "user-manual" / "chapter.md", title="Manual Chapter", tags=["Guide"], body="This is a chapter.")
    write_md(topic / "subsection" / "index.md", title="Subsection", body="Subsection description.")
    write_md(topic / "subsection" / "sub-guide.md", title="Sub Guide", tags=["Guide"], body="Sub guide description.")
    all_dirs = ggl.find_directories_with_index(docs_root)

    content = ggl.build_main_guides_list(all_dirs, docs_root)
    assert content.startswith("---\r\ntitle: Guides List\r\n---\r\n")
    assert "### [Test Topic](../test-topic/index.md)" in content
    assert "#### Tutorials" in content
    assert "##### [\"Test Something\"](../test-topic/tutorial/test-something.md)" in content
    assert "#### [Topic User Manual](../test-topic/user-manual/index.md)" in content
    assert "#### [Topic Guide](../test-topic/topic-guide.md)" in content
    assert "#### [Subsection](../test-topic/subsection/index.md) Guides" in content
    assert "##### [Sub Guide](../test-topic/subsection/sub-guide.md)" in content


def test_run_end_to_end_writes_guides_list_and_parent_sections(docs_root):
    topic = docs_root / "test-topic"
    write_md(topic / "index.md", title="Test Topic", body="This is a test topic.")
    write_md(topic / "guide.md", title="Guide", tags=["Guide"])
    result = ggl.run(docs_root)
    assert result["directories_with_index"] == 2
    assert result["updated_parent_sections"] >= 1
    assert "### Guides" in ggl.read_text(topic / "index.md")
    assert "## Guides List" in ggl.read_text(docs_root / "guides-list" / "index.md")
