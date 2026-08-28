#!/usr/bin/env python3
"""generate_guides_lists.py - Generate per-directory guides sections and the main Guides List.

Performs two phases for the Zensical-based TCAT Wiki documentation site:

  - PHASE 1: For each directory with index.md, create a "### Guides" section
    (or "### Table of Contents" for user manual or tutorial pages) listing:
      * Tutorials first (under a "Tutorials" subsection)
      * User manual subdirectories next
      * Direct guides in that directory next
      * Subsections for non-user-manual subdirectories and their guides

  - PHASE 2: Regenerate docs/guides-list/index.md with a hierarchical listing
    across all topics, maintaining consistent ordering with tutorials first,
    then user manuals, then regular guides at each level.

Guide files must have a "- Guide" frontmatter tag. User manual index files
must have a "- User Manual" tag (which also implies Guide). Tutorial files
must have a "- Tutorial" tag (which also implies Guide).

Special frontmatter flags are YAML comments inside frontmatter:

  - # exclude-from-parent-guides-list
  - # exclude-from-main-guides-list
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.resolve()
DEFAULT_DOCS_DIR = REPO_ROOT / "docs"

CRLF = "\r\n"
EXCLUDE_PARENT_FLAG = "exclude-from-parent-guides-list"
EXCLUDE_MAIN_FLAG = "exclude-from-main-guides-list"

FRONTMATTER_RE = re.compile(r"(?s)^---\r?\n(.*?)\r?\n---")
TITLE_RE = re.compile(r"title:\s*(.+?)(?:\r?\n|$)")
NAV_ORDER_RE = re.compile(r"nav_order:\s*(\d+)")
DESCRIPTION_RE = re.compile(
    r"(?s)(?:^|\r?\n)##\s+.+?(?:\r?\n)(.*?)(?=\r?\n(?:_For a list of all guides|---|#{2,3} (?:Guides|Table of Contents)))"
)
REMOVE_GUIDES_SECTION_RE = re.compile(
    r"(?s)\r?\n\r?\n#{2,3} (Guides|Table of Contents)\r?\n.*$"
)


@dataclass(frozen=True)
class GuideInfo:
    title: str = ""
    description: str = ""
    is_guide: bool = False
    is_user_manual: bool = False
    is_tutorial: bool = False
    exclude_from_parent: bool = False
    exclude_from_main: bool = False
    nav_order: int | None = None


@dataclass(frozen=True)
class GuideEntry:
    type: str
    path: Path
    info: GuideInfo
    file: Path | None = None
    directory: Path | None = None
    nav_order: int | None = None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    if text and not text.endswith(("\r\n", "\n")):
        text += CRLF
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def sort_nav_then_path(nav_order: int | None, path: Path) -> tuple[int, str]:
    return (nav_order if nav_order is not None else sys.maxsize, str(path))


def normalize_for_compare(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")


def get_guide_info(file_path: Path) -> GuideInfo:
    """Extract guide metadata from a markdown file's frontmatter and body."""
    try:
        content = read_text(file_path)
    except OSError:
        return GuideInfo()

    frontmatter_match = FRONTMATTER_RE.search(content)
    frontmatter = frontmatter_match.group(1) if frontmatter_match else ""

    is_guide = "- Guide" in frontmatter
    is_user_manual = "- User Manual" in frontmatter
    is_tutorial = "- Tutorial" in frontmatter
    if is_user_manual or is_tutorial:
        is_guide = True

    exclude_from_parent = f"# {EXCLUDE_PARENT_FLAG}" in frontmatter
    exclude_from_main = f"# {EXCLUDE_MAIN_FLAG}" in frontmatter

    nav_order_match = NAV_ORDER_RE.search(frontmatter)
    nav_order = int(nav_order_match.group(1)) if nav_order_match else None

    title_match = TITLE_RE.search(content)
    title = title_match.group(1).strip() if title_match else ""

    description_match = DESCRIPTION_RE.search(content)
    description = ""
    if description_match:
        description = description_match.group(1).strip()
        description = re.sub(r"^[\s\r\n]+|[\s\r\n]+$", "", description)

    return GuideInfo(
        title=title,
        description=description,
        is_guide=is_guide,
        is_user_manual=is_user_manual,
        is_tutorial=is_tutorial,
        exclude_from_parent=exclude_from_parent,
        exclude_from_main=exclude_from_main,
        nav_order=nav_order,
    )


