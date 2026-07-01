#!/usr/bin/env python3
"""akb-build-glossary.py - Generate assistant knowledge base glossary from abbreviations.md.

Input:  includes/abbreviations.md  (Markdown abbreviations plugin syntax)
Output: docs/assistant/cross-platform/concept/abbreviations.md
        (schema.md-compliant knowledge base article)

Run from any working directory; paths are resolved relative to this file.
"""

import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
INPUT_PATH = REPO_ROOT / "includes" / "abbreviations.md"
OUTPUT_PATH = (
    REPO_ROOT
    / "docs"
    / "assistant"
    / "cross-platform"
    / "concept"
    / "abbreviations.md"
)

# Regex matching Markdown abbreviation plugin entries: *[ABBR]: Expansion
ABBR_RE = re.compile(r"^\*\[(.+?)\]:\s+(.+)$")


def parse_abbreviations(text: str) -> list[tuple[str, str]]:
    """Return a list of (abbreviation, expansion) tuples, sorted case-insensitively."""
    entries: list[tuple[str, str]] = []
    for line in text.splitlines():
        m = ABBR_RE.match(line)
        if m:
            entries.append((m.group(1), m.group(2)))
    return sorted(entries, key=lambda x: x[0].lower())


def build_table(entries: list[tuple[str, str]]) -> str:
    """Return a Markdown table of abbreviations."""
    rows = "\n".join(f"| {abbr} | {expansion} |" for abbr,
                     expansion in entries)
    return f"| Abbreviation | Expansion |\n| :----------- | :-------- |\n{rows}"


def build_output(entries: list[tuple[str, str]]) -> str:
    """Return the complete content of the output file."""
    today = date.today().isoformat()
    table = build_table(entries)
    count = len(entries)

    frontmatter = f"""\
---
title: Abbreviations and Acronyms Glossary
tags:
    - Assistant
slug: abbreviations
doc_type: concept
questions:
    - What does an abbreviation mean?
    - What does <acronym> stand for?
    - What is <abbreviation> short for?
    - What does TCAT stand for?
    - What does OSW stand for?
    - What does TDEI stand for?
    - What does OS-CONNECT stand for?
products:
    - AccessMap
    - AVIV ScoutRoute
    - OpenSidewalks
    - OS-CONNECT
    - QA/QC Reports
    - Rapid
    - TDEI
    - Walksheds
    - WayKeeper
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - glossary
    - abbreviations
    - acronyms
risk_level: low
authority_level: official
review_status: reviewed
last_reviewed: {today}
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim:
        - This list is exhaustive of all possible abbreviations in the domain.
        - No other meanings are possible for these abbreviations.
        - Abbreviations not listed here have no accepted expansion.
related_pages: []
---"""

    body = f"""\
<!-- @format -->

# Abbreviations and Acronyms Glossary

## Short Answer

This page lists all {count} abbreviations, acronyms, and initialisms used across TCAT Wiki \
documentation and TCAT platforms and tools.

## Significance

TCAT documentation spans transportation, accessibility, geospatial, and software domains, each \
with their own vocabulary. A shared, machine-readable glossary helps all audiences — planners, \
advocates, developers, and the public — interpret documentation correctly without specialist \
background, and allows assistants to resolve abbreviations precisely.

## What This Means

The table below maps each abbreviated form to its full expansion. Entries are sorted \
alphabetically and sourced directly from `includes/abbreviations.md`, the single source of \
truth for all abbreviations used site-wide.

{table}

## What This Does Not Mean

- Entries listed here are not endorsements of or official definitions for external organizations \
(for example, FHWA, AASHTO, or UN).
- Expansions reflect TCAT internal usage, which may differ from general-domain usage for \
ambiguous abbreviations.
- This list does not cover every possible abbreviation used in external data sources or \
third-party tools integrated with TCAT platforms.

## How To Use This

Look up an unfamiliar abbreviation by scanning or searching the table above. For product-specific \
or schema-specific meanings, follow links in the relevant product documentation.

## Example

A planner reviewing an OS-CONNECT data export sees the column label "CRS". Looking up CRS in \
this glossary returns "Coordinate Reference System", clarifying that this field stores the \
spatial projection of the dataset.

## Assistant Guidance

When a user asks what an abbreviation means or an acronym stands for, retrieve the matching row \
from this glossary and return the expansion directly. Do not infer expansions for abbreviations \
not present in this table; instead, acknowledge the ambiguity and suggest the user check the \
relevant product documentation or contact the TCAT team.

## Related Concepts

- [Dispatch](../../dispatch.md)
"""

    return frontmatter + "\n\n" + body


def main() -> int:
    if not INPUT_PATH.exists():
        print(f"ERROR: Input file not found: {INPUT_PATH}", file=sys.stderr)
        return 1

    text = INPUT_PATH.read_text(encoding="utf-8")
    entries = parse_abbreviations(text)

    if not entries:
        print(
            f"ERROR: No abbreviation entries found in {INPUT_PATH}", file=sys.stderr
        )
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    output = build_output(entries)
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Generated {OUTPUT_PATH} ({len(entries)} entries).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
