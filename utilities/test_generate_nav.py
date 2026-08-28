"""Tests for utilities/generate_nav.py."""

import importlib.util
import sys
from pathlib import Path

MODULE_PATH = Path(__file__).parent / "generate_nav.py"
spec = importlib.util.spec_from_file_location("generate_nav", MODULE_PATH)
generate_nav = importlib.util.module_from_spec(spec)
sys.modules["generate_nav"] = generate_nav
spec.loader.exec_module(generate_nav)


def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_get_markdown_title_uses_frontmatter_title(tmp_path):
    test_file = tmp_path / "test-frontmatter.md"
    write_text(
        test_file,
        "---\n"
        "title: My Custom Title\n"
        "tags:\n"
        "    - Guide\n"
        "---\n\n"
        "# Heading Title\n",
    )
    assert generate_nav.get_markdown_title(test_file) == "My Custom Title"


def test_get_markdown_title_unquotes_frontmatter_title(tmp_path):
    test_file = tmp_path / "test-quoted.md"
    write_text(test_file, '---\ntitle: "Quoted: Title"\n---\n\n# Heading\n')
    assert generate_nav.get_markdown_title(test_file) == "Quoted: Title"


def test_get_markdown_title_falls_back_to_heading(tmp_path):
    test_file = tmp_path / "test-heading.md"
    write_text(test_file, "# Heading Only Title\n\nContent here.\n")
    assert generate_nav.get_markdown_title(test_file) == "Heading Only Title"


def test_get_markdown_title_returns_none_without_title(tmp_path):
    test_file = tmp_path / "test-empty.md"
    write_text(test_file, "Just some content without any title.\n")
    assert generate_nav.get_markdown_title(test_file) is None


def test_get_markdown_title_returns_none_for_missing_file(tmp_path):
    assert generate_nav.get_markdown_title(tmp_path / "missing.md") is None


def test_get_nav_order_reads_frontmatter_value(tmp_path):
    test_file = tmp_path / "test-nav-order.md"
    write_text(test_file, "---\ntitle: Ordered Page\nnav_order: 5\n---\n\n# Content\n")
    assert generate_nav.get_nav_order(test_file) == 5


def test_get_nav_order_returns_none_when_missing(tmp_path):
    test_file = tmp_path / "test-no-nav-order.md"
    write_text(test_file, "---\ntitle: Unordered Page\n---\n\n# Content\n")
    assert generate_nav.get_nav_order(test_file) is None


def test_get_nav_order_reads_first_frontmatter_key(tmp_path):
    test_file = tmp_path / "test-nav-first.md"
    write_text(test_file, "---\nnav_order: 1\ntitle: First Page\n---\n")
    assert generate_nav.get_nav_order(test_file) == 1


def test_get_nav_order_returns_none_for_missing_file(tmp_path):
    assert generate_nav.get_nav_order(tmp_path / "missing.md") is None


def test_protect_toml_string_wraps_in_quotes():
    assert generate_nav.protect_toml_string("Hello World") == '"Hello World"'


def test_protect_toml_string_escapes_internal_quotes():
    assert generate_nav.protect_toml_string('Say "Hello"') == '"Say \\"Hello\\""'


def test_protect_toml_string_escapes_backslashes():
    assert generate_nav.protect_toml_string(r"Path\To\File") == r'"Path\\To\\File"'


def test_protect_toml_string_escapes_quotes_and_backslashes():
    assert generate_nav.protect_toml_string(r'C:\Path "quoted"') == r'"C:\\Path \"quoted\""'


def test_convert_to_title_maps_known_names():
    assert generate_nav.convert_to_title("osw") == "OSW"
    assert generate_nav.convert_to_title("tdei") == "TDEI"
    assert generate_nav.convert_to_title("josm") == "JOSM"
    assert generate_nav.convert_to_title("opensidewalks") == "OpenSidewalks"
    assert generate_nav.convert_to_title("accessmap") == "AccessMap"
    assert generate_nav.convert_to_title("aviv-scoutroute") == "AVIV ScoutRoute"


def test_convert_to_title_returns_none_for_index_names():
    assert generate_nav.convert_to_title("index") is None
    assert generate_nav.convert_to_title("index.md") is None


def test_convert_to_title_formats_kebab_and_snake_case():
    assert generate_nav.convert_to_title("user-manual") == "User Manual"
    assert generate_nav.convert_to_title("my-great-guide") == "My Great Guide"
    assert generate_nav.convert_to_title("user_guide") == "User Guide"
    assert generate_nav.convert_to_title("my-guide.md") == "My Guide"


def test_build_navigation_toml_basic_structure(tmp_path):
    docs = tmp_path / "nav-test-docs"
    write_text(docs / "index.md", "---\ntitle: Home\n---\n\n# Welcome\n")
    write_text(docs / "my-section" / "index.md", "---\ntitle: My Section\n---\n")
    write_text(docs / "my-section" / "first-page.md", "---\ntitle: First Page\n---\n")

    nav = generate_nav.build_navigation_toml(docs)

    assert nav.startswith("nav = [")
    assert nav.endswith("]")
    assert '{"Home" = "index.md"}' in nav
    assert '{"My Section" = [' in nav
    assert '"my-section/index.md"' in nav
    assert '{"First Page" = "my-section/first-page.md"}' in nav


