"""Pytest suite validating the real docs/assistant/ knowledge base content.

Unlike test_akb_generate_dispatch.py and test_build_site.py (which use
temp fixture trees), these tests validate the actual authored content
under docs/assistant/ against the authoring contract in
docs/assistant/schema.md, and cross-check it against the generated
docs/assistant/dispatch.md registry.
"""

import re
from collections import defaultdict
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent
ASSISTANT_DIR = REPO_ROOT / "docs" / "assistant"
DISPATCH_PATH = ASSISTANT_DIR / "dispatch.md"
SCHEMA_PATH = ASSISTANT_DIR / "schema.md"

# Top-level files that live directly in the assistant root and are never
# treated as topic directories (mirrors akb_generate_dispatch.py).
TOP_LEVEL_PEERS = {"index.md", "dispatch.md", "schema.md", "intents.md"}

DOC_TYPE_SUBDIRS = ("concept", "workflow")

# Cross-cutting topic directories whose pages legitimately span multiple
# products with no single "owning" product/topic-folder match. Exempt from
# the products/topics first-entry-matches-parent-topic-folder checks below
# (but still subject to test_all_products_have_matching_topic_slug).
EXEMPT_TOPIC_DIRS = {"cross-platform", "support"}

REQUIRED_SECTIONS = [
    "## Short Answer",
    "## Significance",
    "## What This Means",
    "## What This Does Not Mean",
    "## How To Use This",
    "## Example",
    "## Assistant Guidance",
    "## Related Concepts",
]

