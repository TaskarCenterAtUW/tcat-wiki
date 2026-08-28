#!/usr/bin/env python3
"""generate_nav.py - Generate and update the Zensical nav structure in zensical.toml.

Scans the docs directory structure, extracts Markdown titles from frontmatter
or fallback H1 headings, builds Zensical's TOML nav array-of-objects, and
updates the `nav = [...]` section in the repository's zensical.toml while
preserving all other file content unchanged.
"""

# Name: TCAT Wiki - Navigation Section Generator
# Version: 5.0.1
# Date: 2026-05-07
# Author: Amy Bordenave, Taskar Center for Accessible Technology, University of Washington
# License: CC-BY-ND 4.0 International

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.resolve()
DEFAULT_DOCS_DIR = REPO_ROOT / "docs"
DEFAULT_ZENSICAL_PATH = REPO_ROOT / "zensical.toml"
OUTPUT_NEWLINE = "\r\n"

TITLE_MAP = {
    "osw": "OSW",
    "tdei": "TDEI",
    "josm": "JOSM",
    "aviv-scoutroute": "AVIV ScoutRoute",
    "accessmap": "AccessMap",
    "walksheds": "Walksheds",
    "tdei-walkshed": "TDEI Walkshed",
    "tdei-workspaces": "TDEI Workspaces",
    "opensidewalks": "OpenSidewalks",
    "tdei-core": "TDEI Core",
    "rapid": "Rapid",
    "workspaces": "Workspaces",
    "index": "",
    "os-connect": "OS-CONNECT",
    "assistant": "Knowledge Base",
}

FRONTMATTER_RE = re.compile(r"(?s)^---\r?\n(.*?)\r?\n---")
TITLE_RE = re.compile(r"title:\s*(.+)")
NAV_ORDER_RE = re.compile(r"nav_order:\s*(\d+)")
HEADING_RE = re.compile(r"^#\s+(.+)")
NAV_SECTION_RE = re.compile(r"(?ms)^nav\s*=\s*\[.*?^\]")
NAV_COMMENT_RE = re.compile(r"(?ms)(#.*nav.*\r?\n(?:#.*\r?\n)*)")
THEME_SECTION_RE = re.compile(r"(?m)^\[project\.theme\]")


def get_markdown_title(file_path):
    """Return a Markdown title from frontmatter or the first top-level heading."""
    try:
        content = Path(file_path).read_text(encoding="utf-8")
    except OSError:
        return None

    frontmatter_match = FRONTMATTER_RE.search(content)
    if frontmatter_match:
        title_match = TITLE_RE.search(frontmatter_match.group(1))
        if title_match:
            return title_match.group(1).strip().strip('"').strip("'")

    heading_match = HEADING_RE.search(content)
    if heading_match:
        return heading_match.group(1).strip()

    return None


def protect_toml_string(text):
    """Return text wrapped as a TOML basic string with quotes and backslashes escaped."""
    escaped = text.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    return f'"{escaped}"'


def convert_to_title(name):
    """Convert a file or directory name to a display title."""
    base_name = Path(name).stem
    mapped = TITLE_MAP.get(base_name.lower())
    if mapped is not None:
        return mapped or None
    result = base_name.replace("-", " ").replace("_", " ").lower().title()
    return result


def get_nav_order(file_path):
    """Return nav_order from Markdown frontmatter, or None if absent."""
    try:
        content = Path(file_path).read_text(encoding="utf-8")
    except OSError:
        return None

    frontmatter_match = FRONTMATTER_RE.search(content)
    if not frontmatter_match:
        return None

    nav_order_match = NAV_ORDER_RE.search(frontmatter_match.group(1))
    if not nav_order_match:
        return None
    return int(nav_order_match.group(1))


def get_preferred_title(file_path, base_name):
    """Return mapped title first, then frontmatter title, then a derived title."""
    mapped = TITLE_MAP.get(base_name.lower())
    if mapped:
        return mapped

    frontmatter_title = get_markdown_title(file_path)
    if frontmatter_title:
        return frontmatter_title

    return convert_to_title(base_name)


def _relative_docs_path(path, docs_base_path):
    """Return a docs-relative path using forward slashes."""
    docs_root = Path(docs_base_path).resolve()
    target = Path(path).resolve()
    return str(target)[len(str(docs_root)) + 1:].replace("\\", "/")