def test_update_zensical_nav_replaces_existing_section(tmp_path):
    test_toml = tmp_path / "test-update.toml"
    write_text(
        test_toml,
        "[project]\n"
        'site_name = "Test Site"\n\n'
        "nav = [\n"
        '  {"Old" = "old.md"},\n'
        "]\n\n"
        "[project.theme]\n"
        'language = "en"\n',
    )
    new_nav = 'nav = [\n  {"New" = "new.md"},\n]'

    changed = generate_nav.update_zensical_nav(test_toml, new_nav)
    content = test_toml.read_text(encoding="utf-8")

    assert changed is True
    assert '{"New" = "new.md"}' in content
    assert '{"Old" = "old.md"}' not in content
    assert 'site_name = "Test Site"' in content
    assert "[project.theme]" in content


def test_update_zensical_nav_returns_false_when_unchanged(tmp_path):
    test_toml = tmp_path / "test-no-change.toml"
    write_text(test_toml, '[project]\nnav = [\n  {"Same" = "same.md"},\n]\n')
    same_nav = 'nav = [\n  {"Same" = "same.md"},\n]'
    assert generate_nav.update_zensical_nav(test_toml, same_nav) is False


def test_generated_nav_uses_toml_inline_table_syntax(tmp_path):
    docs = tmp_path / "format-test-docs"
    write_text(docs / "index.md", "---\ntitle: Test Home\n---\n")
    nav = generate_nav.build_navigation_toml(docs)
    assert '{"Test Home" = "index.md"}' in nav
    assert "= '" not in nav
    assert nav.startswith("nav = [")
    assert nav.endswith("]")


def test_build_navigation_toml_handles_colons_in_titles(tmp_path):
    docs = tmp_path / "special-docs"
    write_text(docs / "index.md", "---\ntitle: Home\n---\n")
    write_text(docs / "special-guide.md", '---\ntitle: "Guide: Special Characters"\n---\n')
    nav = generate_nav.build_navigation_toml(docs)
    assert '"Guide: Special Characters"' in nav


def test_section_with_only_index_still_appears(tmp_path):
    docs = tmp_path / "empty-section-docs"
    write_text(docs / "index.md", "---\ntitle: Home\n---\n")
    write_text(docs / "empty-dir" / "index.md", "---\ntitle: Empty Section\n---\n")
    nav = generate_nav.build_navigation_toml(docs)
    assert '"empty-dir/index.md"' in nav


def test_resources_directory_is_excluded_from_navigation(tmp_path):
    docs = tmp_path / "resources-docs"
    write_text(docs / "index.md", "---\ntitle: Home\n---\n")
    (docs / "resources" / "images").mkdir(parents=True)
    nav = generate_nav.build_navigation_toml(docs)
    assert "resources" not in nav


def test_files_sort_by_nav_order_then_name(tmp_path):
    docs = tmp_path / "nav-order-docs"
    write_text(docs / "index.md", "---\ntitle: Home\n---\n")
    section = docs / "manual"
    write_text(section / "index.md", "---\ntitle: Manual\n---\n")
    write_text(section / "zebra.md", "---\ntitle: Zebra Page\n---\n")
    write_text(section / "beta.md", "---\ntitle: Second Page\nnav_order: 2\n---\n")
    write_text(section / "alpha.md", "---\ntitle: First Page\nnav_order: 1\n---\n")

    nav = generate_nav.build_navigation_toml(docs)

    alpha_pos = nav.index('"First Page"')
    beta_pos = nav.index('"Second Page"')
    zebra_pos = nav.index('"Zebra Page"')
    assert alpha_pos < beta_pos
    assert beta_pos < zebra_pos


def test_subdirectories_sort_by_nav_order_then_name(tmp_path):
    docs = tmp_path / "subdir-order-docs"
    write_text(docs / "index.md", "---\ntitle: Home\n---\n")
    topic = docs / "topic"
    write_text(topic / "index.md", "---\ntitle: Topic\n---\n")
    write_text(topic / "zdir" / "index.md", "---\ntitle: Zdir Section\n---\n")
    write_text(topic / "bdir" / "index.md", "---\ntitle: Bdir Section\nnav_order: 2\n---\n")
    write_text(topic / "adir" / "index.md", "---\ntitle: Adir Section\nnav_order: 1\n---\n")

    nav = generate_nav.build_navigation_toml(docs)

    adir_pos = nav.index('"Adir"')
    bdir_pos = nav.index('"Bdir"')
    zdir_pos = nav.index('"Zdir"')
    assert adir_pos < bdir_pos
    assert bdir_pos < zdir_pos


def test_integration_builds_nested_structure(tmp_path):
    docs = tmp_path / "integration-docs"
    write_text(docs / "index.md", "---\ntitle: TCAT Wiki\n---\n")
    write_text(docs / "opensidewalks" / "index.md", "---\ntitle: OpenSidewalks\n---\n")
    write_text(docs / "opensidewalks" / "schema" / "index.md", "---\ntitle: Schema\n---\n")
    write_text(
        docs / "opensidewalks" / "schema" / "core-edges-in-osw.md",
        "---\ntitle: Core Edges in OSW\n---\n",
    )
    write_text(docs / "tdei" / "index.md", "---\ntitle: TDEI\n---\n")

    nav = generate_nav.build_navigation_toml(docs)
    lines = nav.splitlines()
    first_entry = next(line for line in lines if "{" in line)

    assert nav.startswith("nav = [")
    assert nav.endswith("]")
    assert '"TCAT Wiki"' in first_entry
    assert '{"OpenSidewalks" = [' in nav
    assert '{"Schema" = [' in nav
    assert '{"TDEI" = [' in nav