VALID_PUBLICATION_STATUSES = {"stub", "draft", "published", "archived"}
VALID_RISK_LEVELS = {"low", "medium", "high"}
VALID_AUTHORITY_LEVELS = {"provisional", "explanatory", "official"}
VALID_RETRIEVAL_PRIORITIES = {"low", "medium", "high"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
ROW_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+\.md)`\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|")
HEADING_RE = re.compile(r"^(#{2,4})\s+(.*)$")
BASE_RE = re.compile(r"^Base:\s*`([^`]+)`")


def parse_frontmatter(text):
    """Parse simple top-level ``key: value`` YAML frontmatter into a dict.

    Mirrors the parser in utilities/akb_generate_dispatch.py: only scalar
    top-level keys are captured, not nested maps/lists.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    props = {}
    for line in match.group(1).split("\n"):
        if not line or line[0] in " \t#-":
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] in "'\"" and value[-1] == value[0]:
            value = value[1:-1]
        if value:
            props[key] = value
    return props


LIST_ITEM_RE = re.compile(r"^\s*-\s*(.+)$")


def parse_frontmatter_list(text, key):
    """Parse a top-level ``key:``-introduced YAML block list into a list of strings.

    Only handles the simple block-list style used throughout docs/assistant/
    (``key:`` on its own line, followed by indented ``- value`` lines), which
    mirrors how ``products``/``topics`` are actually authored. An inline
    ``key: []`` (empty list) or missing key both yield ``[]``.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return []
    lines = match.group(1).split("\n")
    items = []
    in_list = False
    for line in lines:
        stripped = line.strip()
        if not in_list:
            if stripped == f"{key}:":
                in_list = True
            continue
        if line and line[0] in " \t":
            m = LIST_ITEM_RE.match(line)
            if not m:
                break
            value = m.group(1).strip()
            if len(value) >= 2 and value[0] in "'\"" and value[-1] == value[0]:
                value = value[1:-1]
            items.append(value)
        else:
            break
    return items


CODE_TABLE_CELL_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|", re.MULTILINE)


def extract_schema_vocab(schema_text, start_heading, end_heading):
    """Return the set of backtick-quoted values in table rows between two headings."""
    start_idx = schema_text.index(start_heading) + len(start_heading)
    end_idx = schema_text.index(end_heading, start_idx)
    section = schema_text[start_idx:end_idx]
    return set(CODE_TABLE_CELL_RE.findall(section))


def topic_dirs():
    """Every subdirectory of docs/assistant/ (each is a topic)."""
    if not ASSISTANT_DIR.is_dir():
        return []
    return sorted(p for p in ASSISTANT_DIR.iterdir() if p.is_dir())


def all_topic_articles():
    """Yield (topic_name, doc_type, path) for every index.md/concept/workflow file.

    doc_type is "policy" for a topic's own index.md, else "concept"/"workflow"
    based on which subdirectory the file lives in.
    """
    for topic in topic_dirs():
        index_path = topic / "index.md"
        if index_path.exists():
            yield topic.name, "policy", index_path
        for sub in DOC_TYPE_SUBDIRS:
            subdir = topic / sub
            if subdir.is_dir():
                for f in sorted(subdir.glob("*.md")):
                    yield topic.name, sub, f


ARTICLES = list(all_topic_articles())
ARTICLE_IDS = [
    f"{topic}/{doc_type}/{path.name}" for topic, doc_type, path in ARTICLES
]


def rel(path: Path) -> str:
    """POSIX-style path relative to ASSISTANT_DIR, for comparison with dispatch.md."""
    return path.relative_to(ASSISTANT_DIR).as_posix()


# =============================================================================
# Directory structure
# =============================================================================

def test_topics_exist():
    assert topic_dirs(), "No topic directories found under docs/assistant/"


def test_topic_dirs_have_only_expected_children():
    expected = {"index.md", "concept", "workflow"}
    bad = []
    for topic in topic_dirs():
        children = {p.name for p in topic.iterdir()}
        if children != expected:
            bad.append((topic.name, sorted(children)))
    assert not bad, f"Topic dirs with unexpected children (want exactly {expected}): {bad}"


def test_every_topic_has_index_md():
    missing = [t.name for t in topic_dirs() if not (t / "index.md").exists()]
    assert not missing, f"Topics missing index.md: {missing}"


def test_no_index_md_inside_concept_or_workflow():
    stray = []
    for topic in topic_dirs():
        for sub in DOC_TYPE_SUBDIRS:
            subdir = topic / sub
            if subdir.is_dir() and (subdir / "index.md").exists():
                stray.append(rel(subdir / "index.md"))
    assert not stray, f"index.md found inside concept/ or workflow/ subdirectories: {stray}"


def test_no_stray_files_at_assistant_root():
    """Every file directly under docs/assistant/ must be a known top-level peer."""
    stray = []
    for entry in ASSISTANT_DIR.iterdir():
        if entry.is_file() and entry.name not in TOP_LEVEL_PEERS:
            stray.append(entry.name)
    assert not stray, f"Unexpected files directly under docs/assistant/: {stray}"


# =============================================================================
# Per-article frontmatter checks
# =============================================================================

@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_slug_matches_filename_or_topic_index(topic, doc_type, path):
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    slug = fm.get("slug")
    if doc_type == "policy":
        expected = f"{topic}-index"
        assert slug == expected, f"{rel(path)}: slug '{slug}' != expected '{expected}'"
    else:
        assert slug == path.stem, f"{rel(path)}: slug '{slug}' != filename '{path.stem}'"


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_doc_type_matches_location(topic, doc_type, path):
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    assert fm.get("doc_type") == doc_type, (
        f"{rel(path)}: doc_type '{fm.get('doc_type')}' != expected '{doc_type}' "
        f"(based on its location on disk)"
    )


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_required_sections_present_and_ordered(topic, doc_type, path):
    text = path.read_text(encoding="utf-8")
    body = FRONTMATTER_RE.sub("", text, count=1)
    assert re.search(r"(?m)^# ", body), f"{rel(path)}: missing an H1 title"
    positions = []
    for section in REQUIRED_SECTIONS:
        idx = body.find(section)
        assert idx != -1, f"{rel(path)}: missing required section '{section}'"
        positions.append(idx)
    assert positions == sorted(
        positions), f"{rel(path)}: required sections are out of order"


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_frontmatter_enum_values_valid(topic, doc_type, path):
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    assert fm.get("publication_status") in VALID_PUBLICATION_STATUSES, (
        f"{rel(path)}: invalid publication_status {fm.get('publication_status')!r}"
    )
    assert fm.get("risk_level") in VALID_RISK_LEVELS, (
        f"{rel(path)}: invalid risk_level {fm.get('risk_level')!r}"
    )
    assert fm.get("authority_level") in VALID_AUTHORITY_LEVELS, (
        f"{rel(path)}: invalid authority_level {fm.get('authority_level')!r}"
    )
    assert fm.get("retrieval_priority") in VALID_RETRIEVAL_PRIORITIES, (
        f"{rel(path)}: invalid retrieval_priority {fm.get('retrieval_priority')!r}"
    )


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_title_is_present(topic, doc_type, path):
    fm = parse_frontmatter(path.read_text(encoding="utf-8"))
    assert fm.get("title"), f"{rel(path)}: missing or empty title"


UID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_uid_is_canonical_uuidv4(topic, doc_type, path):
    uid = parse_frontmatter(path.read_text(encoding="utf-8")).get("uid")
    assert uid and UID_RE.fullmatch(uid), f"{rel(path)}: invalid uid {uid!r}"


def test_uids_are_unique_and_not_retired():
    values = []
    for _topic, _doc_type, path in ARTICLES:
        values.append(parse_frontmatter(path.read_text(encoding="utf-8")).get("uid"))
    assert len(values) == len(set(values)), "Assistant page UIDs must be unique"
    retired_path = REPO_ROOT / "utilities" / "akb-retired-uuids.txt"
    retired = {
        line.strip() for line in retired_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    assert not retired.intersection(values), "Live pages must not use retired UIDs"


# =============================================================================
# products/topics controlled vocabulary (docs/assistant/schema.md)
# =============================================================================

@pytest.fixture(scope="module")
def schema_products():
    schema_text = SCHEMA_PATH.read_text(encoding="utf-8")
    return extract_schema_vocab(schema_text, "## Product tags", "## Topic tags")


@pytest.fixture(scope="module")
def schema_topics():
    schema_text = SCHEMA_PATH.read_text(encoding="utf-8")
    return extract_schema_vocab(
        schema_text, "## Topic tags (`topics`)", "## Related Concepts"
    )


@pytest.fixture(scope="module")
def schema_product_slugs():
    """Return a dict mapping each schema Product name to its Slug column value.

    Parses the ``## Product tags`` table's ``Product`` and ``Slug`` columns
    directly (rather than reusing ``extract_schema_vocab``, which only
    captures a single backtick-quoted column per row).
    """
    schema_text = SCHEMA_PATH.read_text(encoding="utf-8")
    start_idx = schema_text.index("## Product tags")
    end_idx = schema_text.index("## Topic tags", start_idx)
    section = schema_text[start_idx:end_idx]
    row_re = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", re.MULTILINE)
    return dict(row_re.findall(section))


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_products_match_schema_vocabulary(topic, doc_type, path, schema_products):
    text = path.read_text(encoding="utf-8")
    products = parse_frontmatter_list(text, "products")
    assert products, f"{rel(path)}: missing or empty products list"
    unknown = [p for p in products if p not in schema_products]
    assert not unknown, (
        f"{rel(path)}: products {unknown} not in docs/assistant/schema.md's "
        "Product tags table"
    )


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_topics_match_schema_vocabulary(topic, doc_type, path, schema_topics):
    text = path.read_text(encoding="utf-8")
    topics = parse_frontmatter_list(text, "topics")
    assert topics, f"{rel(path)}: missing or empty topics list"
    unknown = [t for t in topics if t not in schema_topics]
    assert not unknown, (
        f"{rel(path)}: topics {unknown} not in docs/assistant/schema.md's "
        "controlled vocabulary tables"
    )


@pytest.mark.parametrize(
    "topic,doc_type,path",
    [(t, d, p) for t, d, p in ARTICLES if t not in EXEMPT_TOPIC_DIRS],
    ids=[i for (t, _, _), i in zip(ARTICLES, ARTICLE_IDS)
         if t not in EXEMPT_TOPIC_DIRS],
)
def test_first_product_matches_parent_topic_folder(topic, doc_type, path, schema_product_slugs):
    """The first ``products`` entry must be the product owning this topic folder.

    Every article lives under ``docs/assistant/{topic}/``, and every
    single-product topic folder corresponds 1:1 with a `Product` row in the
    schema's Product tags table (matched via that row's `Slug` column). The
    first entry in `products` must be that product, though the list is not
    limited to it (a page may also cite other related products further down
    the list). ``cross-platform`` and ``support`` are cross-cutting sections
    with no single owning product and are exempt (see EXEMPT_TOPIC_DIRS).
    """
    expected_product = next(
        (product for product, slug in schema_product_slugs.items() if slug == topic), None
    )
    assert expected_product, (
        f"{rel(path)}: topic folder '{topic}' has no matching Slug in "
        "docs/assistant/schema.md's Product tags table"
    )
    text = path.read_text(encoding="utf-8")
    products = parse_frontmatter_list(text, "products")
    assert products, f"{rel(path)}: missing or empty products list"
    assert products[0] == expected_product, (
        f"{rel(path)}: first products entry '{products[0]}' != expected "
        f"'{expected_product}' (based on parent topic folder '{topic}')"
    )


@pytest.mark.parametrize(
    "topic,doc_type,path",
    [(t, d, p) for t, d, p in ARTICLES if t not in EXEMPT_TOPIC_DIRS],
    ids=[i for (t, _, _), i in zip(ARTICLES, ARTICLE_IDS)
         if t not in EXEMPT_TOPIC_DIRS],
)
def test_first_topic_matches_parent_topic_folder(topic, doc_type, path):
    """The first ``topics`` entry must be the parent topic folder's own slug.

    Checked purely against in-file frontmatter (no schema lookup needed):
    since test_first_product_matches_parent_topic_folder already guarantees
    the first `products` entry is correct for this topic folder, the first
    `topics` entry just needs to equal the topic folder name itself, which is
    also that product's slug. ``cross-platform`` and ``support`` are exempt
    (see EXEMPT_TOPIC_DIRS).
    """
    text = path.read_text(encoding="utf-8")
    topics = parse_frontmatter_list(text, "topics")
    assert topics, f"{rel(path)}: missing or empty topics list"
    assert topics[0] == topic, (
        f"{rel(path)}: first topics entry '{topics[0]}' != expected "
        f"'{topic}' (parent topic folder name)"
    )


@pytest.mark.parametrize("topic,doc_type,path", ARTICLES, ids=ARTICLE_IDS)
def test_all_products_have_matching_topic_slug(topic, doc_type, path, schema_product_slugs):
    """Every ``products`` entry must have its slug equivalent present in ``topics``.

    Applies to all articles, including cross-platform/ and support/: for each
    product listed, that product's schema `Slug` (docs/assistant/schema.md's
    Product tags table) must also appear somewhere in the page's `topics`
    list, so a page's full set of owning products is discoverable from
    `topics` alone.
    """
    text = path.read_text(encoding="utf-8")
    products = parse_frontmatter_list(text, "products")
    topics = parse_frontmatter_list(text, "topics")
    assert products, f"{rel(path)}: missing or empty products list"
    assert topics, f"{rel(path)}: missing or empty topics list"
    missing = []
    for product in products:
        slug = schema_product_slugs.get(product)
        if slug is None:
            # Already reported by test_products_match_schema_vocabulary.
            continue
        if slug not in topics:
            missing.append((product, slug))
    assert not missing, (
        f"{rel(path)}: products missing their slug in topics (product, expected_slug): "
        f"{missing}"
    )


# =============================================================================
# Slug collisions
# =============================================================================

def test_slug_collisions_within_and_across_topics():
    """Flag slug collisions between two articles of the *same* doc_type in the
    *same* topic.

    Articles are addressed by their full path (topic/doc_type/filename), not
    by slug alone, so a bare slug is never required to be globally unique.
    Collisions across topics, and collisions between a concept/ and a
    workflow/ article sharing a slug within the same topic, are both
    expected/allowed and are not flagged. Only a same-topic, same-doc_type
    collision indicates two files that would be ambiguous to each other
    within their own directory (e.g. duplicate filenames), which is flagged.
    """
    by_topic_type_slug = defaultdict(list)
    for topic, doc_type, path in ARTICLES:
        if doc_type == "policy":
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        by_topic_type_slug[(topic, doc_type, fm.get("slug"))].append(path)

    same_topic_same_type = [
        (key, [rel(p) for p in paths])
        for key, paths in by_topic_type_slug.items()
        if len(paths) > 1
    ]

    assert not same_topic_same_type, (
        f"Slug collisions within the same topic and doc_type: {same_topic_same_type}"
    )


# =============================================================================
# dispatch.md cross-validation
# =============================================================================

def parse_dispatch_rows(text):
    """Return a list of (heading_stack, file_path, status) for each table row.

    heading_stack is a tuple of enclosing heading texts (H2-H4), most recent
    last, so rows can be grouped/attributed regardless of the exact heading
    depth/format used by the registry. file_path is resolved against the most
    recent preceding "Base: `assistant/{topic}/{doc_type}/`" line, so it is
    comparable to the ASSISTANT_DIR-relative paths produced by rel() (matching
    how a consuming agent would actually resolve each row: Base + filename).
    A bare filename with no preceding Base line is left unresolved (as-is).
    """
    stack = []
    base = None
    rows = []
    for line in text.splitlines():
        hm = HEADING_RE.match(line)
        if hm:
            level = len(hm.group(1))
            title = hm.group(2).strip()
            stack = [s for s in stack if s[0] < level]
            stack.append((level, title))
            continue
        bm = BASE_RE.match(line)
        if bm:
            base = bm.group(1).removeprefix("assistant/")
            continue
        rm = ROW_RE.match(line)
        if rm:
            uid = rm.group(1)
            fname = rm.group(2)
            file_path = f"{base}{fname}" if base else fname
            rows.append((tuple(t for _, t in stack), file_path, uid, rm.group(4)))
    return rows


@pytest.fixture(scope="module")
def dispatch_text():
    assert DISPATCH_PATH.exists(), "docs/assistant/dispatch.md not found"
    return DISPATCH_PATH.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def dispatch_rows(dispatch_text):
    registry = dispatch_text.split("## Registry", 1)[-1]
    return parse_dispatch_rows(registry)


def test_dispatch_frontmatter_is_valid(dispatch_text):
    fm = parse_frontmatter(dispatch_text)
    assert fm.get("slug") == "dispatch"
    assert fm.get("publication_status") in VALID_PUBLICATION_STATUSES


def test_dispatch_has_no_rows_for_nonexistent_files(dispatch_rows):
    missing = []
    for heading_stack, file_path, _uid, _status in dispatch_rows:
        if not (ASSISTANT_DIR / file_path).exists():
            missing.append((file_path, heading_stack))
    assert not missing, (
        f"dispatch.md lists {len(missing)} file(s) that do not exist on disk "
        f"(stale/orphaned rows). First 20: {missing[:20]}"
    )


def test_dispatch_has_no_duplicate_rows(dispatch_rows):
    counts = defaultdict(int)
    for _heading_stack, file_path, _uid, _status in dispatch_rows:
        counts[file_path] += 1
    dupes = {path: n for path, n in counts.items() if n > 1}
    assert not dupes, f"dispatch.md lists the same file more than once: {dupes}"


def test_dispatch_lists_every_topic_article_exactly_once(dispatch_rows):
    """Every concept/workflow article has exactly one registry table row.

    Topic index.md files (doc_type "policy") are intentionally excluded: the
    generator links them via a "See [topic/index.md]" prose line rather than
    a table row, per akb_generate_dispatch.py's render_topic().
    """
    listed_counts = defaultdict(int)
    for _heading_stack, file_path, _uid, _status in dispatch_rows:
        listed_counts[file_path] += 1

    absent_or_duplicated = []
    for topic, doc_type, path in ARTICLES:
        if doc_type == "policy":
            continue
        path_key = rel(path)
        count = listed_counts.get(path_key, 0)
        if count != 1:
            absent_or_duplicated.append((path_key, count))
    assert not absent_or_duplicated, (
        f"{len(absent_or_duplicated)} article(s) under docs/assistant/ missing from "
        "dispatch.md (count 0), or listed more than once (count > 1). "
        f"First 20: {absent_or_duplicated[:20]}"
    )


def test_dispatch_publication_status_matches_frontmatter(dispatch_rows):
    row_status = {}
    for _heading_stack, file_path, _uid, status in dispatch_rows:
        row_status[file_path] = status

    mismatches = []
    for topic, doc_type, path in ARTICLES:
        path_key = rel(path)
        if path_key not in row_status:
            continue  # already reported by test_dispatch_lists_every_topic_article_exactly_once
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        actual_status = fm.get("publication_status", "stub")
        if row_status[path_key] != actual_status:
            mismatches.append((path_key, row_status[path_key], actual_status))
    assert not mismatches, (
        f"dispatch.md publication_status disagrees with file frontmatter for "
        f"{len(mismatches)} file(s) (path, dispatch_status, actual_status). "
        f"First 20: {mismatches[:20]}"
    )


def test_dispatch_uids_match_frontmatter(dispatch_rows):
    row_uids = {file_path: uid for _heading, file_path, uid, _status in dispatch_rows}
    mismatches = []
    for _topic, _doc_type, path in ARTICLES:
        key = rel(path)
        if key in row_uids:
            actual = parse_frontmatter(path.read_text(encoding="utf-8")).get("uid")
            if row_uids[key] != actual:
                mismatches.append((key, row_uids[key], actual))
    dispatch_uid = parse_frontmatter(DISPATCH_PATH.read_text(encoding="utf-8")).get("uid")
    assert row_uids.get("dispatch.md") == dispatch_uid
    assert not mismatches, f"Dispatch UID mismatches: {mismatches[:20]}"