def _sort_nav_entries(entries):
    """Sort PowerShell-style by nav_order (missing last), then by name."""
    return sorted(
        entries,
        key=lambda entry: (
            entry["nav_order"] if entry["nav_order"] is not None else sys.maxsize,
            entry["name"],
        ),
    )


def build_directory_nav(dir_path, indent_level=1, docs_base_path=None):
    """Return TOML navigation lines for one directory subtree."""
    dir_path = Path(dir_path)
    docs_base_path = Path(docs_base_path)
    items = []
    indent = "    " * indent_level
    child_indent = "    " * (indent_level + 1)

    dir_name = dir_path.name
    relative_path = _relative_docs_path(dir_path, docs_base_path)
    dir_title = convert_to_title(dir_name)

    index_file = dir_path / "index.md"
    has_index = index_file.exists()

    subdirs = []
    for subdir in sorted((child for child in dir_path.iterdir() if child.is_dir()), key=lambda p: p.name):
        if subdir.name == "resources":
            continue
        index_path = subdir / "index.md"
        subdirs.append(
            {
                "directory": subdir,
                "name": subdir.name,
                "nav_order": get_nav_order(index_path) if index_path.exists() else None,
            }
        )
    subdirs = [entry["directory"] for entry in _sort_nav_entries(subdirs)]

    markdown_files = []
    for md_file in sorted(dir_path.glob("*.md"), key=lambda p: p.name):
        if md_file.name == "index.md":
            continue
        markdown_files.append(
            {
                "file": md_file,
                "name": md_file.name,
                "nav_order": get_nav_order(md_file),
            }
        )
    markdown_files = [entry["file"] for entry in _sort_nav_entries(markdown_files)]

    subitems = []

    if has_index:
        subitems.append(
            {"type": "simple", "content": f'"{relative_path}/index.md"', "indent": child_indent}
        )

    for md_file in markdown_files:
        file_relative_path = _relative_docs_path(md_file, docs_base_path)
        file_title = get_preferred_title(md_file, md_file.stem)
        escaped_title = protect_toml_string(file_title)
        subitems.append(
            {
                "type": "simple",
                "content": f"{{{escaped_title} = \"{file_relative_path}\"}}",
                "indent": child_indent,
            }
        )

    for subdir in subdirs:
        subdir_items = build_directory_nav(
            subdir, indent_level=indent_level + 1, docs_base_path=docs_base_path
        )
        if not subdir_items:
            continue
        cleaned_lines = [
            line.rstrip(",") if index == len(subdir_items) - 1 else line
            for index, line in enumerate(subdir_items)
        ]
        subitems.append({"type": "nested", "lines": cleaned_lines})

    if subitems:
        escaped_dir_title = protect_toml_string(dir_title)
        if len(subitems) == 1 and subitems[0]["type"] == "simple":
            single_item = subitems[0]
            items.append(f"{indent}{{{escaped_dir_title} = [ {single_item['content']} ]}},")
        else:
            items.append(f"{indent}{{{escaped_dir_title} = [")
            for index, subitem in enumerate(subitems):
                comma = "" if index == len(subitems) - 1 else ","
                if subitem["type"] == "simple":
                    items.append(f"{subitem['indent']}{subitem['content']}{comma}")
                else:
                    for nested_index, line in enumerate(subitem["lines"]):
                        items.append(f"{line}{comma}" if nested_index == len(subitem["lines"]) - 1 else line)
            items.append(f"{indent}]}},")

    return items