def get_directory_title(index_path: Path) -> str:
    """Extract the title from an index.md file's frontmatter."""
    try:
        content = read_text(index_path)
    except OSError:
        return ""
    match = TITLE_RE.search(content)
    return match.group(1).strip() if match else ""


def is_user_manual_directory(directory: Path) -> bool:
    index_path = directory / "index.md"
    return index_path.is_file() and get_guide_info(index_path).is_user_manual


def is_tutorial_directory(directory: Path) -> bool:
    index_path = directory / "index.md"
    return index_path.is_file() and get_guide_info(index_path).is_tutorial


def get_relative_markdown_path(from_path: Path | str, to_path: Path | str) -> str:
    relative_path = os.path.relpath(os.fspath(to_path), os.fspath(from_path))
    return relative_path.replace("\\", "/")


def _is_excluded(info: GuideInfo, exclude_flag: str) -> bool:
    if exclude_flag == EXCLUDE_PARENT_FLAG:
        return info.exclude_from_parent
    return info.exclude_from_main


def get_guides_in_directory(directory: Path, exclude_own_index: bool, exclude_flag: str) -> list[Path]:
    """Return guide files sorted as tutorials, user manuals, then regular guides."""
    index_path = directory / "index.md"
    tutorials: list[tuple[Path, int | None]] = []
    user_manuals: list[tuple[Path, int | None]] = []
    regular_guides: list[tuple[Path, int | None]] = []

    def maybe_add(file_path: Path) -> None:
        if exclude_own_index and file_path == index_path:
            return
        info = get_guide_info(file_path)
        if not info.is_guide or _is_excluded(info, exclude_flag):
            return
        target = (file_path, info.nav_order)
        if info.is_tutorial:
            tutorials.append(target)
        elif info.is_user_manual:
            user_manuals.append(target)
        else:
            regular_guides.append(target)

    for md_file in sorted(directory.glob("*.md"), key=lambda path: path.name):
        maybe_add(md_file)

    tutorial_subdir = directory / "tutorial"
    if tutorial_subdir.is_dir():
        for md_file in sorted(tutorial_subdir.glob("*.md"), key=lambda path: path.name):
            maybe_add(md_file)

        for subdir in sorted((path for path in tutorial_subdir.iterdir() if path.is_dir()), key=lambda path: path.name):
            sub_index = subdir / "index.md"
            if sub_index.is_file():
                maybe_add(sub_index)

    sorted_tutorials = [path for path, _ in sorted(tutorials, key=lambda item: sort_nav_then_path(item[1], item[0]))]
    sorted_user_manuals = [path for path, _ in sorted(user_manuals, key=lambda item: sort_nav_then_path(item[1], item[0]))]
    sorted_regular_guides = [path for path, _ in sorted(regular_guides, key=lambda item: sort_nav_then_path(item[1], item[0]))]
    return sorted_tutorials + sorted_user_manuals + sorted_regular_guides


def get_subdirectories(directory: Path) -> list[Path]:
    """Return child dirs with index.md, sorted as tutorials, user manuals, regular."""
    tutorial_dirs: list[tuple[Path, int | None]] = []
    user_manual_dirs: list[tuple[Path, int | None]] = []
    regular_dirs: list[tuple[Path, int | None]] = []

    for child in sorted((path for path in directory.iterdir() if path.is_dir()), key=lambda path: path.name):
        if child.name in {"resources", "tutorial"}:
            continue
        index_path = child / "index.md"
        if not index_path.is_file():
            continue
        info = get_guide_info(index_path)
        target = (child, info.nav_order)
        if is_tutorial_directory(child):
            tutorial_dirs.append(target)
        elif is_user_manual_directory(child):
            user_manual_dirs.append(target)
        else:
            regular_dirs.append(target)

    sorted_tutorials = [path for path, _ in sorted(tutorial_dirs, key=lambda item: sort_nav_then_path(item[1], item[0]))]
    sorted_user_manuals = [path for path, _ in sorted(user_manual_dirs, key=lambda item: sort_nav_then_path(item[1], item[0]))]
    sorted_regular_dirs = [path for path, _ in sorted(regular_dirs, key=lambda item: sort_nav_then_path(item[1], item[0]))]
    return sorted_tutorials + sorted_user_manuals + sorted_regular_dirs