def build_navigation_toml(docs_base_path):
    """Return the complete nav = [...] TOML block for a docs tree."""
    docs_base_path = Path(docs_base_path)
    nav_items_list = []

    root_index = docs_base_path / "index.md"
    if root_index.exists():
        home_title = get_preferred_title(root_index, "index") or "Home"
        escaped_title = protect_toml_string(home_title)
        nav_items_list.append({"type": "simple", "content": f"    {{{escaped_title} = \"index.md\"}}"})

    excluded_dirs = {"resources", "guides-list", "local-storage"}
    root_directories = sorted(
        (
            child
            for child in docs_base_path.iterdir()
            if child.is_dir() and child.name not in excluded_dirs
        ),
        key=lambda path: path.name,
    )
    for directory in root_directories:
        sub_nav = build_directory_nav(directory, indent_level=1, docs_base_path=docs_base_path)
        cleaned_lines = [
            line.rstrip(",") if index == len(sub_nav) - 1 else line
            for index, line in enumerate(sub_nav)
        ]
        nav_items_list.append({"type": "block", "lines": cleaned_lines})

    guides_list_path = docs_base_path / "guides-list"
    guides_index = guides_list_path / "index.md"
    if guides_index.exists():
        guides_title = get_preferred_title(guides_index, "guides-list") or "Guides List"
        escaped_title = protect_toml_string(guides_title)
        nav_items_list.append(
            {"type": "simple", "content": f"    {{{escaped_title} = \"guides-list/index.md\"}}"}
        )

    root_files = sorted(
        (
            child
            for child in docs_base_path.glob("*.md")
            if child.name != "index.md"
        ),
        key=lambda path: path.name,
    )
    for md_file in root_files:
        file_title = get_preferred_title(md_file, md_file.stem)
        escaped_title = protect_toml_string(file_title)
        nav_items_list.append({"type": "simple", "content": f"    {{{escaped_title} = \"{md_file.name}\"}}"})

    nav_items = ["nav = ["]
    for index, item in enumerate(nav_items_list):
        comma = "" if index == len(nav_items_list) - 1 else ","
        if item["type"] == "simple":
            nav_items.append(f"{item['content']}{comma}")
        else:
            for line_index, line in enumerate(item["lines"]):
                nav_items.append(f"{line}{comma}" if line_index == len(item["lines"]) - 1 else line)
    nav_items.append("]")
    return OUTPUT_NEWLINE.join(nav_items)


def update_zensical_nav(zensical_file_path, new_nav_content):
    """Replace or insert the nav section in zensical.toml. Return True if changed."""
    zensical_file_path = Path(zensical_file_path)
    with zensical_file_path.open("r", encoding="utf-8", newline="") as handle:
        content = handle.read()

    nav_match = NAV_SECTION_RE.search(content)
    if nav_match:
        current_nav = nav_match.group(0)
        current_nav_normalized = current_nav.replace("\r\n", "\n").rstrip()
        new_nav_normalized = new_nav_content.replace("\r\n", "\n").rstrip()
        if current_nav_normalized == new_nav_normalized:
            return False
        new_content = NAV_SECTION_RE.sub(new_nav_content, content, count=1)
        with zensical_file_path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(new_content)
        return True

    nav_comment_match = NAV_COMMENT_RE.search(content)
    if nav_comment_match:
        insert_point = nav_comment_match.start(0) + len(nav_comment_match.group(0))
        new_content = (
            content[:insert_point]
            + new_nav_content
            + OUTPUT_NEWLINE
            + OUTPUT_NEWLINE
            + content[insert_point:]
        )
    else:
        theme_match = THEME_SECTION_RE.search(content)
        if theme_match:
            insert_point = theme_match.start(0)
            new_content = (
                content[:insert_point]
                + new_nav_content
                + OUTPUT_NEWLINE
                + OUTPUT_NEWLINE
                + content[insert_point:]
            )
        else:
            new_content = content.rstrip() + OUTPUT_NEWLINE + OUTPUT_NEWLINE + new_nav_content + OUTPUT_NEWLINE

    with zensical_file_path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(new_content)
    return True


def main(argv=None):
    """Run the nav generator CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=None,
        help="Docs directory to scan (default: ..\\docs when run from utilities\\).",
    )
    parser.add_argument(
        "--zensical-file",
        type=Path,
        default=None,
        help="zensical.toml file to update (default: ..\\zensical.toml when run from utilities\\).",
    )
    args = parser.parse_args(argv)

    current_dir = Path.cwd()
    if current_dir.name != "utilities":
        print("Error: This script must be run from the utilities/ directory", file=sys.stderr)
        print(f"Current location: {current_dir}", file=sys.stderr)
        return 1

    docs_path = args.docs_dir or Path("..\\docs")
    zensical_path = args.zensical_file or Path("..\\zensical.toml")

    if not docs_path.exists():
        print(f"Error: docs directory not found at {docs_path}", file=sys.stderr)
        return 1

    if not zensical_path.exists():
        print(f"Error: zensical.toml not found at {zensical_path}", file=sys.stderr)
        return 1

    print(f"Generating Zensical navigation from '{docs_path}'...")
    nav_toml = build_navigation_toml(docs_path)
    print("Updating zensical.toml...")

    try:
        changed = update_zensical_nav(zensical_path, nav_toml)
    except Exception as exc:
        print(f"Error updating zensical.toml: {exc}", file=sys.stderr)
        return 1

    if changed:
        print("Successfully updated zensical.toml navigation section")
    else:
        print("Navigation section is already up to date. No changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