def build_guide_entry(guide_file: Path, from_path: Path, header_level: str) -> str:
    info = get_guide_info(guide_file)
    relative_path = get_relative_markdown_path(from_path, guide_file)
    entry = f"{header_level} [{info.title}]({relative_path}){CRLF}"
    if info.description:
        entry += f"{CRLF}{info.description}{CRLF}"
    return entry


def build_section_header(
    title: str,
    index_path: Path,
    from_path: Path,
    header_level: str,
    is_user_manual: bool,
) -> str:
    relative_path = get_relative_markdown_path(from_path, index_path)
    suffix = "" if is_user_manual else " Guides"
    header = f"{header_level} [{title}]({relative_path}){suffix}{CRLF}"
    info = get_guide_info(index_path)
    if info.description:
        header += f"{CRLF}{info.description}{CRLF}"
    header += CRLF
    return header


def get_all_guides_at_level(
    directory: Path,
    exclude_flag: str,
    subdirectories: list[Path] | None = None,
) -> list[GuideEntry]:
    tutorial_entries: list[GuideEntry] = []
    user_manual_entries: list[GuideEntry] = []
    regular_entries: list[GuideEntry] = []

    for subdir in subdirectories or []:
        index_path = subdir / "index.md"
        info = get_guide_info(index_path)
        if not info.is_guide or _is_excluded(info, exclude_flag):
            if is_tutorial_directory(subdir) or is_user_manual_directory(subdir):
                continue
        if is_tutorial_directory(subdir):
            if info.is_guide and not _is_excluded(info, exclude_flag):
                tutorial_entries.append(
                    GuideEntry(
                        type="Tutorial",
                        path=index_path,
                        info=info,
                        file=index_path,
                        directory=subdir,
                        nav_order=info.nav_order,
                    )
                )
        elif is_user_manual_directory(subdir):
            if info.is_guide and not _is_excluded(info, exclude_flag):
                user_manual_entries.append(
                    GuideEntry(
                        type="UserManual",
                        path=index_path,
                        info=info,
                        directory=subdir,
                        nav_order=info.nav_order,
                    )
                )

    for guide in get_guides_in_directory(directory, exclude_own_index=True, exclude_flag=exclude_flag):
        info = get_guide_info(guide)
        if info.is_tutorial:
            tutorial_entries.append(
                GuideEntry(
                    type="Tutorial",
                    path=guide,
                    info=info,
                    file=guide,
                    nav_order=info.nav_order,
                )
            )
        else:
            regular_entries.append(
                GuideEntry(
                    type="Guide",
                    path=guide,
                    info=info,
                    file=guide,
                    nav_order=info.nav_order,
                )
            )

    tutorial_entries.sort(key=lambda entry: sort_nav_then_path(entry.nav_order, entry.path))
    user_manual_entries.sort(key=lambda entry: sort_nav_then_path(entry.nav_order, entry.path))
    regular_entries.sort(key=lambda entry: sort_nav_then_path(entry.nav_order, entry.path))
    return tutorial_entries + user_manual_entries + regular_entries


def update_parent_guides_section(directory: Path, docs_path: Path) -> bool:
    """Update a directory index.md with a Guides or Table of Contents section."""
    index_path = directory / "index.md"
    parent_dir = directory
    subdirs = get_subdirectories(parent_dir)
    all_entries = get_all_guides_at_level(parent_dir, EXCLUDE_PARENT_FLAG, subdirs)

    has_subdir_content = False
    for subdir in subdirs:
        if is_user_manual_directory(subdir) or is_tutorial_directory(subdir):
            continue
        subdir_entries = get_all_guides_at_level(
            subdir,
            EXCLUDE_PARENT_FLAG,
            get_subdirectories(subdir),
        )
        if subdir_entries:
            has_subdir_content = True
            break
        subdir_index = subdir / "index.md"
        if subdir_index.is_file():
            info = get_guide_info(subdir_index)
            if info.is_guide and not info.exclude_from_parent:
                has_subdir_content = True
                break

    if not all_entries and not has_subdir_content:
        return False

    is_user_manual = is_user_manual_directory(parent_dir)
    is_tutorial = is_tutorial_directory(parent_dir)
    section_title = "Table of Contents" if (is_user_manual or is_tutorial) else "Guides"

    page_title = get_directory_title(index_path)
    relative_parts = index_path.relative_to(docs_path).parts
    dir_depth = len(relative_parts) - 1
    rel_path_to_guides_list = ("../" * dir_depth) + "guides-list/index.md"

    guides_section = f"{CRLF}{CRLF}### {section_title}{CRLF}{CRLF}"
    guides_section += f"{page_title} {section_title}{CRLF}{CRLF}"

    if not is_user_manual and not is_tutorial:
        guides_section += (
            "_For a list of all guides on the TCAT Wiki, refer to the "
            f"[Guides List]({rel_path_to_guides_list})._{{ .guides-list-ref }}"
            f"{CRLF}{CRLF}"
        )

    tutorial_entries = [entry for entry in all_entries if entry.type == "Tutorial"]
    user_manual_entries = [entry for entry in all_entries if entry.type == "UserManual"]
    regular_entries = [entry for entry in all_entries if entry.type == "Guide"]

    if tutorial_entries:
        guides_section += f"#### Tutorials{CRLF}{CRLF}"
        for entry in tutorial_entries:
            if entry.file is None:
                continue
            guides_section += build_guide_entry(entry.file, parent_dir, "#####")
            guides_section += CRLF

    for entry in user_manual_entries:
        guides_section += build_guide_entry(entry.path, parent_dir, "####")
        guides_section += CRLF

    for entry in regular_entries:
        if entry.file is None:
            continue
        guides_section += build_guide_entry(entry.file, parent_dir, "####")
        guides_section += CRLF

    for subdir in subdirs:
        if is_user_manual_directory(subdir) or is_tutorial_directory(subdir):
            continue
        subdir_index = subdir / "index.md"
        subdir_title = get_directory_title(subdir_index)
        subdir_entries = get_all_guides_at_level(
            subdir,
            EXCLUDE_PARENT_FLAG,
            get_subdirectories(subdir),
        )
        if not subdir_entries:
            info = get_guide_info(subdir_index)
            if info.is_guide and not info.exclude_from_parent:
                guides_section += build_guide_entry(subdir_index, parent_dir, "####")
                guides_section += CRLF
            continue

        guides_section += build_section_header(
            subdir_title,
            subdir_index,
            parent_dir,
            "####",
            False,
        )

        sub_tutorials = [entry for entry in subdir_entries if entry.type == "Tutorial"]
        sub_user_manuals = [entry for entry in subdir_entries if entry.type == "UserManual"]
        sub_regular = [entry for entry in subdir_entries if entry.type == "Guide"]

        if sub_tutorials:
            guides_section += f"##### Tutorials{CRLF}{CRLF}"
            for entry in sub_tutorials:
                if entry.file is None:
                    continue
                guides_section += build_guide_entry(entry.file, parent_dir, "######")
                guides_section += CRLF

        for entry in sub_user_manuals:
            guides_section += build_guide_entry(entry.path, parent_dir, "#####")
            guides_section += CRLF

        for entry in sub_regular:
            if entry.file is None:
                continue
            guides_section += build_guide_entry(entry.file, parent_dir, "#####")
            guides_section += CRLF

    original_content = read_text(index_path)
    content = REMOVE_GUIDES_SECTION_RE.sub("", original_content)
    content = content.rstrip() + guides_section.rstrip()
    if normalize_for_compare(original_content) == normalize_for_compare(content):
        return False
    write_text(index_path, content)
    return True


def build_main_guides_list(all_directories: list[Path], docs_path: Path) -> str:
    """Build docs/guides-list/index.md content."""
    content = (
        f"---{CRLF}title: Guides List{CRLF}---{CRLF}{CRLF}"
        f"<!-- @format -->{CRLF}{CRLF}"
        f"## Guides List{CRLF}{CRLF}"
        "Guides, tutorials, and user manuals produced by TCAT and/or its "
        f"partners are listed below.{CRLF}{CRLF}"
    )
    guides_list_path = docs_path / "guides-list"

    topic_groups: dict[str, list[Path]] = {}
    for directory in all_directories:
        if directory.name == "guides-list":
            continue
        path_parts = directory.relative_to(docs_path).parts
        if not path_parts:
            continue
        topic_groups.setdefault(path_parts[0], []).append(directory)

    for topic in sorted(topic_groups):
        directories = topic_groups[topic]
        topic_dir = next((d for d in directories if len(d.relative_to(docs_path).parts) == 1), None)
        if topic_dir is None:
            continue

        topic_index_path = topic_dir / "index.md"
        topic_title = get_directory_title(topic_index_path)

        has_guides = False
        for directory in directories:
            index_path = directory / "index.md"
            if is_user_manual_directory(directory) or is_tutorial_directory(directory):
                info = get_guide_info(index_path)
                if info.is_guide and not info.exclude_from_main:
                    has_guides = True
                    break
            else:
                if get_guides_in_directory(directory, True, EXCLUDE_MAIN_FLAG):
                    has_guides = True
                    break

        if not has_guides:
            continue

        topic_relative_path = get_relative_markdown_path(guides_list_path, topic_index_path)
        content += f"### [{topic_title}]({topic_relative_path}){CRLF}{CRLF}"

        dirs_by_parent: dict[Path, list[Path]] = {}
        for directory in directories:
            dirs_by_parent.setdefault(directory.parent, []).append(directory)

        def directory_depth_in_topic(directory: Path) -> int:
            return len(directory.relative_to(docs_path).parts) - 1

        def append_directory_hierarchy(parent_path: Path, depth: int, text: str) -> str:
            if parent_path not in dirs_by_parent:
                return text

            tutorial_dirs: list[tuple[Path, int | None]] = []
            user_manual_dirs: list[tuple[Path, int | None]] = []
            regular_dirs: list[tuple[Path, int | None]] = []

            for child in dirs_by_parent[parent_path]:
                index_path = child / "index.md"
                nav_order = get_guide_info(index_path).nav_order if index_path.is_file() else None
                target = (child, nav_order)
                if is_tutorial_directory(child):
                    if depth > 1:
                        tutorial_dirs.append(target)
                elif is_user_manual_directory(child):
                    if depth > 1:
                        user_manual_dirs.append(target)
                else:
                    regular_dirs.append(target)

            for directory, _nav_order in sorted(tutorial_dirs, key=lambda item: sort_nav_then_path(item[1], item[0])):
                index_path = directory / "index.md"
                info = get_guide_info(index_path)
                if not info.is_guide or info.exclude_from_main:
                    continue
                header_level = "#" * (directory_depth_in_topic(directory) + 3)
                text += build_guide_entry(index_path, guides_list_path, header_level) + CRLF

            for directory, _nav_order in sorted(user_manual_dirs, key=lambda item: sort_nav_then_path(item[1], item[0])):
                index_path = directory / "index.md"
                info = get_guide_info(index_path)
                if not info.is_guide or info.exclude_from_main:
                    continue
                header_level = "#" * (directory_depth_in_topic(directory) + 3)
                text += build_guide_entry(index_path, guides_list_path, header_level) + CRLF

            for directory, _nav_order in sorted(regular_dirs, key=lambda item: sort_nav_then_path(item[1], item[0])):
                index_path = directory / "index.md"
                guides = get_guides_in_directory(directory, True, EXCLUDE_MAIN_FLAG)
                has_children = directory in dirs_by_parent
                child_tutorials = []
                child_user_manuals = []
                if has_children:
                    child_tutorials = [
                        child for child in dirs_by_parent[directory] if is_tutorial_directory(child)
                    ]
                    child_user_manuals = [
                        child for child in dirs_by_parent[directory] if is_user_manual_directory(child)
                    ]

                if not guides and not has_children:
                    continue

                dir_title = get_directory_title(index_path)
                depth_in_topic = directory_depth_in_topic(directory)
                if depth_in_topic > 0:
                    header_level = "#" * (depth_in_topic + 3)
                    text += build_section_header(
                        dir_title,
                        index_path,
                        guides_list_path,
                        header_level,
                        False,
                    )

                tutorial_guides = []
                non_tutorial_guides = []
                for guide in guides:
                    if get_guide_info(guide).is_tutorial:
                        tutorial_guides.append(guide)
                    else:
                        non_tutorial_guides.append(guide)

                child_tut_entries = [
                    (
                        child,
                        get_guide_info(child / "index.md").nav_order,
                        get_guide_info(child / "index.md"),
                    )
                    for child in child_tutorials
                ]

                if tutorial_guides or child_tut_entries:
                    tutorial_header_level = "#" * (depth_in_topic + 4)
                    tutorial_guide_level = "#" * (depth_in_topic + 5)
                    text += f"{tutorial_header_level} Tutorials{CRLF}{CRLF}"
                    for guide in tutorial_guides:
                        text += build_guide_entry(guide, guides_list_path, tutorial_guide_level) + CRLF
                    for tut_dir, nav_order, info in sorted(
                        child_tut_entries,
                        key=lambda item: sort_nav_then_path(item[1], item[0]),
                    ):
                        if not info.is_guide or info.exclude_from_main:
                            continue
                        text += build_guide_entry(tut_dir / "index.md", guides_list_path, tutorial_guide_level) + CRLF

                child_um_entries = [
                    (
                        child,
                        get_guide_info(child / "index.md").nav_order,
                        get_guide_info(child / "index.md"),
                    )
                    for child in child_user_manuals
                ]
                for um_dir, nav_order, info in sorted(
                    child_um_entries,
                    key=lambda item: sort_nav_then_path(item[1], item[0]),
                ):
                    if not info.is_guide or info.exclude_from_main:
                        continue
                    guide_header_level = "#" * (depth_in_topic + 4)
                    text += build_guide_entry(um_dir / "index.md", guides_list_path, guide_header_level) + CRLF

                for guide in non_tutorial_guides:
                    guide_header_level = "#" * (depth_in_topic + 4)
                    text += build_guide_entry(guide, guides_list_path, guide_header_level) + CRLF

                if has_children:
                    non_special_children = [
                        child
                        for child in dirs_by_parent[directory]
                        if not is_user_manual_directory(child)
                        and not is_tutorial_directory(child)
                    ]
                    if non_special_children:
                        text = append_directory_hierarchy(directory, depth + 1, text)

            return text

        topic_guides = get_guides_in_directory(topic_dir, True, EXCLUDE_MAIN_FLAG)
        topic_tutorials = [guide for guide in topic_guides if get_guide_info(guide).is_tutorial]
        topic_regular_guides = [guide for guide in topic_guides if not get_guide_info(guide).is_tutorial]

        topic_tutorial_dirs: list[Path] = []
        for child in dirs_by_parent.get(topic_dir, []):
            if not is_tutorial_directory(child):
                continue
            tut_index_path = child / "index.md"
            tut_info = get_guide_info(tut_index_path)
            if tut_info.is_guide and not tut_info.exclude_from_main:
                topic_tutorial_dirs.append(tut_index_path)

        if topic_tutorials or topic_tutorial_dirs:
            content += f"#### Tutorials{CRLF}{CRLF}"
            for guide in topic_tutorials:
                content += build_guide_entry(guide, guides_list_path, "#####")
                content += CRLF
            for tut_dir_index in topic_tutorial_dirs:
                content += build_guide_entry(tut_dir_index, guides_list_path, "#####")
                content += CRLF

        child_entries = []
        for child in dirs_by_parent.get(topic_dir, []):
            index_path = child / "index.md"
            nav_order = get_guide_info(index_path).nav_order if index_path.is_file() else None
            child_entries.append((child, nav_order))
        for child, _nav_order in sorted(child_entries, key=lambda item: sort_nav_then_path(item[1], item[0])):
            if is_tutorial_directory(child):
                continue
            if is_user_manual_directory(child):
                um_index_path = child / "index.md"
                um_info = get_guide_info(um_index_path)
                if um_info.is_guide and not um_info.exclude_from_main:
                    content += build_guide_entry(um_index_path, guides_list_path, "####")
                    content += CRLF

        for guide in topic_regular_guides:
            content += build_guide_entry(guide, guides_list_path, "####")
            content += CRLF

        content = append_directory_hierarchy(topic_dir, 1, content)

    return content.rstrip()


def find_docs_path() -> Path:
    if DEFAULT_DOCS_DIR.is_dir():
        return DEFAULT_DOCS_DIR
    raise FileNotFoundError(
        "docs directory not found. Please run this script from the repository root or utilities directory."
    )


def find_directories_with_index(docs_path: Path) -> list[Path]:
    directories = []
    for directory in sorted((path for path in docs_path.rglob("*") if path.is_dir()), key=lambda path: str(path)):
        if directory.name == "resources":
            continue
        if (directory / "index.md").is_file():
            directories.append(directory)
    return directories


def run(docs_path: Path | None = None) -> dict[str, int | Path]:
    docs_path = (docs_path or find_docs_path()).resolve()
    all_directories = find_directories_with_index(docs_path)

    updated = 0
    for directory in all_directories:
        if update_parent_guides_section(directory, docs_path):
            updated += 1

    main_content = build_main_guides_list(all_directories, docs_path)
    guides_list_path = docs_path / "guides-list" / "index.md"
    existing_guides_list = read_text(guides_list_path) if guides_list_path.exists() else ""
    if normalize_for_compare(existing_guides_list) != normalize_for_compare(main_content):
        write_text(guides_list_path, main_content)
    return {
        "docs_path": docs_path,
        "directories_with_index": len(all_directories),
        "updated_parent_sections": updated,
        "guides_list_path": guides_list_path,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    parse_args(argv)
    print()
    print("TCAT Wiki - Guides Lists Generator v5.1.0")
    print("===========================================")
    print()
    try:
        docs_path = find_docs_path()
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Scanning: {docs_path}")
    print()
    all_directories = find_directories_with_index(docs_path)
    print(f"Found {len(all_directories)} directories with index.md files")
    print()
    print("PHASE 1: Updating parent directory index.md files")
    print("---------------------------------------------------")
    print()
    updated = 0
    try:
        for directory in all_directories:
            if update_parent_guides_section(directory, docs_path):
                updated += 1
                print(f"  [OK] Updated: {directory.name}")
    except Exception as exc:  # pragma: no cover - CLI error path
        print(f"Failed processing {directory}: {exc}", file=sys.stderr)
        return 1

    print()
    print("PHASE 2: Generating main guides-list/index.md")
    print("-----------------------------------------------")
    print()
    try:
        main_content = build_main_guides_list(all_directories, docs_path)
        guides_list_path = docs_path / "guides-list" / "index.md"
        existing_guides_list = read_text(guides_list_path) if guides_list_path.exists() else ""
        if normalize_for_compare(existing_guides_list) != normalize_for_compare(main_content):
            write_text(guides_list_path, main_content)
        print("[OK] Generated main guides list")
    except Exception as exc:  # pragma: no cover - CLI error path
        print(f"Failed generating main guides list: {exc}", file=sys.stderr)
        return 1

    print()
    print("===========================================")
    print("Guides list generation complete!")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
